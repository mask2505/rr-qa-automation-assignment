import pytest

BASE_URL = "https://tmdb-discover.surge.sh"


@pytest.fixture
def app(page):
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    return page


def pytest_html_report_title(report):
    report.title = "RR QA Automation Report"


def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata["Project"] = "RR Automation Assignment"
        config._metadata["Tester"] = "Manoj Kumar"
        config._metadata["Framework"] = "PyTest + Playwright"
        config._metadata["Browser"] = "Chromium"


def pytest_html_results_table_header(cells):
    cells.insert(1, "<th>TC ID</th>")
    cells.insert(2, "<th>Priority</th>")


def pytest_html_results_table_row(report, cells):
    cells.insert(
        1,
        f"<td>{getattr(report, 'tc_id', 'N/A')}</td>"
    )
    cells.insert(
        2,
        f"<td>{getattr(report, 'priority', 'N/A')}</td>"
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    tc_id_marker = item.get_closest_marker("tc_id")
    priority_marker = item.get_closest_marker("priority")

    report.tc_id = (
        tc_id_marker.args[0]
        if tc_id_marker
        else "N/A"
    )

    report.priority = (
        priority_marker.args[0]
        if priority_marker
        else "N/A"
    )