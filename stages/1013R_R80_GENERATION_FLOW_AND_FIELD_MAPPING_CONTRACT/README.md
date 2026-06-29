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
