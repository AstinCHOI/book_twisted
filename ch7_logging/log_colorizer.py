#-*- coding: utf-8 -*-
import sys

from twisted.python.log import FileLogObserver

class ColorizedLogObserver(FileLogObserver):
    def emit(self, eventDict):
        # Set text color
        self.write("\033[0m")

        if eventDict["isError"]:
            # ANSI escape sequence : red text color
            self.write("\033[91m")
            FileLogObserver.emit(self, eventDict)

    def Logger():
        return ColorizedLogObserver(sys.stdout).emit
