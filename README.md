# Digital Twin

Digital Twin is a personal memory vault that turns saved information into structured, tagged objects for memory-first retrieval.

## Project Layout

```text
src/digital_twin/
  schemas/     Object models and validation
  storage/     Local persistence adapters
  extraction/  Input parsing and object drafting
  tagging/     Tag normalization and generation
  retrieval/   Memory-first search and ranking
  cli/         Command-line entry points
data/
  objects/     Local memory object storage
tests/         Unit and smoke tests by project area
```

## Local Development

The implementation is scaffolded but not wired to a package manager yet. Add commands here as the runtime and test framework are selected.
