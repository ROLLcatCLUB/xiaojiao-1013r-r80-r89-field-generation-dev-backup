from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1"
PACKAGE_DIR = BASE / "1013R_R88_FIELD_GENERATION_GPT_REVIEW_PACKAGE"
ZIP_PATH = BASE / "1013R_R88_FIELD_GENERATION_GPT_REVIEW_PACKAGE.zip"


ITEMS = [
    {
        "source": BASE / "1013R_R88_FIELD_GENERATION_QUALITY_STATIC_LAB",
        "target": "R88_FIELD_GENERATION_QUALITY_STATIC_LAB",
        "reason": "Current static lab for visible fields, engineering fields, generation placeholders, and 7-group/47-item classroom-flow line contract.",
    },
    {
        "source": BASE / "1013R_R83_LESSON_GENERATION_NORMALIZER_DRY_RUN",
        "target": "R83_LESSON_GENERATION_NORMALIZER_DRY_RUN",
        "reason": "Recent normalizer evidence proving field_patch_candidates can be accepted or rejected by contract.",
    },
    {
        "source": BASE / "1013R_R84_EDIT_CARD_BRIDGE_VISIBLE_SMOKE",
        "target": "R84_EDIT_CARD_BRIDGE_VISIBLE_SMOKE",
        "reason": "Recent edit-card bridge evidence: candidates route to existing before/after/suggestion slots.",
    },
    {
        "source": BASE / "1013R_R85_LOCAL_FIXTURE_VISIBLE_GENERATION_SMOKE",
        "target": "R85_LOCAL_FIXTURE_VISIBLE_GENERATION_SMOKE",
        "reason": "Recent local fixture visible generation smoke.",
    },
    {
        "source": BASE / "1013R_R86_PROVIDER_SANDBOX_DRY_RUN",
        "target": "R86_PROVIDER_SANDBOX_DRY_RUN",
        "reason": "Recent provider sandbox evidence, including provider/fallback status and normalized output.",
    },
    {
        "source": BASE / "1013R_R87_PROVIDER_OR_FIXTURE_VISIBLE_GENERATION_SMOKE",
        "target": "R87_PROVIDER_OR_FIXTURE_VISIBLE_GENERATION_SMOKE",
        "reason": "Recent visible generation smoke copied page, not the main R21 page.",
    },
    {
        "source": BASE / "1013R_R80_GENERATION_FLOW_AND_FIELD_MAPPING_CONTRACT",
        "target": "references/R80_GENERATION_FLOW_AND_FIELD_MAPPING_CONTRACT",
        "reason": "Upstream generation flow and field mapping contract.",
    },
    {
        "source": BASE / "1013R_R81_LESSON_SCHEMA_FIELD_MAP_ADAPTER",
        "target": "references/R81_LESSON_SCHEMA_FIELD_MAP_ADAPTER",
        "reason": "Single-lesson 14-field adapter used by R88.",
    },
    {
        "source": BASE / "1013R_R82_LESSON_GENERATION_REQUEST_RESPONSE_CONTRACT",
        "target": "references/R82_LESSON_GENERATION_REQUEST_RESPONSE_CONTRACT",
        "reason": "Request/response contract used by R83-R87.",
    },
    {
        "source": BASE / "1013I_R6N_R9A_field_label_disambiguation_before_runtime_schema",
        "target": "references/R6N_R9A_BIG_UNIT_CANONICAL_FIELD_LEDGER",
        "reason": "Canonical big-unit field source referenced by R88.",
    },
    {
        "source": ROOT / "scripts" / "build_1013r_r88_field_generation_quality_static_lab.py",
        "target": "scripts/build_1013r_r88_field_generation_quality_static_lab.py",
        "reason": "Builder for the R88 static lab.",
    },
    {
        "source": ROOT / "scripts" / "build_1013r_r83_r87_visible_generation_chain.py",
        "target": "scripts/build_1013r_r83_r87_visible_generation_chain.py",
        "reason": "Builder for the recent R83-R87 generation chain.",
    },
]


def copy_item(source: Path, target: Path) -> dict:
    record = {
        "source": str(source),
        "target": str(target),
        "exists": source.exists(),
        "kind": "directory" if source.is_dir() else "file",
        "copied": False,
    }
    if not source.exists():
        return record
    target.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target)
    else:
        shutil.copy2(source, target)
    record["copied"] = True
    return record


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_zip(source_dir: Path, zip_path: Path) -> None:
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(source_dir.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(source_dir.parent))


