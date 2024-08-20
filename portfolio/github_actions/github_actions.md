### Setting Up GitHub Actions

To set up GitHub Actions in my repository, I followed these steps:

1. **Create `.github/workflows` Directory**:
   I created a `.github/workflows` directory at the root level of my project.

2. **Add the Workflow File**:
   Inside this directory, I placed the `python-app.yml` file, which defines my workflow for automating tasks. This YAML file includes instructions for GitHub Actions, such as:
   - Specifying that the workflow should run on `push` or `pull_request` events.
   - Setting up the Python environment.
   - Running my tests.

3. **Organize Project Structure**:
   In my project structure, I kept my code organized in the `portfolio/github_actions` directory. This directory contains:
   - `main.py` (the main code file)
   - `test_main.py` (the test file)

4. **Stage and Commit Changes**:
   After setting up the `.github/workflows` directory and the `python-app.yml` file, I used Git to:
   - Stage and commit these changes.

5. **Push Changes to GitHub**:
   I pushed the changes to GitHub.

6. **Verify Workflow Execution**:
   I verified that the workflow ran as expected by checking the "Actions" tab in my GitHub repository.
