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
