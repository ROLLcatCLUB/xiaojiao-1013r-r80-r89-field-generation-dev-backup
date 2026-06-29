import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_OUTPUT = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1"
R21_HTML = (
    BASE_OUTPUT
    / "1013R_R21_page_copy_binds_unified_package"
    / "prep_room_page_copy_binds_unified_package_1013R_R21.html"
)
R81_DIR = BASE_OUTPUT / "1013R_R81_LESSON_SCHEMA_FIELD_MAP_ADAPTER"
R82_DIR = BASE_OUTPUT / "1013R_R82_LESSON_GENERATION_REQUEST_RESPONSE_CONTRACT"
R83_DIR = BASE_OUTPUT / "1013R_R83_LESSON_GENERATION_NORMALIZER_DRY_RUN"
R84_DIR = BASE_OUTPUT / "1013R_R84_EDIT_CARD_BRIDGE_VISIBLE_SMOKE"
R85_DIR = BASE_OUTPUT / "1013R_R85_LOCAL_FIXTURE_VISIBLE_GENERATION_SMOKE"
R86_DIR = BASE_OUTPUT / "1013R_R86_PROVIDER_SANDBOX_DRY_RUN"
R87_DIR = BASE_OUTPUT / "1013R_R87_PROVIDER_OR_FIXTURE_VISIBLE_GENERATION_SMOKE"

REQUEST_PATH = R82_DIR / "lesson_generation_request_envelope_1013R_R82.json"
FIXTURE_PATH = R82_DIR / "lesson_generation_smoke_fixtures_1013R_R82.json"
FIELD_MAP_PATH = R81_DIR / "lesson_14_field_mapping_1013R_R81.json"
R87_HTML = R87_DIR / "prep_room_r87_provider_or_fixture_visible_generation_smoke_1013R_R87.html"

ALLOWED_SCHEMA_KEYS = {
    "lesson_identity",
    "inherited_unit_context",
    "textbook_anchor",
    "lesson_concept_slice",
    "lesson_focus_question",
    "lesson_objectives",
    "student_starting_point",
    "key_difficult_points",
    "lesson_task_evidence",
    "classroom_flow",
    "courseware_plan",
    "handout_plan",
    "assessment_plan",
    "material_requests",
}

ALLOWED_TARGET_SECTIONS = {
    "lesson_header",
    "basis",
    "goals",
    "analysis",
    "keypoints",
    "preparation",
    "teaching_process",
    "assessment",
    "courseware_plan",
    "handout_plan",
    "material_requests",
}

REQUIRED_CANDIDATE_KEYS = [
    "field_patch_id",
    "schema_key",
    "canonical_field_key",
    "target_field_key",
    "target_section",
    "target_line_contract_id",
    "target_destination",
    "before_summary",
    "after_candidate",
    "xiaojiao_suggestion",
    "impact_scope",
    "source_refs",
    "teacher_review_required",
    "preview_only",
    "formal_apply_allowed",
    "applied",
    "patch_type",
]

SECTION_SELECTORS = {
    "lesson_header": [".nb-main-title", ".nb-title", "[data-r21-route-anchor='lesson_header']"],
    "basis": ["#nb-section-basis", "[data-edit-target^='section:basis']"],
    "goals": ["#nb-section-goals", "[data-edit-target^='section:goals']"],
    "analysis": ["#nb-section-analysis", "[data-edit-target^='section:analysis']"],
    "keypoints": ["#nb-section-keypoints", "[data-edit-target^='section:keypoints']"],
    "preparation": ["#nb-section-preparation", "[data-edit-target^='section:preparation']"],
    "teaching_process": ["#nb-section-teaching-process", "[id^='nb-step-']", ".nb-readable-step"],
    "assessment": ["#nb-section-assessment", "[data-edit-target^='section:assessment']"],
    "courseware_plan": [
        "[data-r21-route-anchor='courseware_entry']",
        "[data-r21-route-anchor='classroom_display_screen']",
        ".courseware-rail",
    ],
    "handout_plan": ["[data-r32-derivative-id='worksheet']", ".r32-derivative-panel"],
    "material_requests": [".nb-material-front-prompt", "[data-r49-material-requests-prompt='true']"],
}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def now_ms():
    return round(time.time() * 1000)


def reject(reason, detail=None):
    raise ValueError(json.dumps({"reason": reason, "detail": detail}, ensure_ascii=False))


def parse_rejection(exc):
    try:
        return json.loads(str(exc))
    except Exception:
        return {"reason": "normalizer_error", "detail": str(exc)}


def ensure_plain_json_text(raw_text):
    text = (raw_text or "").strip()
    if text.startswith("```") or text.endswith("```"):
        reject("markdown_code_fence", "Model output must be raw JSON, not fenced markdown.")
    if not text.startswith("{"):
        reject("not_json_object", "Model output must start with a JSON object.")
    return json.loads(text)


