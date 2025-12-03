from Task_class import Task   # Hash table stores Task objects
class HashTable:
    def __init__(self, size=10):
        self.size = size                  # Number of buckets in hash table
        # Create list of lists for chaining (collision handling)
        self.table = [[] for _ in range(size)]
                                          

    # hash the job id to get the bucket index
    def hash(self, job_id):
        return job_id % self.size         # Simple hash function: remainder of division

    # insert a task into the hash table
    def insert(self, task):
        index = self.hash(task.job_id)    # Compute bucket index for this task
        for t in self.table[index]:       # Check existing tasks in this bucket
            if t.job_id == task.job_id:   # If task already exists, do nothing
                return
        self.table[index].append(task)    # Insert task into the bucket list

    # search for a task by job id
    def search(self, job_id):
        index = self.hash(job_id)         # Compute the correct bucket
        for t in self.table[index]:       # Iterate over tasks in the bucket
            if t.job_id == job_id:        # If found, return the task object
                return t
        return None                       # Return None if not found

    # remove a task by job id
    def remove(self, job_id):
        index = self.hash(job_id)         # Compute bucket index
        for t in self.table[index]:       # Iterate over bucket elements
            if t.job_id == job_id:        # Find matching task
                self.table[index].remove(t)  
                                           # Remove task from list
                return True               # Indicate successful removal
        return False                      # Task not found
