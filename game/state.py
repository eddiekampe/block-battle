from game.helper.output import Response


class State(object):

    _state = {
        "round": 0,
        "this_piece_type": "",
        "next_piece_type": "",
        "this_piece_position": "0,0"
    }

    def update(self, state, value):
        """
        Minimalistic state parser
        """
        if state not in self._state.keys():
            Response.put("Could not parse state {}: {}".format(state, value))

        self._state[state] = value

    def get_piece_position(self):
        return tuple(self._state["this_piece_position"].split(","))