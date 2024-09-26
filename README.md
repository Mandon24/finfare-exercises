# finfare-exercises
Repo containing my solutions to Finfare take home exercises

# Selenium Prompt
Write a Test Suite that does the following:
1. Opens a webpage www.google.com/finance on a chrome browser
2. Verifies the page is loaded by asserting the page title
3. Retrieves the stock symbols listed under the section “You may be interested in info”
(please note, this is a sample of what to look for on the above browser link and the stock
data will differ day to day)
4. Compare the stock symbols retrieved from (3) with given test data
5. Print all stock symbols that are in (3) but not in given test data
6. Print all stock symbols that are in given test data but not in (3)

# GitHub Actions Prompt
Create Github Actions workflows that:
- Can run manually and have automatic nightly runs.
- Manual workflow should have option to run full set of test or test case 5 and 6 from Problem#1.

When you have completed all steps, please submit email with a link to your public GitHub
project.

Please be sure to answer all questions above before submitting.

## Setup

### Virtual Environment
Set up your local env with `python -m venv venv\finfare-exercises`

### Requirements
Install project requirements locally with `pip install -r requirements-dev.txt`
