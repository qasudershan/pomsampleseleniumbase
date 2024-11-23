import pytest
from seleniumbase import BaseCase

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome, edge, safari, firefox.",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run tests in headless mode.",
    )

