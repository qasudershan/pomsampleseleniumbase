
This is an automation framework for the Prezent project using SeleniumBase, which leverages Selenium WebDriver for browser automation and pytest for testing. This framework supports various browsers and runs tests in headless or GUI mode.

########Prerequisites#############

1. Python 3x
2. Virtual Environment
python -m venv venv
3. Install dependencies
pip install -r requirements.txt
4. Folder Structure
prezentTestProject_Seleniumbase/
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── profile_page.py
│   ├── templates_page.py
│
├── tests/
│   ├── __init__.py
│   ├── base_test.py
│   ├── test_login_profile.py
│
├── venv/                  # Virtual environment folder
│
├── conftest.py
├── requirements.txt
├── pytest.ini             # configuration for pytest
├── README.md              # Documentation for the project

5. Running tests
>>>pytest --browser=chrome --headless

options for browsers include: 
chrome
edge
safari
firefox

6. Tests report: The test reports are generated in HTML format and can be found in report.html.


