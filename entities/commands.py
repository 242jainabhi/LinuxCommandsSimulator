from abc import ABCMeta, abstractmethod

from entities.directory import Directory
from entities.hierarchy_manager import HierarchyManager
from entities.metadata import Metadata


class BaseCommand(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, arguments:  list, hierarchy_manager: HierarchyManager):
        raise NotImplementedError


class PrintWorkingDir(BaseCommand):
    def __init__(self):
        pass

    def execute(self, arguments:  list, hierarchy_manager: HierarchyManager):
        current_dir = hierarchy_manager.getCurrentDir()
        print(current_dir.getPath())


class ListDir(BaseCommand):
    def __init__(self):
        pass

    def execute(self, arguments:  list, hierarchy_manager: HierarchyManager):
        current_dir = hierarchy_manager.getCurrentDir()
        directory_content = list(current_dir.getDirectories().keys()) + list(current_dir.getFiles().keys())
        for i in directory_content:
            print(i, end=' ')
        print()


class ChangeDir(BaseCommand):
    def __init__(self):
        pass

    def execute(self, arguments:  list, hierarchy_manager: HierarchyManager):
        Helper().validateArguments(arguments)
        dirName = arguments[0]
        if dirName == '..':
            hierarchy_manager.current_dir = hierarchy_manager.current_dir.parent
        else:
            childDirs = hierarchy_manager.current_dir.getDirectories().keys()
            if dirName in childDirs:
                hierarchy_manager.current_dir = hierarchy_manager.current_dir.getDirectories()[dirName]
            else:
                raise Exception


class MakeDir(BaseCommand):
    def __init__(self):
        pass

    def execute(self, arguments:  list, hierarchy_manager: HierarchyManager):
        Helper().validateArguments(arguments)

        dirName = arguments[0]
        current_dir = hierarchy_manager.getCurrentDir()

        Helper().validate_duplication(dirName, current_dir)

        metadata = Metadata(dirName)
        directory = Directory(metadata, current_dir)
        current_dir.addDirectory(directory)

class RemoveDir(BaseCommand):
    def __init__(self):
        pass

    def execute(self, arguments:  list, hierarchy_manager: HierarchyManager):
        dirName = arguments[0]
        current_dir = hierarchy_manager.getCurrentDir()
        if dirName in current_dir.getDirectories():
            del current_dir.getDirectories()[dirName]
        else:
            raise Exception


class Helper:
    def validateArguments(self, arguments):
        if len(arguments) != 1:
            raise Exception

    def validate_duplication(self, item, current_dir):
        files = current_dir.getFiles()
        if item in files:
            raise Exception
        directories = current_dir.getDirectories()
        if item in directories:
            raise Exception
