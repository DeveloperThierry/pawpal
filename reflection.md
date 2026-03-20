# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
The UML design has Entity Name, Attributes, Relationships and Methods.
- What classes did you include, and what responsibilities did you assign to each?
I included classes for Owner, Pet, Task, Scheduler. The owner has pets. Tasks are descriptive, has priority, and specified duration.

**b. Design changes**

- Did your design change during implementation?
It did not change much except for a few minor specification such as setting the priority to medium.
- If yes, describe at least one change and why you made it.
The change is just to ensure that the priority is set to medium.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
The scheduler heavily considers both. Priority is measured using integers 3 being the lowest and 1 the highest.
- How did you decide which constraints mattered most?
IN the real world it is important that tasks are carried out in a datatime order because of the biology and convenience.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
The scheduler checks for conflicts based on start time then duration for overlaps.
- Why is that tradeoff reasonable for this scenario?
It is reasonable because in the real world people maybe able to multitask but it would require too much mathematical complexity therefore, this way is more practical for the project.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I mainly used ai to guide me through the code logic and debug errors that occcurred
- What kinds of prompts or questions were most helpful?
The most helpful were the debugging prompts because they offered multiple soltuions to resolve conflicts

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
I did not accept when it offered to change code that was working properly beforehand.
- How did you evaluate or verify what the AI suggested?
I would rerun the streamlit application right after making a change to ensure the incremental changes made a difference.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
I tested the conflict case where two tasks occur at the same time.
- Why were these tests important?
This is important because in these cases, I would prefer the case with the higher priority to win

**b. Confidence**

- How confident are you that your scheduler works correctly?
I would state that I am confident it works
- What edge cases would you test next if you had more time?
Something that would be cool to test are difference timezones.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I would say that I am glad the code is working and runs.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I would have liked to work with data and large datasets in the future.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
I can confidently say this lesson enhanced my understanding of OOP in Python