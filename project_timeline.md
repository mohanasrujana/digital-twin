# Digital Twin Project Timeline

This timeline turns the Digital Twin system instructions into an implementation plan. It is organized as relative phases so the schedule can be started from any date.

**Last updated:** 2026-07-07

## Current Status

- Phase 0: Complete. Packaging, dependency policy, local setup instructions, linting, ignore rules, and the first test command are in place.
- Phase 1: Mostly complete. MVP scope, workflow, object types, storage path, and retrieval rules are documented in `README.md` and `src/digital_twin/schemas/objects.py`.
- Phase 1 implementation note: schema constants exist, but runtime object validation still needs to be built in Phase 2.
- Phase 2: Not started. Core modules are currently placeholders in `extraction/text.py`, `storage/json_store.py`, `retrieval/search.py`, and `cli/main.py`.
- Current implementation state: scaffolded package layout exists, but the save/search memory loop is not implemented.
- README reflects the current Phase 0 setup: editable install, `ruff`, `unittest`, syntax checks, and dependency policy are documented.
- MVP is functionally complete after Phase 2 when the plain-text save/search loop works and is tested. MVP is release-ready after Phase 6 hardening.

## Phase Map

Phase 2 is the first thin vertical slice: it should create the smallest end-to-end loop that can save plain text, structure it, store it locally, and retrieve it from memory. Phases 3 and 4 should deepen that slice rather than repeat it: Phase 3 improves extraction and tagging quality, and Phase 4 improves retrieval quality, ranking, grouping, and query handling.

```text
Phase 0 tooling -> Phase 1 scope -> Phase 2 thin memory loop -> Phase 3 extraction quality -> Phase 4 retrieval quality -> Phase 5 domain workflows -> Phase 6 hardening
```

## Dependency Order

```text
packaging -> test runner -> schemas -> validation -> storage -> tagging -> extraction -> retrieval -> CLI -> domain workflows -> hardening
```

## Decision Log


| Topic                     | Decision                                                                                                                          | Status                            |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| MVP object types          | `restaurant`, `recipe`, `skincare`                                                                                                | Decided                           |
| Full object type universe | `restaurant`, `recipe`, `skincare`, `travel`, `food-product`, `pantry-item`, `nutrition-log`, `product`, `recommendation`, `note` | Documented in system instructions |
| Storage                   | Local JSON at `data/objects/memory.json` for MVP                                                                                  | Decided                           |
| Retrieval source order    | Search saved memory before outside sources                                                                                        | Decided                           |
| Web search                | Only when explicitly requested by the user                                                                                        | Decided                           |
| Memory data tracking      | Keep empty `data/objects/memory.json` as a tracked seed file for the scaffold; do not commit real personal memory                 | Decided                           |
| ID format                 | UUID string generated at save time                                                                                                | Decided                           |
| Timestamps                | ISO 8601 UTC strings                                                                                                              | Decided                           |
| Missing metadata          | Required metadata keys must exist; incomplete extraction may use explicit defaults such as `unknown`, `not-visited`, `not-tried`, or `not-reviewed` | Decided                           |
| Runtime validation module | Put runtime validation in `src/digital_twin/schemas/validate.py`; keep schema constants in `objects.py`                           | Decided                           |
| Extraction strategy       | Start rule-based for MVP plain text; consider LLM-assisted extraction later                                                       | Decided                           |
| Tag generation location   | Put reusable tag generation in `src/digital_twin/tagging/generate.py`; keep normalization in `normalize.py`                       | Decided                           |
| CLI framework             | Use standard-library `argparse` for the MVP                                                                                       | Decided                           |
| Packaging                 | Use `pyproject.toml` with a `src/` package layout                                                                                 | Decided                           |
| Dependency management     | Keep runtime dependencies empty until needed; install development tools through the `dev` optional dependency group               | Decided                           |
| Linter                    | Use `ruff` with `python3 -m ruff check src tests`                                                                                | Decided                           |
| Test runner               | Use standard-library `unittest` with `python3 -m unittest discover -s tests`                                                       | Decided                           |
| CI                        | Defer CI until the first implementation-heavy phase; planned checks are `ruff`, syntax compilation, and `unittest`                | Deferred                          |