def normalize_candidate(candidate, index, source_stage):
    if not isinstance(candidate, dict):
        reject("candidate_not_object", {"index": index})

    missing = [key for key in REQUIRED_CANDIDATE_KEYS if key not in candidate]
    if missing:
        reject("missing_candidate_keys", {"index": index, "missing": missing})

    schema_key = str(candidate.get("schema_key") or "").strip()
    target_section = str(candidate.get("target_section") or "").strip()
    target_destination = str(candidate.get("target_destination") or "").strip()

    if schema_key not in ALLOWED_SCHEMA_KEYS:
        reject("unknown_schema_key", {"index": index, "schema_key": schema_key})
    if str(candidate.get("canonical_field_key") or "").strip() != schema_key:
        reject("canonical_field_key_mismatch", {"index": index, "schema_key": schema_key})
    if str(candidate.get("target_field_key") or "").strip() != schema_key:
        reject("target_field_key_mismatch", {"index": index, "schema_key": schema_key})
    if target_section not in ALLOWED_TARGET_SECTIONS:
        reject("unknown_target_section", {"index": index, "target_section": target_section})
    if target_destination != "existing_edit_card_before_after_suggestion_panel":
        reject("standalone_or_unknown_destination", {"index": index, "target_destination": target_destination})
    if candidate.get("formal_apply_allowed") is not False:
        reject("formal_apply_allowed_must_be_false", {"index": index})
    if candidate.get("applied") is not False:
        reject("applied_must_be_false", {"index": index})
    if candidate.get("preview_only") is not True:
        reject("preview_only_must_be_true", {"index": index})
    if candidate.get("teacher_review_required") is not True:
        reject("teacher_review_required_must_be_true", {"index": index})
    if not isinstance(candidate.get("impact_scope"), list):
        reject("impact_scope_must_be_list", {"index": index})
    if not isinstance(candidate.get("source_refs"), list):
        reject("source_refs_must_be_list", {"index": index})

    normalized = deepcopy(candidate)
    normalized["normalized_candidate_id"] = f"r83_norm_{index + 1:02d}_{schema_key}"
    normalized["source_response_stage"] = source_stage
    normalized["review_status"] = "pending_teacher_review"
    normalized["candidate_display_contract"] = {
        "display_surface": "existing_edit_card",
        "display_panel": "before_after_suggestion",
        "show_before": True,
        "show_after": True,
        "show_xiaojiao_suggestion": True,
        "standalone_blue_card_created": False,
    }
    normalized["boundary_flags"] = {
        "preview_only": True,
        "formal_apply_allowed": False,
        "formal_apply_performed": False,
        "database_written": False,
        "feishu_written": False,
        "memory_written": False,
    }
    return normalized


def normalize_response(response, source_label):
    if not isinstance(response, dict):
        reject("response_not_object", source_label)
    if response.get("boundary_flags", {}).get("formal_apply_performed") is not False:
        reject("formal_apply_performed_must_be_false", source_label)

    candidates = response.get("field_patch_candidates")
    if not isinstance(candidates, list) or not candidates:
        reject("field_patch_candidates_missing_or_empty", source_label)
    if len(candidates) > 8:
        reject("too_many_field_patch_candidates", {"count": len(candidates)})

    normalized_candidates = [
        normalize_candidate(candidate, index, response.get("response_stage") or source_label)
        for index, candidate in enumerate(candidates)
    ]

    return {
        "schema_id": "normalized_lesson_candidates_1013R_R83",
        "stage": "1013R_R83_LESSON_GENERATION_NORMALIZER_DRY_RUN",
        "source_label": source_label,
        "request_id": response.get("request_id") or "unknown",
        "lesson_design_mode": response.get("lesson_design_mode") or "",
        "intent_summary": response.get("intent_summary") or "",
        "lesson_logic_brief": response.get("lesson_logic_brief") or {},
        "target_resolution": response.get("target_resolution") or [],
        "step_reasoning_updates": response.get("step_reasoning_updates") or [],
        "field_patch_candidates": normalized_candidates,
        "quality_gate_update": response.get("quality_gate_update") or {},
        "material_requests": response.get("material_requests") or [],
        "teacher_questions": response.get("teacher_questions") or [],
        "ui_binding_hint": response.get("ui_binding_hint") or {},
        "boundary_flags": {
            "teacher_review_required": True,
            "preview_only": True,
            "formal_apply_allowed": False,
            "formal_apply_performed": False,
            "database_written": False,
            "feishu_written": False,
            "memory_written": False,
            "formal_export_created": False,
            "official_archive_created": False,
        },
        "created_at_ms": now_ms(),
    }


def build_r83():
    fixture = read_json(FIXTURE_PATH)
    valid_response = fixture["valid_response"]
    normalized = normalize_response(valid_response, "r82_valid_smoke_fixture")
    write_json(R83_DIR / "normalized_lesson_candidates_1013R_R83.json", normalized)

    rejection_cases = []
    for invalid in fixture.get("invalid_responses", []):
        case_id = invalid.get("case_id")
        try:
            if "raw_text" in invalid:
                parsed = ensure_plain_json_text(invalid.get("raw_text") or "")
                normalize_response(parsed, case_id or "raw_text")
            else:
                normalize_response(invalid.get("response") or {}, case_id or "invalid_response")
            rejection_cases.append({"case_id": case_id, "accepted": True, "reason": "ERROR_should_have_rejected"})
        except Exception as exc:
            rejection_cases.append({"case_id": case_id, "accepted": False, **parse_rejection(exc)})

    validation = {
        "stage": "1013R_R83_LESSON_GENERATION_NORMALIZER_DRY_RUN",
        "result": "PASS",
        "source_fixture": str(FIXTURE_PATH),
        "normalized_candidate_count": len(normalized["field_patch_candidates"]),
        "allowed_schema_key_count": len(ALLOWED_SCHEMA_KEYS),
        "required_candidate_key_count": len(REQUIRED_CANDIDATE_KEYS),
        "invalid_response_case_count": len(rejection_cases),
        "invalid_response_rejected_count": sum(1 for item in rejection_cases if not item.get("accepted")),
        "all_invalid_responses_rejected": all(not item.get("accepted") for item in rejection_cases),
        "formal_apply_allowed": False,
        "r21_page_modified": False,
        "standalone_blue_card_created": False,
    }
    if not validation["all_invalid_responses_rejected"]:
        validation["result"] = "FAIL"
    write_json(R83_DIR / "normalizer_rejection_report_1013R_R83.json", {"cases": rejection_cases})
    write_json(R83_DIR / "validate_1013R_R83_normalizer_result.json", validation)
    return normalized, validation


