from entities.commands import PrintWorkingDir, ListDir, ChangeDir, MakeDir, RemoveDir


class BaseExecutor():
    pass


class Executor(BaseExecutor):
    def __init__(self, hierarchy_manager):
        self.commands = {'pwd': PrintWorkingDir(),
                         'ls': ListDir(),
                         'cd': ChangeDir(),
                         'mkdir': MakeDir(),
                         'rm': RemoveDir()
                         }
        self.hierarchy_manager = hierarchy_manager

    @staticmethod
    def parser(command_sentence):
        command_words = command_sentence.split()
        command, flags, arguments = command_words[0], None, command_words[1:]
        return {
                'command_name': command,
                'flags': flags,
                'arguments': arguments
                }

    def execute(self, command_sentence):
        parsed_command = self.parser(command_sentence)
        command_name = parsed_command['command_name']
        if command_name in self.commands:
            command = self.commands[command_name]
            command.execute(parsed_command['arguments'], self.hierarchy_manager)
        else:
            raise Exception("Invalid Command. Allowed commands are ['pwd', 'mkdir', 'ls', 'rm', 'cd']")