## Deferred Type Map


| Type             | Target phase  | Notes                                                                   |
| ---------------- | ------------- | ----------------------------------------------------------------------- |
| `restaurant`     | MVP / Phase 2 | First-release object type                                               |
| `recipe`         | MVP / Phase 2 | First-release object type                                               |
| `skincare`       | MVP / Phase 2 | First-release object type                                               |
| `travel`         | Phase 5       | Domain workflow expansion                                               |
| `product`        | Phase 5       | General saved products and shopping decisions                           |
| `food-product`   | Phase 5       | Needed for pantry and nutrition workflows                               |
| `pantry-item`    | Phase 5       | Represents food currently owned by the user                             |
| `nutrition-log`  | Phase 5       | Daily summaries in Phase 5, weekly trends Post-MVP                      |
| `recommendation` | Post-MVP      | Useful for friend recommendations and general discoveries               |
| `note`           | Post-MVP      | Generic fallback object for information that does not fit a richer type |




## Input Source Map


| Input source          | Target phase  | Notes                                                            |
| --------------------- | ------------- | ---------------------------------------------------------------- |
| Plain text            | MVP / Phase 2 | First save path                                                  |
| Manual CLI input      | MVP / Phase 2 | First interface                                                  |
| URL                   | Post-MVP      | Reuse extraction, tagging, validation, and storage path          |
| Website article       | Post-MVP      | Treat as URL extraction                                          |
| Screenshot            | Post-MVP      | Needs OCR or vision extraction                                   |
| Image                 | Post-MVP      | Needs image metadata and review flow                             |
| YouTube               | Post-MVP      | Needs transcript or content extraction                           |
| TikTok                | Post-MVP      | Needs platform extraction and source metadata                    |
| Instagram Reel        | Post-MVP      | Needs platform extraction and source metadata                    |
| Voice note            | Post-MVP      | Needs transcription before text extraction                       |
| Friend recommendation | Post-MVP      | Should likely produce `recommendation` plus linked domain object |
| Explicit web search   | Post-MVP      | Add only after memory-first behavior is stable; start with a gated stub before any real integration |




## CLI Command Matrix


| Command       | Target phase | Purpose                                         |
| ------------- | ------------ | ----------------------------------------------- |
| `save`        | Phase 2      | Save plain text into structured memory          |
| `search`      | Phase 2      | Retrieve saved memory by natural-language query |
| `list`        | Phase 6      | Inspect saved objects during hardening          |
| `show <id>`   | Phase 6      | Retrieve one object by ID                       |
| `update <id>` | Phase 6      | Correct metadata, notes, tags, or type          |
| `delete <id>` | Phase 6      | Remove saved local memory                       |
| `export`      | Post-MVP     | Export memory objects for portability           |
| `import`      | Post-MVP     | Import validated memory objects                 |




## Data And Privacy Notes

- The MVP stores memory locally in `data/objects/memory.json`.
- `data/objects/memory.json` stays tracked only as an empty seed file; do not commit real personal memory.
- Test fixtures should not use real personal data.
- Deletion, export, and import should be planned before broad domain expansion.
- Web search must remain opt-in and should not run automatically from empty retrieval results.

## Phase 0: Repo And Tooling Bootstrap

**Duration:** Before Week 1 or first implementation session

**Goal:** Make the repo installable, testable, and predictable before feature work starts.

**Deliverables:**

- Done: Python packaging file at `pyproject.toml`
- Done: chosen test runner and documented test command
- Done: chosen linter and documented lint command
- Done: local development setup instructions
- Done: dependency management decision
- Done: optional CI plan for lint and tests is documented as deferred

**Acceptance criteria:**

- Done: the package can be imported from a clean local setup after `python3 -m pip install -e .`
- Done: the documented lint command runs
- Done: the documented test command runs with the initial smoke test
- Done: generated Python artifacts are ignored
- Done: README no longer says tests are not wired

**Primary files:**

- `pyproject.toml`
- `README.md`
- `.gitignore`
- `tests/`

