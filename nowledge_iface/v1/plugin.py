from abc import ABC
from enum import Enum


class PluginKind(Enum):
    READER = "reader"  # extracting content out of documents
    WRITER = "writer"  # modifying documents
    READ_WRITE = "reader_writer"  # extracting and modifying documents
    CONVERTER = "converter"  # converting documents between types
    STORAGE = "storage"  # storing plugin


class NowledgePlugin(ABC):
    @classmethod
    def name(cls) -> str:
        """
        Provides short, human-readable name,
        eg. Simple Text File Descriptor
        """
        raise NotImplementedError

    @classmethod
    def ident(cls) -> str:
        """
        Provides unique extractor identifier,
        eg. 'org.example.simple-txt-file-extractor'
        """
        raise NotImplementedError

    @classmethod
    def contact(cls) -> str:
        """
        Contact string (might be public website or an email address)
        """
        raise NotImplementedError

    def setup(self):
        pass

    def close(self):
        pass

    def __enter__(self):
        return self.setup() or self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
