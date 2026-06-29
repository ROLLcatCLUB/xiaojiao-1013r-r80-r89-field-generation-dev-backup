from __future__ import annotations

import json
from pathlib import Path


STAGE = "1013R_R81_LESSON_SCHEMA_FIELD_MAP_ADAPTER"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / STAGE
BASE = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1"
R79A_DIR = BASE / "1013R_R79A_TEACHING_DESIGN_STRUCTURE_SOURCE_COMPARISON"
R79B_DIR = BASE / "1013R_R79B_TEACHING_DESIGN_CONTRACT_VISUAL_PROTOTYPE"
R80_DIR = BASE / "1013R_R80_GENERATION_FLOW_AND_FIELD_MAPPING_CONTRACT"
R21_HTML = BASE / "1013R_R21_page_copy_binds_unified_package" / "prep_room_page_copy_binds_unified_package_1013R_R21.html"


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text.strip() + "\n", encoding="utf-8")


LESSON_FIELDS = [
    {
        "order": 1,
        "schema_key": "lesson_identity",
        "label": "课时身份",
        "visible_section": "lesson_header",
        "target_section_id": "lesson_header",
        "target_selectors": [".nb-main-title", ".nb-title", "[data-r21-route-anchor='lesson_header']", ".nb-state-row"],
        "route_role": "header_identity",
        "generation_role": "确认年级、单元、课题、课时、教材页码和课时序号。",
        "candidate_policy": "preview_identity_only",
        "line_contract_policy": "facts_only_no_invention",
        "formal_apply_allowed": False,
    },
    {
        "order": 2,
        "schema_key": "inherited_unit_context",
        "label": "继承单元主线",
        "visible_section": "本课依据",
        "target_section_id": "basis",
        "target_selectors": ["#nb-section-basis", "[data-edit-target^='section:basis']"],
        "route_role": "unit_spine_inheritance",
        "generation_role": "把单元主题、大观念、基本问题、表现性任务带入本课依据。",
        "candidate_policy": "must_read_big_unit_before_lesson_candidate",
        "line_contract_policy": "one_or_more_inheritance_lines",
        "formal_apply_allowed": False,
    },
    {
        "order": 3,
        "schema_key": "textbook_anchor",
        "label": "教材锚点",
        "visible_section": "本课依据",
        "target_section_id": "basis",
        "target_selectors": ["#nb-section-basis", ".nb-material-front-prompt", "[data-r49-material-requests-prompt='true']"],
        "route_role": "source_anchor_or_gap",
        "generation_role": "定位教材页、图例、练习、材料来源；缺失时转入资料补充。",
        "candidate_policy": "source_fact_or_material_request_only",
        "line_contract_policy": "textbook_page_or_gap_line",
        "formal_apply_allowed": False,
    },
    {
        "order": 4,
        "schema_key": "lesson_concept_slice",
        "label": "本课概念切片",
        "visible_section": "本课依据",
        "target_section_id": "basis",
        "target_selectors": ["#nb-section-basis", "[data-edit-target^='section:basis']"],
        "route_role": "lesson_slice_from_unit_big_idea",
        "generation_role": "说明本课从单元大观念中切出哪一块可教、可观察的内容。",
        "candidate_policy": "must_link_unit_big_idea_and_textbook_anchor",
        "line_contract_policy": "concept_slice_line",
        "formal_apply_allowed": False,
    },
    {
        "order": 5,
        "schema_key": "lesson_focus_question",
        "label": "本课驱动问题",
        "visible_section": "本课依据",
        "target_section_id": "basis",
        "target_selectors": ["#nb-section-basis", "[data-edit-target^='section:basis']"],
        "route_role": "lesson_question",
        "generation_role": "把单元基本问题转成这一课能展开的驱动问题。",
        "candidate_policy": "question_candidate_not_slogan",
        "line_contract_policy": "driving_question_line",
        "formal_apply_allowed": False,
    },
    {
        "order": 6,
        "schema_key": "lesson_objectives",
        "label": "课时目标",
        "visible_section": "教学目标",
        "target_section_id": "goals",
        "target_selectors": ["#nb-section-goals", "[data-edit-target^='section:goals']"],
        "route_role": "observable_objectives",
        "generation_role": "把课标、单元学习目标和本课任务转成可观察目标。",
        "candidate_policy": "objective_must_have_observable_behavior",
        "line_contract_policy": "2_to_5_goal_lines_allowed",
        "formal_apply_allowed": False,
    },
    {
        "order": 7,
        "schema_key": "student_starting_point",
        "label": "学生起点",
        "visible_section": "学情分析",
        "target_section_id": "analysis",
        "target_selectors": ["#nb-section-analysis", "[data-edit-target^='section:analysis']"],
        "route_role": "student_context",
        "generation_role": "写清学生已有经验、常见困难和进入本课的可用支架。",
        "candidate_policy": "do_not_fake_real_student_profile",
        "line_contract_policy": "prior_experience_gap_support_lines",
        "formal_apply_allowed": False,
    },
    {
        "order": 8,
        "schema_key": "key_difficult_points",
        "label": "重难点",
        "visible_section": "教学重难点",
        "target_section_id": "keypoints",
        "target_selectors": ["#nb-section-keypoints", "[data-edit-target^='section:keypoints']"],
        "route_role": "lesson_keypoints",
        "generation_role": "区分本课学习重点和理解/表现难点。",
        "candidate_policy": "focus_and_difficulty_separated",
        "line_contract_policy": "focus_line_and_difficulty_line",
        "formal_apply_allowed": False,
    },
    {
        "order": 9,
        "schema_key": "lesson_task_evidence",
        "label": "本课任务与证据",
        "visible_section": "学习单与评价",
        "target_section_id": "assessment",
        "target_selectors": ["#nb-section-assessment", "[data-edit-target^='section:assessment']", ".r32-derivative-panel"],
        "route_role": "task_evidence_bridge",
        "generation_role": "定义学生产出、说明、互评或课堂观察证据。",
        "candidate_policy": "task_and_evidence_must_match",
        "line_contract_policy": "task_output_evidence_criteria_lines",
        "formal_apply_allowed": False,
    },
    {
        "order": 10,
        "schema_key": "classroom_flow",
        "label": "教学过程",
        "visible_section": "教学过程",
        "target_section_id": "teaching_process",
        "target_selectors": ["#nb-section-teaching-process", "[id^='nb-step-']", ".nb-readable-step"],
        "route_role": "lesson_step_contract_host",
        "generation_role": "生成步骤级教学过程，并拆成教师动作、学生活动、材料/屏幕、评价证据。",
        "candidate_policy": "line_level_step_contract_required_before_patch",
        "line_contract_policy": "step_contracts_first_then_local_patches",
        "formal_apply_allowed": False,
    },
    {
        "order": 11,
        "schema_key": "courseware_plan",
        "label": "课件/大屏计划",
        "visible_section": "右栏大屏/课件预览",
        "target_section_id": "courseware_plan",
        "target_selectors": ["[data-r21-route-anchor='courseware_entry']", "[data-r21-route-anchor='classroom_display_screen']", ".courseware-rail", ".courseware-screen-mini"],
        "route_role": "derived_object_preview",
        "generation_role": "从教学过程派生每个环节的大屏/课件屏幕意图。",
        "candidate_policy": "derived_from_classroom_flow_only",
        "line_contract_policy": "screen_by_step_lines",
        "formal_apply_allowed": False,
    },
    {
        "order": 12,
        "schema_key": "handout_plan",
        "label": "学习单/学生任务单计划",
        "visible_section": "学习单与评价 / 右栏学习单",
        "target_section_id": "handout_plan",
        "target_selectors": ["#nb-section-assessment", "[data-r32-derivative-id='worksheet']", ".r32-derivative-panel"],
        "route_role": "derived_handout_preview",
        "generation_role": "从学习活动和证据要求派生轻量学习单。",
        "candidate_policy": "handout_is_derived_not_main_text_dump",
        "line_contract_policy": "handout_item_lines",
        "formal_apply_allowed": False,
    },
    {
        "order": 13,
        "schema_key": "assessment_plan",
        "label": "评价计划",
        "visible_section": "学习单与评价 / 右栏评价表",
        "target_section_id": "assessment",
        "target_selectors": ["#nb-section-assessment", "[data-r32-derivative-id='assessment_rubric']", ".r32-derivative-panel"],
        "route_role": "assessment_bridge",
        "generation_role": "把本课任务证据转成过程评价、作品评价和反馈语言。",
        "candidate_policy": "evaluation_must_have_evidence_basis",
        "line_contract_policy": "criteria_evidence_feedback_lines",
        "formal_apply_allowed": False,
    },
    {
        "order": 14,
        "schema_key": "material_requests",
        "label": "资料补充",
        "visible_section": "资料补充提示位",
        "target_section_id": "material_requests",
        "target_selectors": [".nb-material-front-prompt", "[data-r49-material-requests-prompt='true']", "[data-canonical-field-key='material_requests']"],
        "route_role": "missing_source_gate",
        "generation_role": "缺教材、课时安排、示范图、学生作品、真实学情时只提示补资料。",
        "candidate_policy": "action_prompt_only_no_formal_write",
        "line_contract_policy": "missing_material_action_lines",
        "formal_apply_allowed": False,
    },
]