**Exit criteria:**

- Done: a new contributor can install or run the package using documented commands
- Done: test infrastructure exists before implementation-heavy phases
- Done: generated artifacts are ignored before test or compile commands are run
- Done: CI is explicitly deferred with planned checks

**Example data:**

- Test command example: `python3 -m unittest discover -s tests`
- Lint command example: `python3 -m ruff check src tests`
- Import check example: `python3 -c "import digital_twin"`
- Syntax check example: `python3 -m compileall src`

**Repo and tooling implementation order:**

- [x] Choose packaging approach
  - Add `pyproject.toml`
  - Confirm package import path
  - Document install command
- [x] Implement `unittest` per the Decision Log
  - Use standard-library `unittest`
  - Add an initial smoke test
  - Update `README.md` with the test command
- [x] Implement `ruff` linting
  - Add `ruff` to the `dev` optional dependency group
  - Configure lint settings in `pyproject.toml`
  - Update `README.md` with the lint command
- [x] Confirm generated-file policy
  - Keep `__pycache__/` ignored
  - Keep the empty `data/objects/memory.json` seed tracked
  - Do not commit real personal memory
  - Keep fixtures separate from personal data
- [x] Confirm seed data path
  - Ensure `data/objects/` exists for local storage
  - Keep an empty tracked `memory.json` seed file
  - If real user memory will be saved locally, create an ignored local-data path before storing personal data
- [x] Decide CI scope
  - Decide whether to add GitHub Actions now or defer it
  - If added, run syntax checks and tests on push

## Phase 1: Product Foundation

**Duration:** Week 1

**Goal:** Define the minimum viable Digital Twin experience and the system boundaries.

**Deliverables:**

- Confirmed core workflow: `Save -> Extract -> Tag -> Structure -> Store -> Retrieve`
- Finalized supported object types for the first release: `restaurant`, `recipe`, and `skincare`
- Defined required fields for every object type: `id`, `title`, `type`, `source`, `created_at`, `updated_at`, `tags`, `notes`, and `metadata`
- Decided where memory objects are stored: `data/objects/memory.json`
- Defined how saved objects are cited during retrieval: cite by `title`, `type`, and `id`

**Acceptance criteria:**

- Done: the MVP scope is documented in `README.md`
- Done: each supported object type has a schema in `src/digital_twin/schemas/objects.py`
- Done: retrieval rules clearly prioritize saved memory over web search

**Primary files:**

- `README.md`
- `project_timeline.md`
- `digital_twin_system_instructions.md`
- `src/digital_twin/schemas/objects.py`

**Exit criteria:**

- The MVP boundary is clear enough that non-MVP features can be deferred without debate
- The first-release object types and required fields are documented in one place
- Storage and retrieval rules are documented before implementation starts
- The next phase can begin without changing the product scope

**Example data:**

- Workflow example: `Save -> Extract -> Tag -> Structure -> Store -> Retrieve`
- MVP object types: `restaurant`, `recipe`, `skincare`
- Citation example: `Cafe Sol (restaurant, id: 123e4567-e89b-12d3-a456-426614174000)`

**Product foundation implementation order:**

- [x] Review the Digital Twin system instructions
  - Identify the core promise of the product
  - Identify what the MVP must do before any domain expansion
  - Identify what the MVP should explicitly not do yet
- [x] Define the core workflow
  - Document `Save -> Extract -> Tag -> Structure -> Store -> Retrieve`
  - Confirm which layer owns each step
  - Confirm which steps run synchronously in the MVP
- [x] Document layer ownership
  - Extraction owns turning raw input into object drafts
  - Tagging owns normalization and reusable tag-generation helpers
  - Storage owns persistence and read/write behavior
  - Retrieval owns query handling, ranking, citations, and no-match responses
- [x] Define the initial object scope
  - Confirm first-release object types: `restaurant`, `recipe`, `skincare`
  - Move non-MVP types into the roadmap
  - Avoid adding domain workflows before the generic memory loop works
- [x] Define the universal memory object shape
  - Confirm required base fields
  - Confirm type-specific metadata expectations
  - Confirm citation fields for retrieval
