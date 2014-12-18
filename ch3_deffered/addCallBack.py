from twisted.internet.defer import Deferred

# 1.
# def myCallback(result):
# 	print result

# d = Deferred()
# d.addCallback(myCallback)
# d.callback("Trigering callback.")

# 2.
# def myErrback(failure):
# 	print failure

# d = Deferred()
# d.addErrback(myErrback)
# d.errback(u"Trigering errback.")

# 3.
def addBold(result):
	return "<b>%s</b>" % (result,)


def addItalic(result):
	return "<i>%s</i>" % (result,)


def printHTML(result):
	print result

d = Deferred()
d.addCallback(addBold)
d.addCallback(addItalic)
d.addCallback(printHTML)
d.callback("Hello World")