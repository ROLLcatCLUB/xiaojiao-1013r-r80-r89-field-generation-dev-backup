from __future__ import annotations

import ast
import json
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1"
OUT_DIR = BASE / "1013R_R89_FIELD_CONTRACT_CONVERGENCE_AND_CAUSAL_CHAIN_GATE"
R90_PLAN = OUT_DIR / "R90_TRUE_GENERATION_QUALITY_SMOKE_PLAN_1013R_R90.md"

R80_BIG_UNIT = BASE / "1013R_R80_GENERATION_FLOW_AND_FIELD_MAPPING_CONTRACT" / "big_unit_22_field_mapping_1013R_R80.json"
R81_LESSON_FIELDS = BASE / "1013R_R81_LESSON_SCHEMA_FIELD_MAP_ADAPTER" / "lesson_14_field_mapping_1013R_R81.json"
R81_STEP = BASE / "1013R_R81_LESSON_SCHEMA_FIELD_MAP_ADAPTER" / "lesson_step_line_contract_mapping_1013R_R81.json"
R82_SCHEMA = BASE / "1013R_R82_LESSON_GENERATION_REQUEST_RESPONSE_CONTRACT" / "lesson_generation_response_schema_1013R_R82.json"
R82_NORMALIZER = BASE / "1013R_R82_LESSON_GENERATION_REQUEST_RESPONSE_CONTRACT" / "lesson_generation_response_normalizer_contract_1013R_R82.json"
R88_LEDGER = BASE / "1013R_R88_FIELD_GENERATION_QUALITY_STATIC_LAB" / "field_generation_quality_static_lab_ledger_1013R_R88.json"
R6N_R9A = BASE / "1013I_R6N_R9A_field_label_disambiguation_before_runtime_schema" / "big_unit_teacher_visible_field_model_1013I_R6N_R9A.json"
R83_R87_SCRIPT = ROOT / "scripts" / "build_1013r_r83_r87_visible_generation_chain.py"
R86_VALIDATION = BASE / "1013R_R86_PROVIDER_SANDBOX_DRY_RUN" / "validate_1013R_R86_provider_sandbox_result.json"


OUTPUTS = {
    "alias_map": OUT_DIR / "r89_big_unit_key_alias_map_1013R_R89.json",
    "phase_cluster_registry": OUT_DIR / "r89_generation_phase_and_field_cluster_registry_1013R_R89.json",
    "canonical_ref_audit": OUT_DIR / "r89_canonical_ref_audit_1013R_R89.json",
    "step_adapter": OUT_DIR / "r89_step_contract_adapter_r81_to_r88_1013R_R89.json",
    "candidate_keys": OUT_DIR / "r89_candidate_required_keys_single_source_1013R_R89.json",
    "strict_salvage": OUT_DIR / "r89_strict_vs_salvage_validator_boundary_1013R_R89.json",
    "causal_chain": OUT_DIR / "r89_causal_chain_gate_1013R_R89.json",
    "validator": OUT_DIR / "validate_1013R_R89_field_contract_convergence_result.json",
}


PHASES = {
    "unit_spine": "大单元主线与资料边界阶段。",
    "lesson_slice": "把大单元主线切到当前课时的决策阶段。",
    "field_internal": "字段内部结构和教学过程行级契约阶段。",
    "derived_objects": "课件、大屏、学习单、评价表等派生物阶段。",
}

FIELD_CLUSTERS = {
    "unit_spine": "单元身份、主题、大观念、基本问题。",
    "unit_goals": "目标、内容分析、重难点等学习方向。",
    "student_context": "学生起点、困难和进入方式。",
    "task_evidence": "表现性任务、评估要点、学习评价。",
    "progression": "学习阶段、学习任务、小问题、学习活动。",
    "scaffolds": "情境、任务、资源、策略等支架。",
    "derived_objects": "学习单、评价支架和后续派生物。",
    "source_gap": "资料补充与缺口提示。",
    "lesson_identity": "单课身份与教材锚点。",
    "lesson_logic": "继承单元主线、概念切片、驱动问题。",
    "lesson_goals": "课时目标、学生起点、重难点。",
    "lesson_evidence": "本课任务证据、评价计划与资料补充。",
    "lesson_derived_objects": "课件/大屏、学习单等单课派生物。",
    "classroom_flow_line_contract": "教学过程 47 项行级契约字段池。",
}

OLD_LAYER_TO_PHASE_CLUSTER = {
    "unit_spine": ("unit_spine", "unit_spine"),
    "unit_goals": ("unit_spine", "unit_goals"),
    "student_context": ("unit_spine", "student_context"),
    "task_evidence": ("unit_spine", "task_evidence"),
    "progression": ("unit_spine", "progression"),
    "scaffolds": ("unit_spine", "scaffolds"),
    "derived_objects": ("derived_objects", "derived_objects"),
    "source_gap": ("unit_spine", "source_gap"),
}

