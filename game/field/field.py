from game.helper.output import Output


class Field(object):

    def __init__(self, field_string):

        self._parse(field_string)
        self._print_matrix()

    def _parse(self, field_string):

        rows = field_string.split(";")
        columns = rows[-1].split(",")

        height = len(rows)
        width = len(columns)

        self.grid = [[0] * width for _ in range(height)]

        rows = field_string.split(";")

        for i in range(height):
            cells = rows[i].split(",")
            for j in range(width):
                self.grid[i][j] = cells[j]

    def _print_matrix(self):

        Output.debug("#" * 50)

        for columns in self.grid:
            Output.debug(columns)

        Output.debug("#" * 50)