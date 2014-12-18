from twisted.internet.defer import Deferred

def callback1(result):
	print "Callback 1 said:", result
	return result

def callback2(result):
	print "Callback 2 said:", result

def callback3(result):
	raise Exception("Callback 3")

def errback1(failure):
	print "Errback 1 had an error on", failure
	return failure

def errback2(failure):
	raise Exception("Errback 2")

def errback3(failure):
	print "Errback 3 took care of", failure
	return "Everything is fine now."

d = Deferred()

# 1.
# d.addCallback(callback1)
# d.addCallback(callback2)
# d.callback("Test")

# 2.
# d.addCallback(callback1)
# d.addCallback(callback2)
# d.addCallback(callback3)
# d.callback("Test")

# 3.
# d.addCallback(callback1)
# d.addCallback(callback2)
# d.addCallback(callback3)
# d.addErrback(errback3)
# d.callback("Test")

# 4.
# d.addErrback(errback1)
# d.errback(u"Test")

# 5.
# d.addErrback(errback1)
# d.addErrback(errback3)
# d.errback(u"Test")

# 6.
# d.addErrback(errback2)
# d.errback(u"Test")

# 7. vs 3. (none vs care exception)
# d.addCallback(callback1)
# d.addCallback(callback2)
# d.addCallbacks(callback3, errback3)
# d.callback(u"Test")

# 8.
d.addCallback(callback3)
d.addCallbacks(callback2, errback3)
d.addCallbacks(callback1, errback2)
d.callback(u"Test")