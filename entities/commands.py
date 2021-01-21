from abc import ABCMeta, abstractmethod

from entities.directory import Directory
from entities.hierarchy_manager import HierarchyManager
from metadata.metadata import Metadata


class BaseCommand(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, arguments:  list, hierarchy_manager: HierarchyManager):
        raise NotImplementedError


class PrintWorkingDir(BaseCommand):
    def __init__(self):
        pass

    def execute(self, arguments:  list, hierarchy_manager: HierarchyManager):
        current_dir = hierarchy_manager.getCurrentDir()
        print(current_dir.get_path())


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
        Helper().validate_arguments(arguments)
        dir_name = arguments[0]
        if dir_name == '..':
            hierarchy_manager.current_dir = hierarchy_manager.current_dir.parent
        else:
            child_dirs = hierarchy_manager.current_dir.getDirectories().keys()
            if dir_name in child_dirs:
                hierarchy_manager.current_dir = hierarchy_manager.current_dir.getDirectories()[dir_name]
            else:
                raise Exception("Invalid directory")


class MakeDir(BaseCommand):
    def __init__(self):
        pass

    def execute(self, arguments:  list, hierarchy_manager: HierarchyManager):
        Helper().validate_arguments(arguments)

        dir_name = arguments[0]
        current_dir = hierarchy_manager.getCurrentDir()

        Helper().validate_duplication(dir_name, current_dir)

        metadata = Metadata(dir_name)
        directory = Directory(metadata, current_dir)
        current_dir.addDirectory(directory)


class RemoveDir(BaseCommand):
    def __init__(self):
        pass

    def execute(self, arguments:  list, hierarchy_manager: HierarchyManager):
        try:
            dir_name = arguments[0]
        except IndexError as e:
            raise e
        else:
            current_dir = hierarchy_manager.getCurrentDir()
            if dir_name in current_dir.getDirectories():
                del current_dir.getDirectories()[dir_name]
            else:
                raise Exception('Directory not found')


class Helper:
    @staticmethod
    def validate_arguments(arguments):
        if len(arguments) != 1:
            raise Exception("Not enough arguments")

    @staticmethod
    def validate_duplication(item, current_dir):
        files = current_dir.getFiles()
        if item in files:
            raise Exception('File already exists!')
        directories = current_dir.getDirectories()
        if item in directories:
            raise Exception('Directory already exists!')
