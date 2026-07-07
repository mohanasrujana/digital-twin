import unittest

from digital_twin.schemas.objects import MEMORY_STORAGE_PATH, OBJECT_TYPES, RETRIEVAL_RULES

class PackageSmokeTest(unittest.TestCase):
    def test_mvp_constants_are_available(self):
        self.assertEqual(OBJECT_TYPES, ("restaurant", "recipe", "skincare"))
        self.assertEqual(MEMORY_STORAGE_PATH, "data/objects/memory.json")
        self.assertTrue(RETRIEVAL_RULES)


if __name__ == "__main__":
    unittest.main()
