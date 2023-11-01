Testing Georgia and Lulu Website

The project aims to test the functionality and behavior of the Georgia and Lulu website using the BDD (Behavior-Driven Development) method. 
Scenarios are described in a user-friendly language using the Gherkin syntax.

Prerequisites:

Install Pycharm Community Edition: https://www.jetbrains.com/pycharm/download/
Install Python: https://www.python.org/downloads/
Install Chrome Browser: The tests are designed to run in Chrome.

Installation:

1.Clone the repository by entering the following command in Git Bash:
git clone https://github.com/AndreeaPopa9/ExamProject_BDD

To navigate to the project folder, run the following command:
cd ExamProject_BDD.

2. Install the Selenium library by entering the following command in the terminal:
pip install selenium or pip install -U selenium (for an up-to-date version)

3. Install WebDriver by entering the following command in the terminal:
pip install webdriver-manager

5. Install the Behave library by entering the following command in the terminal:
pip install behave

7. To generate BDD reports, enter the following command in the terminal:
pip install behave-html-formatter


Troubleshooting:

1. If step 2 doesn't work, try the command:
py -m pip install selenium
2. If step 3 doesn't work, try the command:
py -m pip install webdriver-manager

Another option:
File -> Settings -> Click on Project: ExamProject_BDD -> Python Interpreter -> +
Search for "selenium" -> Install Package
Search for "webdriver-manager" -> Install Package

Running Tests:

1. Run all tests by entering the following command in the terminal: -behave
2. Run a single test by entering the following command in the terminal:
-behave -i <desired feature file>
Example: behave -i signin.feature
3. Run a test with a specific tag by entering the following command in the terminal:
behave --tags=<tag_name>

Generating Reports:

1. For all tests, use the command:
behave -f html -o behave-report.html
2. For a specific test, use the command:
behave -f html -o behave-report.html -i <desired feature file>
3. For a specific tag, use the command:
behave -f html -o behave-report.html --tags=<tag_name>

Accessing Reports:

1. Click on the behave-report.html file.
2. Click on the icon on the right of the page to open it in the desired browser or click on the Python icon to open it in Python.






