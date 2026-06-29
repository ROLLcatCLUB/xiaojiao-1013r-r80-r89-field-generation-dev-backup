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
