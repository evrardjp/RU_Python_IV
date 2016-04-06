#!/usr/bin/env python
# *-* coding:utf-8 *-*

"""

:mod:`lab_multi` -- Investigate multiprocessing / multithreading
=========================================

LAB_multi Learning Objective: Learn to use the multiprocessing and multithreading modules
                              to perform parallel tasks.
::

 a. Write a command line parser that accepts the following args:
    -p --process : use multiprocessing
    -t --thread  : use threading
    -w --workers : number of workers to spawn
    -i --items   : number of work items to process

 b. In the main process, create a Queue for all the workers to use for their input work items,
    and a Queue for the workers to use to send their processed items back.  Make sure to share
    the Queue with the workers when they are created.

 c. Write a worker function.  The workers should take items from the Queue, process them,
    and put the results in the output queue.

 d. Write a function called create_workers() that creates the workers based on the
    multiprocessing or threading module as requested by the command line arguments.

 e. Write the main loop to process command line args, create the Queues, build the workers,
    start the workers, generate the work tasks, feed the work tasks to the workers, and print the
    results coming back in the results Queue.

Note: add args as necessary to the skeleton functions below
"""

# Don't change this function


def work_task(item):
    """This is the work to be done on each input item"""
    def is_prime(num):
        for j in xrange(2, num):
            if (num % j) == 0:
                return False
        return True

    index = 0
    check = 0
    while index < item:
        check += 1
        if is_prime(check):
            index += 1
    return check


# Don't change this function
def generate_work(num_items):
    import random
    return [random.randint(1, 2000) for x in xrange(num_items)]

# Add your code down here


def worker():
    """This is the thread/process main function that will implement c. above"""
    pass


def create_workers():
    """This function creates workers of the requested type and wires them into the queues,
    per step d. above"""
    pass

if __name__ == "__main__":
    pass
