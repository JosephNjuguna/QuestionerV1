# Questioner

**Badges**
---

[![Build Status](https://travis-ci.org/JosephNjuguna/Questioner.svg?branch=develop)](https://travis-ci.org/JosephNjuguna/Questioner)

[![Coverage Status](https://coveralls.io/repos/github/JosephNjuguna/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/JosephNjuguna/Questioner?branch=develop)

This is a Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize
questions to be answered. Other users can vote on asked questions and they bubble to the top
or bottom of the log.
----
#Rquirements

asn1crypto==0.24.0
astroid==2.1.0
atomicwrites==1.2.1
attrs==18.2.0
cffi==1.11.5
Click==7.0
cryptography==2.4.2
Flask==1.0.2
idna==2.8
isort==4.3.4
itsdangerous==1.1.0
Jinja2==2.10
jwt==0.5.4
lazy-object-proxy==1.3.1
MarkupSafe==1.1.0
mccabe==0.6.1
more-itertools==5.0.0
pluggy==0.8.0
py==1.7.0
pycparser==2.19
pylint==2.2.2
pytest==4.1.0
six==1.12.0
typed-ast==1.1.1
Werkzeug==0.14.1
wrapt==1.10.11

---
#Installing 
>Clone this repo to your machine
>Open the Questioner folder from the directory it was stored :
> Open in terminal  and starts the local server by running the following command : flask run`
---
#Running Test 
At the root of the folder run `python -m pytest`

you will get to run a couple of test for the app
#What is tested?
AUTHENTICATION> USER GET RECORD OF SPECIFIC QUESTION

> User log in 
> User sign up
MEETUP
> USER RSVP FOR A MEETUP
> USER GET SPECIFIC RECORDS OF A MEETUP
> USER GET ALL UP COMING MEETUPS
> USER GET RECORD OF SPECIFIC QUESTION IN A MEET UP
QUESTION
> USER CAN POST QUESTION
> USER CAN UPVOTE QUESTION 
> USER CAN DOWNVOTE QUESTION
