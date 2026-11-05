# Lab 2 — Reflection

**Project:** Book Club Reading Challenge & Discussion Portal (Problem #55)
**Student:** Keshav Agrawal (PES1UG24CS719)
**Backlog:** 3 Epics, 13 User Stories, 47 story points · **Sprint 1:** 22 pts · **Sprint 2:** 25 pts (1 week each)

**1. Did your estimations reflect the actual effort?**

Mostly. Small, well-understood stories such as *Nominate a Book* (2 pts) and *Set Personal Reading Goal* (2 pts) were straightforward, and their low estimates held. The stories with the most uncertainty were the ones that got higher points: *Spoiler-Tag a Comment* (5) because spoilers must also be hidden from previews, notifications and search, *Cast One Vote Per Poll* (5) because duplicate votes must be blocked, and *Live Vote Tally* (8) because of the real-time requirement in NFR-001. Using the Fibonacci scale forced a clear jump between "simple" (2–3) and "complex/uncertain" (5–8) work instead of arguing over 4 vs 5. In a real team, *Live Vote Tally* is the story most likely to have been under-estimated and could be split further.

**2. Was your backlog well-prioritised?**

Yes. Priorities were set by user impact. Logging progress, protecting members from spoilers and fair one-person-one-vote polling are the core of the portal and were marked **High**. Discussion threads, nominations and mobile polish were **Medium**, and the lead's nomination review queue was **Low** because the lead can manage without it at first. The order also respected dependencies: chapter threads (2.1, 2.2) came before spoiler tagging (2.3, 2.4), and nominations (3.1) came before polls and voting (3.3, 3.4).

**3. How did your simulated sprint align with your plan?**

Each sprint had a single goal and a similar load (22 and 25 points), and all committed stories were moved To Do → In Progress → Done and the sprint completed, so both sprints met their goals. Because the sprint was simulated within one lab session, stories were completed in bursts rather than steadily across a full week. A real sprint would spread this work over the week.

**4. What insights did the burndown chart give about your team's capacity?**

The burndown chart shows remaining story points against the ideal guideline. Because the work was moved to Done in a short burst, the red line stays flat and then drops sharply, which the handout lists as a sign of work not being completed steadily. In a real sprint, finishing all 22–25 points would suggest a velocity of roughly 22–25 points per week, which would be the starting capacity for Sprint 3. If the team consistently finished early, it should commit to more points. If the line stayed above the guideline, it should commit to fewer or split the large stories such as *Live Vote Tally*.
