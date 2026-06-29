from __future__ import annotations

import json
from pathlib import Path


STAGE = "1013R_R80_GENERATION_FLOW_AND_FIELD_MAPPING_CONTRACT"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / STAGE

R79A_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R79A_TEACHING_DESIGN_STRUCTURE_SOURCE_COMPARISON"
R79B_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R79B_TEACHING_DESIGN_CONTRACT_VISUAL_PROTOTYPE"
R79C5_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R79C5_BIG_UNIT_FIELD_ID_CHIPS"
R21_HTML = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R21_page_copy_binds_unified_package" / "prep_room_page_copy_binds_unified_package_1013R_R21.html"


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text.strip() + "\n", encoding="utf-8")


BIG_UNIT_FIELDS = [
    {
        "order": 1,
        "label": "单元信息",
        "page_field_key": "unit_info",
        "contract_key": "big_unit.unit_info",
        "visual_contract_id": "R79C5-BU/unit_info",
        "source_concept_fields": ["unit_identity"],
        "generation_role": "unit_identity_context",
        "hidden_generation_dimensions": [],
        "line_landing_policy": "identity facts only; no invented textbook data",
        "required": True,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 2,
        "label": "单元主题",
        "page_field_key": "unit_theme",
        "contract_key": "big_unit.unit_theme",
        "visual_contract_id": "R79C5-BU/unit_theme",
        "source_concept_fields": ["unit_theme"],
        "generation_role": "name the unit learning territory",
        "hidden_generation_dimensions": ["visual_language.theme_signal"],
        "line_landing_policy": "theme and learning scope may be separate lines",
        "required": True,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 3,
        "label": "大观念",
        "page_field_key": "big_idea",
        "contract_key": "big_unit.big_idea",
        "visual_contract_id": "R79C5-BU/big_idea",
        "source_concept_fields": ["big_idea", "key_concepts"],
        "generation_role": "transferable understanding, not activity summary",
        "hidden_generation_dimensions": ["visual_language.core_understanding"],
        "line_landing_policy": "one core understanding line; avoid slogan-only phrasing",
        "required": True,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 4,
        "label": "基本问题",
        "page_field_key": "essential_question",
        "contract_key": "big_unit.essential_question",
        "visual_contract_id": "R79C5-BU/essential_question",
        "source_concept_fields": ["essential_question", "big_idea"],
        "generation_role": "drive inquiry across the unit",
        "hidden_generation_dimensions": ["visual_language.question_focus"],
        "line_landing_policy": "driving question and transfer question can be separate lines",
        "required": True,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 5,
        "label": "单元学习目标",
        "page_field_key": "unit_learning_goals",
        "contract_key": "big_unit.unit_learning_goals",
        "visual_contract_id": "R79C5-BU/unit_learning_goals",
        "source_concept_fields": ["unit_learning_goals", "core_literacy_targets", "knowledge_and_skills"],
        "generation_role": "convert unit spine into observable learning outcomes",
        "hidden_generation_dimensions": ["visual_language.learning_goal_dimension"],
        "line_landing_policy": "each goal must name observable behavior and evidence direction",
        "required": True,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 6,
        "label": "单元内容分析",
        "page_field_key": "content_analysis",
        "contract_key": "big_unit.content_analysis",
        "visual_contract_id": "R79C5-BU/content_analysis",
        "source_concept_fields": ["content_analysis", "key_concepts", "visual_language"],
        "generation_role": "explain content path and learning focus from textbook and references",
        "hidden_generation_dimensions": ["visual_language.content_reading"],
        "line_landing_policy": "textbook reading and learning focus can be separate lines",
        "required": True,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 7,
        "label": "学情分析",
        "page_field_key": "student_context",
        "contract_key": "big_unit.student_context",
        "visual_contract_id": "R79C5-BU/student_context",
        "source_concept_fields": ["student_context"],
        "generation_role": "describe prior experience, misconception, and accessible entry",
        "hidden_generation_dimensions": ["visual_language.student_access"],
        "line_landing_policy": "prior experience and common gap should remain distinct",
        "required": True,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 8,
        "label": "学习重难点",
        "page_field_key": "key_difficult_points",
        "contract_key": "big_unit.key_difficult_points",
        "visual_contract_id": "R79C5-BU/key_difficult_points",
        "source_concept_fields": ["key_difficult_points", "knowledge_and_skills"],
        "generation_role": "distinguish learning focus and learning difficulty",
        "hidden_generation_dimensions": ["visual_language.difficulty_focus"],
        "line_landing_policy": "focus and difficulty must not be collapsed into one vague sentence",
        "required": True,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 9,
        "label": "表现性任务",
        "page_field_key": "performance_task",
        "contract_key": "big_unit.performance_task",
        "visual_contract_id": "R79C5-BU/performance_task",
        "source_concept_fields": ["performance_task", "assessment_scheme"],
        "generation_role": "define final product and revision evidence",
        "hidden_generation_dimensions": ["visual_language.work_expression"],
        "line_landing_policy": "task output and evidence requirement can be separate lines",
        "required": True,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 10,
        "label": "任务评估要点",
        "page_field_key": "task_assessment_points",
        "contract_key": "big_unit.task_assessment_points",
        "visual_contract_id": "R79C5-BU/task_assessment_points",
        "source_concept_fields": ["task_assessment_points", "assessment_scheme", "performance_task"],
        "generation_role": "turn task into assessable evidence points",
        "hidden_generation_dimensions": ["visual_language.evidence_quality"],
        "line_landing_policy": "criteria should point to observable work or explanation evidence",
        "required": True,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 11,
        "label": "学习阶段",
        "page_field_key": "learning_stage",
        "contract_key": "big_unit.learning_stage",
        "visual_contract_id": "R79C5-BU/learning_stage",
        "source_concept_fields": ["learning_progression.learning_stage"],
        "generation_role": "name the progression stages",
        "hidden_generation_dimensions": ["visual_language.progression_axis"],
        "line_landing_policy": "stage count is flexible; not fixed to three lines",
        "required": True,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 12,
        "label": "学习任务",
        "page_field_key": "learning_task",
        "contract_key": "big_unit.learning_task",
        "visual_contract_id": "R79C5-BU/learning_task",
        "source_concept_fields": ["learning_progression.learning_task"],
        "generation_role": "assign work students actually do in each stage",
        "hidden_generation_dimensions": ["visual_language.task_materiality"],
        "line_landing_policy": "task lines must align with learning_stage but may be 2 to 5 items",
        "required": True,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 13,
        "label": "小问题",
        "page_field_key": "guiding_question",
        "contract_key": "big_unit.guiding_question",
        "visual_contract_id": "R79C5-BU/guiding_question",
        "source_concept_fields": ["learning_progression.guiding_question", "essential_question"],
        "generation_role": "break essential question into stage-level prompts",
        "hidden_generation_dimensions": ["visual_language.question_ladder"],
        "line_landing_policy": "each question must point to a visible observation or decision",
        "required": True,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 14,
        "label": "学习活动",
        "page_field_key": "learning_activity",
        "contract_key": "big_unit.learning_activity",
        "visual_contract_id": "R79C5-BU/learning_activity",
        "source_concept_fields": ["learning_progression.learning_activity"],
        "generation_role": "convert stage task into classroom activity sequence",
        "hidden_generation_dimensions": ["visual_language.activity_operation"],
        "line_landing_policy": "activities must stay grounded in material/action/evidence, not slogans",
        "required": True,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 15,
        "label": "学习评价",
        "page_field_key": "learning_assessment",
        "contract_key": "big_unit.learning_assessment",
        "visual_contract_id": "R79C5-BU/learning_assessment",
        "source_concept_fields": ["learning_progression.learning_assessment", "assessment_scheme"],
        "generation_role": "place assessment into the learning process",
        "hidden_generation_dimensions": ["visual_language.assessment_visibility"],
        "line_landing_policy": "assessment must match stage task and evidence",
        "required": True,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 16,
        "label": "情境支架",
        "page_field_key": "context_scaffold",
        "contract_key": "big_unit.context_scaffold",
        "visual_contract_id": "R79C5-BU/context_scaffold",
        "source_concept_fields": ["scaffold_pack.context_scaffold"],
        "generation_role": "make the learning situation understandable and motivating",
        "hidden_generation_dimensions": ["visual_language.context_bridge"],
        "line_landing_policy": "context should support the task, not become a decorative story",
        "required": False,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 17,
        "label": "任务支架",
        "page_field_key": "task_scaffold",
        "contract_key": "big_unit.task_scaffold",
        "visual_contract_id": "R79C5-BU/task_scaffold",
        "source_concept_fields": ["scaffold_pack.task_scaffold"],
        "generation_role": "break task into doable moves",
        "hidden_generation_dimensions": ["visual_language.task_steps"],
        "line_landing_policy": "scaffold must lower task difficulty without replacing student thinking",
        "required": False,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 18,
        "label": "资源支架",
        "page_field_key": "resource_scaffold",
        "contract_key": "big_unit.resource_scaffold",
        "visual_contract_id": "R79C5-BU/resource_scaffold",
        "source_concept_fields": ["scaffold_pack.resource_scaffold", "material_requests"],
        "generation_role": "name resources needed to support perception, comparison, and creation",
        "hidden_generation_dimensions": ["visual_language.resource_need"],
        "line_landing_policy": "resource gaps route to material_requests, not fabricated evidence",
        "required": False,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 19,
        "label": "策略支架",
        "page_field_key": "strategy_scaffold",
        "contract_key": "big_unit.strategy_scaffold",
        "visual_contract_id": "R79C5-BU/strategy_scaffold",
        "source_concept_fields": ["scaffold_pack.strategy_scaffold"],
        "generation_role": "provide thinking, observation, comparison, and expression strategies",
        "hidden_generation_dimensions": ["visual_language.strategy_language"],
        "line_landing_policy": "strategy can be teacher prompt, sentence frame, or observation route",
        "required": False,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 20,
        "label": "学习单",
        "page_field_key": "learning_sheet",
        "contract_key": "big_unit.learning_sheet",
        "visual_contract_id": "R79C5-BU/learning_sheet",
        "source_concept_fields": ["scaffold_pack.learning_sheet"],
        "generation_role": "translate learning process into student-facing worksheet prompts",
        "hidden_generation_dimensions": ["visual_language.sheet_observation"],
        "line_landing_policy": "worksheet item must correspond to activity and evidence",
        "required": False,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 21,
        "label": "评价支架",
        "page_field_key": "assessment_scaffold",
        "contract_key": "big_unit.assessment_scaffold",
        "visual_contract_id": "R79C5-BU/assessment_scaffold",
        "source_concept_fields": ["scaffold_pack.assessment_scaffold", "assessment_scheme"],
        "generation_role": "make criteria readable and usable by teacher and students",
        "hidden_generation_dimensions": ["visual_language.criteria_language"],
        "line_landing_policy": "criteria language must connect to observable task evidence",
        "required": False,
        "candidate_allowed_later": True,
        "write_policy": "preview_only_until_teacher_confirmed",
    },
    {
        "order": 22,
        "label": "资料补充",
        "page_field_key": "material_requests",
        "contract_key": "big_unit.material_requests",
        "visual_contract_id": "R79C5-BU/material_requests",
        "source_concept_fields": ["material_requests"],
        "generation_role": "surface missing sources and teacher actions",
        "hidden_generation_dimensions": ["visual_language.missing_reference_need"],
        "line_landing_policy": "action prompt only; never writes formal lesson package content",
        "required": False,
        "candidate_allowed_later": False,
        "write_policy": "action_prompt_only_no_formal_write",
    },
]


