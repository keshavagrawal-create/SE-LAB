# Lab 2 — Reflection

**Project:** Book Club Reading Challenge & Discussion Portal (Problem #55)
**Student:** Keshav Agrawal (PES1UG24CS719)
**Jira project:** Book Club Portal (`BCP`, company-managed Scrum)
**Backlog:** 3 Epics, 13 User Stories, 47 story points · **Sprint 1:** 6 stories, 22 pts · **Sprint 2:** 7 stories, 25 pts (1-week sprints)

**1. Did your estimations reflect the actual effort?**

Relative to each other, mostly yes. Small, well-understood stories such as *Nominate a Book* (2) and *Set Personal Reading Goal* (2) were simple, and their low estimates held. The higher estimates went to the stories with the most uncertainty: *Spoiler-Tag a Comment* (5), because spoilers must also be hidden from previews, notifications and search; *Cast One Vote Per Poll* (5), because duplicate votes must be blocked; and *Live Vote Tally* (8), because of the real-time requirement in NFR-001. The Fibonacci scale forced a clear jump between "simple" (2–3) and "complex/uncertain" (5–8) work. In a simulated sprint the points could not be checked against real development time. *Live Vote Tally* is the story most likely to be under-estimated in a real team and could be split into "record vote" and "push live updates".

**2. Was your backlog well-prioritised?**

Yes. Priority followed user impact. Logging progress, spoiler protection, creating the poll and one-vote-per-member are the core of the portal, so they were **High**. Discussion threads, nominations, goal setting, mobile layout and the live tally were **Medium**, and the lead's nomination review queue was **Low**. The backlog was ranked in that order, High first. The sprint split also respected dependencies: chapter threads (2.1, 2.2) were done in the same sprint as spoiler tagging (2.3, 2.4), and nominations (3.1) in the same sprint as the poll and voting (3.3, 3.4).

**3. How did your simulated sprint align with your plan?**

Both sprints met their goals. Sprint 1 completed all 6 committed stories (22 points) and Sprint 2 all 7 (25 points), and each story moved To Do → In Progress → Done. Because this was a simulation inside one lab session, each sprint was finished within minutes instead of over the planned week. The board snapshots show the flow mid-sprint: in Sprint 1 there were 1 To Do, 3 In Progress and 2 Done. One process lesson came from Sprint 1: the stories were added at the same moment the sprint was started. Jira recorded them as **scope changes after the sprint start**, so Sprint 1 began at 0 points and has no guideline. For Sprint 2 the stories were added first and the sprint started afterwards. The burndown then shows the proper 25-point guideline, which is how sprint planning is supposed to work: commit first, then start.

**4. What insights did the burndown chart give about your team's capacity?**

In both charts the red "remaining" line falls straight to 0 on the first day, while the grey guideline (Sprint 2) runs from 25 down to 0 across the week and stays flat over the weekend. That sharp drop is the pattern the handout describes for work that was not done steadily: here because the sprint was simulated, but in a real team it would point to stories finished in bursts or estimated too loosely. Taken at face value, the team completed 22 and 25 points, so a velocity of about **22–25 points per 1-week sprint** is a reasonable starting capacity for Sprint 3. If the team kept finishing far ahead of the guideline, it should commit to more points per sprint. If the line stayed above the guideline, it should commit to fewer points or split large stories such as *Live Vote Tally*.
