# Lab 2 — Jira Walkthrough (≈ 30–40 min)

Everything to type is in [`backlog.md`](./backlog.md). Take each screenshot marked 📸 and save it in `screenshots/` with the file name shown.

## 1. Create the project
1. Jira → **Projects → +** → **Software development → Scrum → Use template**.
2. Choose **Company-managed**, name it **Book Club Portal** (key `BCP`) → **Next**.

## 2. Add Epics and Stories — two options

**Option A: Import the CSV (fastest)**
1. **Settings ⚙ → System → External System Import → CSV** (or the project's **⋯ → Import work items**), upload [`jira_import.csv`](./jira_import.csv).
2. Map the columns: `Issue Id` → *Issue Id*, `Issue Type` → *Issue Type*, `Summary` → *Summary*, `Description` → *Description*, `Priority` → *Priority*, `Story Points` → *Story point estimate* / *Story Points*, `Parent` → *Parent*.
3. Import. You should get 3 Epics and 13 Stories, each Story already under its Epic with priority and points.

**Option B: Manually (the way the handout shows)**
1. **Backlog → Create → Epic**: create the 3 Epics with the names and descriptions in `backlog.md`.
2. Press **E** to show the Epic panel. For each Epic, click the **arrow next to it → Create work item → Story** and enter the story title and the *As a / I want / So that* text.
3. Open each story and set the **Priority** and **Story points** (under *More fields*) from the table.

📸 `01_backlog_epics.png`: the Backlog with the Epic panel open and all stories listed.
📸 `02_story_points.png`: click an Epic's arrow so the point totals show, or open one story with *Story points* visible.

## 3. Prioritise
Drag the stories in the backlog into the **Prioritised backlog order** from `backlog.md` (High at the top, Low at the bottom).

## 4. Sprint 1
1. **Create sprint** → *Sprint 1*. Drag in stories **1.1, 1.2, 2.1, 2.2, 2.3, 2.4** (22 pts).
2. **Start sprint**: duration **1 week**, goal *"Core reading tracking and spoiler-safe chapter discussions"*.
3. On **Active sprints**, move the stories **To Do → In Progress**, wait a few minutes, then move them to **Done**. Do them a few at a time rather than all at once, so the burndown shows a real slope.

📸 `03_sprint_board.png`: the Active Sprint board while some cards are In Progress and some are Done.

4. **Reports → Burndown Chart** (choose Sprint 1).

📸 `04_burndown_sprint1.png`

5. **Complete sprint**.

## 5. Sprint 2 (the handout says to finish 2 sprints)
Repeat with stories **1.3, 1.4, 3.1, 3.2, 3.3, 3.4, 3.5** (25 pts), goal *"Book nominations, monthly voting and mobile polish"*.

📸 `05_sprint2_board.png`, `06_burndown_sprint2.png`, then complete the sprint.

📸 `07_epics_done.png`: the Backlog with the Epic panel showing the completed progress bars.

## 6. Finish
- Check the [`reflection.md`](./reflection.md) answers against what your burndown actually showed and adjust any lines that don't match.
- Export `reflection.md` (or copy it into Word) as **PDF** together with the Epic and Burndown screenshots, which are the handout's PDF deliverables.
- Keep the Jira project. You have to demo it to the instructor.