STEP_FIELDS = [
    "step_id",
    "step_order",
    "step_name",
    "duration",
    "step_goal",
    "teacher_talk",
    "student_task",
    "material_requirements",
    "tech_support",
    "success_criteria",
    "guiding_questions",
    "feedback_points",
    "ppt_page_note",
    "design_intent",
    "evidence_capture",
    "source_refs",
    "generation_slot",
]

MINIMUM_STEP_FIELDS = [
    "step_goal",
    "teacher_talk",
    "student_task",
    "success_criteria",
    "guiding_questions",
    "source_refs",
    "generation_slot",
]


LEGACY_TO_R81 = {
    "unit_basic_info": ["lesson_identity", "inherited_unit_context"],
    "curriculum_basis": ["inherited_unit_context", "textbook_anchor"],
    "core_literacy_goals": ["lesson_objectives"],
    "student_starting_point": ["student_starting_point"],
    "unit_questions": ["lesson_concept_slice", "lesson_focus_question"],
    "knowledge_and_skills": ["lesson_concept_slice", "key_difficult_points"],
    "performance_task": ["lesson_task_evidence"],
    "learning_progression": ["classroom_flow"],
    "lesson_task_chain": ["classroom_flow", "lesson_task_evidence"],
    "assessment_evidence": ["lesson_task_evidence", "assessment_plan"],
    "skills_materials_scaffolds": ["courseware_plan", "handout_plan", "material_requests"],
    "material_requests": ["material_requests"],
    "classroom_flow": ["classroom_flow"],
    "scaffold_pack": ["courseware_plan", "handout_plan", "material_requests"],
    "visual_language": ["lesson_concept_slice", "lesson_objectives", "classroom_flow", "assessment_plan"],
}


