### Which of these functions in the asyncio module is used to concurrently execute a set of coroutines?
gather

### What is the default number of processes created when initializing an instance of multiprocessing.Pool?
It matches the number of CPU cores on your system

### Which method of a futures instance can be used to check whether its execution is complete?
done()

### A function my_func has been defined with the async keyword before it. What is the type of object returned by invoking my_func()?
coroutine

### Which of these functions in the concurrent.futures module will iterate over futures instances and return those which have finished execution?
as_completed()

### Which of these types of tasks is multiprocessing better suited for?
CPU bound tasks

### The following call is made to an instance my_pool of type multiprocessing.Pool: my_pool.map(my_func, my_list). What is the number of tasks which will be created?
len(my_list)