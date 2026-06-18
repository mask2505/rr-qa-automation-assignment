import pytest

BASE_URL = "https://tmdb-discover.surge.sh"


@pytest.fixture
def app(page):
    page.goto(BASE_URL)
    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")

        if page:
            page.screenshot(
                path=f"screenshots/{item.name}.png"
            )
