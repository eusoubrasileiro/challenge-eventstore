## Progress Report

- [x] Understand the concept of Event Driven Programming and Event Store.
- [ ] Translate/Adapt the code to Python
- [x] How to implement multi-thread access to a method. Solution: `Lock`
- [x] Write first tests
- [x] How to keep an object iterator updated on a multithread env.?
Solution: Tried without event-handers but it seams impossible to keep the iterator synchronized.
- [ ] Write event functionallity.

Assumptions:
The event store will be instantiate in main thread. Its *lock* will be passed to the worker-threads (clients).
Every time someone uses the insert method it will need to get the lock
of the main thread.
w