def bridge_candidate(candidate):
    target_section = candidate["target_section"]
    selectors = SECTION_SELECTORS.get(target_section, [f"#nb-section-{target_section}"])
    return {
        "bridge_id": f"r84_bridge_{candidate['normalized_candidate_id']}",
        "field_patch_id": candidate["field_patch_id"],
        "schema_key": candidate["schema_key"],
        "canonical_field_key": candidate["canonical_field_key"],
        "target_field_key": candidate["target_field_key"],
        "target_section": target_section,
        "target_step_id": candidate.get("target_step_id") or "",
        "target_line_contract_id": candidate.get("target_line_contract_id") or "",
        "target_destination": "existing_edit_card_before_after_suggestion_panel",
        "target_selectors": selectors,
        "edit_card_slots": {
            "before_slot": candidate["before_summary"],
            "after_slot": candidate["after_candidate"],
            "xiaojiao_suggestion_slot": candidate["xiaojiao_suggestion"],
        },
        "visible_smoke_action": "open_existing_r6p_modal_with_before_after_suggestion",
        "standalone_blue_card_created": False,
        "formal_apply_allowed": False,
        "preview_only": True,
    }


def build_r84(normalized):
    bridges = [bridge_candidate(candidate) for candidate in normalized["field_patch_candidates"]]
    payload = {
        "schema_id": "edit_card_bridge_smoke_1013R_R84",
        "stage": "1013R_R84_EDIT_CARD_BRIDGE_VISIBLE_SMOKE",
        "source": str(R83_DIR / "normalized_lesson_candidates_1013R_R83.json"),
        "bridge_rule": "normalized field_patch_candidates open the existing R21/R6P before-after-suggestion modal; they do not create body blue cards.",
        "uses_existing_edit_card": True,
        "standalone_blue_card_created": False,
        "formal_apply_allowed": False,
        "r21_page_modified": False,
        "bridges": bridges,
    }
    validation = {
        "stage": "1013R_R84_EDIT_CARD_BRIDGE_VISIBLE_SMOKE",
        "result": "PASS",
        "bridge_count": len(bridges),
        "all_have_canonical_field_key": all(bool(item["canonical_field_key"]) for item in bridges),
        "all_route_to_existing_edit_card": all(
            item["target_destination"] == "existing_edit_card_before_after_suggestion_panel" for item in bridges
        ),
        "standalone_blue_card_created": False,
        "formal_apply_allowed": False,
        "r21_page_modified": False,
    }
    if not validation["bridge_count"] or not validation["all_have_canonical_field_key"] or not validation["all_route_to_existing_edit_card"]:
        validation["result"] = "FAIL"
    write_json(R84_DIR / "edit_card_bridge_smoke_1013R_R84.json", payload)
    write_json(R84_DIR / "validate_1013R_R84_edit_card_bridge_result.json", validation)
    return payload, validation


def build_r85(bridge_payload):
    visible_payload = {
        "schema_id": "local_fixture_visible_generation_payload_1013R_R85",
        "stage": "1013R_R85_LOCAL_FIXTURE_VISIBLE_GENERATION_SMOKE",
        "source": str(R84_DIR / "edit_card_bridge_smoke_1013R_R84.json"),
        "provider_runtime_connected": False,
        "candidate_source": "r82_valid_fixture_via_r83_normalizer",
        "visible_contract": {
            "host": "R21 copied page only",
            "entry": "right tool panel .r45r47-model-loop",
            "display": "existing .r6p-modal-backdrop",
            "candidate_slots": ["before_summary", "after_candidate", "xiaojiao_suggestion"],
            "formal_apply_allowed": False,
        },
        "bridges": bridge_payload["bridges"],
    }
    validation = {
        "stage": "1013R_R85_LOCAL_FIXTURE_VISIBLE_GENERATION_SMOKE",
        "result": "PASS",
        "candidate_source": visible_payload["candidate_source"],
        "provider_runtime_connected": False,
        "visible_candidate_count": len(visible_payload["bridges"]),
        "uses_existing_modal": True,
        "formal_apply_allowed": False,
        "r21_page_modified": False,
    }
    if not validation["visible_candidate_count"]:
        validation["result"] = "FAIL"
    write_json(R85_DIR / "local_fixture_visible_generation_payload_1013R_R85.json", visible_payload)
    write_json(R85_DIR / "validate_1013R_R85_local_fixture_visible_result.json", validation)
    return visible_payload, validation


def resolve_minimax_config():
    api_key = (os.environ.get("MINIMAX_API_KEY") or os.environ.get("MINIAMX_API_KEY") or "").strip()
    base_url = (
        os.environ.get("MINIMAX_API_BASE")
        or os.environ.get("MINIAMX_API_BASE")
        or os.environ.get("XIAOBEI_MINIMAX_API_BASE")
        or "https://api.minimaxi.com/v1/text/chatcompletion_v2"
    ).strip()
    model = (os.environ.get("MINIMAX_MODEL") or os.environ.get("MINIAMX_MODEL") or "MiniMax-M3").strip()
    return {"api_key": api_key, "base_url": base_url.rstrip("/"), "model": model}


