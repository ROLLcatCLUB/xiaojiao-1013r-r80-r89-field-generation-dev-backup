from __future__ import annotations

import json
from pathlib import Path


BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
R21_HTML = ROOT / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R21_page_copy_binds_unified_package" / "prep_room_page_copy_binds_unified_package_1013R_R21.html"

EXPECTED_LESSON_KEYS = [
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

EXPECTED_SECTIONS = {"basis", "analysis", "goals", "keypoints", "teaching_process", "assessment", "material_requests"}
MINIMUM_STEP_FIELDS = [
    "step_goal",
    "teacher_talk",
    "student_task",
    "success_criteria",
    "guiding_questions",
    "source_refs",
    "generation_slot",
]


def load_json(name: str) -> dict:
    return json.loads((BASE / name).read_text(encoding="utf-8"))


def assert_true(checks: list[dict], name: str, condition: bool, details: str) -> None:
    checks.append({"name": name, "pass": bool(condition), "details": details})
    if not condition:
        raise AssertionError(f"{name}: {details}")


def main() -> None:
    checks: list[dict] = []
    lesson = load_json("lesson_14_field_mapping_1013R_R81.json")
    steps = load_json("lesson_step_line_contract_mapping_1013R_R81.json")
    migration = load_json("r79b_lesson_field_migration_adapter_1013R_R81.json")
    envelope = load_json("lesson_candidate_envelope_contract_1013R_R81.json")
    flow = (BASE / "lesson_generation_flow_to_existing_surface_1013R_R81.md").read_text(encoding="utf-8")
    foundation = (BASE / "existing_foundation_reuse_report_1013R_R81.md").read_text(encoding="utf-8")

    fields = lesson["lesson_fields"]
    keys = [item["schema_key"] for item in fields]
    assert_true(checks, "covers_14_lesson_schema_fields", keys == EXPECTED_LESSON_KEYS, str(keys))
    assert_true(checks, "all_candidates_preview_only", all(item["formal_apply_allowed"] is False for item in fields), "formal_apply_allowed false for all")

    target_sections = {item["target_section_id"] for item in fields}
    assert_true(checks, "maps_to_existing_sections", EXPECTED_SECTIONS.issubset(target_sections), str(sorted(target_sections)))
    assert_true(checks, "classroom_flow_routes_to_teaching_process", next(item for item in fields if item["schema_key"] == "classroom_flow")["target_section_id"] == "teaching_process", "classroom_flow target")
    assert_true(checks, "courseware_routes_right_rail", next(item for item in fields if item["schema_key"] == "courseware_plan")["route_role"] == "derived_object_preview", "courseware route")
    assert_true(checks, "material_requests_action_prompt_only", next(item for item in fields if item["schema_key"] == "material_requests")["candidate_policy"] == "action_prompt_only_no_formal_write", "material policy")

    step_keys = [item["key"] for item in steps["step_fields"]]
    assert_true(checks, "step_contract_fields_present", len(step_keys) == 17 and all(key in step_keys for key in MINIMUM_STEP_FIELDS), str(step_keys))
    assert_true(checks, "minimum_step_contract_exact", steps["minimum_generation_contract"] == MINIMUM_STEP_FIELDS, str(steps["minimum_generation_contract"]))
    assert_true(checks, "no_standalone_blue_card", steps["candidate_slot_policy"]["standalone_blue_card_allowed"] is False, str(steps["candidate_slot_policy"]))
    assert_true(checks, "no_inline_body_write", steps["candidate_slot_policy"]["inline_body_write_allowed"] is False, str(steps["candidate_slot_policy"]))

    legacy = migration["legacy_to_r81_schema_key"]
    assert_true(checks, "legacy_learning_progression_migrates_to_classroom_flow", "classroom_flow" in legacy["learning_progression"], str(legacy["learning_progression"]))
    assert_true(checks, "legacy_assessment_migrates", set(legacy["assessment_evidence"]) == {"lesson_task_evidence", "assessment_plan"}, str(legacy["assessment_evidence"]))
    assert_true(checks, "visual_language_hidden_distribution", set(legacy["visual_language"]) == {"lesson_concept_slice", "lesson_objectives", "classroom_flow", "assessment_plan"}, str(legacy["visual_language"]))

    required_envelope_keys = set(envelope["required_keys"])
    for key in ["schema_key", "canonical_field_key", "target_field_key", "target_line_contract_id", "target_destination", "formal_apply_allowed", "applied"]:
        assert_true(checks, f"candidate_envelope_requires_{key}", key in required_envelope_keys, str(required_envelope_keys))
    assert_true(checks, "candidate_defaults_preview_only", envelope["defaults"]["preview_only"] is True and envelope["defaults"]["formal_apply_allowed"] is False and envelope["defaults"]["applied"] is False, str(envelope["defaults"]))

    for phrase in ["不做页面重写", "读取大单元主线", "映射到现有正文段", "拆教学过程行级契约", "候选进入旧编辑卡"]:
        assert_true(checks, f"flow_contains_{phrase}", phrase in flow, phrase)
    for phrase in ["R21 页面承载", "R6P section edit data", "R45-R47", "R50-R60", "不改 R21 HTML"]:
        assert_true(checks, f"foundation_contains_{phrase}", phrase in foundation, phrase)

    flags = lesson["boundary_flags"]
    assert_true(checks, "boundary_flags_no_side_effects", all(value is False for value in flags.values()), str(flags))

    if R21_HTML.exists():
        text = R21_HTML.read_text(encoding="utf-8", errors="ignore")
        r21_contains_r81 = "1013R_R81_LESSON_SCHEMA_FIELD_MAP_ADAPTER" in text or "lesson_14_field_mapping_1013R_R81" in text
    else:
        r21_contains_r81 = False
    assert_true(checks, "r21_not_modified_by_R81_marker", not r21_contains_r81, f"r21_contains_r81={r21_contains_r81}")

    result = {
        "stage": "1013R_R81_LESSON_SCHEMA_FIELD_MAP_ADAPTER",
        "status": "PASS",
        "summary": {
            "lesson_schema_field_count": len(fields),
            "step_contract_field_count": len(step_keys),
            "minimum_step_contract_count": len(steps["minimum_generation_contract"]),
            "r79b_old_field_map_is_active": False,
            "r21_modified_by_r81": r21_contains_r81,
            "formal_apply_allowed": False,
        },
        "checks": checks,
    }
    (BASE / "validate_1013R_R81_lesson_schema_field_map_adapter_result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
