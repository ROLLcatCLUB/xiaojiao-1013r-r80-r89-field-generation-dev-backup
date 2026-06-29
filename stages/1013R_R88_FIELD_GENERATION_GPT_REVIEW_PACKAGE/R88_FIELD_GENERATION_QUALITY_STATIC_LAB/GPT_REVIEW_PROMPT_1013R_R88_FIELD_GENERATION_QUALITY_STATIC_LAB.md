# GPT Review Prompt - 1013R R88 Field Generation Quality Static Lab

请审核这个静态页是否足够支撑“从大单元到单课再到教学过程行级契约”的模型生成质量验证。

## 审核对象

- HTML: `D:\Documents\SmartEdu\xiaobei-core\outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R88_FIELD_GENERATION_QUALITY_STATIC_LAB\field_generation_quality_static_lab_1013R_R88.html`
- Ledger: `D:\Documents\SmartEdu\xiaobei-core\outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R88_FIELD_GENERATION_QUALITY_STATIC_LAB\field_generation_quality_static_lab_ledger_1013R_R88.json`
- Validator: `D:\Documents\SmartEdu\xiaobei-core\outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R88_FIELD_GENERATION_QUALITY_STATIC_LAB\validate_1013R_R88_field_generation_quality_static_lab_result.json`

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