CONCEPT_MAPPINGS = {
    "learning_progression": {
        "page_field_keys": ["learning_stage", "learning_task", "guiding_question", "learning_activity", "learning_assessment"],
        "page_labels": ["学习阶段", "学习任务", "小问题", "学习活动", "学习评价"],
        "page_field_policy": "decompose_to_visible_fields; never render learning_progression as a page field",
    },
    "scaffold_pack": {
        "page_field_keys": ["context_scaffold", "task_scaffold", "resource_scaffold", "strategy_scaffold", "learning_sheet", "assessment_scaffold"],
        "page_labels": ["情境支架", "任务支架", "资源支架", "策略支架", "学习单", "评价支架"],
        "page_field_policy": "decompose_to_visible_fields; never render scaffold_pack as a page field",
    },
    "assessment_scheme": {
        "page_field_keys": ["task_assessment_points", "learning_assessment", "assessment_scaffold"],
        "page_labels": ["任务评估要点", "学习评价", "评价支架"],
        "page_field_policy": "split_between_task_criteria_process_assessment_and_assessment_scaffold",
    },
    "unit_identity": {
        "page_field_keys": ["unit_info"],
        "page_labels": ["单元信息"],
        "page_field_policy": "rename_to_current_visible_unit_info_field",
    },
    "visual_language": {
        "page_field_keys": [],
        "page_labels": [],
        "page_field_policy": "hidden_generation_dimension_only; no visible top-level page field",
    },
}


