import os
import sys


class Output(object):

    @staticmethod
    def write(string):
        """
        Helper method to make sure new line and flush is not omitted
        :param string: String to write
        """
        sys.stdout.write(string + "\n")
        sys.stdout.flush()

    @staticmethod
    def debug(string):

        if os.getenv("DEBUG", default=False):
            print string