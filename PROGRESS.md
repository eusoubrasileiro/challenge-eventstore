## Progress Report  

- [x] Understand the concept of Event Driven Programming and Event Store.  
- [x] Translate/Adapt the code to Python  
- [x] How to implement multi-thread access to a method. Solution: `Lock`  
- [x] Write first tests  
- [x] How to keep an object iterator updated on a multi-thread environment?
Solution: Tried without event-handers but it seams impossible to keep the iterator synchronized.  
- [x] Write event functionality.  
- [x] Remove event functionality due 2.  

Assumptions:  
 1. The event store will be instantiate in main thread. Its *lock* will be passed to the worker-threads (clients). Every time someone uses the insert method it will need to lock the main thread.  
 2. There is no definition about the expected behavior of the `Iterator` when data is inserted or removed on the source `EventStore`. Nothing is said about updating it.  

## About design choices  

- `EventStore` was implemented using a python-dictionary `dict` for its simplicity, key index capability and reasons below.  
- Used python `threading` module for multi-threading for simplicity. It's widely known that 'real' multi-thread in Python is only possible through the `multiprocessing` module due the Global Interpreter Lock (GIL) limitations. Despite of that the code can be easily ported due `list` and `dict` being supported by the `multiprocessing.Manager` class. This class can be used to exchange/update data between processes.  
- Code can be better optimized by, some ideas:  
  - Choosing appropriately when to lock or release the thread owning the `EventStore`.  
  - Maintaining the `EventStore`events dictionary sorted and making sorted insertions.  

## About Tests  

- From python folder run like this : `python -m unittest -v tests/test_eventstore.py`  
- All tests written somehow show that the code is thread-safe.
- Could write more tests for `Iterator`, started didn't finish.
