from eventstore.Event import Event

class EventStore(object):
    """
    Store event objects on a python list
    """
    def __init__(self, threadLock):
        self._lock = threadLock # main thread locker
        self._events = {} # dictionary
        self._id_count = 1 # first id

    def insert(self, event):
        """insert event object on the list"""
        self._lock.acquire()
        self._events.update({self._id_count : event}) # id, event pair
        self._id_count += 1
        self._lock.release()

    def removeAll(self, type):
        """Remove all events of specified type"""
        self._lock.acquire()
        for id, event in self._events.items():
            if event.type == type:
                del self._events[id]
        self._lock.release()

    def remove(self, id):
        """remove specified event by id from eventstore"""
        self._lock.acquire()
        if id in self._events:
            del self._events[id]
        self._lock.release()

    def query(self, type, startTime, endTime):
        """"Retrieves an iterator for events based on their type and timestamp."""
        self._lock.acquire()
        events = self._events.copy() # dont need to search with a lock
        self._lock.release()
        sorted_events = sorted(events.items(), key=lambda kv: kv[1].timestamp())
        query = {k: v for k, v in sorted_events.items()
                    if v.type == type and
                        (v.timestamp() >= startTime and v.timestamp() < endTime)}
        return query
