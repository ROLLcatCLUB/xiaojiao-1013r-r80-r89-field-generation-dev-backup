from __future__ import annotations

import json
from pathlib import Path


BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
R21_HTML = ROOT / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R21_page_copy_binds_unified_package" / "prep_room_page_copy_binds_unified_package_1013R_R21.html"

EXPECTED_SCHEMA_KEYS = [
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
]

EXPECTED_TOP_LEVEL_KEYS = [
    "response_stage",
    "request_id",
    "lesson_design_mode",
    "intent_summary",
    "lesson_logic_brief",
    "target_resolution",
    "step_reasoning_updates",
    "field_patch_candidates",
    "quality_gate_update",
    "material_requests",
    "teacher_questions",
    "ui_binding_hint",
    "boundary_flags",
]

REQUIRED_CANDIDATE_KEYS = [
    "field_patch_id",
    "schema_key",
    "canonical_field_key",
    "target_field_key",
    "target_section",
    "target_step_id",
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
]

ALLOWED_TARGET_SECTIONS = {
    "lesson_header",
    "basis",
    "goals",
    "analysis",
    "keypoints",
    "assessment",
    "teaching_process",
    "courseware_plan",
    "handout_plan",
    "material_requests",
}


def load_json(name: str) -> dict:
    return json.loads((BASE / name).read_text(encoding="utf-8"))


def assert_true(checks: list[dict], name: str, condition: bool, details: str) -> None:
    checks.append({"name": name, "pass": bool(condition), "details": details})
    if not condition:
        raise AssertionError(f"{name}: {details}")


def validate_response(response: dict) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if not isinstance(response, dict):
        return False, ["top_level_not_object"]
    for key in EXPECTED_TOP_LEVEL_KEYS:
        if key not in response:
            errors.append(f"missing_top_level:{key}")
    if errors:
        return False, errors
    if response.get("lesson_logic_brief", {}).get("visual_language_use") and "visual_language" in [c.get("schema_key") for c in response.get("field_patch_candidates", [])]:
        errors.append("visual_language_visible_schema_key")
    for item in response.get("target_resolution", []):
        if item.get("schema_key") not in EXPECTED_SCHEMA_KEYS:
            errors.append("unknown_schema_key")
        if item.get("target_section") not in ALLOWED_TARGET_SECTIONS:
            errors.append("unknown_target_section")
    if not isinstance(response.get("step_reasoning_updates"), list):
        errors.append("step_reasoning_updates_not_array")
    if not isinstance(response.get("field_patch_candidates"), list):
        errors.append("field_patch_candidates_not_array")
        return False, errors
    for patch in response.get("field_patch_candidates", []):
        for key in REQUIRED_CANDIDATE_KEYS:
            if key not in patch:
                errors.append(f"missing_candidate_key:{key}")
        if patch.get("schema_key") not in EXPECTED_SCHEMA_KEYS:
            errors.append("unknown_schema_key")
        if patch.get("target_section") not in ALLOWED_TARGET_SECTIONS:
            errors.append("unknown_target_section")
        if patch.get("target_destination") != "existing_edit_card_before_after_suggestion_panel":
            errors.append("standalone_blue_card_destination")
        if patch.get("formal_apply_allowed") is not False:
            errors.append("formal_apply_allowed_true")
        if patch.get("applied") is not False:
            errors.append("applied_true")
        if patch.get("preview_only") is not True:
            errors.append("preview_only_not_true")
        if patch.get("teacher_review_required") is not True:
            errors.append("teacher_review_required_not_true")
        if not patch.get("target_line_contract_id"):
            errors.append("missing_target_line_contract_id")
        if patch.get("schema_key") == "material_requests" and patch.get("target_section") != "material_requests":
            errors.append("material_requests_wrong_target")
    flags = response.get("boundary_flags", {})
    for key in ["formal_apply_performed", "database_written", "memory_written", "feishu_written", "formal_export_created", "official_archive_created"]:
        if flags.get(key) is not False:
            errors.append(f"side_effect_flag_not_false:{key}")
    if flags.get("teacher_review_required") is not True:
        errors.append("teacher_review_required_boundary_missing")
    return not errors, errors


