# Use-Case Flow Specification

**Use Case:** Cast Vote in Monthly Book Poll
**Primary Actor:** Club Member
**Supporting Actor / System Function (included):** Verify User Session
**Related Use Cases:** Nominate Book, View Poll Results, Create Monthly Poll (Discussion Lead)

---

## Preconditions
1. The Club Member is authenticated and has an active session with the system.
2. A monthly poll listing nominated books is currently open for voting.
3. The Club Member has **not** already cast a vote in the current poll cycle.

## Postconditions
1. The Club Member's vote is recorded and permanently associated with their member ID and the current poll ID.
2. The poll's vote tally is updated in real time.
3. The Club Member's voting status for the current poll cycle is set to "Voted," preventing further votes in this cycle.

---

## Main Success Scenario
1. The Club Member navigates to the "Monthly Poll" section of the portal.
2. The system displays the list of nominated books available for the current voting cycle.
3. The Club Member selects one book and clicks "Cast Vote."
4. The system performs the included use case **Verify User Session**, confirming the member is authenticated and has not already voted this cycle.
5. The system records the vote against the Club Member's ID and the active poll ID.
6. The system updates the poll's live vote tally.
7. The system displays a confirmation message ("Your vote has been recorded") and disables further voting controls for that member on the current poll.

---

## Alternate Flow

### A1 — Duplicate Vote Attempt
*Triggered at Step 4, when session verification detects the member has already voted in the current poll cycle.*

4a. The system detects, during **Verify User Session**, that the Club Member has already submitted a vote for the active poll.
4b. The system displays an error message: "You have already voted this month."
4c. The system does **not** update the vote tally and does **not** record a new vote.
4d. The system redirects the Club Member to the "View Poll Results" screen.
4e. Use case ends.

---
*Prepared for: PES University – Dept. of CSE — Lab 1: Requirements Engineering & UML Use-Case Modelling*
*Problem Statement #55 — Book Club Reading Challenge & Discussion Portal*
