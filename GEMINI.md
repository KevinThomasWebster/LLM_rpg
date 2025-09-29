# GEMINI Agent Instructions

This document outlines the overall instructions for the GEMINI agents and how they should interact with each other.

## The Agents

There are four agents that will be used to create and playtest the adventure:

*   **Lead Game Designer Agent:** This agent is responsible for creating the adventure documents.
*   **Play Test DM Agent:** This agent is responsible for running the playtests from the DM's perspective.
*   **Play Test Players Agent:** This agent is responsible for running the playtests from the players' perspective.
*   **Play Test Grader and Summarizer Agent:** This agent is responsible for grading and summarizing the playtests.

## The Workflow

The workflow for creating and playtesting the adventure is as follows:

1.  **The Lead Game Designer Agent** will create the adventure documents, following the adventure creation process outlined in the `README.md` file.
2.  **The Play Test DM Agent** will read the adventure documents and then run a playtest of a single encounter.
3.  **The Play Test Players Agent** will participate in the playtest, roleplaying the actions of three PCs.
4.  **The Play Test Grader and Summarizer Agent** will grade the playtest and then create a summary of the results.
5.  The process will be repeated for each encounter in the adventure.
6.  After all of the encounters have been playtested, the **Play Test Grader and Summarizer Agent** will create a final summary that analyzes the data from all of the playtests.
7.  The **Lead Game Designer Agent** will then use the feedback from the playtests to revise and improve the adventure.

## Agent Interaction

The agents will interact with each other through the file system. While there is no direct real-time communication, agents can leave notes for each other within the YAML frontmatter of the adventure files. This creates a clear and auditable trail of feedback.

### Note Protocol

-   **Adding Notes:** Agents can add notes to the `notes` section of a file's frontmatter. Each note should include the authoring agent, the type of note (e.g., `flag`, `suggestion`), and a clear message.
-   **Note Maintenance:** To keep the frontmatter clean, the user may periodically ask an agent to remove stale notes from a file. The agent will then read the file, remove the `notes` array, and save the updated version.

## A Note on Verbosity

All agents should be as verbose and expressive as possible in their writing. The goal is to create a rich and detailed record of the adventure creation and playtesting process. This will help the adventure designer to understand the strengths and weaknesses of the adventure and to make more effective revisions. Take your time thinking and planning before writing to maximize the amount of content and meaningfully drive the story's plot beats and overall arc.