#!/bin/bash

tmux kill-server

cd ~/project-22-fal-12-hackathon-team-2

git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate

pip install -r requirements.txt

tmux new-session -d 'flask run --host=0.0.0.0'