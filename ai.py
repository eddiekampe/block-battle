import sys
import fileinput

# Python translation of the Java starter implementation
# found at http://theaigames.com/competitions/ai-block-battle/getting-started

class Bot(object):


    def __init__(self):
        pass

    def run(self):
        """
        Handles the game logic
        """
        for line in fileinput.input():

            if len(line) == 0:
                continue

            parts = line.split(" ")
            command = parts[0]

            if command == "settings":
                # Store game settings
                break

            elif command == "update":
                # Store game updates
                break

            elif command == "action":
                # Take action
                print "Drop"
                sys.stdout.flush()



if __name__ == "__main__":


    bot = Bot()
    bot.run()
