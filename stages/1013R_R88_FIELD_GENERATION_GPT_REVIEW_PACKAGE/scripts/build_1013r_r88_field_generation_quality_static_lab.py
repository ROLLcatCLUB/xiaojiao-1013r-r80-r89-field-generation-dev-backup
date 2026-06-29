from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_OUTPUT = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1"
OUT_DIR = BASE_OUTPUT / "1013R_R88_FIELD_GENERATION_QUALITY_STATIC_LAB"
R81_FIELD_MAP = BASE_OUTPUT / "1013R_R81_LESSON_SCHEMA_FIELD_MAP_ADAPTER" / "lesson_14_field_mapping_1013R_R81.json"
R6N_R9A_BIG_UNIT = (
    BASE_OUTPUT
    / "1013I_R6N_R9A_field_label_disambiguation_before_runtime_schema"
    / "big_unit_teacher_visible_field_model_1013I_R6N_R9A.json"
)
HTML_PATH = OUT_DIR / "field_generation_quality_static_lab_1013R_R88.html"
LEDGER_PATH = OUT_DIR / "field_generation_quality_static_lab_ledger_1013R_R88.json"
VALIDATION_PATH = OUT_DIR / "validate_1013R_R88_field_generation_quality_static_lab_result.json"


BIG_UNIT_FIELDS = [
    {
        "order": 1,
        "visible_label": "单元信息",
        "engineering_key": "big_unit.unit_basic_info",
        "canonical_ref": "unit_basic_info",
        "generation_layer": "unit_spine",
        "generation_slot_id": "R88-GEN/big_unit.unit_basic_info",
        "quality_focus": ["事实锚定", "年级教材清楚", "课时范围清楚"],
    },
    {
        "order": 2,
        "visible_label": "单元主题",
        "engineering_key": "big_unit.unit_theme",
        "canonical_ref": "unit_theme",
        "generation_layer": "unit_spine",
        "generation_slot_id": "R88-GEN/big_unit.unit_theme",
        "quality_focus": ["主题可统领", "不是口号", "能连到作品表达"],
    },
    {
        "order": 3,
        "visible_label": "大观念",
        "engineering_key": "big_unit.big_idea",
        "canonical_ref": "big_idea",
        "generation_layer": "unit_spine",
        "generation_slot_id": "R88-GEN/big_unit.big_idea",
        "quality_focus": ["可迁移理解", "不写成步骤", "能统领单课"],
    },
    {
        "order": 4,
        "visible_label": "基本问题",
        "engineering_key": "big_unit.essential_question",
        "canonical_ref": "unit_questions",
        "generation_layer": "unit_spine",
        "generation_slot_id": "R88-GEN/big_unit.essential_question",
        "quality_focus": ["可持续追问", "贴近儿童", "能落到课堂活动"],
    },
    {
        "order": 5,
        "visible_label": "单元学习目标",
        "engineering_key": "big_unit.learning_goals",
        "canonical_ref": "core_literacy_goals",
        "generation_layer": "unit_goals",
        "generation_slot_id": "R88-GEN/big_unit.learning_goals",
        "quality_focus": ["可观察行为", "学科语言适度", "目标不过满"],
    },
    {
        "order": 6,
        "visible_label": "单元内容分析",
        "engineering_key": "big_unit.content_analysis",
        "canonical_ref": "knowledge_and_skills",
        "generation_layer": "unit_goals",
        "generation_slot_id": "R88-GEN/big_unit.content_analysis",
        "quality_focus": ["教材线索", "美术语言隐性支撑", "活动关系清楚"],
    },
    {
        "order": 7,
        "visible_label": "学情分析",
        "engineering_key": "big_unit.student_context",
        "canonical_ref": "student_starting_point",
        "generation_layer": "student_context",
        "generation_slot_id": "R88-GEN/big_unit.student_context",
        "quality_focus": ["不伪造班情", "儿童经验具体", "困难可转支架"],
    },
    {
        "order": 8,
        "visible_label": "学习重难点",
        "engineering_key": "big_unit.key_difficult_points",
        "canonical_ref": "knowledge_and_skills",
        "generation_layer": "unit_goals",
        "generation_slot_id": "R88-GEN/big_unit.key_difficult_points",
        "quality_focus": ["重点难点分开", "不重复目标", "能指导活动"],
    },
    {
        "order": 9,
        "visible_label": "表现性任务",
        "engineering_key": "big_unit.performance_task",
        "canonical_ref": "performance_task",
        "generation_layer": "task_evidence",
        "generation_slot_id": "R88-GEN/big_unit.performance_task",
        "quality_focus": ["学生产出明确", "证据可见", "不空泛"],
    },
    {
        "order": 10,
        "visible_label": "任务评估要点",
        "engineering_key": "big_unit.task_assessment_points",
        "canonical_ref": "assessment_evidence",
        "generation_layer": "task_evidence",
        "generation_slot_id": "R88-GEN/big_unit.task_assessment_points",
        "quality_focus": ["和任务对应", "标准可判断", "不只看好看"],
    },
    {
        "order": 11,
        "visible_label": "学习阶段",
        "engineering_key": "big_unit.learning_stages",
        "canonical_ref": "learning_progression",
        "generation_layer": "progression",
        "generation_slot_id": "R88-GEN/big_unit.learning_stages",
        "quality_focus": ["阶段递进", "不是课时流水账", "承接大观念"],
    },
    {
        "order": 12,
        "visible_label": "学习任务",
        "engineering_key": "big_unit.learning_tasks",
        "canonical_ref": "lesson_task_chain",
        "generation_layer": "progression",
        "generation_slot_id": "R88-GEN/big_unit.learning_tasks",
        "quality_focus": ["任务链清楚", "每课有责任", "能切到单课"],
    },
    {
        "order": 13,
        "visible_label": "小问题",
        "engineering_key": "big_unit.micro_questions",
        "canonical_ref": "unit_questions",
        "generation_layer": "progression",
        "generation_slot_id": "R88-GEN/big_unit.micro_questions",
        "quality_focus": ["问题能驱动活动", "儿童能回答", "层级不乱"],
    },
    {
        "order": 14,
        "visible_label": "学习活动",
        "engineering_key": "big_unit.learning_activities",
        "canonical_ref": "lesson_task_chain",
        "generation_layer": "progression",
        "generation_slot_id": "R88-GEN/big_unit.learning_activities",
        "quality_focus": ["活动服务任务", "可上课", "有观察点"],
    },
    {
        "order": 15,
        "visible_label": "学习评价",
        "engineering_key": "big_unit.learning_assessment",
        "canonical_ref": "assessment_evidence",
        "generation_layer": "task_evidence",
        "generation_slot_id": "R88-GEN/big_unit.learning_assessment",
        "quality_focus": ["过程证据", "作品证据", "表达证据"],
    },
    {
        "order": 16,
        "visible_label": "情境支架",
        "engineering_key": "big_unit.scaffold.context",
        "canonical_ref": "skills_materials_scaffolds",
        "generation_layer": "scaffolds",
        "generation_slot_id": "R88-GEN/big_unit.scaffold.context",
        "quality_focus": ["情境贴近儿童", "不喧宾夺主", "能引出任务"],
    },
    {
        "order": 17,
        "visible_label": "任务支架",
        "engineering_key": "big_unit.scaffold.task",
        "canonical_ref": "skills_materials_scaffolds",
        "generation_layer": "scaffolds",
        "generation_slot_id": "R88-GEN/big_unit.scaffold.task",
        "quality_focus": ["步骤清楚", "降低难度", "不替学生完成"],
    },
    {
        "order": 18,
        "visible_label": "资源支架",
        "engineering_key": "big_unit.scaffold.resource",
        "canonical_ref": "skills_materials_scaffolds",
        "generation_layer": "scaffolds",
        "generation_slot_id": "R88-GEN/big_unit.scaffold.resource",
        "quality_focus": ["材料真实", "来源可补", "不虚构教材图"],
    },
    {
        "order": 19,
        "visible_label": "策略支架",
        "engineering_key": "big_unit.scaffold.strategy",
        "canonical_ref": "skills_materials_scaffolds",
        "generation_layer": "scaffolds",
        "generation_slot_id": "R88-GEN/big_unit.scaffold.strategy",
        "quality_focus": ["方法可操作", "语言可教", "能迁移到单课"],
    },
    {
        "order": 20,
        "visible_label": "学习单",
        "engineering_key": "big_unit.handout_plan",
        "canonical_ref": "skills_materials_scaffolds",
        "generation_layer": "derived_objects",
        "generation_slot_id": "R88-GEN/big_unit.handout_plan",
        "quality_focus": ["不堆文字", "任务辅助", "能记录证据"],
    },
    {
        "order": 21,
        "visible_label": "评价支架",
        "engineering_key": "big_unit.assessment_scaffold",
        "canonical_ref": "assessment_evidence",
        "generation_layer": "derived_objects",
        "generation_slot_id": "R88-GEN/big_unit.assessment_scaffold",
        "quality_focus": ["评价语言儿童化", "标准可判断", "能反馈改进"],
    },
    {
        "order": 22,
        "visible_label": "资料补充",
        "engineering_key": "big_unit.material_requests",
        "canonical_ref": "material_requests",
        "generation_layer": "source_gap",
        "generation_slot_id": "R88-GEN/big_unit.material_requests",
        "quality_focus": ["只提示补资料", "不写正式课包", "来源缺口清楚"],
    },
]


