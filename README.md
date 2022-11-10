# Production Engineering - Week 1 - Portfolio Site


## Getting Started

You need to do all your work here.

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal. We'll go through how to host it in the cloud in the next few weeks!* 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Inspiration
We took inspiration from two websites 1) Dapi.com 2) MLH website. We wanted to combine the simplicity and elegance of Dapi's website with the wholesome vibes of MLH's website. One of our biggest features is that our design emphasizes scrolling down this is because we believe that scrolling down really enhances the UX of a website
## What it does
It showcases the team members experiences, work, hobbies and places they've visited.
## How we built it
Paulin built the front end, and Alexis built the back end. We created a branch per feature, and whenever we move to a new feature, we create it out of the previous branch. Then we made a PR to main
## Challenges we ran into
It was hard to come up with arquitecture of the portfolio. For most of the project, we thought we were going to need a HTML files per team member. Fortunately, towards the end, we were able to figure out how to share same HTML and CSS files. 
## Accomplishments that we're proud of
- We believe the CSS was the best part of our project. We were able to add some animations, box shadows and sticky nav bar.  We invested a lot of time watching several videos from Kevin Powel 
## What we learned
- We learned that sometimes designing the architecture is as important as coding it. Many times we had to go back because our design hit a dead end
- We learned how to learn new technologies like flask and jinja. I
- This project would not have been possible without stack overflow. So we realized that is very important to contribute to the community
 
## What's next for Alexis&Paulin Portfolio
Regarding the code quality 
- Changing the name of CSS selectors
- Separating CSS in different files
Regarding features
- Adding mobile mode
- Adding dark mode
- Add spotify, maybe?
- Add a gallery of photos
