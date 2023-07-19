from enum import Enum
from .item import FolderGenerator, FileGenerator

class FileType(Enum):
    file = 0
    folder = 1


class ItemGenerator:
    def execute(self, file_type: FileType, path: str):
        print("execute was called")
        if file_type == FileType.file:
            generator = FileGenerator()
        else:
            generator = FolderGenerator()

        result = generator.generate(path)

        if "copied" in result:
            return "copied"
        
        return result