def main() -> None:
    checks: list[dict] = []
    request = load_json("lesson_generation_request_envelope_1013R_R82.json")
    response_schema = load_json("lesson_generation_response_schema_1013R_R82.json")
    normalizer = load_json("lesson_generation_response_normalizer_contract_1013R_R82.json")
    quality = load_json("lesson_generation_quality_gate_contract_1013R_R82.json")
    fixtures = load_json("lesson_generation_smoke_fixtures_1013R_R82.json")
    prompt = (BASE / "lesson_generation_prompt_contract_1013R_R82.md").read_text(encoding="utf-8")

    assert_true(checks, "request_allows_14_schema_keys", request["allowed_schema_keys"] == EXPECTED_SCHEMA_KEYS, str(request["allowed_schema_keys"]))
    assert_true(checks, "response_top_level_keys_exact", response_schema["top_level_required_keys"] == EXPECTED_TOP_LEVEL_KEYS, str(response_schema["top_level_required_keys"]))
    assert_true(checks, "candidate_required_keys_include_r81", set(REQUIRED_CANDIDATE_KEYS).issubset(set(response_schema["field_patch_candidate_required_keys"])), str(response_schema["field_patch_candidate_required_keys"]))
    assert_true(checks, "normalizer_allowed_schema_keys", normalizer["allowed_schema_keys"] == EXPECTED_SCHEMA_KEYS, str(normalizer["allowed_schema_keys"]))

    for phrase in ["只输出 JSON 对象", "不要 markdown", "不要输出完整正式教案", "schema_key", "existing_edit_card_before_after_suggestion_panel", "禁止 `standalone_blue_card`", "visual_language", "缺教材"]:
        assert_true(checks, f"prompt_contains_{phrase}", phrase in prompt, phrase)

    gate_ids = {gate["gate_id"] for gate in quality["quality_gates"]}
    for gate in ["source_gap_check", "unit_spine_consistency_check", "r81_schema_key_check", "target_section_check", "line_contract_check", "visual_language_hidden_check", "teacher_gate_check", "side_effect_check"]:
        assert_true(checks, f"quality_gate_{gate}", gate in gate_ids, str(gate_ids))

    valid_ok, valid_errors = validate_response(fixtures["valid_response"])
    assert_true(checks, "valid_smoke_response_accepted", valid_ok, str(valid_errors))

    invalid_results = []
    for case in fixtures["invalid_responses"]:
        if "raw_text" in case:
            rejected = case["raw_text"].lstrip().startswith("```")
            reasons = ["markdown_code_fence"] if rejected else []
        else:
            rejected, reasons = validate_response(case["response"])
            rejected = not rejected
        invalid_results.append({"case_id": case["case_id"], "rejected": rejected, "reasons": reasons})
    assert_true(checks, "invalid_smoke_responses_rejected", all(item["rejected"] for item in invalid_results), str(invalid_results))

    if R21_HTML.exists():
        text = R21_HTML.read_text(encoding="utf-8", errors="ignore")
        r21_contains_r82 = "1013R_R82_LESSON_GENERATION_REQUEST_RESPONSE_CONTRACT" in text or "lesson_generation_request_envelope_1013R_R82" in text
    else:
        r21_contains_r82 = False
    assert_true(checks, "r21_not_modified_by_R82_marker", not r21_contains_r82, f"r21_contains_r82={r21_contains_r82}")

    result = {
        "stage": "1013R_R82_LESSON_GENERATION_REQUEST_RESPONSE_CONTRACT",
        "status": "PASS",
        "summary": {
            "allowed_schema_key_count": len(request["allowed_schema_keys"]),
            "response_top_level_key_count": len(response_schema["top_level_required_keys"]),
            "required_candidate_key_count": len(REQUIRED_CANDIDATE_KEYS),
            "valid_smoke_response_accepted": valid_ok,
            "invalid_smoke_responses_rejected": all(item["rejected"] for item in invalid_results),
            "r21_modified_by_r82": r21_contains_r82,
            "model_provider_runtime_connected": False,
            "formal_apply_allowed": False,
        },
        "invalid_results": invalid_results,
        "checks": checks,
    }
    (BASE / "validate_1013R_R82_lesson_generation_request_response_contract_result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