LESSON_FIELDS = [
    {
        "order": 1,
        "schema_key": "lesson_identity",
        "label": "课时身份",
        "adapter_target": "lesson.identity",
        "landing_surface": "single_lesson_field_map_to_be_built_after_R80",
        "generation_role": "name grade, unit, lesson, page, period, and material scope",
    },
    {
        "order": 2,
        "schema_key": "inherited_unit_context",
        "label": "继承单元主线",
        "adapter_target": "lesson.inherited_unit_context",
        "landing_surface": "must_read_big_unit_spine_before_lesson_generation",
        "generation_role": "inherit unit_theme, big_idea, essential_question, performance_task",
    },
    {
        "order": 3,
        "schema_key": "textbook_anchor",
        "label": "教材锚点",
        "adapter_target": "lesson.textbook_anchor",
        "landing_surface": "source_anchor_or_material_requests_when_missing",
        "generation_role": "locate textbook pages, images, exercises, and source gaps",
    },
    {
        "order": 4,
        "schema_key": "lesson_concept_slice",
        "label": "本课概念切片",
        "adapter_target": "lesson.lesson_concept_slice",
        "landing_surface": "lesson_core_field",
        "generation_role": "select this lesson's slice of the unit concept",
    },
    {
        "order": 5,
        "schema_key": "lesson_focus_question",
        "label": "本课驱动问题",
        "adapter_target": "lesson.lesson_focus_question",
        "landing_surface": "lesson_core_field",
        "generation_role": "convert unit essential question into a teachable lesson question",
    },
    {
        "order": 6,
        "schema_key": "lesson_objectives",
        "label": "课时目标",
        "adapter_target": "lesson.lesson_objectives",
        "landing_surface": "lesson_objective_field",
        "generation_role": "make lesson outcomes observable and assessable",
    },
    {
        "order": 7,
        "schema_key": "student_starting_point",
        "label": "学生起点",
        "adapter_target": "lesson.student_starting_point",
        "landing_surface": "lesson_student_context_field",
        "generation_role": "state what students can already notice or do and what blocks them",
    },
    {
        "order": 8,
        "schema_key": "key_difficult_points",
        "label": "重难点",
        "adapter_target": "lesson.key_difficult_points",
        "landing_surface": "lesson_key_difficult_points_field",
        "generation_role": "separate teaching focus and difficulty at lesson scale",
    },
    {
        "order": 9,
        "schema_key": "lesson_task_evidence",
        "label": "本课任务与证据",
        "adapter_target": "lesson.lesson_task_evidence",
        "landing_surface": "lesson_task_evidence_field",
        "generation_role": "define what students make, say, compare, revise, or submit",
    },
    {
        "order": 10,
        "schema_key": "classroom_flow",
        "label": "教学过程",
        "adapter_target": "lesson.classroom_flow",
        "landing_surface": "line_level_step_contracts",
        "generation_role": "generate step contracts before line-level edits",
    },
    {
        "order": 11,
        "schema_key": "courseware_plan",
        "label": "课件/大屏计划",
        "adapter_target": "lesson.courseware_plan",
        "landing_surface": "right_rail_courseware_preview_or_task_list",
        "generation_role": "derive screen/page plan from classroom_flow",
    },
    {
        "order": 12,
        "schema_key": "handout_plan",
        "label": "学习单/学生任务单计划",
        "adapter_target": "lesson.handout_plan",
        "landing_surface": "handout_or_learning_sheet_candidate",
        "generation_role": "derive student-facing sheet from activity and evidence",
    },
    {
        "order": 13,
        "schema_key": "assessment_plan",
        "label": "评价计划",
        "adapter_target": "lesson.assessment_plan",
        "landing_surface": "lesson_assessment_field_or_assessment_card",
        "generation_role": "match evidence, criteria, and feedback moments",
    },
    {
        "order": 14,
        "schema_key": "material_requests",
        "label": "资料补充",
        "adapter_target": "lesson.material_requests",
        "landing_surface": "material_gap_prompt_only",
        "generation_role": "ask for missing textbook, image, student work, or schedule evidence",
    },
]


