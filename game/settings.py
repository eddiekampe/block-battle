from game.helper.output import Output


class Settings(object):

    _settings = {
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
        if setting not in self._settings.keys():
            Output.write("Could not parse setting {}: {}".format(setting, value))

        Output.debug("Setting \"{}\": {}".format(setting, value))
        self._settings[setting] = value
