class LOG:
    DEBUG = 0
    INFO = 10
    WARNING = 20
    ERROR = 30


print(LOG.__dict__["INFO"])
print(LOG.__dict__.get("UNKNOWN", LOG.DEBUG))
