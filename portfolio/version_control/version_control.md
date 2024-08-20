# Version Control Setup for Portfolio Repository

## Repository Creation and Cloning

1. **Create the Repository on GitHub**
   - Navigate to GitHub and create a new repository named `Portfolio`.

2. **Clone the Repository to Local Machine**
   - Open Visual Studio Code.
   - Open a terminal within Visual Studio Code.
   - Clone the repository using the following command:
     ```bash
     git@github.com:monikaIBA/Portfolio.git
     ```

## Setting Up the Project Structure

1. **Create Main Folder and Subfolders**
   - Inside Visual Studio Code, create a main folder named `Portfolio`.
   - Add the following subfolders:
     - `version_control`
     - `github_actions`
     - `bug_tracking`
     - `doxygen`

2. **Stage and Commit the New Folders**
   - Stage the new folders for commit:
     ```bash
     git add .
     ```
   - Commit the changes with a descriptive message:
     ```bash
     git commit -m "Added subfolders: version_control, github_actions, bug_tracking, doxygen"
     ```

3. **Push the Commit to GitHub**
   - Push the commit to the `main` branch on GitHub:
     ```bash
     git push origin main
     ```

## Creating and Updating a New Branch

1. **Create a New Branch**
   - Create a new branch named `new branch`:
     ```bash
     git branch new branch
     ```
   - Switch to the newly created branch:
     ```bash
     git checkout new branch
     ```

2. **Keep the New Branch Up-to-Date**
   - Fetch and merge any updates from the remote branch to ensure synchronization:
     ```bash
     git pull origin new branch
     ```

## Summary

- Created and organized the `Portfolio` repository on GitHub.
- Cloned the repository to the local machine and set up the folder structure.
- Staged, committed, and pushed the changes to the `main` branch.
- Created a new branch and kept it updated with remote changes.