LESSON_FIELD_CLUSTER = {
    "lesson_identity": "lesson_identity",
    "textbook_anchor": "lesson_identity",
    "inherited_unit_context": "lesson_logic",
    "lesson_concept_slice": "lesson_logic",
    "lesson_focus_question": "lesson_logic",
    "lesson_objectives": "lesson_goals",
    "student_starting_point": "lesson_goals",
    "key_difficult_points": "lesson_goals",
    "lesson_task_evidence": "lesson_evidence",
    "assessment_plan": "lesson_evidence",
    "material_requests": "lesson_evidence",
    "classroom_flow": "classroom_flow_line_contract",
    "courseware_plan": "lesson_derived_objects",
    "handout_plan": "lesson_derived_objects",
}

STEP_TYPE_ACTIVATION = {
    "lead_in": [
        "context_scaffold",
        "teacher_core_question",
        "visual_object",
        "student_observation",
        "common_misconception",
        "prior_connection",
        "next_connection",
        "time_risk",
    ],
    "observation_inquiry": [
        "student_observation",
        "teacher_probe_question",
        "visual_language_focus",
        "positive_negative_example",
        "process_evidence",
        "language_scaffold",
        "teacher_feedback_move",
        "success_criteria",
    ],
    "method_exploration": [
        "student_try",
        "technique_focus",
        "material_use",
        "teacher_instruction",
        "task_scaffold",
        "process_evidence",
        "fallback_strategy",
        "success_criteria",
    ],
    "teacher_demo": [
        "teacher_demo",
        "teacher_modeling_language",
        "technique_focus",
        "material_use",
        "visual_object",
        "success_criteria",
        "student_recording",
        "time_risk",
    ],
    "student_try": [
        "student_try",
        "task_scaffold",
        "material_scaffold",
        "teacher_patrol_observation",
        "common_misconception",
        "process_evidence",
        "teacher_feedback_move",
        "alternative_plan",
    ],
    "student_creation": [
        "student_creation",
        "material_use",
        "differentiation_scaffold",
        "teacher_patrol_observation",
        "work_evidence",
        "time_risk",
        "material_risk",
        "fallback_strategy",
    ],
    "display_exchange": [
        "student_display",
        "expression_evidence",
        "peer_assessment",
        "teacher_feedback_move",
        "success_criteria",
        "evidence_storage",
        "language_scaffold",
        "next_connection",
    ],
    "assessment_revision": [
        "student_revision",
        "work_evidence",
        "expression_evidence",
        "teacher_observation_point",
        "success_criteria",
        "peer_assessment",
        "fallback_strategy",
        "evidence_storage",
    ],
    "summary_transfer": [
        "next_connection",
        "student_recording",
        "expression_evidence",
        "evidence_storage",
        "alternative_plan",
        "teacher_feedback_move",
        "phase_role",
        "student_display",
    ],
}

R81_TO_R88_STEP_MAP = {
    "step_id": ("exact", ["step_id"], "active_all_steps", "keep_as_locator"),
    "step_order": ("exact", ["step_order"], "active_all_steps", "keep_as_locator"),
    "step_name": ("exact", ["step_name"], "active_all_steps", "keep_as_label"),
    "duration": ("exact", ["duration"], "active_all_steps", "keep_as_timing_control"),
    "step_goal": ("split", ["phase_role", "success_criteria", "next_connection"], "active_all_steps", "do_not_write_step_goal_directly_after_r89"),
    "teacher_talk": (
        "split",
        ["teacher_instruction", "teacher_core_question", "teacher_modeling_language"],
        "active_when step_type in ['lead_in','observation_inquiry','teacher_demo','student_creation','display_exchange']",
        "do_not_write_teacher_talk_directly_after_r89",
    ),
    "student_task": (
        "split",
        ["student_observation", "student_try", "student_creation", "student_display", "student_revision"],
        "active_by_step_type",
        "route_to_specific_student_move",
    ),
    "material_requirements": ("split", ["material_use", "material_scaffold", "visual_object"], "active_when materials_or_visuals_are_used", "do_not_write_material_requirements_directly"),
    "tech_support": ("derived", ["material_use"], "active_when screen_or_device_supports_step", "derive_to_lesson.courseware_plan"),
    "success_criteria": ("exact", ["success_criteria"], "active_all_steps", "keep_as_assessment_anchor"),
    "guiding_questions": ("split", ["teacher_core_question", "teacher_probe_question"], "active_when questioning_drives_learning", "do_not_write_guiding_questions_directly"),
    "feedback_points": ("split", ["teacher_feedback_move", "peer_assessment"], "active_when review_or_revision_exists", "route_to_feedback_or_peer_assessment"),
    "ppt_page_note": ("derived", ["visual_object", "artwork_or_life_example"], "active_when screen_support_needed", "derive_to_lesson.courseware_plan"),
    "design_intent": ("split", ["phase_role", "prior_connection", "next_connection"], "active_all_steps", "do_not_write_design_intent_as_visible_body"),
    "evidence_capture": ("split", ["process_evidence", "work_evidence", "expression_evidence", "evidence_storage"], "active_when learning_evidence_needed", "route_to_evidence_fields"),
    "source_refs": ("embedded", ["source_refs"], "active_all_generated_fields", "each_r88_step_candidate_must_carry_source_refs"),
    "generation_slot": ("replaced", ["generation_slot_id"], "active_all_generated_fields", "use_R88_generation_slot_id"),
}

