from nowledge_iface.extractor import ContentIndexing, INDEXING_TYPES


def test_all_indexing_kinds_has_type_defined():
    for indexing in ContentIndexing:
        assert indexing in INDEXING_TYPES.keys(), f"Indexing type {indexing} has no type associated"