- [x] Define storage and retrieval boundaries
  - Confirm local JSON storage path
  - Confirm saved memory is searched before outside sources
  - Confirm web search requires explicit user intent
- [x] Document the MVP done criteria
  - Update `README.md` with the scope, workflow, and rules
  - Update `project_timeline.md` with phase-level plan
  - Keep implementation decisions visible before writing code
- [x] Keep planning documents synchronized
  - Update `digital_twin_system_instructions.md` when product boundaries change
  - Update `README.md` when implementation commands or MVP criteria change
  - Update `project_timeline.md` when phase scope or status changes

## Phase 2: Object Model And Storage

**Duration:** Weeks 2-3

**Goal:** Build the first thin vertical slice of the structured memory layer.

**Deliverables:**

- Universal object model implementation
- Type-specific schema validation
- Object create and read operations, with update deferred to Phase 6
- MVP metadata support for restaurants, recipes, and skincare
- Basic object ID and timestamp handling
- Minimal save/search loop across storage, extraction, tagging, retrieval, and CLI

**Acceptance criteria:**

- Saved items are persisted as structured objects
- Invalid objects are rejected with clear errors
- Existing objects can be retrieved by ID and type

**Primary files:**

- `src/digital_twin/schemas/objects.py`
- `src/digital_twin/schemas/validate.py`
- `src/digital_twin/storage/json_store.py`
- `src/digital_twin/tagging/normalize.py`
- `src/digital_twin/tagging/generate.py`
- `src/digital_twin/extraction/text.py`
- `src/digital_twin/retrieval/search.py`
- `src/digital_twin/cli/main.py`
- `data/objects/memory.json`
- `tests/schemas/`
- `tests/storage/`
- `tests/tagging/`
- `tests/extraction/`
- `tests/retrieval/`
- `tests/cli/`

**Exit criteria:**

- Memory objects validate against the base schema and type-specific metadata requirements
- Invalid objects fail with clear, test-covered errors
- Objects can be saved, loaded, and retrieved by ID without data loss
- Generated files are ignored before running validation or test commands

**Example data:**

- Restaurant: `Cafe Sol`, type `restaurant`, tags `mexican`, `san-jose`, metadata `cuisine`, `location`, `visit_status`, `review_status`
- Recipe: `Weeknight Dal`, type `recipe`, tags `lentils`, `dinner`, metadata `ingredients`, `meal_type`, `tried_status`
- Skincare: `Daily SPF`, type `skincare`, tags `sunscreen`, `spf`, metadata `brand`, `product_type`, `review_status`

**Structured memory layer implementation order:**

- [ ] Lock the MVP object contract
  - Confirm the Decision Log values are still correct before coding
  - Confirm supported object types: `restaurant`, `recipe`, `skincare`
  - Confirm required base fields: `id`, `title`, `type`, `source`, `created_at`, `updated_at`, `tags`, `notes`, `metadata`
  - Confirm required metadata per object type:
    - `restaurant`: `cuisine`, `location`, `visit_status`, `review_status`
    - `recipe`: `ingredients`, `meal_type`, `tried_status`
    - `skincare`: `brand`, `product_type`, `review_status`
- [ ] Add memory object validation
  - Create `src/digital_twin/schemas/validate.py`
  - Reject missing base fields
  - Reject unsupported object types
  - Reject invalid `tags` values
  - Reject invalid `metadata` values
  - Reject missing type-specific metadata fields
  - Add tests for valid and invalid memory objects
- [ ] Add tag normalization
  - Normalize tags to lowercase kebab-case
  - Remove blank tags
  - Deduplicate tags while preserving first-seen order
  - Add tests for casing, spacing, punctuation, blanks, and duplicates
- [ ] Add reusable tag generation
  - Create `src/digital_twin/tagging/generate.py`
  - Generate candidate tags from object type, title, metadata, and notes
  - Reuse `normalize.py` before storing generated tags
  - Add tests for generated tag candidates and normalization handoff
