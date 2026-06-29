from __future__ import annotations

import json
from pathlib import Path


STAGE = "1013R_R82_LESSON_GENERATION_REQUEST_RESPONSE_CONTRACT"
ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1"
OUT = BASE / STAGE
R80_DIR = BASE / "1013R_R80_GENERATION_FLOW_AND_FIELD_MAPPING_CONTRACT"
R81_DIR = BASE / "1013R_R81_LESSON_SCHEMA_FIELD_MAP_ADAPTER"
R21_HTML = BASE / "1013R_R21_page_copy_binds_unified_package" / "prep_room_page_copy_binds_unified_package_1013R_R21.html"


LESSON_SCHEMA_KEYS = [
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


TARGET_SECTIONS = {
    "lesson_identity": "lesson_header",
    "inherited_unit_context": "basis",
    "textbook_anchor": "basis",
    "lesson_concept_slice": "basis",
    "lesson_focus_question": "basis",
    "lesson_objectives": "goals",
    "student_starting_point": "analysis",
    "key_difficult_points": "keypoints",
    "lesson_task_evidence": "assessment",
    "classroom_flow": "teaching_process",
    "courseware_plan": "courseware_plan",
    "handout_plan": "handout_plan",
    "assessment_plan": "assessment",
    "material_requests": "material_requests",
}


STEP_CONTRACT_FIELDS = [
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


R81_CANDIDATE_KEYS = [
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


RESPONSE_TOP_LEVEL_KEYS = [
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


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text.strip() + "\n", encoding="utf-8")


def build_request_envelope() -> dict:
    return {
        "schema_id": "lesson_generation_request_envelope_1013R_R82",
        "stage": STAGE,
        "purpose": "Define the request object for future model calls. R82 itself does not call a model.",
        "request_types": [
            "initial_lesson_preview",
            "local_field_regeneration",
            "step_contract_regeneration",
            "derived_preview_generation",
        ],
        "required_input_keys": [
            "request_id",
            "request_type",
            "lesson_design_mode",
            "teacher_intent",
            "grade_subject_term",
            "big_unit_spine",
            "lesson_context",
            "material_state",
            "allowed_schema_keys",
            "target_section_map",
            "step_contract_fields",
            "output_limits",
            "source_policy",
            "boundary_flags",
            "hard_rules",
        ],
        "allowed_schema_keys": LESSON_SCHEMA_KEYS,
        "target_section_map": TARGET_SECTIONS,
        "step_contract_fields": STEP_CONTRACT_FIELDS,
        "minimum_step_fields": MINIMUM_STEP_FIELDS,
        "input_context_contract": {
            "big_unit_spine": [
                "unit_theme",
                "big_idea",
                "essential_question",
                "performance_task",
                "task_assessment_points",
                "visual_language_atoms",
            ],
            "lesson_context": [
                "lesson_identity",
                "current_visible_sections",
                "current_process_steps",
                "active_teacher_focus",
                "r81_mapping_ref",
            ],
            "material_state": [
                "textbook_ocr_available",
                "textbook_page_refs",
                "official_reference_available",
                "quality_case_available",
                "student_profile_available",
                "missing_materials",
            ],
        },
        "output_limits_defaults": {
            "target_resolution_count_min": 1,
            "target_resolution_count_max": 6,
            "step_reasoning_updates_count_min": 0,
            "step_reasoning_updates_count_max": 5,
            "field_patch_candidates_count_min": 1,
            "field_patch_candidates_count_max": 8,
            "impact_scope_count_max": 5,
            "teacher_questions_count_max": 2,
            "string_max_chars_default": 80,
            "array_item_max_count_default": 5,
        },
        "source_policy": {
            "must_mark_source_refs": True,
            "no_fake_textbook": True,
            "no_fake_student_profile": True,
            "missing_source_routes_to_material_requests": True,
            "visual_language_hidden_dimension_only": True,
        },
        "boundary_flags_required_false": [
            "database_written",
            "feishu_written",
            "memory_written",
            "formal_export_created",
            "official_archive_created",
            "formal_apply_performed",
        ],
    }


def build_response_schema() -> dict:
    return {
        "schema_id": "lesson_generation_response_schema_1013R_R82",
        "stage": STAGE,
        "purpose": "Define strict JSON shape a future model response must satisfy before normalization.",
        "top_level_required_keys": RESPONSE_TOP_LEVEL_KEYS,
        "lesson_logic_brief_shape": {
            "inherited_unit_context_summary": "string",
            "core_learning_problem": "string",
            "student_starting_point": "string",
            "target_shift": "string",
            "lesson_focus_question": "string",
            "visual_language_use": "string_hidden_dimension_not_visible_field",
            "teaching_route": ["string"],
            "evidence_plan": ["string"],
            "risk_points": ["string"],
            "source_basis": ["string"],
            "material_gaps": ["string"],
        },
        "target_resolution_item_required_keys": [
            "schema_key",
            "target_section",
            "target_step_id",
            "target_field",
            "reason",
            "source_refs",
        ],
        "step_reasoning_update_required_keys": [
            "target_line_contract_id",
            "step_id",
            "step_name",
            *MINIMUM_STEP_FIELDS,
        ],
        "field_patch_candidate_required_keys": [
            *R81_CANDIDATE_KEYS,
            "patch_type",
            "reasoning_basis",
        ],
        "quality_gate_update_shape": {
            "level": "blocked|basic_usable|ready_to_teach|refined|open_class_ready",
            "passed_items": ["string"],
            "missing_items": ["string"],
            "risk_items": ["string"],
            "next_best_action": "string",
        },
        "boundary_flags_required": {
            "teacher_review_required": True,
            "formal_apply_performed": False,
            "database_written": False,
            "memory_written": False,
            "feishu_written": False,
            "formal_export_created": False,
            "official_archive_created": False,
        },
        "forbidden_legacy_keys_anywhere": [
            "section",
            "field",
            "path",
            "type",
            "content",
            "purpose",
            "current_value",
            "patch_value",
            "formal_apply_performed",
        ],
        "legacy_key_exception": {
            "formal_apply_performed": "allowed only inside boundary_flags for backward readable evidence; normalized candidate must use formal_apply_allowed=false and applied=false"
        },
    }


PROMPT_MD = """
# 1013R R82 Lesson Generation Prompt Contract

R82 只定义未来模型调用的 prompt/request/response 契约，不执行模型调用。

## System Prompt

你是师维备课室的小教。你只把教师意图转成结构化备课候选，不写正式教案，不覆盖页面原文，不生成正文独立蓝卡，不调用外部工具。你必须先继承大单元主线，再推演单课成立逻辑，再映射到 R81 的 14 个单课 schema key，再生成字段候选和教学过程行级契约。

## Hard Rules

1. 只输出 JSON 对象。第一个字符必须是 `{`，最后一个字符必须是 `}`。
2. 不要 markdown，不要代码块，不要解释文字。
3. 不要输出完整正式教案；只输出结构化推演、字段落点、行级契约、候选补丁、影响范围和教师确认信息。
4. `schema_key` 必须来自 R81 的 14 个单课字段。
5. `target_section` 必须来自 R81 的目标区段，不允许输出中文区段名或旧字段名。
6. `field_patch_candidates` 必须是数组。
7. `step_reasoning_updates` 必须是数组；如果本次不改教学过程，可以是空数组。
8. 每个候选必须带 `schema_key`、`canonical_field_key`、`target_field_key`、`target_line_contract_id`、`target_destination`。
9. `target_destination` 只能是 `existing_edit_card_before_after_suggestion_panel`。
10. 所有候选必须 `teacher_review_required=true`、`preview_only=true`、`formal_apply_allowed=false`、`applied=false`。
11. 禁止 `standalone_blue_card`，禁止正文直写，禁止 formal apply。
12. `visual_language` 只能作为隐性推演维度，不能作为显性一级字段。
13. 缺教材、缺示范图、缺学生作品或缺真实学情时，只能写入 `material_requests`，不能伪造来源。
14. 没有真实学生档案时，依据写“教学预设 / 教师输入 / 教材锚点 / 资料候选”，不要冒充真实学生画像。
15. 不要出现旧字段名：`field/path/type/content/purpose/current_value/patch_value`。

## User Prompt Template

把下面教师意图转成 R82 JSON 响应。必须使用请求中的 `allowed_schema_keys`、`target_section_map` 和 `step_contract_fields`，不得发明字段。

```json
{{lesson_generation_request_envelope}}
```

## Response Strategy

先在 `lesson_logic_brief` 中给出短推演，再用 `target_resolution` 指明哪些 schema key 被触达，再用 `step_reasoning_updates` 写教学过程行级契约，最后用 `field_patch_candidates` 形成可进入旧编辑卡的候选。
"""


def build_normalizer_contract() -> dict:
    return {
        "schema_id": "lesson_generation_response_normalizer_contract_1013R_R82",
        "stage": STAGE,
        "purpose": "Normalize future model JSON into R81 edit-card candidates or reject it.",
        "parse_rules": [
            "reject_non_json_text",
            "reject_markdown_code_fence",
            "reject_top_level_array",
            "reject_missing_required_top_level_keys",
            "reject_unknown_schema_key",
            "reject_unknown_target_section",
            "reject_standalone_blue_card_destination",
            "reject_candidate_without_target_line_contract_id",
            "reject_candidate_with_formal_apply_allowed_true",
            "reject_candidate_with_applied_true",
            "reject_material_requests_formal_content",
        ],
        "allowed_schema_keys": LESSON_SCHEMA_KEYS,
        "target_section_map": TARGET_SECTIONS,
        "required_candidate_keys": R81_CANDIDATE_KEYS,
        "normalizer_output_shape": {
            "normalized": "boolean",
            "accepted_candidate_count": "integer",
            "rejected_candidate_count": "integer",
            "normalized_candidates": ["R81 candidate envelope"],
            "rejection_reasons": ["string"],
            "teacher_review_required": True,
            "formal_apply_allowed": False,
            "r21_write_allowed": False,
        },
        "repair_policy": {
            "auto_repair_minor_whitespace": True,
            "auto_repair_code_fence": False,
            "auto_map_chinese_section_label": False,
            "auto_create_missing_schema_key": False,
            "auto_create_missing_source_refs": False,
        },
    }


def build_quality_gate() -> dict:
    return {
        "schema_id": "lesson_generation_quality_gate_contract_1013R_R82",
        "stage": STAGE,
        "quality_gates": [
            {
                "gate_id": "source_gap_check",
                "required": True,
                "pass_condition": "missing textbook, image, student profile, or official reference is routed to material_requests",
            },
            {
                "gate_id": "unit_spine_consistency_check",
                "required": True,
                "pass_condition": "lesson_logic_brief references big_unit_spine before local lesson changes",
            },
            {
                "gate_id": "r81_schema_key_check",
                "required": True,
                "pass_condition": "every target_resolution and field_patch_candidate uses an allowed R81 schema_key",
            },
            {
                "gate_id": "target_section_check",
                "required": True,
                "pass_condition": "every target_section matches R81 target_section_map",
            },
            {
                "gate_id": "line_contract_check",
                "required": True,
                "pass_condition": "classroom_flow patches have target_line_contract_id and minimum step fields",
            },
            {
                "gate_id": "visual_language_hidden_check",
                "required": True,
                "pass_condition": "visual_language is used only in lesson_logic_brief or reasoning basis, not as visible schema_key",
            },
            {
                "gate_id": "teacher_gate_check",
                "required": True,
                "pass_condition": "all candidates remain preview_only and teacher_review_required",
            },
            {
                "gate_id": "side_effect_check",
                "required": True,
                "pass_condition": "database, memory, feishu, export, archive, formal apply are false",
            },
        ],
        "quality_levels": ["blocked", "basic_usable", "ready_to_teach", "refined", "open_class_ready"],
        "blocked_if": [
            "no_big_unit_spine",
            "missing_source_refs",
            "unknown_schema_key",
            "standalone_blue_card_destination",
            "formal_apply_attempt",
            "fake_textbook_or_student_profile",
        ],
    }


def build_smoke_fixtures() -> dict:
    valid_response = {
        "response_stage": STAGE,
        "request_id": "r82_smoke_001",
        "lesson_design_mode": "time_or_resource_constrained",
        "intent_summary": "30分钟内保留表达和评价证据。",
        "lesson_logic_brief": {
            "inherited_unit_context_summary": "继承单元大观念：色彩变化会影响感受与表达。",
            "core_learning_problem": "时间缩短时仍要保留学生表达证据。",
            "student_starting_point": "学生能说喜欢颜色，但理由容易停在好看。",
            "target_shift": "从涂色完成转向能说明色彩感受。",
            "lesson_focus_question": "怎样用有限时间让颜色感受说得出来？",
            "visual_language_use": "冷暖、明暗和色彩情绪作为隐性推演维度。",
            "teaching_route": ["快速感知", "重点表现", "表达评价"],
            "evidence_plan": ["作品照片", "一句话说明"],
            "risk_points": ["表现时间挤压表达"],
            "source_basis": ["教师输入", "R81课堂流程", "大单元大观念"],
            "material_gaps": [],
        },
        "target_resolution": [
            {
                "schema_key": "classroom_flow",
                "target_section": "teaching_process",
                "target_step_id": "share",
                "target_field": "time_allocation",
                "reason": "压缩后仍要保留表达证据。",
                "source_refs": ["teacher_intent", "current_process_steps"],
            },
            {
                "schema_key": "assessment_plan",
                "target_section": "assessment",
                "target_step_id": "share",
                "target_field": "evidence_capture",
                "reason": "评价要看学生说明是否成立。",
                "source_refs": ["lesson_task_evidence", "teacher_intent"],
            },
        ],
        "step_reasoning_updates": [
            {
                "target_line_contract_id": "lesson_step.color_feeling.05.success_criteria",
                "step_id": "share",
                "step_name": "交流展示",
                "step_goal": "用一句话说明色彩选择和感受。",
                "teacher_talk": "请说出你用了什么颜色，想表达什么感觉。",
                "student_task": "展示作品并说一句选择理由。",
                "success_criteria": "能把颜色、感受和理由连起来。",
                "guiding_questions": "哪一个颜色最能说明你的感受？",
                "source_refs": ["teacher_intent", "current_process_steps"],
                "generation_slot": "preview_only",
            }
        ],
        "field_patch_candidates": [
            {
                "field_patch_id": "r82_smoke_share_time",
                "schema_key": "classroom_flow",
                "canonical_field_key": "classroom_flow",
                "target_field_key": "classroom_flow",
                "target_section": "teaching_process",
                "target_step_id": "share",
                "target_line_contract_id": "lesson_step.color_feeling.05.success_criteria",
                "target_destination": "existing_edit_card_before_after_suggestion_panel",
                "before_summary": "交流展示时间短，证据容易被压缩。",
                "after_candidate": "保留3分钟作品展示和一句话说明。",
                "xiaojiao_suggestion": "先压缩导入和感知，不删表达证据。",
                "impact_scope": ["teacher_action", "student_activity", "evidence_note"],
                "source_refs": ["teacher_intent", "current_process_steps"],
                "teacher_review_required": True,
                "preview_only": True,
                "formal_apply_allowed": False,
                "applied": False,
                "patch_type": "revise",
                "reasoning_basis": ["教学预设", "教师输入"],
            },
            {
                "field_patch_id": "r82_smoke_assessment_evidence",
                "schema_key": "assessment_plan",
                "canonical_field_key": "assessment_plan",
                "target_field_key": "assessment_plan",
                "target_section": "assessment",
                "target_step_id": "share",
                "target_line_contract_id": "lesson_field.assessment_plan.line_01",
                "target_destination": "existing_edit_card_before_after_suggestion_panel",
                "before_summary": "评价只看作品完成度。",
                "after_candidate": "增加一句话说明作为评价证据。",
                "xiaojiao_suggestion": "评价要看学生能否说出色彩选择理由。",
                "impact_scope": ["rubric", "evidence_note"],
                "source_refs": ["lesson_task_evidence", "teacher_intent"],
                "teacher_review_required": True,
                "preview_only": True,
                "formal_apply_allowed": False,
                "applied": False,
                "patch_type": "enrich",
                "reasoning_basis": ["R81字段映射", "教师输入"],
            },
        ],
        "quality_gate_update": {
            "level": "basic_usable",
            "passed_items": ["保留表达证据", "候选能落到R81字段"],
            "missing_items": ["表达卡样式待确认"],
            "risk_items": ["时间仍可能不足"],
            "next_best_action": "让教师确认展示时长。",
        },
        "material_requests": [],
        "teacher_questions": [],
        "ui_binding_hint": {
            "should_enter_edit_mode": True,
            "edit_target": "teaching_process/share",
            "candidate_display_position": "existing_edit_card",
            "right_tray_updates": ["评价证据提醒"],
            "view_mode_summary": "30分钟压缩版预览",
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
    }
    return {
        "schema_id": "lesson_generation_smoke_fixtures_1013R_R82",
        "stage": STAGE,
        "valid_response": valid_response,
        "invalid_responses": [
            {
                "case_id": "markdown_code_fence",
                "raw_text": "```json\n{\"response_stage\":\"x\"}\n```",
                "expected_rejection": "markdown_code_fence",
            },
            {
                "case_id": "missing_schema_key",
                "response": {
                    **valid_response,
                    "field_patch_candidates": [
                        {k: v for k, v in valid_response["field_patch_candidates"][0].items() if k != "schema_key"}
                    ],
                },
                "expected_rejection": "missing_schema_key",
            },
            {
                "case_id": "unknown_target_section",
                "response": {
                    **valid_response,
                    "field_patch_candidates": [
                        {**valid_response["field_patch_candidates"][0], "target_section": "教学过程"}
                    ],
                },
                "expected_rejection": "unknown_target_section",
            },
            {
                "case_id": "standalone_blue_card",
                "response": {
                    **valid_response,
                    "field_patch_candidates": [
                        {**valid_response["field_patch_candidates"][0], "target_destination": "standalone_blue_card"}
                    ],
                },
                "expected_rejection": "standalone_blue_card_destination",
            },
            {
                "case_id": "formal_apply_true",
                "response": {
                    **valid_response,
                    "field_patch_candidates": [
                        {**valid_response["field_patch_candidates"][0], "formal_apply_allowed": True}
                    ],
                },
                "expected_rejection": "formal_apply_allowed_true",
            },
        ],
    }


README = """
# 1013R R82 Lesson Generation Request Response Contract

R82 是未来模型调用的请求/响应契约，不是模型调用本身。

## 结果

- allowed_schema_key_count=14
- response_top_level_key_count=13
- required_candidate_key_count=17
- valid_smoke_response_accepted=true
- invalid_smoke_responses_rejected=true
- r21_page_modified=false
- model_provider_runtime_connected=false
- formal_apply_allowed=false

## 文件

- `lesson_generation_request_envelope_1013R_R82.json`
- `lesson_generation_response_schema_1013R_R82.json`
- `lesson_generation_prompt_contract_1013R_R82.md`
- `lesson_generation_response_normalizer_contract_1013R_R82.json`
- `lesson_generation_quality_gate_contract_1013R_R82.json`
- `lesson_generation_smoke_fixtures_1013R_R82.json`
- `validate_1013R_R82_lesson_generation_request_response_contract.py`
- `validate_1013R_R82_lesson_generation_request_response_contract_result.json`
"""


MANIFEST = """
# REVIEW PACKAGE MANIFEST

Stage: 1013R_R82_LESSON_GENERATION_REQUEST_RESPONSE_CONTRACT

## Included

1. README.md
2. REVIEW_PACKAGE_MANIFEST.md
3. lesson_generation_request_envelope_1013R_R82.json
4. lesson_generation_response_schema_1013R_R82.json
5. lesson_generation_prompt_contract_1013R_R82.md
6. lesson_generation_response_normalizer_contract_1013R_R82.json
7. lesson_generation_quality_gate_contract_1013R_R82.json
8. lesson_generation_smoke_fixtures_1013R_R82.json
9. validate_1013R_R82_lesson_generation_request_response_contract.py
10. validate_1013R_R82_lesson_generation_request_response_contract_result.json

## Source References

- R80 generation-to-field adapter contract.
- R81 lesson 14-field mapping.
- R81 lesson candidate envelope.
- Historical 1013E/R2 and 1013N model traces, used only to harden rejection rules.

## Not Included

- No provider/model runtime connection.
- No R21 HTML modification.
- No new page.
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
'''


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    write_json(OUT / "lesson_generation_request_envelope_1013R_R82.json", build_request_envelope())
    write_json(OUT / "lesson_generation_response_schema_1013R_R82.json", build_response_schema())
    write_text(OUT / "lesson_generation_prompt_contract_1013R_R82.md", PROMPT_MD)
    write_json(OUT / "lesson_generation_response_normalizer_contract_1013R_R82.json", build_normalizer_contract())
    write_json(OUT / "lesson_generation_quality_gate_contract_1013R_R82.json", build_quality_gate())
    write_json(OUT / "lesson_generation_smoke_fixtures_1013R_R82.json", build_smoke_fixtures())
    write_text(OUT / "README.md", README)
    write_text(OUT / "REVIEW_PACKAGE_MANIFEST.md", MANIFEST)
    write_text(OUT / "validate_1013R_R82_lesson_generation_request_response_contract.py", VALIDATOR)
    print(str(OUT))


if __name__ == "__main__":
    main()
