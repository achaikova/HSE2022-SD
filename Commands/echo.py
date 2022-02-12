from typing import List, Tuple

from optional import Optional

from Executor.context import Context


class Echo:
    """
    Return the given arguments.
    """

    def __init__(self, args: List[str]):
        """
        :param args: command arguments
        """
        self.args = args

    def execute(self, context: Context) -> int:
        """
        Return command arguments
        :returns: Tuple of command result and status code
        :rtype: int
        """
        result = " ".join(self.args)
        context.state = Optional.of(result)
        return 0

    def __str__(self):
        return f'ECHO {self.args}'

    def __eq__(self, other):
        if isinstance(other, Echo):
            return self.args == other.args
        return False
