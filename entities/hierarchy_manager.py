from abc import ABCMeta, abstractmethod

from entities.directory import Directory
from metadata.metadata import Metadata


class BaseHierarchyManager(metaclass=ABCMeta):
    @abstractmethod
    def getCurrentDir(self):
        raise NotImplementedError


class HierarchyManager(BaseHierarchyManager):
    def __init__(self):
        root_meta_data = Metadata('/')
        self.root_dir = Directory(root_meta_data, None)
        # self.root_dir.parent = None
        self.current_dir = self.root_dir

    def getCurrentDir(self) -> Directory:
        '''
        :return: current dir object
        '''
        return self.current_dir

    def updateCurrentDir(self, directory):
        self.current_dir = directory

    def getRootDir(self):
        return self.root_dir