def build_lesson_mapping() -> dict:
    return {
        "schema_id": "lesson_14_field_mapping_1013R_R81",
        "stage": STAGE,
        "purpose": "Turn the R79A lesson schema into the active single-lesson field map, using R80's adapter rule and the existing R21/R50/R60/R6P/R45-R47 foundation.",
        "source_priority": [
            str(R79A_DIR / "lesson_design_schema_v2_1013R_R79A.json"),
            str(R80_DIR / "lesson_schema_mapping_1013R_R80.json"),
            str(R21_HTML),
            str(R79B_DIR / "teaching_design_contract_visual_map_1013R_R79B.json"),
        ],
        "boundary_flags": {
            "r21_page_modified": False,
            "new_static_page_created": False,
            "model_provider_runtime_connected": False,
            "database_write": False,
            "feishu_write": False,
            "memory_write": False,
            "formal_apply_allowed": False,
            "r79b_old_field_map_is_active": False,
        },
        "inheritance_rule": "single_lesson_must_inherit_unit_big_idea_and_essential_question_before_generation",
        "structured_reasoning_order": [
            "read_big_unit_spine",
            "derive_lesson_logic",
            "map_to_existing_sections",
            "create_step_line_contracts",
            "route_candidates_to_existing_edit_card",
        ],
        "existing_visible_sections": {
            "basis": "本课依据",
            "analysis": "学情分析",
            "goals": "教学目标",
            "keypoints": "教学重难点",
            "preparation": "教学准备",
            "teaching_process": "教学过程",
            "assessment": "学习单与评价",
            "reflection": "课堂后记",
        },
        "lesson_fields": LESSON_FIELDS,
        "line_count_policy": {
            "fixed_slots": False,
            "description": "Each visible section may receive 1 to 5 line contracts depending on lesson logic. The model must not assume a fixed global line order.",
        },
    }


def build_step_mapping() -> dict:
    return {
        "schema_id": "lesson_step_line_contract_mapping_1013R_R81",
        "stage": STAGE,
        "source_schema": str(R79A_DIR / "lesson_step_contract_schema_v1_1013R_R79A.json"),
        "target_parent_schema_key": "classroom_flow",
        "target_parent_section_id": "teaching_process",
        "target_selectors": ["#nb-section-teaching-process", "[id^='nb-step-']", ".nb-readable-step"],
        "step_id_policy": {
            "known_static_step_ids": ["intro", "sense", "explore", "make", "share"],
            "allow_dynamic_step_ids": True,
            "contract_id_pattern": "lesson_step.{lesson_id}.{step_order}.{field_key}",
        },
        "step_fields": [{"key": key, "required": key in MINIMUM_STEP_FIELDS} for key in STEP_FIELDS],
        "minimum_generation_contract": MINIMUM_STEP_FIELDS,
        "candidate_slot_policy": {
            "target_destination": "existing_edit_card_before_after_suggestion_panel",
            "standalone_blue_card_allowed": False,
            "inline_body_write_allowed": False,
            "preview_only": True,
            "formal_apply_allowed": False,
            "applied": False,
        },
        "field_patch_candidate_required_keys": [
            "field_patch_id",
            "canonical_field_key",
            "target_field_key",
            "target_section",
            "target_step_id",
            "target_line_contract_id",
            "target_field",
            "before_summary",
            "after_candidate",
            "xiaojiao_suggestion",
            "impact_scope",
            "teacher_review_required",
            "formal_apply_allowed",
            "applied",
        ],
    }


