Given you have initialized 2 threads t1 and t2, what occurs when you run the following lines of code?
t1 and t2 run concurrently

What does the target argument to the constructor of Thread represent?
The function which the thread executes

A Semaphore instance is initialized with a value of 3. What occurs if a thread invokes release() on that semaphore.
The semaphore value increments to 4

Which of these represents a situation where you might encounter a race condition?
Two concurrent threads update a common resource

What occurs when a thread A tries to acquire a lock held by another thread B?
A waits until the lock is released by B

Which of these functions is used to make the main thread wait for a spawned thread to complete before it proceeds with its own execution?
join()

What is the effect of invoking the clear() function on an Event instance?
The internal flag is set to False

Which of these is NOT a necessary condition for a deadlock?
Priority access

What method of a Condition instance can be invoked to wake up all threads waiting on it?
notify_all()

What is the default value of a Semaphore instance in Python?
1

Which of these necessary deadlock conditions is prevented by only allowing a process to acquire one lock at a given time?
Hold and Wait

When inheriting from the multithreading.Thread class, what is the name of the function in your class which serves as the target function?
run()