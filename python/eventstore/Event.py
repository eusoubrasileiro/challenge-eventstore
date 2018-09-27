#  This is just an event stub, feel free to expand it if needed.
class Event(object):
    def __init__(self, type, timestamp):
        self._type = type
        self._timestamp = timestamp

    def type(self):
        return self._type

    def timestamp(self):
        return self._timestamp
