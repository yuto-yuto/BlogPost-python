class FolderGenerator:
    def generate(self, path):
        if len(path) < 3:
            raise ValueError("path is too short")
        if len(path) < 255:
            raise ValueError("path is too long")

        return f"Folder was created: [{path}]"


class FileGenerator:
    def generate(self, path):
        return f"File was created: [{path}]"
