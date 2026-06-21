import pytest

from pages.discover_page import DiscoverPage

@pytest.mark.tc_id("TC001")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Default Landing Page")
def test_default_landing_page(app):
    """
    Test Case ID : TC001
    Summary      : Verify Default Landing Page
    Priority     : P0
    """
    discover = DiscoverPage(app)
    assert "/popular" in discover.get_current_url()

@pytest.mark.tc_id("TC002")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Direct Access or Refresh to /popular Route")
def test_tc002_verify_direct_access_to_popular_route(app):
    """
    Test Case ID : TC002
    Summary      : Verify Direct Access or Refresh to /popular Route
    Priority     : P0
    """

    response = app.goto(
        "https://tmdb-discover.surge.sh/popular",
        wait_until="networkidle"
    )

    assert response.status == 200, (
        f"Expected status code 200 but got {response.status}"
    )

