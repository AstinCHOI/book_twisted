from twisted.internet import reactor
from twisted.enterprise import adbapi

dbpool = adbapi.ConnectionPool("sqlite3", "users.db", check_same_thread=False)

def getName(email):
    return dbpool.runQuery("SELECT name FROM users WHERE email = ?", (email,))

def printResults(results):
    for elt in results:
        print elt[0]

def finish():
    dbpool.close()
    reactor.stop()

d = getName("astin@foo.com")
d.addCallback(printResults)

reactor.callLater(1, finish)
reactor.run()
