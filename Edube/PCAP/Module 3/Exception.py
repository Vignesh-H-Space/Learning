
class HardwareError(Exception): 
    pass

class KeyboardError(HardwareError): 
    pass

try:
    
    raise KeyboardError()
    
except HardwareError:
    print("Caught a Hardware Error!")
except KeyboardError:
    print("Caught a Keyboard Error!")