def main() -> None:
    if PACKAGE_DIR.exists():
        shutil.rmtree(PACKAGE_DIR)
    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)

    copied = []
    for item in ITEMS:
        target = PACKAGE_DIR / item["target"]
        record = copy_item(item["source"], target)
        record["reason"] = item["reason"]
        copied.append(record)

    validations = {
        "r88": PACKAGE_DIR / "R88_FIELD_GENERATION_QUALITY_STATIC_LAB" / "validate_1013R_R88_field_generation_quality_static_lab_result.json",
        "r87": PACKAGE_DIR / "R87_PROVIDER_OR_FIXTURE_VISIBLE_GENERATION_SMOKE" / "validate_1013R_R87_visible_generation_smoke_result.json",
        "r86": PACKAGE_DIR / "R86_PROVIDER_SANDBOX_DRY_RUN" / "validate_1013R_R86_provider_sandbox_result.json",
        "r83": PACKAGE_DIR / "R83_LESSON_GENERATION_NORMALIZER_DRY_RUN" / "validate_1013R_R83_normalizer_result.json",
    }
    validation_snapshots = {}
    for key, path in validations.items():
        if path.exists():
            validation_snapshots[key] = json.loads(path.read_text(encoding="utf-8"))

    manifest = {
        "package": "1013R_R88_FIELD_GENERATION_GPT_REVIEW_PACKAGE",
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "purpose": "GPT review package for the field-generation foundation and the recent R83-R88 generation/visibility work.",
        "boundaries": {
            "main_r21_page_modified": False,
            "provider_runtime_connected_by_r88": False,
            "prompt_text_visible_in_r88_html": False,
            "formal_apply_allowed": False,
            "database_write": False,
            "feishu_write": False,
            "memory_write": False,
        },
        "included_items": copied,
        "validation_snapshots": validation_snapshots,
        "recommended_review_order": [
            "README.md",
            "R88_FIELD_GENERATION_QUALITY_STATIC_LAB/field_generation_quality_static_lab_1013R_R88.html",
            "R88_FIELD_GENERATION_QUALITY_STATIC_LAB/field_generation_quality_static_lab_ledger_1013R_R88.json",
            "R88_FIELD_GENERATION_QUALITY_STATIC_LAB/GPT_REVIEW_PROMPT_1013R_R88_FIELD_GENERATION_QUALITY_STATIC_LAB.md",
            "R87_PROVIDER_OR_FIXTURE_VISIBLE_GENERATION_SMOKE/README.md",
            "references/R81_LESSON_SCHEMA_FIELD_MAP_ADAPTER/lesson_14_field_mapping_1013R_R81.json",
        ],
    }

    readme = """# 1013R R88 Field Generation GPT Review Package

This package is for GPT review of the current teaching-design field-generation foundation.

## What To Open First

1. `R88_FIELD_GENERATION_QUALITY_STATIC_LAB/field_generation_quality_static_lab_1013R_R88.html`
2. `R88_FIELD_GENERATION_QUALITY_STATIC_LAB/field_generation_quality_static_lab_ledger_1013R_R88.json`
3. `R88_FIELD_GENERATION_QUALITY_STATIC_LAB/GPT_REVIEW_PROMPT_1013R_R88_FIELD_GENERATION_QUALITY_STATIC_LAB.md`
4. `REVIEW_PACKAGE_MANIFEST.md`

## Scope

- R88 is a standalone static lab, not the main R21 page.
- R88 shows visible fields, engineering fields, canonical references, and generation placeholders.
- R88 does not display generation prompt text.
- R88 does not call provider/model/runtime.
- R88 does not formal apply or write database/Feishu/memory.

## Current Counts

- Big-unit fields: 22
- Single-lesson fields: 14
- Classroom-flow line-contract groups: 7
- Classroom-flow line-contract fields: 47

## Recent Work Included

- R83 normalizer dry run
- R84 edit-card bridge smoke
- R85 local fixture visible smoke
- R86 provider sandbox dry run
- R87 copied visible generation smoke
- R88 field generation quality static lab

## Review Question

Is this field foundation sufficient to support high-quality layered teaching-design generation:

big unit -> lesson slice -> field internal structure -> classroom-flow line contract -> derived courseware/handout/assessment objects?
"""
    (PACKAGE_DIR / "README.md").write_text(readme, encoding="utf-8")

    manifest_md_lines = [
        "# REVIEW_PACKAGE_MANIFEST",
        "",
        "- package: `1013R_R88_FIELD_GENERATION_GPT_REVIEW_PACKAGE`",
        f"- created_at: `{manifest['created_at']}`",
        "- main_r21_page_modified: `false`",
        "- provider_runtime_connected_by_r88: `false`",
        "- prompt_text_visible_in_r88_html: `false`",
        "- formal_apply_allowed: `false`",
        "",
        "## Included Items",
        "",
    ]
    for item in copied:
        manifest_md_lines.append(f"- `{item['target']}` copied={str(item['copied']).lower()} reason={item['reason']}")
    manifest_md_lines.extend(["", "## Validation Snapshot", ""])
    for key, snapshot in validation_snapshots.items():
        manifest_md_lines.append(f"- `{key}` result=`{snapshot.get('result')}`")
    (PACKAGE_DIR / "REVIEW_PACKAGE_MANIFEST.md").write_text("\n".join(manifest_md_lines) + "\n", encoding="utf-8")
    (PACKAGE_DIR / "REVIEW_PACKAGE_MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    build_zip(PACKAGE_DIR, ZIP_PATH)
    zip_hash = file_sha256(ZIP_PATH)
    result = {
        "result": "PASS",
        "package_dir": str(PACKAGE_DIR),
        "zip_path": str(ZIP_PATH),
        "zip_sha256": zip_hash,
        "included_count": len(copied),
        "missing_count": sum(1 for item in copied if not item["exists"]),
        "validation_results": {key: snapshot.get("result") for key, snapshot in validation_snapshots.items()},
    }
    (PACKAGE_DIR / "PACKAGE_RESULT.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
