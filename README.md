# hacketeers

This project's goal is to develop a chatbot to help guide refugees and other
people who might not be familiar with the local language getting a CV they
can then submit to secure employement.

The bot should ask the applicant their language of origin. It will then leverage
the Google Translate API to have a conversation with the applicant in their
chosen language. The bot will then translate the answers back to english and
feed them into a CV. The CV is then returned to the user as a pdf file.

We were unable to complete the chatbot, but a guided questionnaire can be run
on the command line as a proof of concept of the system. The resulting pdf is
outputed to the tmp/ dir in a timestamped directory.

# dependencies

This project was built and tested with python 3.6.6

Use pipenv to install dependencies

First, make use pipenv is installed:

```bash
pip install --user pipenv
```

Then run pipenv in the project folder to setup a virtualenv and install packages:

```bash
pipenv install --python 3
```

Then run the project with pipenv run:

```bash
pipenv run ./questions.py
```

The program also requires a google-translate API key.
Running the project with pipenv should automatically load the .env
file in the repository, which will set up the needed env variable.
