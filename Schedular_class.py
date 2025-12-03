import json                               # Import JSON module to save/load task data
import os                                 # Import OS module to check file existence
import time                               # Import time module for delays
from Task_class import Task
from Queue_class import TaskQueue
from LL_hist_class import TaskHistory
from Hash_table_class import HashTable

class Scheduler:
    # initialize the scheduler with empty queue, history, hash table and json file
    def __init__(self, json_file="tasks.json"):
        self.queue = TaskQueue()          # Create an empty task queue
        self.history = TaskHistory()      # Create an empty linked list for history
        self.hash_table = HashTable()     # Create a hash table for O(1) lookup
        self.json_file = json_file        # Save the name of the JSON file

        self.load_state()                 # Load tasks from file if it exists

    # submit a new task to the queue
    def submit_task(self, job_id, description=""):
        task = Task(job_id, description)  # Create a new Task object
        self.queue.enqueue(task)          # Add the task to the queue
        self.hash_table.insert(task)      # Insert the task into the hash table
        self.save_state()                 # Save updated state to JSON file
        print(f"\nTask Submitted:")
        print(f"  Job ID: {job_id}")
        print(f"  Description: {description}")

    # run the next task in the queue
    def run_next_task(self):
        task = self.queue.dequeue()       # Remove the next task from the queue
        if not task:                      # If no task to run, return None
            print("\nNo tasks in queue to run.")
            return None

        task.status = "done"              # Update status to mark task as completed
        self.history.add_to_history(task) # Add completed task to linked list history

        self.save_state()                 # Save changes to JSON
        print(f"\nTask Executed:")
        print(f"  Job ID: {task.job_id}")
        print(f"  Description: {task.description}")
        print(f"  Status: done")
        return task                       # Return the executed task

    # run all tasks in the queue
    def run_all(self):
        while not self.queue.is_empty():  # Loop until queue becomes empty
            self.run_next_task()          # Run and store each task in history

    # find a task by job id
    def find_job(self, job_id):
        result = self.hash_table.search(job_id)  # Use hash table to find task by ID
        if result:
            # print job id, description and status
            print(f"\nJob Found:")
            print(f"  Job ID: {result.job_id}")
            print(f"  Description: {result.description}")
            print(f"  Status: {result.status}")
        else:
            # print job id not found
            print(f"\nJob {job_id} not found.")
        return result

    # save the state of the scheduler to the json file
    def save_state(self):
        data = {
            "queue": self.queue.to_list(),    # Convert queue tasks to list of dicts
            "history": self.history.get_last_n(9999)
                                              # Save full linked list history
        }
        with open(self.json_file, "w") as f:  # Open JSON file in write mode
            json.dump(data, f, indent=4)      # Write data with pretty formatting

    # load the state of the scheduler from the json file
    def load_state(self):
        if not os.path.exists(self.json_file):  
                                              # Check if JSON file exists
            return                           # If not, skip loading

        with open(self.json_file, "r") as f:  # Open file for reading
            data = json.load(f)              # Load JSON contents as Python dict

        # -------- Load Queue --------
        # create task object and add to queue and hash table
        for t in data.get("queue", []):      # Iterate through saved queued tasks
            task = Task(t["job_id"], t["description"])
                                              # Create Task object
            task.status = t["status"]         # Restore saved status
            self.queue.enqueue(task)          # Put task back in queue
            self.hash_table.insert(task)      # Insert into hash table

        # -------- Load History --------
        # create task object and add to history and hash table
        for t in data.get("history", []):    # Iterate through saved history
            task = Task(t["job_id"], t["description"])
            task.status = t["status"]         # Status should be "done"
            self.history.add_to_history(task) # Insert into linked list
            self.hash_table.insert(task)      # Insert into hash table
    # display all tasks in queue and history
    def display_all_tasks(self):
        print("\nTASKS IN QUEUE")
        if self.queue.is_empty():
            print("No tasks in queue.")
        else:
            for task in self.queue.queue:
                # print job id and status
                print(f"Job {task.job_id} → Status: {task.status}")

        print("\nCOMPLETED TASKS (HISTORY)")
        curr = self.history.head
        if not curr:
            print("No completed tasks.")
        else:
            while curr:
                # print job id and status
                print(f"Job {curr.task.job_id} → Status: {curr.task.status}")
                curr = curr.next
    # display only history 
    def display_history_only(self):
        print("\nCOMPLETED TASKS (HISTORY)")
        # display history from linked list
        self.history.display_history()

# Main program
if __name__ == "__main__":
    scheduler = Scheduler()
    # Main loop: display menu, get user choice, execute action, wait 5 seconds
    while True:
        print("\n" + "=" * 40)
        print("Task Scheduler Menu")
        print("=" * 40)
        print("1) Submit new task")
        print("2) Run next task")
        print("3) Run all tasks")
        print("4) Display all tasks (queue + history)")
        print("5) Find job by ID")
        print("6) Display history only")
        print("0) Exit")
        # get user choice and match with case
        choice = input("\nEnter your choice: ").strip()

        match choice:
            # submit new task
            case "1":
                try:
                    job_id = int(input("Enter job ID (number): "))
                except ValueError:
                    print("Job ID must be a number.")
                    continue
                description = input("Enter description: ")
                scheduler.submit_task(job_id, description)

            # run next task
            case "2":
                scheduler.run_next_task()

            # run all tasks
            case "3":
                scheduler.run_all()

            # display all tasks
            case "4":
                scheduler.display_all_tasks()

            # find job by ID
            case "5":
                try:
                    job_id = int(input("Enter job ID to search: "))
                except ValueError:
                    print("Job ID must be a number.")
                    continue
                scheduler.find_job(job_id)

            # display history only
            case "6":
                scheduler.display_history_only()

            # exit program
            case "0":
                print("Exiting program. Bye!")
                break

            # invalid choice
            case _:
                print("Invalid choice. Please try again.")

        # Wait 5 seconds before showing the menu again (unless user chose to exit)
        print("\nReturning to menu in 5 seconds...")
        time.sleep(5)

