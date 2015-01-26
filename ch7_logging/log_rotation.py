from twisted.python import log, logfile

# logging every 100 bytes during rotating
# will write at /tmp/test.log ... test.log.N

f = logfile.LogFile("test.log", "/tmp", rotateLength=100)
log.startLogging(f)

log.msg("First message")

# rotate manually
f.rotate()

for i in range(5):
    log.msg("Test message", i)

log.msg("Last message")
