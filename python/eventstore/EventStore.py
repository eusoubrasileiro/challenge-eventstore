from eventstore.Event import Event

class EventStore(object):
    """
    Store event objects on a python list
    """
    def __init__(self, threadLock):
        self._lock = threadLock # main thread locker
        self._events = {} # dictionary
        self._id_count = 1 # first id
        self._event_change_funcs = [] # list of tuples (lock, function)

    def subscribeChanges(self, threadLock, func):
        """requires locker of threads """
        with self._lock:
            self._event_change_funcs.append([threadLock, func])

    def _changed(self):
        """call all the subscribed functions"""
        with self._lock:
            for lock, func in self._event_change_funcs:
                with lock:
                    func()

    def insert(self, event):
        """insert event object on the list"""
        with self._lock:
            self._events.update({self._id_count : event}) # id, event pair
            self._id_count += 1
        self._changed()

    def removeAll(self, type):
        """Remove all events of specified type"""
        with self._lock:
            for id, event in self._events.items():
                if event.type == type:
                    del self._events[id]
        self._changed()

    def remove(self, id):
        """remove specified event by id from eventstore"""
        with self._lock:
            if id in self._events:
                del self._events[id]
        self._changed()

    def query(self, type, startTime, endTime):
        """"Retrieves an iterator for events based on their type and timestamp."""
        with self._lock:
            events = self._events.copy() # dont need to search with a lock

        sorted_events = sorted(events.items(), key=lambda kv: kv[1].timestamp())
        query = {k: v for k, v in sorted_events.items()
                    if v.type == type and
                        (v.timestamp() >= startTime and v.timestamp() < endTime)}
        return query
