import os
from abc import ABCMeta, abstractmethod

from entities.file import File


class BaseDirectory(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abstractmethod
    def get_size(self):
        raise NotImplementedError


class Directory(BaseDirectory):
    def __init__(self, meta_data, parent):
        self.metaData = meta_data
        self.parent = parent
        self.directories = {}
        self.files = {}

    def get_name(self):
        return self.metaData.name

    def get_size(self):
        return self.metaData.size

    def get_parent(self):
        return self.parent

    def get_path(self) -> str:
        """
        recursively compute the current dir path, starting from current dir till the root dir
        :return: path to current dir from root
        """
        dir_stack = []
        current_dir = self
        while current_dir is not None:
            dir_stack.append(current_dir.metaData.getName())
            current_dir = current_dir.getParent()

        return self.__generatePathFromDirStack(dir_stack)

    def getDirectories(self):
        return self.directories

    def getFiles(self):
        return self.files

    def addDirectory(self, directory):
        self.directories[directory.getName()] = directory

    def addFile(self, file: File):
        self.files[file.getName()] = file

    @staticmethod
    def __generatePathFromDirStack(dir_stack):
        path = ''
        path_sep = '/'
        root_dir = '/'
        dir_stack.pop()  # removing root dir name
        if len(dir_stack) > 0:
            while dir_stack:
                path += path_sep + dir_stack.pop()
        else:
            return root_dir
        return path
