from eventstore.Event import Event

class EventIterator():
    """An iterator over an event collection tied to a EventStore class"""
    def __init__(self, eventstore, eventdict):
        self._eventstore = eventstore
        self._events = list(eventdict) # turn to a list of tuples for indexing
        self._size = len(self._events)
        self._index = -1
        self.last = False

    def moveNext(self):
        """
        move to the next event (if possible)
        """
        if self._index +1 == self.size:
            self.last = False
        else:
            self.last = True
            self._index += 1
        return self.last

    def current():
        """
        return the current event
        raise IndexError was never called  or its last result was False
        """
        if self.last == False:
            raise IndexError()
        return self._eventstore._events[self._index][1]

    def remove():
        """
        remove current event from its store
        raise IndexError was never called  or its last result was False.
        """
        if self.last == False:
            raise IndexError()
        # remove by id/key
        self._eventstore.remove(self._eventstore._events[self._index][0])
