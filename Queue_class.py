from Task_class import Task   # Queue uses Task objects

class QueueNode:
    # initialize the queue node with a task and a pointer to the next node
    def __init__(self, task):
        self.task = task                  # Store the task object inside the node
        self.next = None                  # Pointer to the next node (initially None)

class TaskQueue:
    def __init__(self):
        self.head = None                  # Pointer to the first node (front of queue)
        self.tail = None                  # Pointer to the last node (back of queue)

    # add a task to the queue
    def enqueue(self, task):
        node = QueueNode(task)            # Create a new node containing the task
        if self.is_empty():               # If queue is empty
            self.head = node              # Set both head and tail to the new node
            self.tail = node
        else:
            self.tail.next = node         # Link the new node to the end of the queue
            self.tail = node              # Update tail to point to the new node

    # remove a task from the queue
    def dequeue(self):
        if self.is_empty():               # Check if queue is empty before removing
            return None                   # Return None if nothing to dequeue
        task = self.head.task             # Get the task from the front node
        self.head = self.head.next        # Move head to the next node
        if self.head is None:             # If queue becomes empty
            self.tail = None              # Update tail to None as well
        return task                       # Return the dequeued task (FIFO)

    # check if the queue is empty
    def is_empty(self):
        return self.head is None          # Queue is empty if head is None

    # view the first task in the queue
    def peek(self):
        if self.is_empty():               # If queue is empty, nothing to view
            return None                   # No front element available
        return self.head.task             # Return the first task without removing it

    # convert the queue to a list of dictionaries
    def to_list(self):
        # Convert all tasks in the queue to dictionaries for saving to JSON
        result = []
        curr = self.head                  # Start from the head of the linked list
        while curr:                       # Loop until we reach the end of the list
            result.append(curr.task.to_dict())  # Add task data as dictionary
            curr = curr.next              # Move to the next node
        return result                     # Return list of all tasks in queue

    # make the queue iterable (for use in for loops)
    def __iter__(self):
        curr = self.head                  # Start from the head of the linked list
        while curr:                       # Loop until we reach the end of the list
            yield curr.task               # Yield each task
            curr = curr.next              # Move to the next node
