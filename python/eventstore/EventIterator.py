from eventstore.Event import Event

class EventIterator():
    """An iterator over an event collection tied to a eventstore"""
    def __init__(self, eventstore, eventdict):
        self._eventstore = eventstore
        self._events = list(eventdict) # turn to a list for indexing
        self._size = len(self._events)
        self._index = 0

    def _parentUpdated(self):
        """eventstore was updated"""
        # search

    def moveNext(self):
        """move to the next event (if possible)"""
        if self._index +1 == self.size:
            self.last = False
        else:
            self.last = True
            self._index += 1
        return self.last

    def current():
        """return the current event"""
        return self._eventstore._events[self._index]

    def remove():
        """
        remove current event from its store
        raise IndexError (if not possible)
        """

        self._eventstore.
