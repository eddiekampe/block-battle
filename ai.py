import sys

from game.state import State
from game.settings import Settings
from game.helper.output import Output


class Bot(object):
    """
    Bot for http://theaigames.com/competitions/ai-block-battle
    """
    def __init__(self):
        self._settings = Settings()
        self._state = State()

    def run(self):
        """
        Handle the game logic
        """
        while not sys.stdin.closed:

            try:
                raw_line = sys.stdin.readline()

                if len(raw_line) == 0:
                    continue

                line = raw_line.strip()

                parts = line.split()
                command = parts[0]

                if command == "settings":
                    self._settings.update(setting=parts[1], value=parts[2])

                elif command == "update":
                    self._state.update(obj=parts[1], state=parts[2], value=parts[3])

                elif command == "action":
                    # Take action
                    Output.write("drop")

            except EOFError:
                return


if __name__ == "__main__":

    bot = Bot()
    bot.run()