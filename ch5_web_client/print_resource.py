from twisted.internet import reactor
from twisted.web.client import getPage
import sys


def printPage(result):
    print result

def printError(failure):
    print >>sys.stderr, failure

def stop(result):
    reactor.stop()


if len(sys.argv) != 2:
    print >>sys.stderr, "Usage: python print_resource.py <URL>"
    exit(1)

# POST example: getPage(sys.argv[1], method='POST', postdata="My test data")
# and you can add cookie, redirect, user-agent with request in getPage()
d = getPage(sys.argv[1])
d.addCallbacks(printPage, printError)
d.addBoth(stop)

reactor.run()
