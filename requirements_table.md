# Requirements Table
### Problem Statement #55 — Book Club Reading Challenge & Discussion Portal
**Actors:** Club Member, Discussion Lead

---

## Complete Requirements Table

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|----|------|--------------|----------|----------------------|-----------|
| **FR-001** | Functional | The system shall allow a Club Member to log and update their current page/percentage progress for the active book, and display progress toward their personal reading goal. | High | **Pass:** Progress bar updates immediately and persists after page refresh. **Fail:** Progress is lost or not reflected after saving. | Gives members a visible, motivating way to track personal reading goals and stay engaged with the club's schedule. |
| **FR-002** | Functional | The system shall hide content inside spoiler-tagged discussion comments until the user explicitly clicks to reveal it or marks that chapter as read. | High | **Pass:** Spoiler text is masked with a blur filter and excluded from search/preview snippets. **Fail:** Spoiler content is exposed in a preview, notification, or search result before reveal. | Protects members who are behind on reading from unwanted plot reveals, encouraging open discussion without fear of spoilers. |
| **FR-003** | Functional | The system shall allow a Discussion Lead to create a dedicated discussion thread for each chapter or reading milestone of the current book, and allow Club Members to post comments within it. | Medium | **Pass:** New thread is created and correctly associated with its chapter/milestone. **Fail:** A thread is created without a valid chapter association, or comments appear under the wrong chapter. | Keeps conversation organized by chapter so members can discuss content relevant to where they are in the book. |
| **FR-004** | Functional | The system shall allow a Discussion Lead to create a monthly poll listing nominated books, and allow each Club Member to cast exactly one vote per poll. | High | **Pass:** One vote per member is recorded and the tally updates correctly. **Fail:** A member is able to submit more than one vote in the same poll cycle. | Enables fair, democratic selection of the next book for the club to read. |
| **FR-005** | Functional | The system shall allow a Club Member to nominate a book (title, author, and a brief reason) for inclusion in the next monthly voting poll. | Medium | **Pass:** A complete nomination appears in the Discussion Lead's review queue. **Fail:** A nomination is accepted without required fields (title/author). | Crowdsources reading suggestions from the community and increases member engagement in book selection. |
| **NFR-001** | Non-Functional — Performance & Security | Monthly poll voting must prevent duplicate votes using user session verification, and vote tallies must update in real time. | High | **Pass:** Benchmarking tests confirm target latency (e.g. tally updates within 2s) and duplicate-vote prevention holds under simulated peak load. **Fail:** Duplicate votes are accepted, or tally updates exceed target latency. | Ensures poll results are trustworthy and the system remains responsive during peak voting periods (e.g. month-end). |
| **NFR-002** | Non-Functional — Usability & Accessibility | Spoiler-tag reveal/blur interactions and reading-progress inputs must be fully usable on both desktop and mobile viewports (minimum width 360px) without loss of functionality. | Medium | **Pass:** All interactive elements remain accessible and functional across 360px–1920px widths in usability testing. **Fail:** Any control is obscured, cut off, or non-functional below 768px width. | Club members participate from a range of devices, so consistent usability on mobile is essential for engagement. |

---
*Prepared for: PES University – Dept. of CSE — Lab 1: Requirements Engineering & UML Use-Case Modelling*