- [ ] Add minimal structured text extraction
  - Return structured memory objects from plain text
  - Infer object type when the user does not provide one
  - Support explicit object type overrides
  - Extract `title` from `Title:` or `Name:` when present
  - Extract type-specific metadata from simple `Key: Value` lines
  - Generate `id`, `created_at`, `updated_at`, and `source`
  - Normalize generated tags before returning the object
  - Validate extracted objects before they leave the extraction layer
  - Add tests for all three MVP object types
- [ ] Add local JSON storage
  - Implement storage for `data/objects/memory.json`
  - Load an empty list when the file does not exist
  - Validate objects on load
  - Validate objects before save
  - Append new objects without dropping existing ones
  - Save JSON in a readable, stable format
  - Add tests using temporary files, not the real memory store
- [ ] Add minimal memory-first retrieval
  - Search title, type, tags, notes, and metadata
  - Rank results deterministically
  - Limit result count
  - Return citations using `title`, `type`, and `id`
  - Return `I couldn't find any matching items in your Digital Twin memory.` when no saved object matches
  - Do not call web search unless the user explicitly asks for online results
  - Add tests for matches, ranking, citations, and empty results
- [ ] Add the CLI workflow
  - Add a `save` command for plain-text memory input
  - Add a `search` command for natural-language memory queries
  - Support an optional `--type` override on save
  - Support an optional store path for tests and local debugging
  - Print saved-object citations after save
  - Print no-match retrieval responses clearly
  - Add CLI smoke tests
- [ ] Wire verification
  - Use the test runner chosen in Phase 0
  - Run the full test suite
  - Run syntax checks if no formatter or linter exists yet
- [ ] Review before expanding the layer
  - Confirm the implementation matches the README MVP done criteria
  - Confirm no generated files are tracked
  - Confirm retrieval answers only from saved memory
  - Confirm no unrelated refactors were introduced
  - Confirm the next feature has a clear boundary before expanding the layer

## Phase 3: Extraction And Tagging

**Duration:** Weeks 4-5

**Goal:** Harden extraction and tagging beyond the Phase 2 vertical slice.

**Deliverables:**

- Better text input extraction
- URL, image, and screenshot extraction plan with implementation deferred unless explicitly pulled forward
- More accurate object type detection
- Domain-specific tag generation rules
- Duplicate tag prevention
- Useful specificity preservation for brands, ingredients, locations, neighborhoods, concerns, dishes, dietary restrictions, and statuses

**Acceptance criteria:**

- A user can save free-form text and receive a structured object
- Tags are normalized and non-duplicative
- Object type selection is accurate for the MVP object types
- Phase 2 extraction behavior is improved without expanding beyond the MVP save path

**Primary files:**

- `src/digital_twin/extraction/text.py`
- `src/digital_twin/tagging/normalize.py`
- `src/digital_twin/tagging/generate.py`
- `src/digital_twin/schemas/objects.py`
- `tests/extraction/`
- `tests/tagging/`
- `tests/fixtures/`

**Exit criteria:**

- Plain text can be converted into a valid structured object for every MVP type
- Tags are normalized, deduplicated, and stable across repeated runs
- Ambiguous or incomplete input produces predictable output or clear errors
- Golden extraction examples exist for restaurant, recipe, and skincare inputs

**Example data:**

- Restaurant input: `Name: Cafe Sol`, `Cuisine: Mexican`, `Location: San Jose`
- Recipe input: `Title: Weeknight Dal`, `Ingredients: lentils, cumin, tomato`, `Meal type: dinner`
- Skincare input: `Name: Daily SPF`, `Brand: Supergoop`, `Product type: sunscreen`

**Extraction and tagging implementation order:**

- [ ] Define extraction inputs and outputs
  - Accept plain text as the first input source
  - Return a structured memory object draft
  - Keep URL, image, and screenshot extraction behind later interfaces
- [ ] Implement text pre-processing
  - Trim empty input
  - Preserve original notes
  - Split simple `Key: Value` lines for metadata extraction
- [ ] Implement object type detection
  - Detect `restaurant`, `recipe`, and `skincare` from keywords and fields
  - Allow explicit type overrides
  - Return clear errors for unsupported types