LESSON_INHERITANCE_MAP = {
    "lesson_identity": ["big_unit.unit_basic_info", "big_unit.learning_tasks"],
    "inherited_unit_context": ["big_unit.unit_theme", "big_unit.big_idea", "big_unit.essential_question"],
    "textbook_anchor": ["big_unit.material_requests", "big_unit.content_analysis"],
    "lesson_concept_slice": ["big_unit.big_idea", "big_unit.learning_stages"],
    "lesson_focus_question": ["big_unit.essential_question", "big_unit.micro_questions"],
    "lesson_objectives": ["big_unit.learning_goals", "big_unit.task_assessment_points"],
    "student_starting_point": ["big_unit.student_context"],
    "key_difficult_points": ["big_unit.key_difficult_points", "big_unit.content_analysis"],
    "lesson_task_evidence": ["big_unit.performance_task", "big_unit.learning_assessment"],
    "classroom_flow": ["big_unit.learning_activities", "big_unit.scaffold.strategy"],
    "courseware_plan": ["big_unit.scaffold.resource", "big_unit.learning_activities"],
    "handout_plan": ["big_unit.handout_plan", "big_unit.learning_assessment"],
    "assessment_plan": ["big_unit.assessment_scaffold", "big_unit.task_assessment_points"],
    "material_requests": ["big_unit.material_requests"],
}