def build_big_unit_mapping() -> dict:
    return {
        "schema_id": "big_unit_22_field_mapping_1013R_R80",
        "stage": STAGE,
        "purpose": "Map GPT/R79A conceptual teaching-design fields back to the current R79C5 22 visible big-unit fields.",
        "source_priority": [
            str(R79C5_DIR / "big_unit_field_id_chips_1013R_R79C5.json"),
            str(R79A_DIR / "unit_design_schema_v2_1013R_R79A.json"),
            "current user correction: 22 visible fields are the big-unit page contract",
        ],
        "boundary_flags": {
            "r21_page_modified": False,
            "new_page_created": False,
            "model_provider_runtime_connected": False,
            "database_write": False,
            "feishu_write": False,
            "formal_apply_allowed": False,
            "r79b_used_as_final_field_standard": False,
        },
        "big_unit_fields": BIG_UNIT_FIELDS,
        "concept_to_visible_field_mapping": CONCEPT_MAPPINGS,
        "line_count_policy": {
            "fixed_second_level_slots": False,
            "notes": "A field may contain 2, 3, 4, or 5 generated lines. Order is stable inside a field, but the model must not assume field A owns global line numbers 1-3.",
        },
    }


def build_lesson_mapping() -> dict:
    return {
        "schema_id": "lesson_schema_mapping_1013R_R80",
        "stage": STAGE,
        "source_schema": str(R79A_DIR / "lesson_design_schema_v2_1013R_R79A.json"),
        "decision": "Do not continue the old R79B lesson field standard. Build the next lesson schema mapping from R79A through this R80 adapter.",
        "structured_reasoning_not_sequential_field_fill": True,
        "lesson_fields": LESSON_FIELDS,
        "inheritance_rule": "single_lesson_must_inherit_unit_big_idea_and_essential_question_before_generation",
        "reuse_foundations": [
            {"id": "R21", "name": "current page carrier", "reuse": True, "rule": "do not rewire or replace the page shell"},
            {"id": "R50_R60", "name": "field-aware edit card and smoke behavior", "reuse": True, "rule": "reuse edit card visibility and no-cross-field checks"},
            {"id": "R6P", "name": "r6p-section-edit-data", "reuse": True, "rule": "reuse section edit data where still compatible"},
            {"id": "R45_R47", "name": "candidate to existing edit-card bridge", "reuse": True, "rule": "keep candidate normalize into before/after/suggestion panel"},
            {"id": "existing_css", "name": "current visual system", "reuse": True, "rule": "do not reset layout or repaint the page foundation"},
            {"id": "right_rail", "name": "right tool/preview rail", "reuse": True, "rule": "route previews and prompts without creating a new product page"},
            {"id": "bottom_xiaojiao_composer", "name": "bottom 小教 input", "reuse": True, "rule": "teacher intent enters generation flow from the existing composer"},
            {"id": "preview_undo_teacher_gate", "name": "preview, undo, and teacher confirmation gates", "reuse": True, "rule": "formal apply stays blocked until teacher confirmation"},
        ],
        "deprecated_r79b_assets": [
            "old_field_map",
            "old_visual_map_data",
            "old_contract_visual_script",
            "old_generation_slot_ids",
        ],
        "replace_only": [
            "R79B old field map",
            "R79B visual map data",
            "R79B contract visual script",
            "generation flow contract",
        ],
        "do_not_replace": [
            "R21 page carrier",
            "R50-R60 edit card foundation",
            "R6P section edit data foundation",
            "R45-R47 edit-card candidate bridge",
            "existing CSS layout",
            "right rail",
            "bottom 小教 input",
        ],
    }


