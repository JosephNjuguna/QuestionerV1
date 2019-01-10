# Questioner
 language : Python
**Badges**
---
[![Build Status](https://travis-ci.org/JosephNjuguna/Questioner.svg?branch=develop)](https://travis-ci.org/JosephNjuguna/Questioner)

[![Coverage Status](https://coveralls.io/repos/github/JosephNjuguna/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/JosephNjuguna/Questioner?branch=develop)

This is a Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize
questions to be answered. Other users can vote on asked questions and they bubble to the top
or bottom of the log.

**Requirements**
Flask==1.0.2
pylint==2.2.2
pytest==4.1.0

**Installing**
Clone this repo to your machine
Open the Questioner folder from the directory it was stored :
Open in terminal  and starts the local server by running the following command : flask run`.

**Running Test**
---
open the praject with terminal and
at the root of the folder run `python -m pytest`
you will get to run a couple of test for the app

**What is tested?**
AUTHENTICATION
---
  1. USER GET RECORD OF SPECIFIC QUESTION
  2. USER LOG IN 
  3. USER SIGN UP

MEETUP
---
1. USER RSVP FOR A MEETUP
2. USER GET SPECIFIC RECORDS OF A MEETUP
3. USER GET ALL UP COMING MEETUPS
4. USER GET RECORD OF SPECIFIC QUESTION IN A MEET UP
 
QUESTION
---
 1. USER CAN POST QUESTION
 2. USER CAN UPVOTE QUESTION 
 3. USER CAN DOWNVOTE QUESTION