STEP_CONTRACT_GROUPS = [
    {
        "group_id": "step_frame",
        "label": "环节骨架",
        "role": "确定这一环节在整堂课中的位置、时长和推进责任。",
        "fields": [
            ("step_id", "环节ID", "稳定定位环节，便于局部重生和追踪。"),
            ("step_order", "环节顺序", "明确课堂推进先后，避免候选串位。"),
            ("step_name", "环节名称", "教师能一眼识别当前环节任务。"),
            ("duration", "时间分配", "控制课堂节奏，暴露时间风险。"),
            ("phase_role", "环节功能", "说明本环节是导入、探究、创作、展示还是评价。"),
            ("prior_connection", "承接上一环节", "说明学生从哪里来，不做断裂活动。"),
            ("next_connection", "引出下一环节", "说明本环节如何推动后续任务。"),
        ],
    },
    {
        "group_id": "teacher_moves",
        "label": "教师行为",
        "role": "把教师在课堂中的语言、示范、巡视和反馈拆开生成。",
        "fields": [
            ("teacher_instruction", "教师指令", "学生听完知道马上要做什么。"),
            ("teacher_core_question", "核心提问", "推动观察、比较、表达或判断。"),
            ("teacher_probe_question", "追问", "当学生回答浅时继续推进思考。"),
            ("teacher_demo", "教师示范", "示范材料、技法、观察或表达方式。"),
            ("teacher_modeling_language", "教师示范语言", "给教师可直接说出口的课堂话术。"),
            ("teacher_patrol_observation", "巡视观察", "教师走动时看什么、记什么、提醒什么。"),
            ("teacher_feedback_move", "即时反馈动作", "教师如何肯定、纠偏、追问或调整。"),
        ],
    },
    {
        "group_id": "student_moves",
        "label": "学生行为",
        "role": "明确学生在每个环节的真实学习动作和可见产出。",
        "fields": [
            ("student_observation", "学生观察", "学生观察什么对象、特征或差异。"),
            ("student_discussion", "学生讨论", "学生和同伴交流什么问题或判断。"),
            ("student_try", "学生尝试", "学生短时试验什么方法或材料。"),
            ("student_creation", "学生创作", "学生正式完成什么作品或局部任务。"),
            ("student_recording", "学生记录", "学生留下词语、选择、草图或学习单记录。"),
            ("student_display", "学生展示", "学生展示什么、以何种方式展示。"),
            ("student_revision", "学生修订", "学生基于反馈做什么调整。"),
        ],
    },
    {
        "group_id": "art_learning_content",
        "label": "美术学习内容",
        "role": "保证教学过程不是泛泛活动，而是有美术学科判断和材料经验。",
        "fields": [
            ("visual_object", "观察对象", "教材图、生活图、作品图或学生作品样例。"),
            ("visual_language_focus", "美术语言焦点", "色彩、线条、形状、构图等隐性支撑点。"),
            ("technique_focus", "技法要点", "学生需要掌握或体验的操作方法。"),
            ("material_use", "材料使用", "纸、笔、颜料、色卡、剪贴等材料怎么用。"),
            ("composition_or_color_focus", "造型/构图/色彩关注点", "这一环节主要看的视觉关系。"),
            ("artwork_or_life_example", "作品或生活例证", "支撑理解的图像或生活经验来源。"),
            ("positive_negative_example", "正反例", "帮助学生分辨有效与无效表现。"),
        ],
    },
    {
        "group_id": "scaffolds",
        "label": "学习支架",
        "role": "把学生做得出来所需要的支架拆清楚，避免教师替学生完成。",
        "fields": [
            ("context_scaffold", "情境支架", "用什么情境让学生愿意进入任务。"),
            ("task_scaffold", "任务支架", "把复杂任务拆成学生可执行步骤。"),
            ("language_scaffold", "语言支架", "给学生观察、表达、互评的句式或词语。"),
            ("material_scaffold", "材料支架", "通过材料或模板降低操作门槛。"),
            ("peer_scaffold", "同伴支架", "安排同桌互看、互说、互评或合作。"),
            ("differentiation_scaffold", "差异化支架", "给不同速度和能力学生不同入口。"),
        ],
    },
    {
        "group_id": "assessment_evidence",
        "label": "评价与证据",
        "role": "让课堂不是只完成作品，而是留下能判断学习发生的证据。",
        "fields": [
            ("process_evidence", "过程证据", "学生观察、试验、讨论或修订过程的证据。"),
            ("work_evidence", "作品证据", "作品中哪些部分能证明学习目标。"),
            ("expression_evidence", "表达证据", "学生用语言说明选择、感受或理由。"),
            ("peer_assessment", "同伴评价", "同伴如何给出可用反馈。"),
            ("teacher_observation_point", "教师观察点", "教师重点记录哪些学生表现。"),
            ("success_criteria", "成功标准", "学生怎样知道自己完成得有效。"),
            ("evidence_storage", "证据留存", "照片、学习单、板贴、评价卡如何保存。"),
        ],
    },
    {
        "group_id": "risk_and_orchestration",
        "label": "风险与调度",
        "role": "提前暴露课堂风险，给出可替换、可补救的调度方案。",
        "fields": [
            ("common_misconception", "常见误区", "学生最可能误解或做偏的地方。"),
            ("time_risk", "时间风险", "本环节可能超时或被压缩的点。"),
            ("material_risk", "材料风险", "材料不足、弄脏、难操作时怎么办。"),
            ("class_management_risk", "课堂秩序风险", "活动组织可能失控的点。"),
            ("fallback_strategy", "补救策略", "出现问题时教师如何快速补救。"),
            ("alternative_plan", "替代方案", "没有某些材料或时间不足时如何替换。"),
        ],
    },
]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def esc(value: object) -> str:
    return html.escape(str(value or ""), quote=True)


