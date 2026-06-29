from __future__ import annotations

import json
from pathlib import Path


BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
R21_HTML = ROOT / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R21_page_copy_binds_unified_package" / "prep_room_page_copy_binds_unified_package_1013R_R21.html"

EXPECTED_LABELS = [
    "单元信息",
    "单元主题",
    "大观念",
    "基本问题",
    "单元学习目标",
    "单元内容分析",
    "学情分析",
    "学习重难点",
    "表现性任务",
    "任务评估要点",
    "学习阶段",
    "学习任务",
    "小问题",
    "学习活动",
    "学习评价",
    "情境支架",
    "任务支架",
    "资源支架",
    "策略支架",
    "学习单",
    "评价支架",
    "资料补充",
]

EXPECTED_KEYS = [
    "unit_info",
    "unit_theme",
    "big_idea",
    "essential_question",
    "unit_learning_goals",
    "content_analysis",
    "student_context",
    "key_difficult_points",
    "performance_task",
    "task_assessment_points",
    "learning_stage",
    "learning_task",
    "guiding_question",
    "learning_activity",
    "learning_assessment",
    "context_scaffold",
    "task_scaffold",
    "resource_scaffold",
    "strategy_scaffold",
    "learning_sheet",
    "assessment_scaffold",
    "material_requests",
]


def load_json(name: str) -> dict:
    return json.loads((BASE / name).read_text(encoding="utf-8"))


def assert_true(checks: list[dict], name: str, condition: bool, details: str) -> None:
    checks.append({"name": name, "pass": bool(condition), "details": details})
    if not condition:
        raise AssertionError(f"{name}: {details}")


def main() -> None:
    checks: list[dict] = []
    big_unit = load_json("big_unit_22_field_mapping_1013R_R80.json")
    lesson = load_json("lesson_schema_mapping_1013R_R80.json")
    visual = load_json("visual_language_hidden_dimension_1013R_R80.json")
    adapter = load_json("generation_to_field_adapter_contract_1013R_R80.json")
    flow = (BASE / "generation_reasoning_flow_contract_1013R_R80.md").read_text(encoding="utf-8")
    migration = (BASE / "r79b_deprecated_visual_map_migration_plan_1013R_R80.md").read_text(encoding="utf-8")

    fields = big_unit["big_unit_fields"]
    labels = [item["label"] for item in fields]
    keys = [item["page_field_key"] for item in fields]
    assert_true(checks, "covers_22_big_unit_fields", len(fields) == 22 and labels == EXPECTED_LABELS and keys == EXPECTED_KEYS, f"count={len(fields)}")

    concept = big_unit["concept_to_visible_field_mapping"]
    assert_true(checks, "learning_progression_decomposed", concept["learning_progression"]["page_field_keys"] == ["learning_stage", "learning_task", "guiding_question", "learning_activity", "learning_assessment"], str(concept["learning_progression"]))
    assert_true(checks, "scaffold_pack_decomposed", concept["scaffold_pack"]["page_field_keys"] == ["context_scaffold", "task_scaffold", "resource_scaffold", "strategy_scaffold", "learning_sheet", "assessment_scaffold"], str(concept["scaffold_pack"]))
    assert_true(checks, "assessment_scheme_decomposed", concept["assessment_scheme"]["page_field_keys"] == ["task_assessment_points", "learning_assessment", "assessment_scaffold"], str(concept["assessment_scheme"]))
    assert_true(checks, "unit_identity_to_unit_info", concept["unit_identity"]["page_field_keys"] == ["unit_info"], str(concept["unit_identity"]))
    assert_true(checks, "visual_language_hidden", concept["visual_language"]["page_field_keys"] == [] and visual["visible_top_level_field"] is False, str(concept["visual_language"]))

    lesson_keys = [item["schema_key"] for item in lesson["lesson_fields"]]
    expected_lesson_keys = [
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
    assert_true(checks, "lesson_schema_uses_R79A_keys", lesson_keys == expected_lesson_keys, str(lesson_keys))

    reuse_ids = {item["id"] for item in lesson["reuse_foundations"]}
    for reuse_id in ["R21", "R50_R60", "R6P", "R45_R47"]:
        assert_true(checks, f"reuse_{reuse_id}", reuse_id in reuse_ids, str(reuse_ids))

    assert_true(checks, "r79b_marked_deprecated", "R79B 不作为最终单课字段标准" in migration and "废弃" in migration, "migration plan contains deprecation")
    assert_true(checks, "r79b_page_foundation_reuse", "不替换页面壳" in migration and "不重做编辑卡" in migration, "migration plan preserves foundation")

    required_phrases = ["结构化推演", "不是顺序填字段", "大单元主线推演", "单课成立逻辑", "字段落点", "行级契约", "局部重生成"]
    for phrase in required_phrases:
        assert_true(checks, f"flow_contains_{phrase}", phrase in flow, phrase)

    required_candidate_keys = set(adapter["candidate_envelope_required_keys"])
    for required in ["canonical_field_key", "target_field_key", "explicit_alias_of", "target_line_contract_id", "formal_apply_allowed", "applied"]:
        assert_true(checks, f"candidate_requires_{required}", required in required_candidate_keys, str(required_candidate_keys))

    forbidden = adapter["forbidden_actions"]
    assert_true(checks, "forbidden_flags_false", all(value is False for value in forbidden.values()), str(forbidden))
    assert_true(checks, "material_requests_no_formal_write", next(item for item in fields if item["page_field_key"] == "material_requests")["write_policy"] == "action_prompt_only_no_formal_write", "material_requests policy")

    if R21_HTML.exists():
        text = R21_HTML.read_text(encoding="utf-8", errors="ignore")
        r21_contains_r80 = "1013R_R80_GENERATION_FLOW_AND_FIELD_MAPPING_CONTRACT" in text or "big_unit_22_field_mapping_1013R_R80" in text
    else:
        r21_contains_r80 = False
    assert_true(checks, "r21_not_modified_by_R80_marker", not r21_contains_r80, f"r21_contains_r80={r21_contains_r80}")

    result = {
        "stage": "1013R_R80_GENERATION_FLOW_AND_FIELD_MAPPING_CONTRACT",
        "status": "PASS",
        "summary": {
            "big_unit_field_count": len(fields),
            "lesson_field_count": len(lesson["lesson_fields"]),
            "visual_language_visible_top_level": visual["visible_top_level_field"],
            "r21_modified_by_r80": r21_contains_r80,
            "formal_apply_allowed": False,
        },
        "checks": checks,
    }
    (BASE / "validate_1013R_R80_generation_flow_field_mapping_result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
