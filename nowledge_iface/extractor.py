import datetime as dt
import typing as t
from abc import ABC
from enum import Enum

EXTRACTORS_KEY = "nowledge.extractor"


class ContentIndexing(Enum):
    NO = 'no'  # lack of indexing
    SIMPLE = 'simple'  # eg. simple text files where represents line number
    SPACE = 'space'  # eg. 2-dimensional coordinates
    RELATIVE_TIME = 'rel_time'  # eg. audio/video media, where indicates time of given result
    ABSOLUTE_TIME = 'abs_time'  # calendars, where indicates certain event


INDEXING_TYPES = {
    ContentIndexing.NO: None,
    ContentIndexing.SIMPLE: int,
    ContentIndexing.SPACE: t.Tuple[float, float],
    ContentIndexing.RELATIVE_TIME: dt.timedelta,
    ContentIndexing.ABSOLUTE_TIME: dt.datetime,
}


class NowledgeExtractor(ABC):
    @classmethod
    def name(cls) -> str:
        """
        Provides short, human-readable name,
        eg. Simple Text File Descriptor
        """
        raise NotImplementedError

    @classmethod
    def org(cls) -> str:
        """
        Provides unique extractor identifier,
        eg. 'org.example.simple-txt-file-extractor'
        """
        raise NotImplementedError

    @classmethod
    def mime_types(cls) -> t.Collection[str]:
        """
        Provides extraction-supported MIME types as defined by RFC6838
        eg. ['text/html', 'audio/mpeg']
        """
        raise NotImplementedError

    @classmethod
    def std_meta_keys(cls, mime_type: str) -> t.Collection[str]:
        """
        Provides standard, expected-to-be-present meta-keys
        for content extracted from specific mime_type file,
        eg. ['header', 'content']
        """
        raise NotImplementedError

    @classmethod
    def key_desc(cls, mime_type: str, meta_key: str, lang: str) -> str:
        """
        Provides human-readable extractor plugin description in given language
        identified by ISO 639-1 code; only en language code is mandatory,
        eg. 'Header (first line)'
        """
        raise NotImplementedError

    def extract_text(self, file_path: str, mime_type: str, meta_key: str) -> t.Iterator[str]:
        """Provides iterator for extracted, unicode-text"""
        raise NotImplementedError
