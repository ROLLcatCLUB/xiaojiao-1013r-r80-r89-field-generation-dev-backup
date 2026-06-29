# R90 True Generation Quality Smoke Plan

R89 result: `PASS`. R90 may start only if R89 remains `PASS`.

## Purpose

R90 is the first real quality smoke after contract convergence. It should prove that the model can generate visible, useful teaching-design candidates through the existing candidate/edit-card route without writing into the formal lesson package.

## Input Scope

- Use R89 alias map for active write keys and legacy reads.
- Use R89 generation phase and field cluster registry.
- Use R89 R81-to-R88 step adapter for classroom-flow line-level fields.
- Use R82 19-key candidate schema as the only candidate key source.
- Use R88 static lab as the visible field-quality target.

## Smoke Path

1. `unit_spine`: generate candidates for unit theme / big idea / essential question, using material gap flags when evidence is missing.
2. `unit_goals`: generate learning goals, content analysis, and key-difficult-points candidates from the unit spine.
3. `progression`: generate learning stages / learning tasks / micro questions as a structured progression, not a flat ordered list.
4. `lesson_slice`: derive one lesson slice from the unit spine and progression.
5. `field_internal`: generate one classroom-flow segment with activated R88 line-level fields only.

## Visible Quality Checks

- Every candidate contains all 19 candidate keys.
- Every candidate has `canonical_field_key`, `target_field_key`, `target_section`, and `target_destination`.
- For classroom flow, every candidate has `target_step_id` and either a real `target_line_contract_id` or an explicit empty/non-applicable marker.
- Generated content lands in candidate slots only, not formal body text.
- Teacher can see before / after_candidate / xiaojiao_suggestion without a giant pasted block.
- Strict raw provider validation and salvage normalization remain separate.

## Hard Stops

- Do not modify R21.
- Do not formal apply.
- Do not write database / Feishu / memory.
- Do not add new fields.
- Do not let old R81 fields become R88 write targets.
- Do not claim generation quality if provider raw validation fails and only salvage succeeds.

## PASS Meaning

R90 PASS means visible model-generated candidates are usable for teacher review. It still does not mean formal application, full runtime integration, or production persistence is safe.
