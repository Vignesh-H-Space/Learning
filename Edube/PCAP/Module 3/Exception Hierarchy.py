class NetworkError(Exception):
    pass

class TimeoutError(NetworkError):
    pass

try:
    raise TimeoutError("Connection timed out!")

except NetworkError:
    print("Caught a General Network Error!")
    
except TimeoutError:
    print("Caught a specific Timeout Error!")