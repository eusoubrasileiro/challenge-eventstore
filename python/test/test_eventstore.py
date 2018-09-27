# from python folder run like this : `python -m unittest -v test.test_eventstore`
import unittest
from threading import Lock, Thread
import random, sys
from eventstore import EventStore, Event

class TestsEventStore(unittest.TestCase):
    def test_CreateStore(self):
        locker = Lock()
        eventstore = EventStore.EventStore(locker)
        pass

    def randomEvent(self):
        """create random event"""
        return Event.Event('random', random.randint(0, sys.maxsize))

    def insertEvent(self, eventstore, event):
        eventstore.insert(event)

    def test_InsertEvent(self):
        """Insert random event from another thread"""
        lock = Lock() # main thread lock
        eventstore = EventStore.EventStore(lock)
        event = self.randomEvent()
        thread = Thread(target=self.insertEvent,
                        args=(eventstore,event))
        thread.start()
        thread.join()
        self.assertEqual(eventstore._events[0], event)

    def test_InsertEvents(self, nthreads=8):
        """Insert random events from other threads"""
        lock = Lock() # main thread lock
        eventstore = EventStore.EventStore(lock)
        events = [self.randomEvent() for i in range(nthreads)]
        threads = []
        for event in events:
            threads.append(Thread(target=self.insertEvent,
                                        args=(eventstore,event)))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        self.assertEqual(len(eventstore._events), nthreads)

    #
    # def test_iterator(self):
    #     self.assertEqual(hello_world(), 'hello world')

if __name__ == '__main__':
    unittest.main()