def resolve_endpoint(base_url):
    lower = base_url.lower()
    if lower.endswith("/text/chatcompletion_v2"):
        return ""
    if "api.minimaxi.com" in lower or "api.minimax.chat" in lower:
        return "/text/chatcompletion_v2"
    return "/chat/completions"


def redact_sensitive(text):
    text = str(text or "")
    text = re.sub(r"Bearer\s+[A-Za-z0-9._\-]+", "Bearer <REDACTED>", text)
    text = re.sub(r"sk-[A-Za-z0-9._\-]{8,}", "sk-<REDACTED>", text)
    text = re.sub(r"(?i)(api[_-]?key[\"'\s:=]+)[A-Za-z0-9._\-]+", r"\1<REDACTED>", text)
    return text


def build_provider_prompt():
    request_contract = read_json(REQUEST_PATH)
    system_prompt = (
        "你是师维智教的小教备课生成器，只能输出可被 JSON.parse 解析的 JSON 对象。"
        "不要使用 Markdown 代码块，不要解释，不要输出注释。"
        "所有字符串必须放在双引号内。"
        "不要写入数据库、飞书、记忆或正式课包。"
        "候选只能进入 existing_edit_card_before_after_suggestion_panel。"
    )
    user_payload = {
        "task": "生成三年级美术《色彩的渐变》单课字段候选，用于R86 provider sandbox。",
        "required_stage": "1013R_R86_PROVIDER_SANDBOX_DRY_RUN",
        "allowed_schema_keys": request_contract["allowed_schema_keys"],
        "target_section_map": request_contract["target_section_map"],
        "teacher_intent": "请把30分钟课堂压缩为保留表达证据和评价证据的可见候选。",
        "hard_rules": [
            "field_patch_candidates数量必须是1到2个",
            "每个中文字符串不超过45字",
            "每个candidate必须带canonical_field_key和target_field_key，且等于schema_key",
            "target_destination必须是existing_edit_card_before_after_suggestion_panel",
            "preview_only=true",
            "formal_apply_allowed=false",
            "applied=false",
            "teacher_review_required=true",
            "不生成正文独立蓝卡",
        ],
        "minimal_response_template": {
            "response_stage": "1013R_R86_PROVIDER_SANDBOX_DRY_RUN",
            "request_id": "r86_provider_sandbox_001",
            "lesson_design_mode": "time_or_resource_constrained",
            "intent_summary": "string",
            "lesson_logic_brief": {
                "inherited_unit_context_summary": "string",
                "core_learning_problem": "string",
                "student_starting_point": "string",
                "target_shift": "string",
                "lesson_focus_question": "string",
                "visual_language_use": "string",
                "teaching_route": ["string"],
                "evidence_plan": ["string"],
                "risk_points": ["string"],
                "source_basis": ["teacher_intent", "current_process_steps"],
                "material_gaps": [],
            },
            "target_resolution": [
                {
                    "schema_key": "classroom_flow",
                    "target_section": "teaching_process",
                    "target_step_id": "share",
                    "target_field": "success_criteria",
                    "reason": "string",
                    "source_refs": ["teacher_intent", "current_process_steps"],
                }
            ],
            "step_reasoning_updates": [],
            "field_patch_candidates": [
                {
                    "field_patch_id": "r86_provider_candidate_01",
                    "schema_key": "classroom_flow",
                    "canonical_field_key": "classroom_flow",
                    "target_field_key": "classroom_flow",
                    "target_section": "teaching_process",
                    "target_step_id": "share",
                    "target_line_contract_id": "lesson_step.color_feeling.05.success_criteria",
                    "target_destination": "existing_edit_card_before_after_suggestion_panel",
                    "before_summary": "string",
                    "after_candidate": "string",
                    "xiaojiao_suggestion": "string",
                    "impact_scope": ["teacher_action", "student_activity", "evidence_note"],
                    "source_refs": ["teacher_intent", "current_process_steps"],
                    "teacher_review_required": True,
                    "preview_only": True,
                    "formal_apply_allowed": False,
                    "applied": False,
                    "patch_type": "revise",
                    "reasoning_basis": ["教学预设", "教师输入"],
                }
            ],
            "quality_gate_update": {
                "level": "basic_usable",
                "passed_items": [],
                "missing_items": [],
                "risk_items": [],
                "next_best_action": "string",
            },
            "material_requests": [],
            "teacher_questions": [],
            "ui_binding_hint": {
                "should_enter_edit_mode": True,
                "edit_target": "teaching_process/share",
                "candidate_display_position": "existing_edit_card",
                "right_tray_updates": [],
                "view_mode_summary": "string",
            },
            "boundary_flags": {
                "teacher_review_required": True,
                "formal_apply_performed": False,
                "database_written": False,
                "memory_written": False,
                "feishu_written": False,
                "formal_export_created": False,
                "official_archive_created": False,
            },
        },
    }
    return system_prompt, json.dumps(user_payload, ensure_ascii=False, indent=2)


