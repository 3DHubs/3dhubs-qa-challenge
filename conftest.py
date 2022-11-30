import pytest


@pytest.fixture(scope="session", autouse=True)
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1536,
            "height": 754,
        }
    }
