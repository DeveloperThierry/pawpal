from datetime import timedelta
from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Task:
    description: str
    scheduled_time: datetime
    priority: int = 2  
    duration_mins: int = 30
    is_completed: bool = False
    frequency: str = "none"

    def mark_complete(self):
        self.is_completed = True


    def complete_and_reschedule(self):
        self.is_completed = True
        if self.frequency == "daily":
            new_time = self.scheduled_time + timedelta(days=1)
            return Task(
                description=self.description, 
                scheduled_time=new_time, 
                priority=self.priority, 
                duration_mins=self.duration_mins,
                frequency=self.frequency
            )
        return None

    

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def get_all_tasks(self) -> List[Task]:
        """Flattens all tasks from all pets into a single list."""
        return [task for pet in self.pets for task in pet.tasks]

class Scheduler:
    @staticmethod
    def get_daily_plan(owner: Owner):
        """Retrieves and sorts all tasks by time and priority."""
        all_tasks = owner.get_all_tasks()
        # Sort logic: Primary sort by time, secondary by priority
        return sorted(all_tasks, key=lambda t: (t.scheduled_time, t.priority))
    
    # In pawpal_system.py inside your Scheduler class
    @staticmethod
    def sort_tasks(tasks: List[Task]):
        """
        Sorts tasks primarily by time, and secondarily by priority.
        Priority 1 (High) comes before Priority 3 (Low).
        """
        return sorted(tasks, key=lambda t: (t.scheduled_time, t.priority))

    def get_conflicts(tasks: List[Task]):
        conflicts = []
        # Sort by time first to compare neighbors
        sorted_tasks = sorted(tasks, key=lambda t: t.scheduled_time)
        
        for i in range(len(sorted_tasks) - 1):
            current_t = sorted_tasks[i]
            next_t = sorted_tasks[i+1]
            
            # Check if they are within 30 minutes of each other
            if next_t.scheduled_time - current_t.scheduled_time < timedelta(minutes=30):
                conflicts.append(f"⚠️ Conflict: '{current_t.description}' and '{next_t.description}' are too close!")
                
        return conflicts