- [ ] Extract shared fields
  - Extract title from `Title:` or `Name:`
  - Preserve notes from the original input
  - Attach source information for traceability
- [ ] Extract type-specific metadata
  - Extract restaurant cuisine, location, visit status, and review status
  - Extract recipe ingredients, meal type, and tried status
  - Extract skincare brand, product type, and review status
- [ ] Generate normalized tags
  - Include object type, title, metadata, and useful keywords
  - Add restaurant tags for cuisine, city, neighborhood, meal type, visit status, review status, and notable dishes
  - Add recipe tags for cuisine, ingredients, meal type, dietary restrictions, cooking style, and tried status
  - Add skincare tags for brand, ingredients, concerns, product type, and review status
  - Convert tags to lowercase kebab-case
  - Remove duplicates and blank tags
- [ ] Validate and test extraction
  - Validate extracted objects before saving
  - Add golden examples for each MVP object type
  - Add tests for ambiguous, incomplete, and explicit-type inputs

## Phase 4: Memory-First Retrieval

**Duration:** Weeks 6-7

**Goal:** Harden memory-first retrieval beyond the Phase 2 vertical slice.

**Deliverables:**

- Query intent detection
- Query-to-tag conversion
- Tag-based retrieval
- Relevance ranking
- Grouped result presentation
- Empty-state response: `I couldn't find any matching items in your Digital Twin memory.`
- Explicit web-search gating behavior

**Acceptance criteria:**

- Example queries in the system instructions return relevant saved objects
- No web search happens unless explicitly requested
- Results include useful object summaries and tags
- Phase 2 retrieval behavior is improved without changing the memory-first contract

**Primary files:**

- `src/digital_twin/retrieval/search.py`
- `src/digital_twin/storage/json_store.py`
- `src/digital_twin/tagging/normalize.py`
- `tests/retrieval/`
- `tests/fixtures/`

**Exit criteria:**

- Natural-language queries return matching saved objects before any outside source is considered
- Empty searches return the exact no-match message
- Result citations include `title`, `type`, and `id`
- Ranking behavior is deterministic and covered by tests

**Example data:**

- Query: `Mexican restaurant in San Jose` -> returns `Cafe Sol (restaurant, id: ...)`
- Query: `dinner recipe with lentils` -> returns `Weeknight Dal (recipe, id: ...)`
- Query: `retinol serum` with no matching object -> returns `I couldn't find any matching items in your Digital Twin memory.`

**Memory-first retrieval implementation order:**

- [ ] Define query behavior
  - Accept natural-language memory queries
  - Treat saved memory as the first and default source
  - Require explicit wording before any online lookup
- [ ] Normalize query terms
  - Tokenize user queries
  - Normalize candidate tags from queries
  - Detect object type filters when obvious
- [ ] Build local search
  - Search stored objects by title, type, tags, notes, and metadata
  - Keep search deterministic for tests
  - Avoid returning objects with no meaningful match
- [ ] Add ranking
  - Score by matched terms or tags
  - Prefer stronger metadata and tag matches
  - Use stable tie-breaking for consistent results
- [ ] Format results
  - Return object summaries
  - Include citations using `title`, `type`, and `id`
  - Group results by object type if multiple domains match
- [ ] Handle empty results
  - Return `I couldn't find any matching items in your Digital Twin memory.`
  - Do not invent results
  - Do not fall back to web search automatically
- [ ] Test retrieval behavior
  - Add tests for matching queries
  - Add tests for ranking order
  - Add tests for citations
  - Add tests for empty results and web-search gating

## Phase 5: Domain Workflows

**Duration:** Weeks 8-10

**Goal:** Implement workflows that make the memory system useful in daily life.

**Deliverables:**

- Restaurant retrieval by cuisine, city, neighborhood, meal type, visit status, and dishes
- Recipe retrieval by cuisine, ingredients, meal type, dietary restriction, cooking style, and tried status
- Skincare retrieval by brand, ingredient, concern, and product type
- Travel retrieval by country, city, activity type, and visit status
- Pantry item tracking with quantity, unit, expiration date, and purchase date
- Recipe matching from pantry contents
- Nutrition log creation and daily summary calculation
- Weekly nutrition summary planning, with trend visualization deferred to Post-MVP