def call_provider(config, system_prompt, user_prompt):
    body = {
        "model": config["model"],
        "temperature": 0.2,
        "max_tokens": 1300,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config['api_key']}",
    }
    request = urllib.request.Request(
        f"{config['base_url']}{resolve_endpoint(config['base_url'])}",
        data=data,
        headers=headers,
        method="POST",
    )
    started = time.perf_counter()
    with urllib.request.urlopen(request, timeout=45) as response:
        response_body = response.read().decode("utf-8")
    latency_ms = round((time.perf_counter() - started) * 1000)
    parsed = json.loads(response_body)
    if isinstance(parsed, dict):
        base_resp = parsed.get("base_resp")
        if isinstance(base_resp, dict) and str(base_resp.get("status_code", "0")) not in {"", "0", "None"}:
            raise RuntimeError(f"provider_business_error: {redact_sensitive(str(base_resp))}")
        content = ((((parsed.get("choices") or [])[0] or {}).get("message") or {}).get("content") or "")
        if not content and isinstance(parsed.get("reply"), str):
            content = parsed["reply"]
        if not content and isinstance(parsed.get("content"), str):
            content = parsed["content"]
    else:
        content = ""
    if not isinstance(content, str) or not content.strip():
        raise RuntimeError("provider_empty_response")
    return content.strip(), latency_ms


def build_r86(fallback_normalized):
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from backend.xiaobei_ai import providers

    config = resolve_minimax_config()
    system_prompt, user_prompt = build_provider_prompt()
    request_record = {
        "stage": "1013R_R86_PROVIDER_SANDBOX_DRY_RUN",
        "provider_family": "minimax",
        "base_url": config["base_url"],
        "model": config["model"],
        "credential_available": bool(config["api_key"]),
        "api_key": "<REDACTED>" if config["api_key"] else "",
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "boundary_flags": {
            "preview_only": True,
            "formal_apply_allowed": False,
            "database_written": False,
            "feishu_written": False,
            "memory_written": False,
        },
    }
    write_json(R86_DIR / "provider_sandbox_request_1013R_R86.json", request_record)

    provider_attempted = bool(config["api_key"])
    provider_success = False
    fallback_used = True
    raw_text = ""
    latency_ms = None
    error = None
    normalized = None
    parsed_provider = None

    if config["api_key"]:
        try:
            provider_response = providers.generate_json_patch(
                {
                    "stage": "1013R_R86_PROVIDER_SANDBOX_DRY_RUN",
                    "sandbox_only": True,
                    "target": "visible_generation_candidate",
                },
                {"system_prompt": system_prompt, "user_prompt": user_prompt},
                {
                    "provider": "openai_compatible",
                    "model": config["model"],
                    "temperature": 0.2,
                    "max_tokens": 1300,
                    "timeout_ms": 60000,
                    "use_response_format": True,
                    "use_reasoning_split": False,
                },
            )
            raw_text = str(provider_response.get("raw_text") or "").strip()
            provider_meta = provider_response.get("provider_meta") if isinstance(provider_response.get("provider_meta"), dict) else {}
            latency_ms = provider_meta.get("latency_ms")
            parsed_provider = ensure_plain_json_text(raw_text)
            normalized = normalize_response(parsed_provider, "r86_provider_response")
            normalized["stage"] = "1013R_R86_PROVIDER_SANDBOX_DRY_RUN"
            normalized["schema_id"] = "provider_sandbox_normalized_1013R_R86"
            provider_success = True
            fallback_used = False
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:1200]
            error = f"provider_http_{exc.code}: {redact_sensitive(detail)}"
        except Exception as exc:
            error = redact_sensitive(str(exc))
    else:
        error = "provider_credential_missing"

    if normalized is None:
        normalized = deepcopy(fallback_normalized)
        normalized["schema_id"] = "provider_sandbox_normalized_1013R_R86"
        normalized["stage"] = "1013R_R86_PROVIDER_SANDBOX_DRY_RUN"
        normalized["source_label"] = "r82_fixture_fallback_after_provider_sandbox"
        for candidate in normalized["field_patch_candidates"]:
            candidate["source_response_stage"] = "1013R_R86_PROVIDER_SANDBOX_DRY_RUN_FALLBACK"

    raw_text_path = R86_DIR / "provider_sandbox_raw_text_1013R_R86.txt"
    if raw_text:
        write_text(raw_text_path, raw_text)
    response_record = {
        "stage": "1013R_R86_PROVIDER_SANDBOX_DRY_RUN",
        "provider_attempted": provider_attempted,
        "provider_success": provider_success,
        "fallback_used": fallback_used,
        "latency_ms": latency_ms,
        "error": error,
        "raw_text_path": str(raw_text_path) if raw_text else "",
        "raw_text_truncated": raw_text[:5000],
        "parsed_provider_response_available": isinstance(parsed_provider, dict),
    }
    validation = {
        "stage": "1013R_R86_PROVIDER_SANDBOX_DRY_RUN",
        "result": "PASS_WITH_FALLBACK" if fallback_used else "PASS",
        "provider_attempted": provider_attempted,
        "provider_success": provider_success,
        "fallback_used": fallback_used,
        "normalized_candidate_count": len(normalized["field_patch_candidates"]),
        "all_candidates_preview_only": all(candidate.get("preview_only") is True for candidate in normalized["field_patch_candidates"]),
        "all_candidates_block_formal_apply": all(candidate.get("formal_apply_allowed") is False for candidate in normalized["field_patch_candidates"]),
        "formal_apply_allowed": False,
        "r21_page_modified": False,
        "error": error,
    }
    if not validation["normalized_candidate_count"]:
        validation["result"] = "FAIL"
    write_json(R86_DIR / "provider_sandbox_response_1013R_R86.json", response_record)
    write_json(R86_DIR / "provider_sandbox_normalized_1013R_R86.json", normalized)
    write_json(R86_DIR / "validate_1013R_R86_provider_sandbox_result.json", validation)
    return normalized, validation


