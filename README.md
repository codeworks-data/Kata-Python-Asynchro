# Kata-Python-Asynchro
This kata is meant to help discover asynchronicity in python.

## Instructions
The idea is that we have a factory sending work to workers but they take time to do their job (not that they are lazy).
In the current implementation, the factory gives work to a worker, waits for the answer, asks another worker for another work etc.
IT takes a lot of time.
It would be better to ask all the workers to do their work and then get the results as they come.

There are more than one way to do this, check those links if you need ideas:
- https://www.python.org/dev/peps/pep-3148/ 
- https://www.python.org/dev/peps/pep-0492/

It would be a good idea to try and do this kata using different methods. 
You may find people on the internet saying one way is inherently better than another. Try and see for yourself.

## Code
In the `src/main` folder, you will find the class `Factory` that sends work to instances of the `Worker` class.

## Test it
You can test your implementation by running the `src/test/FactoryTest` and `src/test/WorkerTest` class.
At the beginning, `test_process_numbers_should_parallelize_the_work` should fail and the other tests should pass.
Your goal is to make all the tests pass but you may have to update them as the code changes.