def chip(text: str, class_name: str = "") -> str:
    return f'<span class="chip {class_name}">{esc(text)}</span>'


def load_lesson_fields() -> list[dict]:
    data = read_json(R81_FIELD_MAP)
    lesson_fields = []
    for item in data.get("lesson_fields", []):
        schema_key = item["schema_key"]
        lesson_fields.append(
            {
                "order": item["order"],
                "visible_label": item["label"],
                "engineering_key": f"lesson.{schema_key}",
                "schema_key": schema_key,
                "target_section": item.get("target_section_id") or item.get("visible_section") or "",
                "visible_section": item.get("visible_section") or "",
                "generation_role": item.get("generation_role") or "",
                "candidate_policy": item.get("candidate_policy") or "",
                "line_contract_policy": item.get("line_contract_policy") or "",
                "inherit_from": LESSON_INHERITANCE_MAP.get(schema_key, []),
                "generation_slot_id": f"R88-GEN/lesson.{schema_key}",
            }
        )
    return lesson_fields


def load_canonical_big_unit_refs() -> dict[str, dict]:
    data = read_json(R6N_R9A_BIG_UNIT)
    refs = {}
    for field in data.get("fields", []):
        refs[field.get("field_key")] = field
    return refs


def build_ledger() -> dict:
    canonical_refs = load_canonical_big_unit_refs()
    lesson_fields = load_lesson_fields()
    big_unit_fields = []
    for field in BIG_UNIT_FIELDS:
        enriched = dict(field)
        canonical = canonical_refs.get(field["canonical_ref"], {})
        enriched["canonical_teacher_label"] = canonical.get("teacher_label") or ""
        enriched["write_policy"] = canonical.get("write_policy") or (
            "action_prompt_only_no_write" if field["canonical_ref"] == "material_requests" else "preview_then_teacher_confirm"
        )
        enriched["generation_placeholder"] = {
            "candidate_state": "empty",
            "candidate_text_slot": f"{field['generation_slot_id']}/candidate_text",
            "quality_note_slot": f"{field['generation_slot_id']}/quality_note",
            "teacher_action_slot": f"{field['generation_slot_id']}/teacher_action",
        }
        big_unit_fields.append(enriched)

    for field in lesson_fields:
        field["generation_placeholder"] = {
            "candidate_state": "empty",
            "candidate_text_slot": f"{field['generation_slot_id']}/candidate_text",
            "quality_note_slot": f"{field['generation_slot_id']}/quality_note",
            "teacher_action_slot": f"{field['generation_slot_id']}/teacher_action",
        }

    step_groups = []
    step_fields = []
    order = 1
    for group in STEP_CONTRACT_GROUPS:
        group_fields = []
        for key, label, focus in group["fields"]:
            field = {
                "order": order,
                "group_id": group["group_id"],
                "group_label": group["label"],
                "engineering_key": f"lesson.classroom_flow.step.{key}",
                "visible_label": label,
                "generation_slot_id": f"R88-GEN/lesson.classroom_flow.step.{key}",
                "quality_focus": focus,
                "generation_placeholder": {
                    "candidate_state": "empty",
                    "candidate_text_slot": f"R88-GEN/lesson.classroom_flow.step.{key}/candidate_text",
                    "quality_note_slot": f"R88-GEN/lesson.classroom_flow.step.{key}/quality_note",
                    "teacher_action_slot": f"R88-GEN/lesson.classroom_flow.step.{key}/teacher_action",
                },
            }
            group_fields.append(field)
            step_fields.append(field)
            order += 1
        step_groups.append(
            {
                "group_id": group["group_id"],
                "label": group["label"],
                "role": group["role"],
                "field_count": len(group_fields),
                "fields": group_fields,
            }
        )

    return {
        "schema_id": "field_generation_quality_static_lab_ledger_1013R_R88",
        "stage": "1013R_R88_FIELD_GENERATION_QUALITY_STATIC_LAB",
        "purpose": "Static field and generation-placeholder lab for validating layered teaching-design generation quality. Prompt text is intentionally omitted.",
        "source_refs": {
            "big_unit_canonical_ledger": str(R6N_R9A_BIG_UNIT),
            "lesson_field_map": str(R81_FIELD_MAP),
        },
        "boundary_flags": {
            "static_page_only": True,
            "r21_page_modified": False,
            "model_provider_runtime_connected": False,
            "prompt_text_visible": False,
            "database_write": False,
            "feishu_write": False,
            "memory_write": False,
            "formal_apply_allowed": False,
        },
        "generation_layers": [
            {
                "layer_id": "unit_spine",
                "label": "大单元主线",
                "description": "先确定单元主题、大观念、基本问题和任务证据，不直接从空白写单课。",
            },
            {
                "layer_id": "lesson_slice",
                "label": "单课切片",
                "description": "把大单元主线切到当前课时，形成本课依据、目标、任务和证据。",
            },
            {
                "layer_id": "field_internal",
                "label": "字段内部结构",
                "description": "每个字段内部继续拆成可观察、可上课、可评价的子结构。",
            },
            {
                "layer_id": "derived_objects",
                "label": "派生物",
                "description": "大屏、学习单、评价表只从已确认的教学过程和证据派生。",
            },
        ],
        "big_unit_fields": big_unit_fields,
        "lesson_fields": lesson_fields,
        "step_contract_groups": step_groups,
        "step_contract_fields": step_fields,
    }


