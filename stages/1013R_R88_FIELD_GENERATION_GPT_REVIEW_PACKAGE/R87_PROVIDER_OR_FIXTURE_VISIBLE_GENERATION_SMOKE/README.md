# 1013R R83-R87 可见生成链路

本包把 R82 的生成契约往后推进到 R87，但不修改主 R21 页面。

## 边界

- 主 R21 页面未写入 R87 标记：`D:\Documents\SmartEdu\xiaobei-core\outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R21_page_copy_binds_unified_package\prep_room_page_copy_binds_unified_package_1013R_R21.html`
- R87 是复制页可见 smoke：`D:\Documents\SmartEdu\xiaobei-core\outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R87_PROVIDER_OR_FIXTURE_VISIBLE_GENERATION_SMOKE\prep_room_r87_provider_or_fixture_visible_generation_smoke_1013R_R87.html`
- 候选只进入旧编辑卡弹层：`existing_edit_card_before_after_suggestion_panel`
- 不生成正文独立蓝卡
- 不 formal apply
- 不写数据库、飞书、记忆或正式课包

## 阶段

- R83：normalizer dry run，校验 R82 valid/invalid fixtures。
- R84：把候选桥接到旧编辑卡 before/after/suggestion 三槽。
- R85：本地 fixture 可见生成 smoke。
- R86：provider sandbox dry run；如果 provider 输出未过契约，自动回退 R82 fixture。
- R87：复制 R21 生成可打开 HTML，右侧工具盒出现“R87生成候选已准备”，点击复用 `.r6p-modal-backdrop`。

## 结果

- R83: `PASS`
- R84: `PASS`
- R85: `PASS`
- R86: `PASS_WITH_FALLBACK` provider_success=False fallback_used=True
- R87: `PASS`
