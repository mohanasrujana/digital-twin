SCOPE = (
    "text-save",
    "extraction",
    "tagging",
    "local-storage",
    "memory-first-retrieval",
)

OBJECT_TYPES = ("restaurant", "recipe", "skincare")

CORE_WORKFLOW = ("save", "extract", "tag", "structure", "store", "retrieve")

OBJECT_REQUIRED_FIELDS = (
    "id",
    "title",
    "type",
    "source",
    "created_at",
    "updated_at",
    "tags",
    "notes",
    "metadata",
)

TYPE_REQUIRED_METADATA_FIELDS = {
    "restaurant": ("cuisine", "location", "visit_status", "review_status"),
    "recipe": ("ingredients", "meal_type", "tried_status"),
    "skincare": ("brand", "product_type", "review_status"),
}

BASE_OBJECT_SCHEMA = {
    "required": OBJECT_REQUIRED_FIELDS,
    "properties": {
        "id": "string",
        "title": "string",
        "type": "string",
        "source": "string",
        "created_at": "datetime",
        "updated_at": "datetime",
        "tags": "list[string]",
        "notes": "string",
        "metadata": "dict",
    },
}

OBJECT_SCHEMAS = {
    object_type: {
        **BASE_OBJECT_SCHEMA,
        "type": object_type,
        "metadata_required": metadata_fields,
    }
    for object_type, metadata_fields in TYPE_REQUIRED_METADATA_FIELDS.items()
}

MEMORY_STORAGE_PATH = "data/objects/memory.json"

CITATION_FIELDS = ("title", "type", "id")

RETRIEVAL_RULES = (
    "Search data/objects/memory.json before any outside source.",
    "Return saved-object citations using title, type, and id.",
    "Return an empty-memory response when there are no saved matches.",
    "Use web search only when the user explicitly asks for it.",
)