def build_migration_adapter() -> dict:
    return {
        "schema_id": "r79b_lesson_field_migration_adapter_1013R_R81",
        "stage": STAGE,
        "decision": "R79B visual map is deprecated as field standard. It may be used only as historical selector evidence and migration input.",
        "legacy_to_r81_schema_key": LEGACY_TO_R81,
        "deprecated": [
            "R79B-L1/L2 field standard",
            "R79B visual map data as active page schema",
            "R79B generation slot ids",
            "standalone body blue cards",
        ],
        "reuse": [
            "R21 page shell",
            "existing CSS",
            "renderLessonSection section hosts",
            "R6P section edit data foundation",
            "R45-R47 candidate host routing and edit-card bridge",
            "R50-R60 field-aware edit card",
            "right rail derivative previews",
            "bottom 小教 composer",
            "preview / undo / teacher gate",
        ],
        "migration_rules": [
            "Normalize any old R79B or R50 field key through legacy_to_r81_schema_key before routing.",
            "Resolve final target_section_id from lesson_14_field_mapping_1013R_R81.",
            "Create line-level step contracts before generating classroom_flow patches.",
            "Route candidates into existing before/after/suggestion edit card only.",
            "Keep visual_language hidden; distribute it into lesson_concept_slice, objectives, classroom_flow, and assessment_plan.",
            "Route missing sources to material_requests only; do not fake教材或学情.",
        ],
    }


def build_candidate_envelope() -> dict:
    return {
        "schema_id": "lesson_candidate_envelope_contract_1013R_R81",
        "stage": STAGE,
        "purpose": "Define the minimum patch envelope for later model candidates after R81.",
        "required_keys": [
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
        ],
        "defaults": {
            "target_destination": "existing_edit_card_before_after_suggestion_panel",
            "teacher_review_required": True,
            "preview_only": True,
            "formal_apply_allowed": False,
            "applied": False,
        },
        "reject_if": [
            "missing_schema_key",
            "missing_canonical_field_key",
            "missing_target_field_key",
            "target_destination_is_standalone_blue_card",
            "formal_apply_allowed_true",
            "applied_true_before_teacher_confirmation",
            "material_requests_generates_formal_content",
            "classroom_flow_patch_without_target_line_contract_id",
        ],
    }


FLOW_MD = """
# 1013R R81 Lesson Schema Field Map Adapter

R81 只做单课字段线路，不做页面重写。它把 R79A 的 14 个 lesson schema key 落到当前 R21 已有承载：正文段落、教学过程步骤、右栏派生物预览和资料补充提示位。

## 为什么要做 R81

R79B 的旧 visual map 把单元字段、单课字段、候选位、正文蓝卡混在一起，不能继续当字段标准。但 R21、R6P、R45-R47、R50-R60 已经有页面承载、编辑卡、候选桥接、preview/undo/teacher gate，这些都不应该推倒重做。

## 单课生成顺序

```text
读取大单元主线
  -> 推演单课成立逻辑
    -> 映射到现有正文段
      -> 拆教学过程行级契约
        -> 候选进入旧编辑卡
```

这里仍然不是顺序填字段。字段数量和行数都由教学逻辑决定，一个字段可以落 1 到 5 条行契约。

## 页面落点

- `basis` 本课依据：继承单元主线、教材锚点、本课概念切片、本课驱动问题。
- `analysis` 学情分析：学生起点。
- `goals` 教学目标：课时目标。
- `keypoints` 教学重难点：学习重点和难点。
- `teaching_process` 教学过程：课堂步骤和行级契约。
- `assessment` 学习单与评价：本课任务与证据、评价计划、学习单关联。
- 右栏派生物：课件/大屏计划、学习单计划、评价表预览。
- `material_requests`：资料缺口提示，不写正式课包。

## 候选进入方式

所有候选只能进入已有编辑卡的“修改前 / 修改后 / 小教建议”结构。禁止正文独立蓝卡，禁止直接覆盖原文，禁止 formal apply。

## R82 才能做什么

R82 可以基于 R81 做 prompt/request envelope，让模型返回严格 JSON 候选。但 R82 仍然应保持 preview_only，不写库、不写飞书、不写正式课包。
"""