def build_visual_language_dimension() -> dict:
    return {
        "schema_id": "visual_language_hidden_dimension_1013R_R80",
        "stage": STAGE,
        "visible_top_level_field": False,
        "hidden_dimension_key": "visual_language",
        "decision": "美术语言不显性放在一级页面字段中；它是生成推演维度，分布落到相关字段和行级契约。",
        "example_topic": "三年级美术《色彩的渐变》",
        "example_dimension_atoms": [
            "色相渐变",
            "明度渐变",
            "纯度变化",
            "冷暖变化",
            "色阶排序",
            "过渡控制",
        ],
        "hidden_landing_fields": [
            {"page_field_key": "big_idea", "label": "大观念", "reason": "turn color change into transferable visual understanding"},
            {"page_field_key": "content_analysis", "label": "单元内容分析", "reason": "read textbook content through visual-language structure"},
            {"page_field_key": "unit_learning_goals", "label": "单元学习目标", "reason": "make perception, comparison, expression, and reflection observable"},
            {"page_field_key": "key_difficult_points", "label": "学习重难点", "reason": "identify the hardest visual operation, not generic appreciation"},
            {"page_field_key": "learning_activity", "label": "学习活动", "reason": "guide observation, sorting, mixing, trial, display, and revision"},
            {"page_field_key": "task_assessment_points", "label": "任务评估要点", "reason": "assess whether color transition evidence is visible"},
            {"page_field_key": "learning_assessment", "label": "学习评价", "reason": "connect process checks to visual-language evidence"},
            {"page_field_key": "resource_scaffold", "label": "资源支架", "reason": "request needed images, cards, gradients, samples, or demonstrations"},
            {"page_field_key": "assessment_scaffold", "label": "评价支架", "reason": "give teacher/student language for visible evidence"},
        ],
        "forbidden": [
            "do_not_render_visual_language_as_visible_top_level_page_field",
            "do_not_create_an_independent_blue_or_orange_model_card_for_visual_language",
            "do_not_treat_visual_language_as_a_formal_content_source_without_textbook_or_teacher_confirmation",
            "do_not_formal_apply_without_teacher_confirmation",
        ],
    }