**Acceptance criteria:**

- The supported example queries work end to end
- Pantry recipe matching ranks recipes by ingredient coverage
- Nutrition summaries calculate calories, protein, carbs, and fat
- New object types are added only after the MVP save/search loop is stable

**Primary files:**

- `src/digital_twin/schemas/objects.py`
- `src/digital_twin/extraction/text.py`
- `src/digital_twin/retrieval/search.py`
- `src/digital_twin/cli/main.py`
- `tests/domain/`
- `tests/fixtures/`

**Exit criteria:**

- MVP domain workflows work before adding travel, product, pantry, or nutrition workflows
- New domain object types have schemas, extraction behavior, retrieval behavior, and tests
- Cross-domain workflows do not weaken memory-first retrieval behavior
- Pantry and nutrition calculations are deterministic and test-covered

**Example data:**

- Travel: `Tokyo ramen shops`, metadata `country`, `city`, `activity_type`, `visit_status`
- Pantry item: `Red lentils`, metadata `quantity`, `unit`, `expiration_date`, `purchase_date`
- Nutrition log: `Breakfast yogurt bowl`, metadata `calories`, `protein`, `carbs`, `fat`, `logged_date`

**Domain workflow implementation order:**

- [ ] Stabilize MVP domains first
  - Complete restaurant workflows for cuisine, location, visit status, dishes, and meal type
  - Complete recipe workflows for ingredients, meal type, dietary restrictions, cooking style, and tried status
  - Complete skincare workflows for brand, ingredients, concern, product type, and review status
- [ ] Add travel support
  - Define travel object metadata
  - Add extraction and tag generation for country, city, activity type, and visit status
  - Add retrieval examples and tests
- [ ] Add product support
  - Define product and food-product metadata
  - Add brand, category, price, review status, and purchase status fields where useful
  - Add retrieval examples and tests
- [ ] Add pantry item tracking
  - Define quantity, unit, expiration date, and purchase date fields
  - Add create, update, list, and expired-soon retrieval behavior
  - Add tests for pantry state changes
- [ ] Add recipe matching from pantry contents
  - Match recipes by ingredient coverage
  - Rank recipes by available ingredients and missing ingredients
  - Return clear explanations for matches
- [ ] Add nutrition logging
  - Define nutrition-log object metadata
  - Track calories, protein, carbs, fat, serving size, and logged date
  - Calculate daily summaries
  - Plan weekly summaries before trend visualization
- [ ] Test end-to-end domain workflows
  - Cover the supported example queries
  - Cover incomplete metadata
  - Cover cross-domain retrieval where relevant

## Phase 6: Quality, Review, And Hardening

**Duration:** Weeks 11-12

**Goal:** Make the MVP reliable enough for real personal use.

**Deliverables:**

- Test coverage for schemas, extraction, tagging, retrieval, and domain workflows
- Golden examples for each object type
- Duplicate and near-duplicate handling
- Error handling for incomplete inputs
- Error message catalog for validation, empty input, unsupported types, missing objects, and empty retrieval
- Documentation for system behavior and known limitations
- Privacy and data-retention review

**Acceptance criteria:**

- Core flows are covered by automated tests
- Saved examples remain stable across changes
- The system handles incomplete or ambiguous input gracefully

**Primary files:**

- `README.md`
- `project_timeline.md`
- `tests/`
- `tests/fixtures/`
- `data/objects/memory.json`
- `.gitignore`

**Exit criteria:**

- The full test suite passes from the documented command
- Golden examples remain stable across schema, extraction, and retrieval changes
- Duplicate and incomplete inputs have clear behavior
- Privacy, local storage, deletion, and export expectations are documented

**Example data:**

- Duplicate save example: two restaurant entries with the same title, location, and notes
- Incomplete input example: `Name: Cafe Sol` without cuisine or location
- Correction example: change `type` from `restaurant` to `recipe` only through an explicit correction flow