FOUNDATION_REPORT = """
# 1013R R81 Existing Foundation Reuse Report

## 复用底座

- R21 页面承载：继续作为当前样板间主线，不重开产品页。
- R6P section edit data：继续作为编辑数据底座和旧编辑卡数据来源。
- R45-R47：继续作为候选定位、host routing 和 edit-card bridge。
- R50-R60：继续作为字段感知编辑卡、行级契约展示、preview/undo/teacher gate。
- 右栏派生物预览：继续承载课件/大屏、学习单、评价表等派生预览。
- 底部小教输入：继续作为教师意图入口。
- 现有 CSS：不重置、不重画、不另起页面风格。

## 替换内容

- 替换 R79B 旧单课字段标准。
- 替换 R79B 旧 visual map 作为 active schema 的位置。
- 替换旧生成槽位理解。

## 不做内容

- 不改 R21 HTML。
- 不生成新静态页。
- 不接模型 provider/runtime。
- 不写数据库、飞书、记忆。
- 不 formal apply。
"""


README = """
# 1013R R81 Lesson Schema Field Map Adapter

R81 把 R79A 单课 14 字段 schema 正式整理成当前系统可使用的单课字段映射层。它不是页面改造，也不是模型生成。

## 结果

- lesson_schema_field_count=14
- step_contract_field_count=17
- minimum_step_contract_count=7
- r79b_old_field_map_is_active=false
- r21_page_modified=false
- new_static_page_created=false
- model_provider_runtime_connected=false
- formal_apply_allowed=false

## 文件

- `lesson_14_field_mapping_1013R_R81.json`
- `lesson_step_line_contract_mapping_1013R_R81.json`
- `r79b_lesson_field_migration_adapter_1013R_R81.json`
- `lesson_candidate_envelope_contract_1013R_R81.json`
- `lesson_generation_flow_to_existing_surface_1013R_R81.md`
- `existing_foundation_reuse_report_1013R_R81.md`
- `validate_1013R_R81_lesson_schema_field_map_adapter.py`
- `validate_1013R_R81_lesson_schema_field_map_adapter_result.json`
"""


MANIFEST = """
# REVIEW PACKAGE MANIFEST

Stage: 1013R_R81_LESSON_SCHEMA_FIELD_MAP_ADAPTER

## Included

1. README.md
2. REVIEW_PACKAGE_MANIFEST.md
3. lesson_14_field_mapping_1013R_R81.json
4. lesson_step_line_contract_mapping_1013R_R81.json
5. r79b_lesson_field_migration_adapter_1013R_R81.json
6. lesson_candidate_envelope_contract_1013R_R81.json
7. lesson_generation_flow_to_existing_surface_1013R_R81.md
8. existing_foundation_reuse_report_1013R_R81.md
9. validate_1013R_R81_lesson_schema_field_map_adapter.py
10. validate_1013R_R81_lesson_schema_field_map_adapter_result.json

## Source References

- R79A lesson schema
- R79A lesson step contract schema
- R80 generation flow and field mapping contract
- R79B historical visual map
- R21 current page carrier, read-only

## Boundaries

- No R21 HTML modification.
- No new static/product page.
- No provider/model/runtime connection.
- No database/Feishu/memory write.
- No formal apply.
"""


VALIDATOR = r'''
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
'''


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    write_json(OUT / "lesson_14_field_mapping_1013R_R81.json", build_lesson_mapping())
    write_json(OUT / "lesson_step_line_contract_mapping_1013R_R81.json", build_step_mapping())
    write_json(OUT / "r79b_lesson_field_migration_adapter_1013R_R81.json", build_migration_adapter())
    write_json(OUT / "lesson_candidate_envelope_contract_1013R_R81.json", build_candidate_envelope())
    write_text(OUT / "lesson_generation_flow_to_existing_surface_1013R_R81.md", FLOW_MD)
    write_text(OUT / "existing_foundation_reuse_report_1013R_R81.md", FOUNDATION_REPORT)
    write_text(OUT / "README.md", README)
    write_text(OUT / "REVIEW_PACKAGE_MANIFEST.md", MANIFEST)
    write_text(OUT / "validate_1013R_R81_lesson_schema_field_map_adapter.py", VALIDATOR)
    print(str(OUT))


if __name__ == "__main__":
    main()
