#!/bin/bash

cd ~/project-22-fal-12-hackathon-team-2

git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate

pip install -r requirements.txt

systemctl restart myportfolio