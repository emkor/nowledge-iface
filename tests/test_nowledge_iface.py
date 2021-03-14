import nowledge_iface.v1 as iface_v1


def test_all_indexing_kinds_has_type_defined():
    for indexing in iface_v1.ContentIndexing:
        assert indexing in iface_v1.INDEXING_TYPES.keys(), f"Indexing type {indexing} has no type associated"
