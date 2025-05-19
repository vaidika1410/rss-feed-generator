#!/bin/bash

echo "========================="

# allowing us to use git
git config --global user.name "${GITHUB_ACTOR}"
git config --global user.email "${INPUT_EMAIL}"
git config --global --add safe.directory /github/workspace

# running python
python3 /usr/bin/feed.py

# pushing to the main branch
git add -A && git commit -m "Update Feed"
git push --set-upstream origin main

echo "========================="
