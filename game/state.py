from game.field.field import Field
from game.helper.output import Output


class GameState(object):

    _state = {
        "round": 0,
        "this_piece_type": "",
        "next_piece_type": "",
        "this_piece_position": "0,0"
    }

    def update(self, state, value):

        if state not in self._state.keys():
            Output.write("Could not parse GameState {}: {}".format(state, value))

        Output.debug("GameState - {}: {}".format(state, value))
        self._state[state] = value

    @property
    def piece_position(self):
        return tuple(self._state["this_piece_position"].split(","))


class PlayerState(object):

    _state = {
        "row_points": 0,
        "combo": 0,
        "field": "",
    }

    def __init__(self, name):
        self._name = name

    def update(self, state, value):

        if state not in self._state.keys():
            Output.write("Could not parse PlayerState {} - {}: {}".format(self._name, state, value))

        if state == "field":

            Output.debug(self._name)
            self._state[state] = Field(value)

        else:
            Output.debug("PlayerState {} - {}: {}".format(self._name, state, value))
            self._state[state] = value


class State(object):

    _game_state = GameState()
    _player_state = {
        "player1": PlayerState("player1"),
        "player2": PlayerState("player2")
    }

    def update(self, obj, state, value):
        """
        Minimalistic state parser
        """
        if obj in ["player1", "player2"]:
            self._player_state[obj].update(state, value)
        elif obj == "game":
            self._game_state.update(state, value)