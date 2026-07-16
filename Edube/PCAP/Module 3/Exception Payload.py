class ServerError(Exception):
    pass

try:
    raise ServerError("Timeout", 404, "Connection Lost")

except ServerError as e:
    print(len(e.args))
    print(e.args[1])
