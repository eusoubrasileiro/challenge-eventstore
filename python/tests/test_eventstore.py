import unittest
from threading import Lock, Thread
import random, sys
from eventstore import EventStore, Event

class TestsEventStore(unittest.TestCase):
    def test_CreateStore(self):
        locker = Lock()
        eventstore = EventStore.EventStore(locker)

    def test_InsertEvent(self):
        """Insert a 'random' event from another thread"""
        lock = Lock() # main thread lock
        eventstore = EventStore.EventStore(lock)
        event = Event.Event('random', random.randint(0, sys.maxsize))
        thread = Thread(target=lambda store, e: store.insert(e),
                        args=(eventstore,event))
        thread.start() # start
        thread.join() # wait for them finishing
        self.assertEqual(eventstore._events[1], event) # assert was inserted

    def test_InsertEvents(self, nthreads=8):
        """Insert random events from other threads"""
        lock = Lock() # main thread lock
        eventstore = EventStore.EventStore(lock)
        # create 'random' events
        events = [Event.Event('random', random.randint(0, sys.maxsize))
                    for i in range(nthreads)]
        threads = []
        for event in events: # each thread add one random event
            threads.append(Thread(target=lambda store, e: store.insert(e),
                                        args=(eventstore, event)))
        for thread in threads: # start all threads
            thread.start()
        for thread in threads: # wait for them to finish
            thread.join()
        for event in events: # assert they were inserted
            self.assertIn(event, eventstore._events.values())

    #
    # def test_RemovebyType(self, nthreads=10):
    #     lock = Lock() # main thread lock
    #     eventstore = EventStore.EventStore(lock)
    #     # two type of events
    #     aevents = [Event('a', i) for i in range(nthreads)]
    #     bevents = [Event('b', i) for i in range(nthreads)]
    #     threads = []
    #     for event in aevents+bevents:
    #         threads.append(Thread(target=self.insertEvent,
    #                                     args=(eventstore, event)))
    #     for thread in threads:
    #         thread.start()
    #     for thread in threads:
    #         thread.join()
    #
    #     for event in events:
    #         self.assertIn(event, eventstore._events.values())

if __name__ == '__main__':
    unittest.main()
