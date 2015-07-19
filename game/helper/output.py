import sys


class Response(object):

    @staticmethod
    def put(string):
        """
        Helper method to make sure new line and flush is not omitted
        :param string: String to write
        """
        sys.stdout.write(string + "\n")
        sys.stdout.flush()