def build_adapter_contract() -> dict:
    return {
        "schema_id": "generation_to_field_adapter_contract_1013R_R80",
        "stage": STAGE,
        "purpose": "Define how generated reasoning is normalized into current field candidates and edit-card patches.",
        "input_sources": [
            "teacher_intent",
            "grade_subject_term",
            "textbook_ocr_or_material_requests",
            "official_teaching_design_reference",
            "quality_big_unit_cases",
            "R79A unit schema",
            "R79A lesson schema",
            "R79A lesson step contract schema",
        ],
        "reasoning_outputs": [
            "unit_spine",
            "lesson_logic",
            "field_landing_plan",
            "line_level_contracts",
            "local_regeneration_candidates",
        ],
        "candidate_envelope_required_keys": [
            "candidate_id",
            "stage",
            "source_reasoning_phase",
            "canonical_field_key",
            "target_field_key",
            "explicit_alias_of",
            "target_section",
            "target_line_contract_id",
            "before_text",
            "after_text",
            "xiaojiao_suggestion",
            "impact_scope",
            "work_object_patch",
            "formal_apply_allowed",
            "applied",
        ],
        "candidate_envelope_defaults": {
            "stage": STAGE,
            "target_destination": "existing_edit_card_before_after_suggestion_panel",
            "formal_apply_allowed": False,
            "applied": False,
            "preview_only": True,
        },
        "normalize_rules": [
            {
                "rule": "reject_missing_canonical_field_key",
                "description": "A candidate without canonical_field_key cannot enter the edit card bridge.",
            },
            {
                "rule": "reject_missing_target_field_key",
                "description": "A candidate must name the visible page field it lands in.",
            },
            {
                "rule": "resolve_alias_before_routing",
                "description": "Old field ids or R79B ids must resolve to the active R80 target field before preview.",
            },
            {
                "rule": "material_requests_action_prompt_only",
                "description": "material_requests may request missing sources but cannot write formal lesson content.",
            },
            {
                "rule": "line_level_patch_after_field_landing",
                "description": "Line patches are generated only after the parent field landing is known.",
            },
        ],
        "quality_gates": [
            "source_gap_check",
            "unit_spine_consistency_check",
            "lesson_inheritance_check",
            "field_target_check",
            "line_contract_check",
            "teacher_preview_gate",
        ],
        "forbidden_actions": {
            "new_page_foundation": False,
            "r21_rewire": False,
            "provider_model_runtime_connection": False,
            "database_write": False,
            "feishu_write": False,
            "memory_write": False,
            "formal_apply": False,
        },
    }


