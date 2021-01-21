from entities.executor import Executor
from entities.hierarchy_manager import HierarchyManager


class Driver():
    def __init__(self):
        self.hierarchy_manager = HierarchyManager()
        self.executor = Executor(self.hierarchy_manager)

    def reset(self):
        self.hierarchy_manager = HierarchyManager()
        self.executor = Executor(self.hierarchy_manager)


if __name__ == '__main__':
    driver = Driver()

    while True:
        command_sentence = input("Enter Command: ")
        if len(command_sentence) < 1:
            print("No input given. Try again!")
            continue
        driver.executor.execute(command_sentence)
