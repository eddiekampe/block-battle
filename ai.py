import sys

# Python translation of the Java starter implementation
# found at http://theaigames.com/competitions/ai-block-battle/getting-started

class Settings(object):

    settings = {
        "timebank": 0,
        "time_per_move": 500,
        "player_names": "player1,player2",
        "your_bot": "player1",
        "field_width": 10,
        "field_height": 20
    }

    def update(self, setting, value):
        """
        Minimalistic setting parser
        """
        if setting not in self.settings.keys():
            output("Could not parse setting {}: {}".format(setting, value))

        self.settings[setting] = value

class Bot(object):

    def __init__(self):
        self.settings = Settings()

    def run(self):
        """
        Handles the game logic
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
                    # Store game settings
                    self.settings.update(setting=parts[1], value=parts[2])

                elif command == "update":
                    # Store game updates
                    pass

                elif command == "action":
                    # Take action
                    output("drop")

            except EOFError:
                return

def output(str):
    """
    Helper method to avoid new line and flush misses
    """
    sys.stdout.write(str + "\n")
    sys.stdout.flush()

if __name__ == "__main__":

    bot = Bot()
    bot.run()