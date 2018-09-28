from eventstore.Event import Event
from eventstore.EventIterator import EventIterator

class EventStore():
    """
    Storage of Event.Event objectsself.
    Use a python dictionary with an integer id as a key"""
    def __init__(self, threadLock):
        self._lock = threadLock # event store thread locker
        self._events = {} # dictionary
        self._id_count = 1 # first id

    def insert(self, event):
        """insert event object on the list"""
        with self._lock:
            self._events.update({self._id_count : event}) # id, event pair
            self._id_count += 1 # increasing ids

    def removeAll(self, type):
        """Remove all events of specified type"""
        with self._lock:
            for id, event in self._events.items():
                if event.type == type:
                    del self._events[id]

    def remove(self, id):
        """remove specified event by id from eventstore"""
        with self._lock:
            if id in self._events:
                del self._events[id]

    def query(self, type, startTime, endTime):
        """"Retrieves an iterator for events based on their type and timestamp."""
        with self._lock:
            events = self._events.copy() # dont need to search with a lock
        # sort dictionary and select desired range
        sorted_events = sorted(events.items(), key=lambda kv: kv[1].timestamp())
        query = {k: v for k, v in sorted_events.items()
                    if v.type == type and
                    (v.timestamp() >= startTime and v.timestamp() < endTime)}
        return EventIterator(self, query)
