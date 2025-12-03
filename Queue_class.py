from Task_class import Task   # Queue uses Task objects
class TaskQueue:
    def __init__(self):
        self.queue = []                   # Use a Python list to store queue elements

    # add a task to the queue
    def enqueue(self, task):
        self.queue.append(task)           # Add task to the end of the queue

    # remove a task from the queue
    def dequeue(self):
        if self.is_empty():               # Check if queue is empty before removing
            return None                   # Return None if nothing to dequeue
        return self.queue.pop(0)          # Remove and return the first element (FIFO)

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0       # Queue is empty if its length is zero

    # view the first task in the queue
    def peek(self):
        if self.is_empty():               # If queue is empty, nothing to view
            return None                   # No front element available
        return self.queue[0]              # Return the first task without removing it

    # convert the queue to a list of dictionaries
    def to_list(self):
        # Convert all tasks in the queue to dictionaries for saving to JSON
        return [task.to_dict() for task in self.queue]
