# What is GIT:
Git is a free and open-source distributed version control system (DVCS) used by developers to track changes in source code during software development. 

It functions like a "time machine" for a project, allowing users to save snapshots of their code, review the history of changes, and revert to previous versions if needed. 

## Key Concepts and Features
- **Version Control**: Git records changes to a project's files over time, keeping a detailed history of who made which change and when. This allows multiple people to work on the same codebase simultaneously without overwriting each other's work.
- **Distributed System**: In Git, every developer has a complete local copy (or "clone") of the entire project repository, including its full history. This allows developers to work offline and ensures a built-in backup of the project.
- **Snapshots, not Deltas**: Unlike older centralized systems, Git thinks of its data more like a series of snapshots of a miniature filesystem. When you commit changes, Git records the state of all your files at that moment.
- **Branching and Merging**: Git offers powerful, lightweight branching capabilities, allowing developers to create isolated lines of development (branches) to work on new features or bug fixes without affecting the main project. Once complete, these changes can be easily integrated back into the main codebase through a process called merging (often via a pull/merge request on hosting platforms).
- **Integrity**: Git ensures the integrity of its data using a cryptographic hash (SHA-1 checksum) for every object and commit, making it impossible to change the contents of any file or directory without Git knowing about it. 

## Git vs. GitHub

It is a common misconception that Git and GitHub are the same thing. 


- `Git` is the software installed locally on your computer to perform version control tasks.

- `GitHub` (along with competitors like GitLab and Bitbucket) is a web-based hosting service for Git repositories. It provides a platform for collaboration, code review, issue tracking, and other project management features that build on top of the core Git functionality. 


## Common Workflow
A typical Git workflow involves three main areas: the working directory, the staging area, and the local repository. 

- Modify files in your working directory.
- Stage the specific changes you want to include in the next snapshot using git add. **Staging Area:** A file maintained by Git that contains all of the information about what files and changes are going to go into your next commit.
- Commit the staged changes to your local repository, creating a permanent snapshot with a descriptive message using git commit.
- Optionally, push your local commits to a remote repository (e.g., on GitHub) to share them with your team using git push. 

Git is an essential tool in modern software development, used by nearly all professional developers globally.

# Useful GIT Commands:

- `git config --global user.email "email" `
- `git config --global user.name "name"` 
---
- `git branch -m` : is used to rename a branch in repository. The `-m` stands for move, which in Git's terminology is synonymous with renaming
- `git branch - m <new-name>` : Rename the current branch. If you are already on the branch.
- `git branch -m <old-name> <new-name>` : Rename a different branch. To rename a branch without switching to it first.

---

- `git init`: Initialize a Local Repository
- `git add {fileName}` : Add file to staging area
- `git add *` : Add All file to staging area
- `git commit -m 'GIT MESSAGE'` : To commit
---

- `git status` : To get information about the current working tree and pending changes.
- `git log`: This command is a powerful utility in Git used to display the commit history of a repository. It allows developers to track changes, review the project's evolution, and identify specific commits by showing a chronological list of snapshots of the project.
---

The `git checkout` command is used to switch between branches, navigate to specific commits, or restore files in your working directory to a previous state.

### Common Uses
- **Switching Branches**: Moves your current working environment to a different branch. `git checkout <branch-name>`.
- **Creating and Switching**: Creates a new branch and switches to it immediately. `git checkout -b <new-branch-name>`.
- **Restoring Files**: Discards local changes to a specific file by reverting it to the version in the last commit. `git checkout -- <file-path>` (or just `git checkout <file-path>`).
- **Viewing Past Commits**: "Time travels" to a specific commit hash, which puts Git into a "detached HEAD" state. `git checkout <commit-hash>`.
- **Return to Previous Branch**: Quickly jumps back to the branch you were last on.`git checkout -`.

Modern Alternatives: \
In Git version 2.23 and later, git checkout was split into two more specific commands to avoid confusion:
- `git switch`: Strictly for changing branches.
- `git restore`: Strictly for undoing local changes to files.

### Checktout Command Example:
- `git checkout main` : It moves the HEAD pointer to the main branch, making it the active branch.
- `git checkout -f main` : Forceful Switch
---
- `git remote add origin <url>` : This command connects your local repository to a remote server (like GitHub or GitLab). It creates an alias named "origin". So we don't have to type the full URL every time we push or pull the code.
- `git push -u origin main` : Push and set the upstream branch. This links our local `main` branch to the remote `origin`.
---
## Large file problem:
In order to push large file greater than 100mb we have to install and use `git lfs`.
- `git lfs install` : install on every git repo
- `git lfs track <large-file-name>` : Start Tracking the large File.
- `git lfs track` : git lfs track without any arguments will list all currently tracked patterns
- `git lfs status`
- `git lfs status --json`
- `git lfs ls-files` : Show the files tracked by lfs
- `git lfs ls-files -s`