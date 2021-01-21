from abc import ABCMeta, abstractmethod


class BaseFile(metaclass=ABCMeta):
    @abstractmethod
    def getName(self):
        raise NotImplementedError

    @abstractmethod
    def getSize(self):
        raise NotImplementedError


class File(BaseFile):
    def __init__(self, meta_data, parent):
        self.metaData = meta_data
        self.parent = parent

    def getName(self):
        return self.metaData.name

    def getSize(self):
        return self.metaData.size
