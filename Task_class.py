# Task class to represent a task in the scheduler
class Task:
    def __init__(self, job_id, description=""):
        self.job_id = job_id              # Store the unique job ID of the task
        self.description = description    # Store text describing what the task does
        self.status = "in_queue"          # Initial status: task is waiting in the queue

    # convert the task to a dictionary
    def to_dict(self):
        # Convert the Task object into a dictionary for saving in JSON files
        return {
            "job_id": self.job_id,        # Include job ID in dictionary
            "description": self.description,  # Include description
            "status": self.status         # Include current status (in_queue or done)
        }
