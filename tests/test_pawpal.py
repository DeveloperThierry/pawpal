import pytest
from datetime import datetime, timedelta
from pawpal_system import Task, Pet, Scheduler, Owner

def test_chronological_sorting():
    """Verify tasks are returned in time order, not insertion order."""
    pet = Pet("Luna", "Cat")
    t1 = Task("Evening Snack", datetime(2026, 3, 20, 20, 0))
    t2 = Task("Morning Breakfast", datetime(2026, 3, 20, 8, 0))
    pet.add_task(t1)
    pet.add_task(t2)
    
    owner = Owner("Jordan", pets=[pet])
    plan = Scheduler.get_daily_plan(owner)
    
    assert plan[0].description == "Morning Breakfast"
    assert plan[1].description == "Evening Snack"

def test_daily_recurrence_logic():
    """Confirm a new task is generated for +1 day."""
    task = Task("Walk", datetime(2026, 3, 20, 10, 0), frequency="daily")
    new_task = task.complete_and_reschedule()
    
    assert task.is_completed is True
    assert new_task is not None
    assert new_task.scheduled_time == task.scheduled_time + timedelta(days=1)
    assert new_task.is_completed is False

def test_conflict_detection_flagging():
    """Verify the scheduler catches identical times."""
    t1 = Task("Meds", datetime(2026, 3, 20, 9, 0))
    t2 = Task("Food", datetime(2026, 3, 20, 9, 0))
    
    conflicts = Scheduler.get_conflicts([t1, t2])
    assert len(conflicts) > 0
    assert "Conflict" in conflicts[0]

def test_task_completion():
    """Verify that mark_complete updates the status."""
    task = Task("Walk", datetime.now())
    assert task.is_completed is False
    task.mark_complete()
    assert task.is_completed is True

def test_add_task_to_pet():
    """Verify that tasks are successfully added to a pet's list."""
    pet = Pet("Buddy", "Dog")
    initial_count = len(pet.tasks)
    pet.add_task(Task("Vet Visit", datetime.now()))
    assert len(pet.tasks) == initial_count + 1