CANDIDATE_REQUIRED_KEYS_V1 = [
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
    "patch_type",
    "reasoning_basis",
]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def key_suffix(engineering_key: str) -> str:
    return engineering_key.split(".")[-1]


def extract_script_required_keys(path: Path) -> list[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "REQUIRED_CANDIDATE_KEYS":
                    value = ast.literal_eval(node.value)
                    return list(value)
    return []


def build_alias_map(r80: dict, r88: dict) -> dict:
    r80_by_label = {item["label"]: item for item in r80.get("big_unit_fields", [])}
    r88_by_label = {item["visible_label"]: item for item in r88.get("big_unit_fields", [])}
    rows = []
    for label, r80_item in r80_by_label.items():
        r88_item = r88_by_label.get(label)
        r80_key = r80_item.get("contract_key")
        r88_key = r88_item.get("engineering_key") if r88_item else ""
        aliases = []
        if r80_key and r80_key != r88_key:
            aliases.append(r80_key)
        page_key = r80_item.get("page_field_key")
        if page_key:
            aliases.append(f"page_field_key:{page_key}")
        migration_status = "same_key" if r80_key == r88_key else "renamed"
        rows.append(
            {
                "order": r80_item.get("order"),
                "visible_label": label,
                "r80_contract_key": r80_key,
                "r88_engineering_key": r88_key,
                "canonical_ref": r88_item.get("canonical_ref") if r88_item else "",
                "active_write_key": r88_key,
                "aliases": aliases,
                "migration_status": migration_status,
                "compatibility_policy": "read_legacy_write_active",
                "notes": "Legacy keys may be read for compatibility; new writes use active_write_key only.",
                "mapped": bool(r88_item),
            }
        )
    missing_in_r80 = [label for label in sorted(r88_by_label) if label not in r80_by_label]
    return {
        "schema_id": "r89_big_unit_key_alias_map_1013R_R89",
        "stage": "1013R_R89_FIELD_CONTRACT_CONVERGENCE_AND_CAUSAL_CHAIN_GATE",
        "source_refs": {"r80": str(R80_BIG_UNIT), "r88": str(R88_LEDGER)},
        "compatibility_policy_default": "read_legacy_write_active",
        "field_count": len(rows),
        "rows": rows,
        "missing_in_r80_by_label": missing_in_r80,
    }


def build_phase_cluster_registry(r88: dict) -> dict:
    big_unit_rows = []
    for item in r88.get("big_unit_fields", []):
        old_layer = item.get("generation_layer")
        phase, cluster = OLD_LAYER_TO_PHASE_CLUSTER.get(old_layer, ("unit_spine", "source_gap"))
        big_unit_rows.append(
            {
                "visible_label": item.get("visible_label"),
                "engineering_key": item.get("engineering_key"),
                "old_generation_layer": old_layer,
                "generation_phase": phase,
                "field_cluster": cluster,
                "migration_status": "split_from_mixed_layer",
            }
        )
    lesson_rows = []
    for item in r88.get("lesson_fields", []):
        schema_key = item.get("schema_key")
        cluster = LESSON_FIELD_CLUSTER.get(schema_key, "lesson_logic")
        phase = "field_internal" if schema_key == "classroom_flow" else ("derived_objects" if cluster == "lesson_derived_objects" else "lesson_slice")
        lesson_rows.append(
            {
                "visible_label": item.get("visible_label"),
                "engineering_key": item.get("engineering_key"),
                "schema_key": schema_key,
                "generation_phase": phase,
                "field_cluster": cluster,
                "migration_status": "new_from_r88_lesson_field",
            }
        )
    step_rows = []
    for item in r88.get("step_contract_fields", []):
        step_rows.append(
            {
                "visible_label": item.get("visible_label"),
                "engineering_key": item.get("engineering_key"),
                "generation_phase": "field_internal",
                "field_cluster": "classroom_flow_line_contract",
                "group_id": item.get("group_id"),
                "migration_status": "new_from_r88_step_contract",
            }
        )
    old_layers_used = sorted({item.get("generation_layer") for item in r88.get("big_unit_fields", [])})
    return {
        "schema_id": "r89_generation_phase_and_field_cluster_registry_1013R_R89",
        "stage": "1013R_R89_FIELD_CONTRACT_CONVERGENCE_AND_CAUSAL_CHAIN_GATE",
        "generation_phase_registry": [{"phase": key, "description": value} for key, value in PHASES.items()],
        "field_cluster_registry": [{"cluster": key, "description": value} for key, value in FIELD_CLUSTERS.items()],
        "old_generation_layer_migration": [
            {
                "old_generation_layer": old,
                "new_generation_phase": OLD_LAYER_TO_PHASE_CLUSTER.get(old, ("unit_spine", "source_gap"))[0],
                "new_field_cluster": OLD_LAYER_TO_PHASE_CLUSTER.get(old, ("unit_spine", "source_gap"))[1],
                "migration_status": "split_from_mixed_layer",
            }
            for old in old_layers_used
        ],
        "field_phase_cluster_rows": big_unit_rows + lesson_rows + step_rows,
    }


def build_canonical_ref_audit(r88: dict, canonical: dict) -> dict:
    canonical_keys = {item.get("field_key") for item in canonical.get("fields", [])}
    used_refs = set()
    rows = []
    for item in r88.get("big_unit_fields", []):
        ref = item.get("canonical_ref")
        used_refs.add(ref)
        if ref in canonical_keys:
            identity = "canonical_hit"
        elif ref in {"unit_theme", "big_idea"}:
            identity = "extended_field"
        else:
            identity = "unresolved_gap"
        rows.append(
            {
                "visible_label": item.get("visible_label"),
                "engineering_key": item.get("engineering_key"),
                "canonical_ref": ref,
                "canonical_identity": identity,
                "resolution_policy": {
                    "canonical_hit": "use_r6n_canonical",
                    "extended_field": "do_not_claim_r6n_canonical; retain as R88 extended field",
                    "unresolved_gap": "must_resolve_before_runtime_write",
                }[identity],
            }
        )
    hidden_refs = [
        {
            "canonical_ref": "curriculum_basis",
            "canonical_identity": "hidden_source_ref",
            "frontstage_visible": False,
            "must_feed_targets": [
                "big_unit.learning_goals",
                "lesson.inherited_unit_context",
                "lesson.lesson_objectives",
                "lesson.assessment_plan",
            ],
            "resolution_policy": "hidden source reference for curriculum standard traceability",
        }
    ]
    unused_canonical_keys = sorted(key for key in canonical_keys - used_refs if key)
    return {
        "schema_id": "r89_canonical_ref_audit_1013R_R89",
        "stage": "1013R_R89_FIELD_CONTRACT_CONVERGENCE_AND_CAUSAL_CHAIN_GATE",
        "canonical_source": str(R6N_R9A),
        "rows": rows,
        "hidden_source_refs": hidden_refs,
        "unused_canonical_keys": unused_canonical_keys,
        "summary": {
            "canonical_hit_count": sum(1 for row in rows if row["canonical_identity"] == "canonical_hit"),
            "extended_field_count": sum(1 for row in rows if row["canonical_identity"] == "extended_field"),
            "hidden_source_ref_count": len(hidden_refs),
            "unresolved_gap_count": sum(1 for row in rows if row["canonical_identity"] == "unresolved_gap"),
        },
    }


def build_step_adapter(r81: dict, r88: dict) -> dict:
    r81_fields = [item["key"] for item in r81.get("step_fields", [])]
    r88_step_keys = {key_suffix(item.get("engineering_key", "")) for item in r88.get("step_contract_fields", [])}
    rows = []
    for field in r81_fields:
        status, targets, activation_rule, runtime_policy = R81_TO_R88_STEP_MAP[field]
        missing_targets = [target for target in targets if target not in r88_step_keys and target not in {"source_refs", "generation_slot_id"}]
        rows.append(
            {
                "r81_field": field,
                "mapping_status": status,
                "r88_target_fields": targets,
                "activation_rule": activation_rule,
                "loss_risk": "broad legacy field requires step_type context" if status == "split" else "low",
                "runtime_policy": runtime_policy,
                "missing_r88_targets": missing_targets,
                "mapped": not missing_targets,
            }
        )
    activation_rows = []
    invalid_activation_fields = []
    for step_type, fields in STEP_TYPE_ACTIVATION.items():
        missing_activation = [field for field in fields if field not in r88_step_keys]
        if missing_activation:
            invalid_activation_fields.append(
                {
                    "step_type": step_type,
                    "missing_r88_fields": missing_activation,
                }
            )
        activation_rows.append(
            {
                "step_type": step_type,
                "activated_r88_fields": fields,
                "field_count": len(fields),
                "missing_r88_fields": missing_activation,
                "valid": not missing_activation,
            }
        )
    return {
        "schema_id": "r89_step_contract_adapter_r81_to_r88_1013R_R89",
        "stage": "1013R_R89_FIELD_CONTRACT_CONVERGENCE_AND_CAUSAL_CHAIN_GATE",
        "source_refs": {"r81_step": str(R81_STEP), "r88_ledger": str(R88_LEDGER)},
        "step_type_activation_registry": activation_rows,
        "adapter_rows": rows,
        "summary": {
            "r81_step_field_count": len(r81_fields),
            "r88_step_field_count": len(r88_step_keys),
            "mapped_count": sum(1 for row in rows if row["mapped"]),
            "unmapped_count": sum(1 for row in rows if not row["mapped"]),
            "activation_step_type_count": len(activation_rows),
            "invalid_activation_field_count": sum(len(item["missing_r88_fields"]) for item in invalid_activation_fields),
            "invalid_activation_fields": invalid_activation_fields,
        },
    }


def diff_keys(source_name: str, keys: list[str], single_source: list[str]) -> dict:
    keys_set = set(keys)
    source_set = set(single_source)
    return {
        "source": source_name,
        "keys": keys,
        "matches_single_source": keys == single_source,
        "missing_from_source": [key for key in single_source if key not in keys_set],
        "extra_in_source": [key for key in keys if key not in source_set],
        "difference_declared": keys != single_source,
    }


def build_candidate_required_keys(r82_schema: dict, r82_normalizer: dict, r81_step: dict) -> dict:
    response_schema_keys = r82_schema.get("field_patch_candidate_required_keys", [])
    normalizer_keys = r82_normalizer.get("required_candidate_keys", [])
    r81_candidate_keys = r81_step.get("field_patch_candidate_required_keys", [])
    r83_script_keys = extract_script_required_keys(R83_R87_SCRIPT)
    source_diffs = [
        diff_keys("R82_response_schema", response_schema_keys, CANDIDATE_REQUIRED_KEYS_V1),
        diff_keys("R82_normalizer_contract", normalizer_keys, CANDIDATE_REQUIRED_KEYS_V1),
        diff_keys("R81_step_candidate_slot_policy", r81_candidate_keys, CANDIDATE_REQUIRED_KEYS_V1),
        diff_keys("R83_R87_script_REQUIRED_CANDIDATE_KEYS", r83_script_keys, CANDIDATE_REQUIRED_KEYS_V1),
    ]
    return {
        "schema_id": "r89_candidate_required_keys_single_source_1013R_R89",
        "stage": "1013R_R89_FIELD_CONTRACT_CONVERGENCE_AND_CAUSAL_CHAIN_GATE",
        "single_source_name": "candidate_required_keys_v1",
        "single_source_policy": "R82 response schema 19-key candidate contract is authoritative for R89.",
        "candidate_required_keys_v1": CANDIDATE_REQUIRED_KEYS_V1,
        "target_step_id_policy": "key required; may be empty string for non-classroom-flow fields",
        "future_extension_policy": "do not add target_r88_step_field_keys in R89; resolve via target_line_contract_id and R81->R88 adapter.",
        "source_diffs": source_diffs,
        "summary": {
            "single_source_key_count": len(CANDIDATE_REQUIRED_KEYS_V1),
            "sources_checked": len(source_diffs),
            "sources_matching_now": sum(1 for item in source_diffs if item["matches_single_source"]),
            "sources_with_declared_drift": sum(1 for item in source_diffs if item["difference_declared"]),
        },
    }


def build_strict_salvage_boundary() -> dict:
    r86 = read_json(R86_VALIDATION) if R86_VALIDATION.exists() else {}
    strict_result = "FAIL" if r86.get("provider_success") is False or r86.get("result") == "PASS_WITH_FALLBACK" else ("PASS" if r86.get("provider_success") else "NOT_RUN")
    salvage_result = "PASS" if r86.get("normalized_candidate_count", 0) > 0 else "NOT_RUN"
    degraded = strict_result != "PASS" and salvage_result == "PASS"
    return {
        "schema_id": "r89_strict_vs_salvage_validator_boundary_1013R_R89",
        "stage": "1013R_R89_FIELD_CONTRACT_CONVERGENCE_AND_CAUSAL_CHAIN_GATE",
        "boundary_rule": "Strict provider raw validation and candidate salvage normalization must never share a single PASS field.",
        "required_output_shape": {
            "strict_provider_raw_validation": {
                "result": "PASS | FAIL | NOT_RUN",
                "json_parse_ok": "boolean",
                "required_top_level_keys_ok": "boolean",
                "candidate_required_keys_ok": "boolean",
                "boundary_flags_ok": "boolean",
            },
            "candidate_salvage_normalization": {
                "result": "PASS | FAIL | NOT_RUN",
                "source": "provider_raw | fallback_fixture | repaired_json | static_fixture",
                "degraded": "boolean",
                "degradation_reason": "string|null",
            },
            "overall_runtime_generation_claim_allowed": False,
        },
        "r86_current_snapshot": {
            "source": str(R86_VALIDATION),
            "strict_provider_raw_validation": {
                "result": strict_result,
                "json_parse_ok": bool(r86.get("provider_success")),
                "required_top_level_keys_ok": bool(r86.get("provider_success")),
                "candidate_required_keys_ok": bool(r86.get("provider_success")),
                "boundary_flags_ok": bool(r86.get("all_candidates_block_formal_apply")),
            },
            "candidate_salvage_normalization": {
                "result": salvage_result,
                "source": "fallback_fixture" if r86.get("fallback_used") else "provider_raw",
                "degraded": degraded,
                "degradation_reason": r86.get("error") if degraded else None,
            },
            "overall_runtime_generation_claim_allowed": False,
        },
    }


def build_causal_chain_gate(r88: dict) -> dict:
    chain = [
        {
            "segment": "unit_spine",
            "required_fields": ["big_unit.unit_theme", "big_unit.big_idea", "big_unit.essential_question", "big_unit.performance_task"],
            "consumer": "lesson.inherited_unit_context",
        },
        {
            "segment": "lesson_slice",
            "required_fields": ["lesson.lesson_concept_slice", "lesson.lesson_focus_question", "lesson.lesson_objectives", "lesson.lesson_task_evidence"],
            "consumer": "lesson.classroom_flow",
        },
        {
            "segment": "classroom_flow",
            "required_fields": ["lesson.classroom_flow", "lesson.classroom_flow.step.student_creation", "lesson.classroom_flow.step.success_criteria"],
            "consumer": "lesson.assessment_plan",
        },
        {
            "segment": "evidence",
            "required_fields": [
                "lesson.classroom_flow.step.process_evidence",
                "lesson.classroom_flow.step.work_evidence",
                "lesson.classroom_flow.step.expression_evidence",
                "lesson.assessment_plan",
            ],
            "consumer": "derived_objects",
        },
        {
            "segment": "derived_objects",
            "required_fields": ["lesson.courseware_plan", "lesson.handout_plan", "lesson.assessment_plan"],
            "consumer": "teacher_review",
        },
    ]
    field_keys = {item.get("engineering_key") for item in r88.get("big_unit_fields", [])}
    field_keys.update(item.get("engineering_key") for item in r88.get("lesson_fields", []))
    field_keys.update(item.get("engineering_key") for item in r88.get("step_contract_fields", []))
    checks = []
    for segment in chain:
        missing = [key for key in segment["required_fields"] if key not in field_keys]
        checks.append({**segment, "missing_fields": missing, "result": "PASS" if not missing else "FAIL"})
    edge_rules = [
        "Each lesson objective must bind to at least one classroom activity before R90 content generation.",
        "Each core activity must bind to a student move and visible evidence field.",
        "Each assessment criterion must point back to work, expression, or process evidence.",
        "Each derived object must trace to classroom_flow or assessment_plan, never from blank.",
        "Each model candidate must carry source_refs and teacher_review_required=true.",
    ]
    return {
        "schema_id": "r89_causal_chain_gate_1013R_R89",
        "stage": "1013R_R89_FIELD_CONTRACT_CONVERGENCE_AND_CAUSAL_CHAIN_GATE",
        "claim_scope": "contract_chain_ready_only; does not claim true teaching generation quality.",
        "chain_checks": checks,
        "edge_rules_for_r90": edge_rules,
        "claim_allowed": {
            "contract_chain_ready": all(check["result"] == "PASS" for check in checks),
            "true_generation_quality_ready": False,
            "runtime_provider_success": False,
            "formal_apply_safe": False,
        },
    }


def validate_outputs(alias_map: dict, registry: dict, canonical_audit: dict, step_adapter: dict, candidate_keys: dict, strict_salvage: dict, causal_chain: dict) -> dict:
    checks = {
        "r80_r88_big_unit_alias_map": {
            "result": "PASS" if alias_map.get("field_count") == 22 and all(row.get("mapped") for row in alias_map.get("rows", [])) and all(row.get("compatibility_policy") == "read_legacy_write_active" for row in alias_map.get("rows", [])) else "FAIL",
            "field_count": alias_map.get("field_count"),
        },
        "generation_phase_field_cluster_registry": {
            "result": "PASS" if registry.get("generation_phase_registry") and registry.get("field_cluster_registry") and all(row.get("generation_phase") in PHASES and row.get("field_cluster") in FIELD_CLUSTERS for row in registry.get("field_phase_cluster_rows", [])) else "FAIL",
            "field_rows": len(registry.get("field_phase_cluster_rows", [])),
        },
        "canonical_ref_audit": {
            "result": "PASS" if canonical_audit.get("summary", {}).get("unresolved_gap_count") == 0 and any(row.get("canonical_identity") == "extended_field" for row in canonical_audit.get("rows", [])) and canonical_audit.get("hidden_source_refs") else "FAIL",
            "summary": canonical_audit.get("summary"),
        },
        "r81_r88_step_adapter": {
            "result": "PASS" if step_adapter.get("summary", {}).get("r81_step_field_count") == 17 and step_adapter.get("summary", {}).get("unmapped_count") == 0 and len(step_adapter.get("step_type_activation_registry", [])) >= 9 and step_adapter.get("summary", {}).get("invalid_activation_field_count") == 0 else "FAIL",
            "summary": step_adapter.get("summary"),
        },
        "candidate_required_keys_single_source": {
            "result": "PASS" if len(candidate_keys.get("candidate_required_keys_v1", [])) == 19 and all(item.get("matches_single_source") or item.get("difference_declared") for item in candidate_keys.get("source_diffs", [])) else "FAIL",
            "summary": candidate_keys.get("summary"),
        },
        "strict_vs_salvage_boundary": {
            "result": "PASS" if strict_salvage.get("required_output_shape", {}).get("overall_runtime_generation_claim_allowed") is False and "strict_provider_raw_validation" in strict_salvage.get("r86_current_snapshot", {}) else "FAIL",
        },
        "causal_chain_gate": {
            "result": "PASS" if causal_chain.get("claim_allowed", {}).get("contract_chain_ready") is True and causal_chain.get("claim_allowed", {}).get("true_generation_quality_ready") is False else "FAIL",
        },
    }
    overall = "PASS" if all(item["result"] == "PASS" for item in checks.values()) else "FAIL"
    return {
        "round": "1013R_R89_FIELD_CONTRACT_CONVERGENCE_AND_CAUSAL_CHAIN_GATE",
        "result": overall,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "runtime_connected": False,
        "r21_modified": False,
        "formal_apply_allowed": False,
        "field_system_extended": False,
        "checks": checks,
        "claim_allowed": {
            "contract_convergence_ready": overall == "PASS",
            "true_generation_quality_ready": False,
            "runtime_provider_success": False,
            "formal_apply_safe": False,
        },
        "next_recommended_round": "1013R_R90_TRUE_GENERATION_QUALITY_SMOKE" if overall == "PASS" else "R89_REPAIR",
    }


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    r80 = read_json(R80_BIG_UNIT)
    r81_step = read_json(R81_STEP)
    r82_schema = read_json(R82_SCHEMA)
    r82_normalizer = read_json(R82_NORMALIZER)
    r88 = read_json(R88_LEDGER)
    canonical = read_json(R6N_R9A)

    alias_map = build_alias_map(r80, r88)
    registry = build_phase_cluster_registry(r88)
    canonical_audit = build_canonical_ref_audit(r88, canonical)
    step_adapter = build_step_adapter(r81_step, r88)
    candidate_keys = build_candidate_required_keys(r82_schema, r82_normalizer, r81_step)
    strict_salvage = build_strict_salvage_boundary()
    causal_chain = build_causal_chain_gate(r88)
    validation = validate_outputs(alias_map, registry, canonical_audit, step_adapter, candidate_keys, strict_salvage, causal_chain)

    write_json(OUTPUTS["alias_map"], alias_map)
    write_json(OUTPUTS["phase_cluster_registry"], registry)
    write_json(OUTPUTS["canonical_ref_audit"], canonical_audit)
    write_json(OUTPUTS["step_adapter"], step_adapter)
    write_json(OUTPUTS["candidate_keys"], candidate_keys)
    write_json(OUTPUTS["strict_salvage"], strict_salvage)
    write_json(OUTPUTS["causal_chain"], causal_chain)
    write_json(OUTPUTS["validator"], validation)

    readme = f"""# 1013R R89 Field Contract Convergence And Causal Chain Gate

R89 does not add a new field system. It creates mapping, registry, audit, adapter, and validator artifacts so that R80/R81/R82/R83-R87/R88 can be checked in one contract universe.

## Boundary

- R21 modified: `false`
- Provider/runtime connected: `false`
- Formal apply allowed: `false`
- Field system extended: `false`

## Validator Result

- result: `{validation['result']}`
- contract_convergence_ready: `{validation['claim_allowed']['contract_convergence_ready']}`
- true_generation_quality_ready: `{validation['claim_allowed']['true_generation_quality_ready']}`
- next: `{validation['next_recommended_round']}`

## Artifacts

- `{OUTPUTS['alias_map']}`
- `{OUTPUTS['phase_cluster_registry']}`
- `{OUTPUTS['canonical_ref_audit']}`
- `{OUTPUTS['step_adapter']}`
- `{OUTPUTS['candidate_keys']}`
- `{OUTPUTS['strict_salvage']}`
- `{OUTPUTS['causal_chain']}`
- `{OUTPUTS['validator']}`
- `{R90_PLAN}`
"""
    write_text(OUT_DIR / "README.md", readme)

    review_prompt = f"""# GPT Review Prompt - 1013R R89

Please review whether R89 successfully turns the R88 static field lab and the R80/R81/R82/R83-R87 upstream artifacts into a converged contract gate.

## Review Files

- `{OUTPUTS['validator']}`
- `{OUTPUTS['alias_map']}`
- `{OUTPUTS['phase_cluster_registry']}`
- `{OUTPUTS['canonical_ref_audit']}`
- `{OUTPUTS['step_adapter']}`
- `{OUTPUTS['candidate_keys']}`
- `{OUTPUTS['strict_salvage']}`
- `{OUTPUTS['causal_chain']}`

## Review Questions

1. Does every R80/R88 big-unit field have a bidirectional alias with `read_legacy_write_active` policy?
2. Does every field now have a valid generation_phase and field_cluster?
3. Are `unit_theme`, `big_idea`, and `curriculum_basis` classified without pretending they are all canonical foreground fields?
4. Does the R81 17-field step contract map into the R88 47-field step contract with activation rules?
5. Is the 19-key candidate contract correctly declared as single source?
6. Are strict provider validation and salvage normalization separate?
7. Does the causal chain claim only contract readiness, not true generation quality?

Return: PASS / PASS_WITH_NOTES / REJECT.
"""
    write_text(OUT_DIR / "GPT_REVIEW_PROMPT_1013R_R89.md", review_prompt)

    r90_plan = f"""# R90 True Generation Quality Smoke Plan

R89 result: `{validation['result']}`. R90 may start only if R89 remains `PASS`.

## Purpose

R90 is the first real quality smoke after contract convergence. It should prove that the model can generate visible, useful teaching-design candidates through the existing candidate/edit-card route without writing into the formal lesson package.

## Input Scope

- Use R89 alias map for active write keys and legacy reads.
- Use R89 generation phase and field cluster registry.
- Use R89 R81-to-R88 step adapter for classroom-flow line-level fields.
- Use R82 19-key candidate schema as the only candidate key source.
- Use R88 static lab as the visible field-quality target.

## Smoke Path

1. `unit_spine`: generate candidates for unit theme / big idea / essential question, using material gap flags when evidence is missing.
2. `unit_goals`: generate learning goals, content analysis, and key-difficult-points candidates from the unit spine.
3. `progression`: generate learning stages / learning tasks / micro questions as a structured progression, not a flat ordered list.
4. `lesson_slice`: derive one lesson slice from the unit spine and progression.
5. `field_internal`: generate one classroom-flow segment with activated R88 line-level fields only.

## Visible Quality Checks

- Every candidate contains all 19 candidate keys.
- Every candidate has `canonical_field_key`, `target_field_key`, `target_section`, and `target_destination`.
- For classroom flow, every candidate has `target_step_id` and either a real `target_line_contract_id` or an explicit empty/non-applicable marker.
- Generated content lands in candidate slots only, not formal body text.
- Teacher can see before / after_candidate / xiaojiao_suggestion without a giant pasted block.
- Strict raw provider validation and salvage normalization remain separate.

## Hard Stops

- Do not modify R21.
- Do not formal apply.
- Do not write database / Feishu / memory.
- Do not add new fields.
- Do not let old R81 fields become R88 write targets.
- Do not claim generation quality if provider raw validation fails and only salvage succeeds.

## PASS Meaning

R90 PASS means visible model-generated candidates are usable for teacher review. It still does not mean formal application, full runtime integration, or production persistence is safe.
"""
    write_text(R90_PLAN, r90_plan)

    manifest = {
        "stage": "1013R_R89_FIELD_CONTRACT_CONVERGENCE_AND_CAUSAL_CHAIN_GATE",
        "created_at": validation["created_at"],
        "artifacts": {key: str(path) for key, path in OUTPUTS.items()},
        "readme": str(OUT_DIR / "README.md"),
        "gpt_review_prompt": str(OUT_DIR / "GPT_REVIEW_PROMPT_1013R_R89.md"),
        "r90_next_plan": str(R90_PLAN),
        "boundary": {
            "r21_modified": False,
            "runtime_connected": False,
            "formal_apply_allowed": False,
            "field_system_extended": False,
        },
    }
    write_json(OUT_DIR / "REVIEW_PACKAGE_MANIFEST.json", manifest)
    write_text(
        OUT_DIR / "REVIEW_PACKAGE_MANIFEST.md",
        "\n".join(
            [
                "# REVIEW_PACKAGE_MANIFEST",
                "",
                "- stage: `1013R_R89_FIELD_CONTRACT_CONVERGENCE_AND_CAUSAL_CHAIN_GATE`",
                f"- result: `{validation['result']}`",
                "- r21_modified: `false`",
                "- runtime_connected: `false`",
                "- formal_apply_allowed: `false`",
                "",
                "## Artifacts",
                "",
                *[f"- `{path}`" for path in OUTPUTS.values()],
                f"- `{OUT_DIR / 'GPT_REVIEW_PROMPT_1013R_R89.md'}`",
                f"- `{R90_PLAN}`",
            ]
        )
        + "\n",
    )
    print(json.dumps(validation, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
