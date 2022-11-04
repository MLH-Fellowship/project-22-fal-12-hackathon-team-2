# Kill all existing tmux sessions. 
#This is to kill any existing flask server that might be running in the background.
tmux kill-server

cd /root/project-22-fal-12-hackathon-team-2

git fetch && git reset origin/main --hard

 
# Enter python virtual environment
source python3-virtualenv/bin/activate

#install python dependencies
pip install -r requirements.txt

tmux new -d -s my_session

tmux send-keys -t my_session "flask run --host=137.184.86.159" Enter


# #!/bin/bash

# cd project-22-fal-12-hackathon-team-2

# git fetch && git reset origin/main --hard

# # Install python virtual environment
# python -m venv python3-virtualenv

# # Enter python virtual environment
# source python3-virtualenv/bin/activate

# #install python dependencies
# pip install -r requirements.txt

# systemctl restart myportfolio