def render_placeholder(slot_id: str, description: str) -> str:
    return f"""
      <div class="placeholder" data-generation-slot-id="{esc(slot_id)}">
        <div class="placeholder-title">模型生成内容占位</div>
        <div class="placeholder-desc">{esc(description)}</div>
        <div class="placeholder-empty">待生成：候选文本 / 质量观察 / 教师动作</div>
      </div>
    """


def render_big_unit_field(field: dict) -> str:
    quality = "".join(chip(item, "quality") for item in field["quality_focus"])
    return f"""
      <article class="field-card" id="big-unit-{esc(field['order'])}" data-visible-field="{esc(field['visible_label'])}" data-engineering-key="{esc(field['engineering_key'])}">
        <div class="field-card-head">
          <div>
            <div class="field-kicker">大单元字段 {esc(field['order'])}</div>
            <h3>{esc(field['visible_label'])}</h3>
          </div>
          <div class="order-pill">{esc(field['order'])}</div>
        </div>
        <div class="meta-row">
          {chip('外显字段: ' + field['visible_label'], 'visible')}
          {chip('工程字段: ' + field['engineering_key'], 'engineering')}
          {chip('canonical: ' + field['canonical_ref'], 'canonical')}
        </div>
        <div class="meta-row">{quality}</div>
        {render_placeholder(field['generation_slot_id'], '生成后贴入本字段候选，不覆盖原文；教师确认后才进入结构化正文。')}
      </article>
    """


def render_lesson_field(field: dict) -> str:
    inherits = "".join(chip(item, "inherit") for item in field["inherit_from"])
    return f"""
      <article class="field-card lesson" data-visible-field="{esc(field['visible_label'])}" data-engineering-key="{esc(field['engineering_key'])}">
        <div class="field-card-head">
          <div>
            <div class="field-kicker">单课字段 {esc(field['order'])} · {esc(field['visible_section'])}</div>
            <h3>{esc(field['visible_label'])}</h3>
          </div>
          <div class="order-pill lesson">{esc(field['order'])}</div>
        </div>
        <div class="meta-row">
          {chip('外显字段: ' + field['visible_label'], 'visible')}
          {chip('工程字段: ' + field['engineering_key'], 'engineering')}
          {chip('target: ' + field['target_section'], 'canonical')}
        </div>
        <div class="role-text">{esc(field['generation_role'])}</div>
        <div class="inherit-block">
          <strong>继承来源</strong>
          <div class="meta-row">{inherits or chip('待绑定大单元字段', 'warn')}</div>
        </div>
        {render_placeholder(field['generation_slot_id'], '生成后先进入字段候选位；可采纳、删除、重试，再决定是否写入正文。')}
      </article>
    """


def render_step_field(field: dict) -> str:
    return f"""
      <article class="step-row">
        <div>
          <strong>{esc(field['order'])}. {esc(field['visible_label'])}</strong>
          <span>{esc(field['engineering_key'])}</span>
        </div>
        <p>{esc(field['quality_focus'])}</p>
        {render_placeholder(field['generation_slot_id'], '教学过程内部行级候选，服务课堂环节，不单独形成正文大饼。')}
      </article>
    """


def render_step_group(group: dict) -> str:
    fields = "\n".join(render_step_field(field) for field in group["fields"])
    return f"""
      <section class="step-group" data-step-group-id="{esc(group['group_id'])}">
        <div class="step-group-head">
          <div>
            <div class="field-kicker">教学过程分组 · {esc(group['group_id'])}</div>
            <h3>{esc(group['label'])}</h3>
            <p>{esc(group['role'])}</p>
          </div>
          <div class="order-pill lesson">{esc(group['field_count'])}</div>
        </div>
        {fields}
      </section>
    """


