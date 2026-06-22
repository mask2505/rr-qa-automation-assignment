import pytest

from pages.discover_page import DiscoverPage

@pytest.mark.tc_id("TC027")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Next Page Navigation")
def test_tc027_verify_next_page_navigation(app):

    discover = DiscoverPage(app)

    current_page = int(discover.get_current_page())

    discover.click_next_page()
    app.wait_for_timeout(3000)

    assert int(discover.get_current_page()) == current_page + 1

@pytest.mark.tc_id("TC028")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Previous Page Navigation")
def test_tc028_verify_previous_page_navigation(app):

    discover = DiscoverPage(app)

    discover.click_page_number(2)
    app.wait_for_timeout(3000)
    discover.click_previous_page()
    app.wait_for_timeout(3000)
    assert discover.get_current_page() == "1"

@pytest.mark.tc_id("TC029")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify Page Number Navigation")
def test_tc029_verify_page_number_navigation(app):

    discover = DiscoverPage(app)

    discover.click_page_number(3)
    app.wait_for_timeout(3000)
    assert discover.get_current_page() == "3"

@pytest.mark.tc_id("TC030")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify Last Available Page Navigation")
def test_tc030_verify_last_available_page_navigation(app):

    discover = DiscoverPage(app)

    last_page = discover.get_last_page_number()

    discover.click_last_page()

    assert discover.get_current_page() == last_page

@pytest.mark.tc_id("TC031")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify Pagination Boundary Behavior")
def test_tc031_verify_pagination_boundary_behavior(app):

    discover = DiscoverPage(app)

    assert discover.get_current_page() == "1"

    discover.click_previous_page()

    assert discover.get_current_page() == "1"