def build_r87_payload(r86_normalized, r86_validation):
    bridges = [bridge_candidate(candidate) for candidate in r86_normalized["field_patch_candidates"]]
    payload = {
        "schema_id": "visible_generation_payload_1013R_R87",
        "stage": "1013R_R87_PROVIDER_OR_FIXTURE_VISIBLE_GENERATION_SMOKE",
        "source": str(R86_DIR / "provider_sandbox_normalized_1013R_R86.json"),
        "source_mode": "provider" if r86_validation.get("provider_success") else "fixture_fallback",
        "provider_success": bool(r86_validation.get("provider_success")),
        "fallback_used": bool(r86_validation.get("fallback_used")),
        "entry_label": "R87生成候选",
        "visible_contract": {
            "source_page": str(R21_HTML),
            "output_page": str(R87_HTML),
            "r21_page_modified": False,
            "copied_page_created": True,
            "right_panel_entry": ".r45r47-model-loop",
            "modal": ".r6p-modal-backdrop",
            "candidate_destination": "existing_edit_card_before_after_suggestion_panel",
            "standalone_blue_card_created": False,
            "formal_apply_allowed": False,
        },
        "bridges": bridges,
        "normalized_response": r86_normalized,
    }
    write_json(R87_DIR / "visible_generation_payload_1013R_R87.json", payload)
    return payload


def html_escape_js_payload(payload):
    return json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")