**Quality and hardening implementation order:**

- [ ] Establish the test baseline
  - Expand the Phase 0 and Phase 2 test baseline
  - Add missing schema, storage, extraction, tagging, retrieval, CLI, and domain workflow coverage
  - Confirm generated artifacts remain ignored before running tests
- [ ] Add golden examples
  - Add stable fixtures for each object type
  - Add expected extraction outputs
  - Add expected retrieval outputs
- [ ] Add duplicate handling
  - Detect exact duplicate saves
  - Detect near-duplicates by title, source, notes, and metadata
  - Decide whether to reject, merge, or warn
- [ ] Improve incomplete-input handling
  - Return clear validation errors
  - Use explicit placeholder values only where accepted by the contract
  - Add correction paths for missing metadata
- [ ] Add correction and update flows
  - Support changing type, metadata, notes, and tags
  - Preserve created timestamps
  - Update `updated_at` on changes
- [ ] Review privacy and retention
  - Document local storage behavior
  - Document what data is saved
  - Document deletion and export expectations
- [ ] Final MVP release check
  - Run the full test suite
  - Verify all README done criteria
  - Verify no hallucinated empty-search results
  - Verify no web search without explicit user request
  - Write MVP release notes

## Post-MVP Roadmap

**Focus areas:**

- Voice note ingestion
- TikTok, Instagram Reel, and YouTube extraction
- Barcode support for food products
- Weekly nutrition trends
- Friend recommendation ingestion
- User feedback loops for correcting tags and metadata
- Cross-domain recommendations, such as recipes from saved restaurants or skincare routines from saved products
- Import and export tools for memory portability

**Post-MVP implementation order:**

- [ ] Add import and export tools
  - Export memory objects to portable JSON
  - Import validated memory objects
  - Handle duplicates during import
- [ ] Add correction feedback loops
  - Treat Phase 6 correction as manual edit/update behavior
  - Treat Post-MVP correction feedback as learning from repeated corrections
  - Let users correct object type, metadata, notes, and tags
  - Use corrections to improve extraction rules
  - Track changed fields clearly
- [ ] Add explicit web-search support
  - Start with a gated stub response for explicit online requests
  - Add real integration only after memory-first retrieval is stable
  - Keep web results separate from saved memory unless the user saves them
- [ ] Add URL extraction
  - Extract readable text from URLs
  - Preserve source URL
  - Reuse the same structured extraction and validation path
- [ ] Add image and screenshot extraction
  - Define image input storage or reference behavior
  - Extract text and visible product/place details
  - Add review flow before saving uncertain metadata
- [ ] Add video and social extraction
  - Add YouTube extraction
  - Add TikTok and Instagram Reel extraction
  - Preserve platform source metadata
- [ ] Add voice note ingestion
  - Transcribe voice notes
  - Preserve transcript as notes
  - Reuse text extraction after transcription
- [ ] Add barcode support
  - Lookup food product metadata from barcode inputs
  - Store product source and confidence
  - Connect barcode products to pantry and nutrition workflows
- [ ] Add trend and recommendation workflows
  - Add weekly nutrition trends
  - Add friend recommendation ingestion
  - Add recipe recommendations from pantry and saved restaurants
  - Add skincare routine suggestions from saved products and concerns

## Key Dependencies

- Packaging and local development setup
- A documented test runner and baseline test suite
- A storage layer for structured memory objects
- An extraction layer for text, URLs, images, screenshots, videos, and voice notes
- A tagging and normalization layer
- A retrieval and ranking layer
- Domain-specific workflow logic for pantry, nutrition, recipes, restaurants, skincare, products, and travel

## Risks

- Over-broad object types may make retrieval noisy
- Extraction quality may vary by input source
- Tag normalization must stay consistent or search quality will degrade
- Recipe matching depends on clean pantry and ingredient metadata
- Nutrition tracking requires reliable serving size and macro data

## MVP Success Metrics

- Users can save information without manually organizing it
- Saved items become structured objects with useful tags
- Natural-language retrieval returns relevant stored objects
- Empty searches do not hallucinate results
- Web search only happens after explicit user request