def render_html(ledger: dict) -> str:
    big_unit_cards = "\n".join(render_big_unit_field(field) for field in ledger["big_unit_fields"])
    lesson_cards = "\n".join(render_lesson_field(field) for field in ledger["lesson_fields"])
    step_cards = "\n".join(render_step_group(group) for group in ledger["step_contract_groups"])
    layer_cards = "\n".join(
        f"""
        <div class="layer-card">
          <span>{esc(layer['layer_id'])}</span>
          <strong>{esc(layer['label'])}</strong>
          <p>{esc(layer['description'])}</p>
        </div>
        """
        for layer in ledger["generation_layers"]
    )

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>1013R R88 字段生成质量静态验证页</title>
  <style>
    :root {{
      --ink: #1f2f2b;
      --muted: #60736c;
      --green: #2d7f72;
      --green-dark: #1b5d52;
      --line: #d9e7df;
      --paper: #fffdf7;
      --warm: #fff6e8;
      --orange: #c97519;
      --blue: #eaf3ff;
      --blue-line: #9bbfe8;
      --grid: rgba(45, 127, 114, .12);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      font: 14px/1.65 "Microsoft YaHei", "PingFang SC", Arial, sans-serif;
      background:
        linear-gradient(var(--grid) 1px, transparent 1px),
        linear-gradient(90deg, var(--grid) 1px, transparent 1px),
        #f8fbf7;
      background-size: 28px 28px;
    }}
    header {{
      position: sticky;
      top: 0;
      z-index: 10;
      height: 72px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 28px;
      background: rgba(255, 255, 255, .92);
      border-bottom: 1px solid var(--line);
      backdrop-filter: blur(10px);
    }}
    .brand {{
      display: flex;
      align-items: baseline;
      gap: 10px;
      color: var(--green-dark);
      font-weight: 800;
      font-size: 24px;
    }}
    .brand span {{ color: var(--muted); font-size: 12px; font-weight: 500; }}
    .stage-chip {{
      border: 1px solid #b7ded3;
      background: #eef9f5;
      color: var(--green-dark);
      border-radius: 999px;
      padding: 6px 12px;
      font-weight: 700;
      font-size: 12px;
    }}
    .layout {{
      display: grid;
      grid-template-columns: 280px minmax(0, 1fr) 320px;
      gap: 18px;
      padding: 18px;
      max-width: 1800px;
      margin: 0 auto;
    }}
    aside, main {{
      border: 1px solid var(--line);
      background: rgba(255, 255, 250, .94);
      box-shadow: 0 16px 40px rgba(31, 47, 43, .08);
    }}
    aside {{
      border-radius: 8px;
      padding: 16px;
      align-self: start;
      position: sticky;
      top: 90px;
      max-height: calc(100vh - 110px);
      overflow: auto;
    }}
    main {{
      border-radius: 8px;
      overflow: hidden;
    }}
    .hero {{
      padding: 28px 32px;
      border-bottom: 1px solid var(--line);
      background: linear-gradient(180deg, #fffef8, #f5fbf5);
    }}
    .hero h1 {{
      margin: 0;
      color: #14231f;
      font-size: 28px;
      letter-spacing: 0;
    }}
    .hero p {{
      max-width: 880px;
      margin: 10px 0 0;
      color: var(--muted);
    }}
    .section {{
      padding: 26px 32px;
      border-bottom: 1px solid var(--line);
    }}
    .section h2 {{
      margin: 0 0 14px;
      font-size: 22px;
      letter-spacing: 0;
    }}
    .nav-title {{
      margin: 0 0 10px;
      color: var(--green-dark);
      font-weight: 800;
    }}
    .nav-link {{
      display: block;
      padding: 8px 10px;
      border-radius: 6px;
      color: var(--ink);
      text-decoration: none;
      border: 1px solid transparent;
    }}
    .nav-link:hover {{
      border-color: #b7ded3;
      background: #eef9f5;
    }}
    .counts {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-top: 16px;
    }}
    .count-card {{
      border: 1px solid var(--line);
      background: #fff;
      border-radius: 8px;
      padding: 10px;
    }}
    .count-card strong {{
      display: block;
      color: var(--green-dark);
      font-size: 20px;
    }}
    .layer-grid {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
    }}
    .layer-card {{
      border: 1px solid #cfe0d8;
      background: #fff;
      border-radius: 8px;
      padding: 12px;
    }}
    .layer-card span {{
      display: inline-block;
      color: var(--orange);
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
    }}
    .layer-card strong {{
      display: block;
      margin-top: 4px;
      color: var(--green-dark);
    }}
    .layer-card p {{ margin: 6px 0 0; color: var(--muted); }}
    .field-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 14px;
    }}
    .field-card {{
      border: 1px solid #f0cb96;
      background: #fffaf1;
      border-radius: 8px;
      padding: 14px;
    }}
    .field-card.lesson {{
      border-color: #bcd8f3;
      background: #f5faff;
    }}
    .field-card-head {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 12px;
    }}
    .field-kicker {{
      color: var(--orange);
      font-weight: 800;
      font-size: 11px;
    }}
    h3 {{
      margin: 2px 0 8px;
      font-size: 18px;
      letter-spacing: 0;
    }}
    .order-pill {{
      min-width: 32px;
      height: 32px;
      display: grid;
      place-items: center;
      border-radius: 50%;
      color: #fff;
      background: var(--orange);
      font-weight: 800;
    }}
    .order-pill.lesson {{ background: #2f75b5; }}
    .meta-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin: 8px 0;
    }}
    .chip {{
      display: inline-flex;
      align-items: center;
      min-height: 22px;
      border: 1px solid #e4d4b8;
      border-radius: 999px;
      padding: 2px 8px;
      background: #fff;
      color: #7b4b10;
      font-size: 11px;
      font-weight: 700;
      white-space: normal;
    }}
    .chip.visible {{ color: #1f6f63; border-color: #b7ded3; background: #f2fbf8; }}
    .chip.engineering {{ color: #255f96; border-color: #bcd8f3; background: #eef6ff; }}
    .chip.canonical {{ color: #83540c; border-color: #f0cb96; background: #fff8ea; }}
    .chip.quality {{ color: #754b10; background: #fff; }}
    .chip.inherit {{ color: #315f7e; border-color: #bcd8f3; background: #f5faff; }}
    .chip.warn {{ color: #a34825; border-color: #efb9aa; background: #fff4f0; }}
    .role-text, .inherit-block {{
      color: var(--muted);
      margin-top: 8px;
    }}
    .placeholder {{
      margin-top: 12px;
      border: 1px dashed #d89843;
      background: rgba(255, 255, 255, .72);
      border-radius: 8px;
      padding: 10px;
    }}
    .placeholder-title {{
      color: var(--orange);
      font-weight: 800;
    }}
    .placeholder-desc {{
      color: var(--muted);
      font-size: 12px;
      margin-top: 3px;
    }}
    .placeholder-empty {{
      margin-top: 8px;
      min-height: 46px;
      display: flex;
      align-items: center;
      border-radius: 6px;
      padding: 8px;
      background: #fff;
      color: #a56b20;
      font-size: 12px;
    }}
    .step-group {{
      border: 1px solid #cfe0d8;
      background: #f9fcf8;
      border-radius: 8px;
      padding: 14px;
      margin-bottom: 16px;
    }}
    .step-group-head {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      padding-bottom: 10px;
      margin-bottom: 10px;
      border-bottom: 1px solid var(--line);
    }}
    .step-group-head p {{
      margin: 4px 0 0;
      color: var(--muted);
    }}
    .step-row {{
      border: 1px solid var(--line);
      background: #fff;
      border-radius: 8px;
      padding: 12px;
      margin-bottom: 10px;
    }}
    .step-row div:first-child {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      color: var(--green-dark);
    }}
    .step-row span {{
      color: #2f75b5;
      font-size: 12px;
    }}
    .step-row p {{
      margin: 6px 0 0;
      color: var(--muted);
    }}
    .quality-panel {{
      display: grid;
      gap: 10px;
    }}
    .quality-item {{
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 10px;
      background: #fff;
    }}
    .quality-item strong {{
      color: var(--green-dark);
    }}
    .warning {{
      border-color: #efb9aa;
      background: #fff7f4;
      color: #8b3525;
    }}
    @media (max-width: 1200px) {{
      .layout {{ grid-template-columns: 1fr; }}
      aside {{ position: static; max-height: none; }}
      .field-grid, .layer-grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="brand">师维 <span>字段生成质量静态验证页</span></div>
    <div class="stage-chip">1013R_R88 · static only · no prompt text</div>
  </header>
  <div class="layout">
    <aside>
      <div class="nav-title">验证导航</div>
      <a class="nav-link" href="#layers">生成层级</a>
      <a class="nav-link" href="#big-unit">大单元 22 字段</a>
      <a class="nav-link" href="#lesson">单课 14 字段</a>
      <a class="nav-link" href="#step-contract">教学过程行级契约</a>
      <a class="nav-link" href="#quality">质量观察</a>
      <div class="counts">
        <div class="count-card"><strong>{len(ledger['big_unit_fields'])}</strong>大单元</div>
        <div class="count-card"><strong>{len(ledger['lesson_fields'])}</strong>单课</div>
        <div class="count-card"><strong>{len(ledger['step_contract_fields'])}</strong>行级</div>
      </div>
    </aside>
    <main>
      <section class="hero">
        <h1>底层字段与内容生成质量验证样板</h1>
        <p>这是一页独立静态页，用来验证“大单元主线 → 单课切片 → 字段内部结构 → 派生物”的生成质量。页面只标注外显字段、工程字段、模型生成内容占位，不展示提示词，不调用模型，不写入正式备课本。</p>
      </section>
      <section class="section" id="layers">
        <h2>一、生成层级</h2>
        <div class="layer-grid">{layer_cards}</div>
      </section>
      <section class="section" id="big-unit">
        <h2>二、大单元 22 字段</h2>
        <div class="field-grid">{big_unit_cards}</div>
      </section>
      <section class="section" id="lesson">
        <h2>三、单课 14 字段</h2>
        <div class="field-grid">{lesson_cards}</div>
      </section>
      <section class="section" id="step-contract">
        <h2>四、教学过程行级契约</h2>
        {step_cards}
      </section>
      <section class="section" id="quality">
        <h2>五、质量观察</h2>
        <div class="quality-panel">
          <div class="quality-item"><strong>大单元先行</strong><br>生成单课前，必须能看见单元主题、大观念、基本问题、表现性任务和评价证据的传递关系。</div>
          <div class="quality-item"><strong>字段内拆解</strong><br>不是每个字段生成一段大文本，而是按字段内部结构生成候选，再由教师采纳、删除或重试。</div>
          <div class="quality-item"><strong>派生物后置</strong><br>大屏、学习单、评价表从已确认的教学过程和证据派生，不抢在主教案之前。</div>
          <div class="quality-item warning"><strong>边界</strong><br>本页不含提示词、不接 provider、不保存、不导出、不 formal apply。所有占位都是待生成容器。</div>
        </div>
      </section>
    </main>
    <aside>
      <div class="nav-title">当前边界</div>
      <div class="quality-panel">
        <div class="quality-item"><strong>页面类型</strong><br>独立静态验证页</div>
        <div class="quality-item"><strong>主线保护</strong><br>不修改 R21 / R87 页面</div>
        <div class="quality-item"><strong>提示词</strong><br>本版隐藏，后续按需单独展开</div>
        <div class="quality-item"><strong>模型内容</strong><br>仅有占位，不执行生成</div>
      </div>
    </aside>
  </div>
</body>
</html>
"""


def validate(ledger: dict) -> dict:
    all_big_unit_complete = all(
        field.get("visible_label") and field.get("engineering_key") and field.get("generation_slot_id")
        for field in ledger["big_unit_fields"]
    )
    all_lesson_complete = all(
        field.get("visible_label") and field.get("engineering_key") and field.get("generation_slot_id")
        for field in ledger["lesson_fields"]
    )
    all_step_complete = all(
        field.get("visible_label") and field.get("engineering_key") and field.get("generation_slot_id")
        for field in ledger["step_contract_fields"]
    )
    step_group_count = len(ledger.get("step_contract_groups", []))
    step_contract_field_count = len(ledger["step_contract_fields"])
    all_step_groups_have_fields = all(
        group.get("group_id") and group.get("label") and group.get("field_count", 0) == len(group.get("fields", []))
        for group in ledger.get("step_contract_groups", [])
    )
    step_contract_depth_sufficient = step_group_count >= 7 and step_contract_field_count >= 40
    html_text = HTML_PATH.read_text(encoding="utf-8") if HTML_PATH.exists() else ""
    prompt_terms = ["system_prompt", "user_prompt", "提示词正文", "required_response_shape"]
    prompt_text_visible = any(term in html_text for term in prompt_terms)
    validation = {
        "stage": "1013R_R88_FIELD_GENERATION_QUALITY_STATIC_LAB",
        "result": "PASS",
        "html": str(HTML_PATH),
        "ledger": str(LEDGER_PATH),
        "big_unit_field_count": len(ledger["big_unit_fields"]),
        "lesson_field_count": len(ledger["lesson_fields"]),
        "step_contract_group_count": step_group_count,
        "step_contract_field_count": step_contract_field_count,
        "all_big_unit_fields_have_visible_engineering_and_placeholder": all_big_unit_complete,
        "all_lesson_fields_have_visible_engineering_and_placeholder": all_lesson_complete,
        "all_step_fields_have_visible_engineering_and_placeholder": all_step_complete,
        "all_step_groups_have_fields": all_step_groups_have_fields,
        "step_contract_depth_sufficient": step_contract_depth_sufficient,
        "prompt_text_visible": prompt_text_visible,
        "model_provider_runtime_connected": False,
        "r21_page_modified": False,
        "formal_apply_allowed": False,
    }
    if not (
        all_big_unit_complete
        and all_lesson_complete
        and all_step_complete
        and all_step_groups_have_fields
        and step_contract_depth_sufficient
    ) or prompt_text_visible:
        validation["result"] = "FAIL"
    return validation


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ledger = build_ledger()
    write_json(LEDGER_PATH, ledger)
    write_text(HTML_PATH, render_html(ledger))
    validation = validate(ledger)
    write_json(VALIDATION_PATH, validation)
    readme = f"""# 1013R R88 Field Generation Quality Static Lab

独立静态验证页，用于检查底层字段、工程字段和模型生成内容占位。

- HTML: `{HTML_PATH}`
- Ledger: `{LEDGER_PATH}`
- Validator: `{VALIDATION_PATH}`
- 大单元字段数: `{validation['big_unit_field_count']}`
- 单课字段数: `{validation['lesson_field_count']}`
- 教学过程分组数: `{validation['step_contract_group_count']}`
- 行级字段数: `{validation['step_contract_field_count']}`
- 提示词正文: 不展示
- Provider/runtime: 未接入
- R21 页面: 未修改
"""
    write_text(OUT_DIR / "README.md", readme)
    review_prompt = f"""# GPT Review Prompt - 1013R R88 Field Generation Quality Static Lab

请审核这个静态页是否足够支撑“从大单元到单课再到教学过程行级契约”的模型生成质量验证。

## 审核对象

- HTML: `{HTML_PATH}`
- Ledger: `{LEDGER_PATH}`
- Validator: `{VALIDATION_PATH}`

## 请重点审核

1. 大单元 22 字段是否覆盖了生成教学设计所需的上位结构。
2. 单课 14 字段是否能从大单元字段继承，而不是从空白生成。
3. 教学过程行级契约是否足够丰富，目前应为 7 组、40 项以上。
4. 教学过程字段是否覆盖课堂真实生成所需的骨架、教师行为、学生行为、美术内容、支架、评价证据、风险调度。
5. 页面是否只做静态验证，不接 provider/runtime，不展示生成提示词，不 formal apply。

## 请给出结论

- PASS / PASS_WITH_NOTES / REJECT
- 需要补充的字段组
- 过细或重复的字段
- 哪些字段应该作为生成输入，哪些字段应该作为生成输出
- 下一步是否可以进入“真实生成质量 smoke”
"""
    write_text(OUT_DIR / "GPT_REVIEW_PROMPT_1013R_R88_FIELD_GENERATION_QUALITY_STATIC_LAB.md", review_prompt)
    manifest = f"""# REVIEW_PACKAGE_MANIFEST

- stage: `1013R_R88_FIELD_GENERATION_QUALITY_STATIC_LAB`
- static_html: `{HTML_PATH}`
- ledger_json: `{LEDGER_PATH}`
- validator_result: `{VALIDATION_PATH}`
- gpt_review_prompt: `{OUT_DIR / "GPT_REVIEW_PROMPT_1013R_R88_FIELD_GENERATION_QUALITY_STATIC_LAB.md"}`
- build_script: `{Path(__file__).resolve()}`
- big_unit_field_count: `{validation['big_unit_field_count']}`
- lesson_field_count: `{validation['lesson_field_count']}`
- step_contract_group_count: `{validation['step_contract_group_count']}`
- step_contract_field_count: `{validation['step_contract_field_count']}`
- prompt_text_visible: `{validation['prompt_text_visible']}`
- model_provider_runtime_connected: `false`
- r21_page_modified: `false`
- formal_apply_allowed: `false`
"""
    write_text(OUT_DIR / "REVIEW_PACKAGE_MANIFEST.md", manifest)
    print(json.dumps(validation, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
