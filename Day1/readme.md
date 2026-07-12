# Day 1: Git, GitHub Setup, and Environment Configuration

A command-line milestone establishing the local development environment and core version control workflow for the MLB-Internship.

## What It Does
- Configures the local Python runtime environment.
- Initializes local repository tracking for project modules.
- Synchronizes project files directly with the remote repository branch.

## Concepts Practiced
- **Git Initialization**: `git init` and configuring user credentials.
- **Staging & Commits**: `git add .` and creating descriptive snapshot points with `git commit`.
- **Remote Linking**: Associating local repos with GitHub using `git remote add`.
- **Branch Management**: Deploying code directly to the host server using `git push`.

## Challenges Faced & Solutions
- **Nested Git Repositories**: Encountered a synchronization block due to accidental nested `.git` configuration folders inside project subdirectories. Fixed by completely purging the hidden tracking folders and re-initializing a clean, unified workspace structure.
- **Terminal Shell Confusion**: Attempted to run system commands inside the active Python interpreter. Resolved by executing `exit()` to leave the interactive shell (`>>>`) and running the script paths directly from the clean PowerShell prompt.

## Files
- `.gitignore`: Prevents system cache and tracking files from entering version control.