GENERATION_FLOW_MD = """
# 1013R R80 Generation Flow And Field Mapping Contract

R80 的任务不是重做页面，也不是接模型。R80 只做一件事：把 R79 讨论出的教学设计生成逻辑，翻译成当前系统可执行的字段映射层和生成流程契约层。

## 边界

- 不重做底座。
- 不重接 R21。
- 不新开产品页。
- 不接 provider/model/runtime。
- 不写数据库、飞书或记忆。
- 不 formal apply。
- 不把 R79B 当最终单课字段标准。
- 不把 `learning_progression`、`scaffold_pack`、`assessment_scheme` 直接当页面字段。
- 不把 `visual_language` 做成显性一级字段。

## 总原则

生成不是顺序填字段，而是结构化推演。

```text
大单元主线推演
  -> 单课成立逻辑
    -> 字段落点
      -> 行级契约
        -> 局部重生成
```

这意味着模型不能按“字段 1、字段 2、字段 3”机械填空。它必须先形成教学设计主线，再把主线投射到不同字段。一个字段内部可以有 2、3、4、5 条行级契约，数量由教学逻辑决定，不由页面固定槽位决定。

## Phase 0 输入解析

解析教师意图、年级、学科、学期、单元、课题、课时、教材页码、资料状态和教师补充要求。输入只能作为 preview 候选依据，不能直接写正式课包。

## Phase 1 资料缺口判断

先判断教材 OCR、单元页、课时安排、示范图、学生作品样例、评价表维度、真实班级学情是否缺失。缺失内容进入 `material_requests`，只做资料补充提示，不写入正式教学设计。

## Phase 2 大单元主线推演

大单元主线先于单课生成，至少形成：

- 单元信息
- 单元主题
- 大观念
- 基本问题
- 表现性任务
- 任务评估要点
- 学习推进结构

`visual_language` 在这里作为隐性推演维度参与理解，例如色相渐变、明度渐变、纯度变化、冷暖变化、色阶排序和过渡控制，但它不成为一级页面字段。

## Phase 3 单课成立逻辑

单课必须继承大单元主线后再成立。单课不能脱离单元语境孤立生成。单课逻辑至少回答：

- 本课从大观念中切出哪一片？
- 本课的驱动问题是什么？
- 学生起点在哪里？
- 本课任务和证据是什么？
- 本课教学过程如何支撑单元表现性任务？

## Phase 4 字段落点

抽象概念字段必须落回当前页面字段：

- `learning_progression` -> 学习阶段 / 学习任务 / 小问题 / 学习活动 / 学习评价
- `scaffold_pack` -> 情境支架 / 任务支架 / 资源支架 / 策略支架 / 学习单 / 评价支架
- `assessment_scheme` -> 任务评估要点 / 学习评价 / 评价支架
- `unit_identity` -> 单元信息
- `visual_language` -> 隐性推演维度，不作为一级页面字段

## Phase 5 行级契约

每个字段内部再拆成行级契约。行级契约包含可定位、可替换、可预览、可撤销的最小写入单元。教学过程类字段还要拆出 teacher_action、student_action、material_or_screen、evidence 和 design_intent。

## Phase 6 局部重生成

教师修改某个字段或某一行时，小教只针对对应字段和行级契约生成候选。候选必须带 `canonical_field_key`、`target_field_key`、`target_line_contract_id` 和 `impact_scope`，不能串字段，不能写进正文，不能 formal apply。

## Phase 7 候选进入旧编辑卡

候选进入已有编辑卡的“修改前 / 修改后 / 小教建议”结构，不再在正文里生成独立蓝卡。旧 R79B 可视化 map 废弃，R21/R50/R60/R6P/R45-R47 的页面、编辑卡、候选桥、CSS、preview/undo/teacher gate 底座复用。

## Phase 8 教师预览采纳

所有候选默认：

```text
preview_only=true
applied=false
formal_apply_allowed=false
```

只有教师确认后，才允许进入后续正式写入流程。R80 本身不实现正式写入。
"""


MIGRATION_PLAN_MD = """
# 1013R R80 R79B Deprecated Visual Map Migration Plan

## 结论

R79B 不作为最终单课字段标准。R79B 的价值是证明当前 R21 样板间上可以做字段可视化、候选位、编辑卡桥接和行级契约提示；但它的旧字段 map、visual map data、contract visual script 和 generation slot id 不能继续当标准。

## 保留

- R21 页面承载。
- 现有 CSS 和页面布局。
- 右侧工具栏和预览区。
- 底部小教输入。
- 旧编辑卡的“修改前 / 修改后 / 小教建议”结构。
- R50-R60 字段感知编辑卡思路。
- R6P section edit data 能复用的部分。
- R45-R47 candidate normalize 到编辑卡的桥接机制。
- preview / undo / teacher gate。

## 废弃

- R79B old field map。
- R79B visual map data。
- R79B contract visual script。
- R79B old generation slot ids。
- 把正文独立蓝卡当作模型候选承载的做法。
- 把旧单课字段标准当作最终字段标准的做法。

## 迁移步骤

1. 冻结 R79B 作为历史原型证据，不再向它追加字段标准。
2. 以 R79A lesson schema 作为单课 schema 来源。
3. 以 R80 lesson_schema_mapping 作为旧页面底座和新单课 schema 之间的 adapter。
4. 替换旧字段 map，不替换页面壳。
5. 替换旧 visual map data，不替换 CSS 基础。
6. 替换旧 contract visual script 的字段表，不重做编辑卡。
7. 候选进入已有 before/after/suggestion 编辑卡，不在正文生成独立蓝卡。
8. R81 再做单课字段 schema map，仍然不重做底座。

## 禁止

- 不回退 R21。
- 不重接 R21/R50/R60/R6P/R45-R47。
- 不新开产品页。
- 不接模型 runtime。
- 不写数据库、飞书或记忆。
- 不 formal apply。
"""


