# Student-CI-Project

A small Python calculator app used to demonstrate Continuous Integration with Jenkins and GitHub webhooks (CMSC 426, In-Class Activity 3).

## Structure
- `app.py` - application code
- `tests/testApp.py` - unit tests (unittest)

## Run locally
    python app.py
    python -m unittest discover -s tests -v

## CI
Jenkins job `Student-CI-Project` pulls this repo, runs the app and tests, and fails the build if any test fails. A GitHub webhook (via an ngrok HTTPS tunnel) triggers a build on every push.

