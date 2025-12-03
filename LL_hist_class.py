from Task_class import Task   # History nodes store Task objects
class HistoryNode:
    # initialize the history node with a task and a pointer to the next node
    def __init__(self, task):
        self.task = task                  # Store the task object inside the node
        self.next = None                  # Pointer to the next node (initially None)


class TaskHistory:
    # initialize the history with a head pointer to the first node
    def __init__(self):
        self.head = None                  # Start with an empty linked list (no history yet)

    # add a task to the history
    def add_to_history(self, task):
        node = HistoryNode(task)          # Create a new node containing the completed task
        node.next = self.head             # Point the new node to the current head
        self.head = node                  # Update head to be the new node

    # display the history
    def display_history(self):
        curr = self.head                  # Start at the head of the linked list
        while curr:                       # Loop until we reach the end of the list
            # print job id and status
            print(f"Job {curr.task.job_id} → {curr.task.status}")  
            curr = curr.next              # Move to the next node

    # get the last N tasks from the history
    def get_last_n(self, n):
        result = []                       # List to store last N history tasks
        curr = self.head                  # Start from the head of the list
        while curr and len(result) < n:   # Continue until we collected N items or reached end
            result.append(curr.task.to_dict())  
                                           # Add task data as dictionary
            curr = curr.next              # Move to the next node
        return result                     # Return list of last N tasks
