# Digital Twin

Digital Twin is a personal memory vault that turns saved information into structured, tagged objects for memory-first retrieval.

## MVP Scope

The MVP memory loop is:

- Text save
- Extraction
- Tagging
- Local storage
- Memory-first retrieval

The initial object types are:

- `restaurant`
- `recipe`
- `skincare`

## MVP Done Criteria

The MVP memory loop is done when:

- A user can save plain text through the CLI.
- The system extracts a structured object from that text.
- The extracted object is assigned one of the initial object types.
- Tags are normalized to lowercase kebab-case with duplicates removed.
- The object is persisted to `data/objects/memory.json`.
- A user can retrieve saved objects with a natural-language memory query.
- Retrieval searches saved memory before any outside source.
- Empty retrieval results return a clear no-match response instead of invented answers.
- The save and retrieval loop is covered by automated tests.

## Product Foundation Decisions

Core workflow:

```text
Save -> Extract -> Tag -> Structure -> Store -> Retrieve
```

For the MVP, this workflow runs synchronously from the CLI: a save command
extracts, tags, structures, validates, and stores the memory object before the
command returns. A search command reads local memory and returns matching saved
objects before considering any outside source.

Layer ownership:

- `extraction` turns raw inputs into object drafts.
- `tagging` owns tag normalization and reusable tag-generation helpers.
- `schemas` owns object contracts and runtime validation.
- `storage` owns local persistence and read/write behavior.
- `retrieval` owns query handling, ranking, citations, and no-match responses.
- `cli` owns user-facing save and search commands.

Supported first-release object types:

- `restaurant`
- `recipe`
- `skincare`

Required fields for every object:

- `id`
- `title`
- `type`
- `source`
- `created_at`
- `updated_at`
- `tags`
- `notes`
- `metadata`

Type-specific required metadata:

- `restaurant`: `cuisine`, `location`, `visit_status`, `review_status`
- `recipe`: `ingredients`, `meal_type`, `tried_status`
- `skincare`: `brand`, `product_type`, `review_status`

Missing metadata policy:

- Required metadata keys must exist on saved objects.
- Incomplete extraction may use explicit defaults such as `unknown`, `not-visited`, `not-tried`, or `not-reviewed`.

Implementation decisions:

- Object IDs are UUID strings generated at save time.
- Timestamps are ISO 8601 UTC strings.
- Runtime validation will live in `src/digital_twin/schemas/validate.py`.
- Reusable tag generation will live in `src/digital_twin/tagging/generate.py`.
- The MVP CLI will use standard-library `argparse`.
- The initial test runner is standard-library `unittest`.

Each first-release object type has a schema in `src/digital_twin/schemas/objects.py`.

Memory objects are stored in `data/objects/memory.json` for the MVP.

Retrieval citations should reference saved objects by `title`, `type`, and `id` so answers can be traced back to memory records.

Retrieval rules:

- Search saved memory in `data/objects/memory.json` first.
- Answer from matching saved objects when possible.
- Return `I couldn't find any matching items in your Digital Twin memory.` when no saved object matches.
- Do not search the web unless the user explicitly asks for online results.

## Project Layout

```text
src/digital_twin/
  schemas/     Object models and validation
    objects.py
    validate.py  Planned Phase 2 runtime validation module
  storage/     Local persistence adapters
  extraction/  Input parsing and object drafting
  tagging/     Tag normalization and generation helpers
    normalize.py
    generate.py  Planned Phase 2 reusable tag-generation module
  retrieval/   Memory-first search and ranking
  cli/         Command-line entry points
data/
  objects/     Local memory object storage
tests/         Unit and smoke tests by project area
```

## Local Development

Run commands from the repository root:

```sh
cd /Users/satyasrujanapilli/digital-twin
```

Check Python syntax for the scaffolded package:

```sh
python3 -m compileall src
```

Inspect tracked and untracked changes:

```sh
git status --short
```

List project files:

```sh
find . -maxdepth 4 -type f -not -path "./.git/*" | sort
```

Run tests after Phase 0 wires the first test suite:

```sh
python3 -m unittest discover -s tests
```
