class ServerError(Exception):
    pass

try:
    raise ServerError("Timeout", 404, "Connection Lost")

