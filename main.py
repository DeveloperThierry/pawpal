from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime

me = Owner("Alex")
luna = Pet("Luna", "Cat")
me.pets.append(luna)

luna.add_task(Task("Morning Kibble", datetime(2024, 5, 20, 8, 0), priority=1))
luna.add_task(Task("Laser Pointer Play", datetime(2024, 5, 20, 18, 0), priority=3))

plan = Scheduler.get_daily_plan(me)

print(f"--- {me.name}'s Daily Plan ---")
for t in plan:
    status = "✅" if t.is_completed else "⏳"
    print(f"{t.scheduled_time.strftime('%H:%M')} | {t.description} ({status})")

