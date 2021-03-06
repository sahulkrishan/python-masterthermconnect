"""Contains all the MasterTherm Exception classes."""
class MasterThermAuthenticationError(Exception):
    """Raised when login returns wrong result."""
    def __init__(self,status,message):
        """Initialize."""
        super(MasterThermAuthenticationError,self).__init__(status)
        self.status = status
        self.message = message

class MasterThermConnectionError(Exception):
    """Raised when communication ended in error."""
    def __init__(self,status,message):
        """Initialize."""
        super(MasterThermConnectionError,self).__init__(status)
        self.status = status
        self.message = message

class MasterThermResponseFormatError(Exception):
    """Raised when page returns an unexpected response."""
    def __init__(self,status):
        """Initialize."""
        super(MasterThermResponseFormatError,self).__init__(status)
        self.status = status

class MasterThermTokenInvalid(Exception):
    """Raised when page returns the Token is not valie."""
    def __init__(self, status):
        """Initialize."""
        super(MasterThermTokenInvalid,self).__init__(status)
        self.status = status