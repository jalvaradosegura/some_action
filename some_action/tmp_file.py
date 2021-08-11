import os
import shutil


class TempFile:
    def __init__(self, folder: str, filename: str, content: str = 'Hello!'):
        self.folder = folder
        self.name = filename
        self.content = content

    def __enter__(self):
        os.mkdir(self.folder)
        with open(f'{self.folder}/{self.name}', 'w') as file:
            file.write(self.content)
        self.file = open(f'{self.folder}/{self.name}', 'r')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.file:
            self.file.close()
        shutil.rmtree(self.folder)