def build_r87_script(payload):
    payload_json = html_escape_js_payload(payload)
    return f"""

<!-- 1013R_R87_PROVIDER_OR_FIXTURE_VISIBLE_GENERATION_SMOKE: copied-page-only injection -->
<style id="r87-visible-generation-smoke-style">
  [data-r87-visible-generation-smoke="true"] .r87-generation-entry {{
    margin-top: 12px;
    border: 1px solid #88b7f0;
    background: #edf5ff;
    color: #16406e;
    border-radius: 8px;
    padding: 10px;
    font-size: 12px;
    box-shadow: 0 8px 24px rgba(32, 83, 128, 0.12);
  }}
  .r87-generation-entry-head {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    margin-bottom: 8px;
    font-weight: 700;
  }}
  .r87-generation-badge {{
    border: 1px solid #88b7f0;
    border-radius: 999px;
    padding: 2px 8px;
    background: #fff;
    color: #245b94;
    font-size: 11px;
    white-space: nowrap;
  }}
  .r87-generation-entry button {{
    border: 1px solid #2d7f72;
    border-radius: 999px;
    background: #2d7f72;
    color: #fff;
    padding: 7px 14px;
    font: inherit;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(45, 127, 114, 0.18);
  }}
  .r87-generation-button-row {{
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 8px;
  }}
  .r87-modal-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }}
  .r87-modal-box {{
    border: 1px solid #d5e0d8;
    border-radius: 8px;
    padding: 10px;
    background: #fffdf8;
    min-height: 88px;
    white-space: pre-wrap;
  }}
  .r87-modal-box.is-after {{
    background: #edf5ff;
    border-color: #9fc2ec;
  }}
  .r87-modal-box-title {{
    font-weight: 700;
    color: #237b6b;
    margin-bottom: 6px;
  }}
  .r87-modal-suggestion {{
    margin-top: 10px;
    border: 1px solid #f0c789;
    border-radius: 8px;
    padding: 10px;
    background: #fff9ed;
  }}
  .r87-modal-actions {{
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 12px;
  }}
  .r87-modal-actions button {{
    border: 1px solid #7aaee8;
    border-radius: 999px;
    background: #fff;
    color: #1d568f;
    padding: 5px 12px;
    font: inherit;
    cursor: pointer;
  }}
  .r87-modal-actions button:first-child {{
    background: #2d7f72;
    border-color: #2d7f72;
    color: #fff;
  }}
  .r87-target-highlight {{
    outline: 2px solid #86b8f0;
    outline-offset: 4px;
    transition: outline 0.2s ease;
  }}
</style>
<script id="r87-visible-generation-smoke-script">
(function () {{
  const payload = {payload_json};
  window.__R87_VISIBLE_GENERATION_SMOKE__ = payload;
  document.documentElement.setAttribute("data-r87-visible-generation-smoke", "true");
  document.documentElement.setAttribute("data-r87-copied-page-only", "true");
  document.documentElement.setAttribute("data-r87-formal-apply-allowed", "false");

  function esc(value) {{
    return String(value ?? "").replace(/[&<>"']/g, function (char) {{
      return ({{ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }})[char];
    }});
  }}

  function firstExisting(selectors) {{
    for (const selector of selectors || []) {{
      try {{
        const node = document.querySelector(selector);
        if (node) return node;
      }} catch (error) {{}}
    }}
    return null;
  }}

  function bridgeFor(index) {{
    const bridges = payload.bridges || [];
    return bridges[index] || bridges[0] || null;
  }}

  function modalNodes() {{
    const backdrop = document.querySelector(".r6p-modal-backdrop");
    return {{
      backdrop,
      title: backdrop?.querySelector?.(".r6p-modal-title"),
      status: backdrop?.querySelector?.(".r6p-modal-status"),
      body: backdrop?.querySelector?.(".r6p-modal-body"),
    }};
  }}

  function openCandidate(index) {{
    const bridge = bridgeFor(index);
    if (!bridge) return;
    const {{ backdrop, title, status, body }} = modalNodes();
    if (!backdrop || !body) return;

    const slots = bridge.edit_card_slots || {{}};
    if (title) title.textContent = "R87生成候选 · " + (bridge.schema_key || "字段");
    if (status) status.textContent = "preview_only · formal_apply_allowed=false · " + (payload.source_mode || "fixture_fallback");
    body.innerHTML = `
      <div class="r87-modal-grid">
        <div class="r87-modal-box">
          <div class="r87-modal-box-title">修改前</div>
          ${{esc(slots.before_slot || "暂无修改前摘要。")}}
        </div>
        <div class="r87-modal-box is-after">
          <div class="r87-modal-box-title">修改后</div>
          ${{esc(slots.after_slot || "暂无修改后候选。")}}
        </div>
      </div>
      <div class="r87-modal-suggestion">
        <div class="r87-modal-box-title">小教建议</div>
        ${{esc(slots.xiaojiao_suggestion_slot || "请教师确认后再推进。")}}
      </div>
      <div class="r87-modal-suggestion">
        <div class="r87-modal-box-title">字段与落点</div>
        canonical_field_key=${{esc(bridge.canonical_field_key)}} · target_section=${{esc(bridge.target_section)}} · target_line_contract_id=${{esc(bridge.target_line_contract_id)}}<br>
        destination=existing_edit_card_before_after_suggestion_panel · standalone_blue_card_created=false
      </div>
      <div class="r87-modal-actions">
        <button type="button" data-r87-action="preview_accept">采纳预览</button>
        <button type="button" data-r87-action="retry">重试</button>
        <button type="button" data-r87-action="cancel">撤回</button>
      </div>
    `;
    body.querySelectorAll("[data-r87-action]").forEach((button) => {{
      button.addEventListener("click", function () {{
        const action = this.getAttribute("data-r87-action");
        const nextStatus = action === "preview_accept"
          ? "已采纳到预览状态，仍未写正式课包。"
          : action === "retry"
            ? "重试按钮已触发 smoke 状态；真实重试留到后续 runtime。"
            : "已撤回本次预览候选。";
        if (status) status.textContent = nextStatus + " formal_apply_allowed=false";
      }});
    }});
    backdrop.classList.add("is-open");
    backdrop.setAttribute("aria-hidden", "false");

    const target = firstExisting(bridge.target_selectors || []);
    if (target) {{
      document.querySelectorAll(".r87-target-highlight").forEach((node) => node.classList.remove("r87-target-highlight"));
      target.classList.add("r87-target-highlight");
      target.scrollIntoView({{ block: "center", behavior: "smooth" }});
      setTimeout(() => target.classList.remove("r87-target-highlight"), 3200);
    }}
  }}

  function installEntry() {{
    if (document.querySelector("[data-r87-generation-entry='true']")) return;
    const host = document.querySelector(".r45r47-model-loop") || document.querySelector(".r30-tool-panel") || document.querySelector(".nb-drawer, .nb-right-rail");
    if (!host) return;
    const bridgeCount = (payload.bridges || []).length;
    const candidateButtons = (payload.bridges || []).map(function (bridge, index) {{
      const labelMap = {{
        classroom_flow: "教学过程",
        lesson_task_evidence: "任务证据",
        assessment_plan: "评价计划",
        courseware_plan: "课件大屏",
        handout_plan: "学习单"
      }};
      const label = labelMap[bridge.schema_key] || bridge.schema_key || "字段";
      return `<button type="button" data-r87-open="${{index}}">打开候选${{index + 1}}：${{esc(label)}}</button>`;
    }}).join("");
    const div = document.createElement("div");
    div.className = "r87-generation-entry";
    div.setAttribute("data-r87-generation-entry", "true");
    div.innerHTML = `
      <div class="r87-generation-entry-head">
        <span>R87生成候选已准备</span>
        <span class="r87-generation-badge">${{esc(payload.source_mode || "fixture_fallback")}}</span>
      </div>
      <div>候选数：${{bridgeCount}} · 点击绿色按钮打开“修改前 / 修改后 / 小教建议”。</div>
      <div class="r87-generation-button-row">
        ${{candidateButtons || '<button type="button" disabled>暂无候选</button>'}}
      </div>
    `;
    host.insertBefore(div, host.firstChild);
    div.querySelectorAll("[data-r87-open]").forEach((button) => {{
      button.addEventListener("click", () => openCandidate(Number(button.getAttribute("data-r87-open") || 0)));
    }});
    if (new URLSearchParams(window.location.search).get("r87_auto_open") === "1") {{
      setTimeout(() => openCandidate(0), 500);
    }}
  }}

  if (document.readyState === "loading") {{
    document.addEventListener("DOMContentLoaded", () => setTimeout(installEntry, 400));
  }} else {{
    setTimeout(installEntry, 400);
  }}
}})();
</script>
"""


