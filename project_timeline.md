# Digital Twin Project Timeline

This timeline turns the Digital Twin system instructions into an implementation plan. It is organized as relative phases so the schedule can be started from any date.

## Phase 1: Product Foundation

**Duration:** Week 1

**Goal:** Define the minimum viable Digital Twin experience and the system boundaries.

**Deliverables:**

- Confirm the core workflow: `Save -> Extract -> Tag -> Structure -> Store -> Retrieve`
- Finalize supported object types for the first release
- Define required fields for every object type
- Decide where memory objects are stored
- Define how saved objects are cited during retrieval

**Acceptance criteria:**

- The MVP scope is documented
- Each supported object type has a schema
- Retrieval rules clearly prioritize saved memory over web search

## Phase 2: Object Model And Storage

**Duration:** Weeks 2-3

**Goal:** Build the structured memory layer.

**Deliverables:**

- Universal object model implementation
- Type-specific schema validation
- Object create, update, and read operations
- Metadata support for restaurants, recipes, skincare, travel, products, pantry items, and nutrition logs
- Basic object ID and timestamp handling

**Acceptance criteria:**

- Saved items are persisted as structured objects
- Invalid objects are rejected with clear errors
- Existing objects can be retrieved by ID and type

## Phase 3: Extraction And Tagging

**Duration:** Weeks 4-5

**Goal:** Convert unstructured input into clean Digital Twin objects.

**Deliverables:**

- Text input extraction
- URL input extraction
- Image and screenshot extraction plan or prototype
- Automatic object type detection
- Normalized kebab-case tag generation
- Duplicate tag prevention
- Useful specificity preservation for brands, ingredients, locations, concerns, dishes, and statuses

**Acceptance criteria:**

- A user can save free-form text and receive a structured object
- Tags are normalized and non-duplicative
- Object type selection is accurate for the MVP object types

## Phase 4: Memory-First Retrieval

**Duration:** Weeks 6-7

**Goal:** Make saved information searchable through natural language.

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

**Acceptance criteria:**

- The supported example queries work end to end
- Pantry recipe matching ranks recipes by ingredient coverage
- Nutrition summaries calculate calories, protein, carbs, and fat

## Phase 6: Quality, Review, And Hardening

**Duration:** Weeks 11-12

**Goal:** Make the MVP reliable enough for real personal use.

**Deliverables:**

- Test coverage for schemas, extraction, tagging, retrieval, and domain workflows
- Golden examples for each object type
- Duplicate and near-duplicate handling
- Error handling for incomplete inputs
- Documentation for system behavior and known limitations
- Privacy and data-retention review

**Acceptance criteria:**

- Core flows are covered by automated tests
- Saved examples remain stable across changes
- The system handles incomplete or ambiguous input gracefully

## Post-MVP Roadmap

**Focus areas:**

- Voice note ingestion
- TikTok, Instagram Reel, and YouTube extraction
- Barcode support for food products
- Weekly nutrition trends
- User feedback loops for correcting tags and metadata
- Cross-domain recommendations, such as recipes from saved restaurants or skincare routines from saved products
- Import and export tools for memory portability

## Key Dependencies

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

## GitHub Issue Sprint Checklist

### Sprint 1: MVP Scope And Project Setup

- [ ] Confirm MVP scope: text save, extraction, tagging, local storage, and memory-first retrieval
- [ ] Choose initial object types: `restaurant`, `recipe`, and `skincare`
- [ ] Create project structure for schemas, storage, extraction, tagging, retrieval, CLI, data, and tests
- [ ] Add initial `data/objects/memory.json` storage file
- [ ] Document local development commands in the README
- [ ] Define done criteria for the MVP memory loop

### Sprint 2: Schemas And Local Storage

- [ ] Implement the universal Digital Twin object schema
- [ ] Add type-specific metadata schemas for restaurants
- [ ] Add type-specific metadata schemas for recipes
- [ ] Add type-specific metadata schemas for skincare products
- [ ] Implement object validation
- [ ] Implement local JSON object storage
- [ ] Add create, read, update, delete, and list operations
- [ ] Add tests for schema validation and storage behavior

### Sprint 3: Manual Save And Tag Normalization

- [ ] Build manual object save flow
- [ ] Generate object IDs and timestamps automatically
- [ ] Implement `normalizeTag`
- [ ] Convert tags to lowercase kebab-case
- [ ] Remove duplicate tags
- [ ] Add default status tags such as `not-visited`, `not-tried`, and `not-reviewed`
- [ ] Add tests for tag normalization and manual save behavior

### Sprint 4: Text Extraction

- [ ] Implement text input save flow
- [ ] Detect object type from plain text
- [ ] Extract title, notes, metadata, and candidate tags from text
- [ ] Generate restaurant tags from cuisine, city, neighborhood, meal type, visit status, and dishes
- [ ] Generate recipe tags from cuisine, ingredients, meal type, dietary restrictions, cooking style, and tried status
- [ ] Generate skincare tags from brand, ingredients, product type, concerns, and review status
- [ ] Save extracted objects to local storage
- [ ] Add golden extraction examples for each initial object type
- [ ] Add tests for text extraction and generated tags

### Sprint 5: Memory-First Retrieval

- [ ] Implement natural-language query handling
- [ ] Convert user queries into normalized tags
- [ ] Detect object type filters from queries when possible
- [ ] Search stored objects by tag matches
- [ ] Rank results by match score
- [ ] Group similar results by object type
- [ ] Return object summaries with relevant tags
- [ ] Return `I couldn't find any matching items in your Digital Twin memory.` when no result exists
- [ ] Prevent web search unless the user explicitly asks for it
- [ ] Add tests for supported example queries and empty results

### Sprint 6: CLI Or Minimal Interface

- [ ] Add `save` command for text input
- [ ] Add `search` command for memory retrieval
- [ ] Add `list` command for saved objects
- [ ] Add `show <id>` command for one object
- [ ] Add `update <id>` command for metadata, notes, and tags
- [ ] Add `delete <id>` command
- [ ] Add clear error messages for invalid commands and missing objects
- [ ] Add smoke tests for the full save and search flow

### Sprint 7: Domain Workflow Expansion

- [ ] Add `travel` object support
- [ ] Add `product` object support
- [ ] Add `food-product` object support
- [ ] Add `pantry-item` object support
- [ ] Add `nutrition-log` object support
- [ ] Implement pantry item tracking with quantity, unit, expiration date, and purchase date
- [ ] Implement recipe matching from pantry contents
- [ ] Implement daily nutrition summary calculations
- [ ] Add tests for each new domain workflow

### Sprint 8: Hardening And MVP Release

- [ ] Add duplicate and near-duplicate detection
- [ ] Add correction flow for changing type, metadata, notes, and tags
- [ ] Add handling for incomplete or ambiguous input
- [ ] Add privacy and data-retention notes
- [ ] Review all example queries from the system instructions
- [ ] Confirm memory-first behavior across all retrieval flows
- [ ] Confirm no hallucinated results are returned for empty searches
- [ ] Run full test suite
- [ ] Create MVP release notes

### Post-MVP Backlog

- [ ] Add URL extraction
- [ ] Add screenshot and image extraction
- [ ] Add YouTube extraction
- [ ] Add Instagram Reel and TikTok extraction
- [ ] Add voice note ingestion
- [ ] Add barcode support for food products
- [ ] Add weekly nutrition trends
- [ ] Add import and export tools
- [ ] Add a richer visual interface