VALIDATOR = r'''
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
'''


README = """
# 1013R R80 Generation Flow And Field Mapping Contract

R80 是字段映射层和生成流程契约层，不是新页面、不是模型接入、不是正式写入。

## 本轮判断

- GPT 的大方向可采纳：整体推演 -> 字段分解 -> 行级契约 -> 局部重生成。
- 当前系统必须以 R79C5 的 22 个大单元字段为可见页面字段。
- R79A 的 `learning_progression`、`scaffold_pack`、`assessment_scheme` 是结构概念，必须降落到 22 个可见字段，不能直接成为页面字段。
- `visual_language` 是隐性推演维度，不显性作为一级字段。
- R79B 不作为最终单课字段标准，但其页面底座、CSS、编辑卡和候选桥接机制要尽量复用。

## 关键计数

- big_unit_visible_field_count=22
- lesson_schema_field_count=14
- visual_language_visible_top_level=false
- r21_page_modified=false
- new_page_created=false
- model_provider_runtime_connected=false
- formal_apply_allowed=false

## 文件

- `big_unit_22_field_mapping_1013R_R80.json`
- `lesson_schema_mapping_1013R_R80.json`
- `visual_language_hidden_dimension_1013R_R80.json`
- `generation_reasoning_flow_contract_1013R_R80.md`
- `generation_to_field_adapter_contract_1013R_R80.json`
- `r79b_deprecated_visual_map_migration_plan_1013R_R80.md`
- `validate_1013R_R80_generation_flow_field_mapping.py`
- `validate_1013R_R80_generation_flow_field_mapping_result.json`
"""


MANIFEST = """
# REVIEW PACKAGE MANIFEST

Stage: 1013R_R80_GENERATION_FLOW_AND_FIELD_MAPPING_CONTRACT

## Included

1. README.md
2. REVIEW_PACKAGE_MANIFEST.md
3. big_unit_22_field_mapping_1013R_R80.json
4. lesson_schema_mapping_1013R_R80.json
5. visual_language_hidden_dimension_1013R_R80.json
6. generation_reasoning_flow_contract_1013R_R80.md
7. generation_to_field_adapter_contract_1013R_R80.json
8. r79b_deprecated_visual_map_migration_plan_1013R_R80.md
9. validate_1013R_R80_generation_flow_field_mapping.py
10. validate_1013R_R80_generation_flow_field_mapping_result.json

## Source References

- R79A unit schema: outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R79A_TEACHING_DESIGN_STRUCTURE_SOURCE_COMPARISON/unit_design_schema_v2_1013R_R79A.json
- R79A lesson schema: outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R79A_TEACHING_DESIGN_STRUCTURE_SOURCE_COMPARISON/lesson_design_schema_v2_1013R_R79A.json
- R79C5 big-unit visible field page data: outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R79C5_BIG_UNIT_FIELD_ID_CHIPS/big_unit_field_id_chips_1013R_R79C5.json
- R79B historical visual prototype: outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R79B_TEACHING_DESIGN_CONTRACT_VISUAL_PROTOTYPE

## Not Included

- No copied R21 HTML.
- No new static page.
- No model provider code.
- No database or Feishu write.
- No formal apply implementation.
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    write_json(OUT / "big_unit_22_field_mapping_1013R_R80.json", build_big_unit_mapping())
    write_json(OUT / "lesson_schema_mapping_1013R_R80.json", build_lesson_mapping())
    write_json(OUT / "visual_language_hidden_dimension_1013R_R80.json", build_visual_language_dimension())
    write_json(OUT / "generation_to_field_adapter_contract_1013R_R80.json", build_adapter_contract())
    write_text(OUT / "generation_reasoning_flow_contract_1013R_R80.md", GENERATION_FLOW_MD)
    write_text(OUT / "r79b_deprecated_visual_map_migration_plan_1013R_R80.md", MIGRATION_PLAN_MD)
    write_text(OUT / "validate_1013R_R80_generation_flow_field_mapping.py", VALIDATOR)
    write_text(OUT / "README.md", README)
    write_text(OUT / "REVIEW_PACKAGE_MANIFEST.md", MANIFEST)
    print(str(OUT))


if __name__ == "__main__":
    main()
