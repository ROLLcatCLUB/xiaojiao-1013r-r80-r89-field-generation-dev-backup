# 1013R R80-R89 Field Generation Dev Backup

This repository is a lightweight development backup for the recent prep-room field-generation line.

It is not the full `xiaobei-core` repository. It does not publish production runtime code, database state, Feishu state, memory state, or formal-apply output.

## Scope

- Range: `1013R_R80` through `1013R_R89`
- Purpose: preserve the recent contract, field mapping, visible smoke, provider/salvage boundary, R88 static lab, and R89 convergence artifacts before R90 work starts.
- Upload type: independent GitHub development backup
- Current next stage: `1013R_R90_TRUE_GENERATION_QUALITY_SMOKE`

## Boundaries

- `R21` page modified by this backup: `false`
- Provider/runtime connected by this backup: `false`
- Formal apply allowed: `false`
- Database / Feishu / memory writes: `false`
- Whole `xiaobei-core` pushed: `false`

## Main Review Entry Points

- `stages/1013R_R89_FIELD_CONTRACT_CONVERGENCE_AND_CAUSAL_CHAIN_GATE/README.md`
- `stages/1013R_R89_FIELD_CONTRACT_CONVERGENCE_AND_CAUSAL_CHAIN_GATE/validate_1013R_R89_field_contract_convergence_result.json`
- `stages/1013R_R89_FIELD_CONTRACT_CONVERGENCE_AND_CAUSAL_CHAIN_GATE/R90_TRUE_GENERATION_QUALITY_SMOKE_PLAN_1013R_R90.md`
- `stages/1013R_R88_FIELD_GENERATION_QUALITY_STATIC_LAB/field_generation_quality_static_lab_1013R_R88.html`
- `scripts/build_1013r_r89_field_contract_convergence.py`

## Included ZIP Hashes

- `zips/1013R_R88_FIELD_GENERATION_GPT_REVIEW_PACKAGE.zip`
  - SHA256: `06f686f13e61145c743d69989deb1184440a13fc45c8f1d9f5bbe4e1897b206e`
- `zips/1013R_R89_FIELD_CONTRACT_CONVERGENCE_GPT_REVIEW_PACKAGE.zip`
  - SHA256: `a500be50853a7318c311de19395613371888287bc403743da66f0710240b5da6`

## Notes For GPT / Future Development

R89 is a contract convergence gate, not proof of true generation quality.

R90 should only prove visible model-generated candidates through candidate slots. It should not write formal body text, modify R21, or claim full runtime quality if strict provider validation fails and only salvage succeeds.