def build_r87_html(payload):
    source_html = R21_HTML.read_text(encoding="utf-8")
    injection = build_r87_script(payload)
    if "</body>" not in source_html:
        raise RuntimeError("R21 html missing </body>")
    output_html = source_html.replace("</body>", injection + "\n</body>", 1)
    write_text(R87_HTML, output_html)

    source_still_clean = "data-r87-visible-generation-smoke" not in source_html
    html_checks = {
        "html_exists": R87_HTML.exists(),
        "copied_from_r21": True,
        "r21_source_unmodified_by_r87_marker": source_still_clean,
        "contains_r87_marker": "data-r87-visible-generation-smoke" in output_html,
        "contains_existing_modal_selector": ".r6p-modal-backdrop" in output_html,
        "contains_right_tool_entry_selector": ".r45r47-model-loop" in output_html,
        "contains_existing_edit_card_destination": "existing_edit_card_before_after_suggestion_panel" in output_html,
        "contains_no_standalone_blue_card_marker": "standalone_blue_card_created=true" not in output_html,
    }
    validation = {
        "stage": "1013R_R87_PROVIDER_OR_FIXTURE_VISIBLE_GENERATION_SMOKE",
        "result": "PASS" if all(html_checks.values()) else "FAIL",
        "html": str(R87_HTML),
        "source_r21_html": str(R21_HTML),
        "r21_page_modified": False,
        "copied_page_created": True,
        "provider_success": payload["provider_success"],
        "fallback_used": payload["fallback_used"],
        "visible_candidate_count": len(payload["bridges"]),
        "formal_apply_allowed": False,
        "standalone_blue_card_created": False,
        "html_checks": html_checks,
    }
    write_json(R87_DIR / "validate_1013R_R87_visible_generation_smoke_result.json", validation)
    return validation


def build_docs(validations):
    manifest = {
        "package": "1013R_R83_R87_VISIBLE_GENERATION_CHAIN",
        "created_by": "scripts/build_1013r_r83_r87_visible_generation_chain.py",
        "main_r21_page_modified": False,
        "copied_visible_smoke_page": str(R87_HTML),
        "stages": [
            {
                "stage": "R83",
                "name": "LESSON_GENERATION_NORMALIZER_DRY_RUN",
                "dir": str(R83_DIR),
                "validator": str(R83_DIR / "validate_1013R_R83_normalizer_result.json"),
            },
            {
                "stage": "R84",
                "name": "EDIT_CARD_BRIDGE_VISIBLE_SMOKE",
                "dir": str(R84_DIR),
                "validator": str(R84_DIR / "validate_1013R_R84_edit_card_bridge_result.json"),
            },
            {
                "stage": "R85",
                "name": "LOCAL_FIXTURE_VISIBLE_GENERATION_SMOKE",
                "dir": str(R85_DIR),
                "validator": str(R85_DIR / "validate_1013R_R85_local_fixture_visible_result.json"),
            },
            {
                "stage": "R86",
                "name": "PROVIDER_SANDBOX_DRY_RUN",
                "dir": str(R86_DIR),
                "validator": str(R86_DIR / "validate_1013R_R86_provider_sandbox_result.json"),
            },
            {
                "stage": "R87",
                "name": "PROVIDER_OR_FIXTURE_VISIBLE_GENERATION_SMOKE",
                "dir": str(R87_DIR),
                "validator": str(R87_DIR / "validate_1013R_R87_visible_generation_smoke_result.json"),
            },
        ],
        "validation_summary": validations,
    }
    write_json(R87_DIR / "REVIEW_PACKAGE_MANIFEST.json", manifest)

    readme = f"""# 1013R R83-R87 可见生成链路

本包把 R82 的生成契约往后推进到 R87，但不修改主 R21 页面。

## 边界

- 主 R21 页面未写入 R87 标记：`{R21_HTML}`
- R87 是复制页可见 smoke：`{R87_HTML}`
- 候选只进入旧编辑卡弹层：`existing_edit_card_before_after_suggestion_panel`
- 不生成正文独立蓝卡
- 不 formal apply
- 不写数据库、飞书、记忆或正式课包

## 阶段

- R83：normalizer dry run，校验 R82 valid/invalid fixtures。
- R84：把候选桥接到旧编辑卡 before/after/suggestion 三槽。
- R85：本地 fixture 可见生成 smoke。
- R86：provider sandbox dry run；如果 provider 输出未过契约，自动回退 R82 fixture。
- R87：复制 R21 生成可打开 HTML，右侧工具盒出现“R87生成候选已准备”，点击复用 `.r6p-modal-backdrop`。

## 结果

- R83: `{validations['r83']['result']}`
- R84: `{validations['r84']['result']}`
- R85: `{validations['r85']['result']}`
- R86: `{validations['r86']['result']}` provider_success={validations['r86'].get('provider_success')} fallback_used={validations['r86'].get('fallback_used')}
- R87: `{validations['r87']['result']}`
"""
    write_text(R87_DIR / "README.md", readme)


def main():
    for directory in [R83_DIR, R84_DIR, R85_DIR, R86_DIR, R87_DIR]:
        directory.mkdir(parents=True, exist_ok=True)

    r83_normalized, r83_validation = build_r83()
    r84_payload, r84_validation = build_r84(r83_normalized)
    _r85_payload, r85_validation = build_r85(r84_payload)
    r86_normalized, r86_validation = build_r86(r83_normalized)
    r87_payload = build_r87_payload(r86_normalized, r86_validation)
    r87_validation = build_r87_html(r87_payload)

    validations = {
        "r83": r83_validation,
        "r84": r84_validation,
        "r85": r85_validation,
        "r86": r86_validation,
        "r87": r87_validation,
    }
    build_docs(validations)
    print(json.dumps({
        "result": "PASS" if all(item.get("result", "").startswith("PASS") for item in validations.values()) else "FAIL",
        "r87_html": str(R87_HTML),
        "validations": {key: value.get("result") for key, value in validations.items()},
        "provider_success": r86_validation.get("provider_success"),
        "fallback_used": r86_validation.get("fallback_used"),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
