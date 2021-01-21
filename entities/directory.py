import os
from abc import ABCMeta, abstractmethod

from entities.file import File


class BaseDirectory(metaclass=ABCMeta):
    @abstractmethod
    def getName(self):
        raise NotImplementedError

    @abstractmethod
    def getSize(self):
        raise NotImplementedError


class Directory(BaseDirectory):
    def __init__(self, meta_data, parent):
        self.metaData = meta_data
        self.parent = parent
        self.directories = {}
        self.files = {}

    def getName(self):
        return self.metaData.name

    def getSize(self):
        return self.metaData.size

    def getParent(self):
        return self.parent

    def getPath(self) -> str:
        """
        recursively compute the current dir path, starting from current dir till the root dir
        :return: path to current dir from root
        """
        dirStack = []
        current_dir = self
        while current_dir is not None:
            dirStack.append(current_dir.metaData.getName())
            current_dir = current_dir.getParent()

        return self.__generatePathFromDirStack(dirStack)

    def getDirectories(self):
        return self.directories

    def getFiles(self):
        return self.files

    def addDirectory(self, directory):
        self.directories[directory.getName()] = directory

    def addFile(self, file: File):
        self.files[file.getName()] = file

    @staticmethod
    def __generatePathFromDirStack(dirStack):
        path = ''
        pathSep = '/'
        root_dir = '/'
        dirStack.pop()  # removing root dir name
        if len(dirStack) > 0:
            while dirStack:
                path += pathSep + dirStack.pop()
        else:
            return root_dir
        return path
