<!-- ccr-overview-v2 -->

### 🟢 Approval recommended

No active review issues are reported for the scoring-logic refactor.

**No open issues** 🎉

<details>
<summary><strong>What changed in this PR</strong></summary>

Refactors the tennis exercise’s scoring logic into smaller helper methods, making the existing rules easier to follow without changing scoring behavior.

**Changes:**
- Extracts helpers for tied scores, regular scores, and advantage or win results.
- Introduces named scoring constants and simplifies point increments.
- Adds Pylint, a dependency lockfile, and a dated README note.

| File | Description |
| ---- | ----------- |
| `viikko5/tennis/uv.lock` | Locks development dependencies and their transitive dependencies. |
| `viikko5/tennis/src/tennis_game.py` | Replaces nested scoring logic with helpers and named constants. |
| `viikko5/tennis/README.md` | Adds a dated note. |
| `viikko5/tennis/pyproject.toml` | Adds Pylint to development dependencies. |
</details>

<sub>Review effort: Balanced</sub>