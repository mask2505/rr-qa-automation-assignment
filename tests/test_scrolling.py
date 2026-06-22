import pytest

from pages.discover_page import DiscoverPage

@pytest.mark.tc_id("TC032")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify Page Scroll Functionality")
def test_tc032_verify_page_scroll_functionality(app):

    discover = DiscoverPage(app)

    discover.scroll_to_bottom()
    app.wait_for_timeout(3000)
    assert discover.get_scroll_position() > 0

@pytest.mark.tc_id("TC033")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify Discovery Filters Remain Accessible During Scroll")
def test_tc033_verify_discovery_filters_accessible_during_scroll(app):

    discover = DiscoverPage(app)

    discover.scroll_to_bottom()
    app.wait_for_timeout(3000)
    assert discover.is_discovery_filters_visible()

    discover.scroll_to_top()
    app.wait_for_timeout(3000)

    assert discover.is_discovery_filters_visible()

@pytest.mark.tc_id("TC034")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify Pagination Controls Are Reachable Through Scrolling")
def test_tc034_verify_pagination_controls_reachable(app):

    discover = DiscoverPage(app)

    discover.scroll_to_bottom()
    app.wait_for_timeout(3000)

    assert discover.is_pagination_visible()

@pytest.mark.tc_id("TC035")
@pytest.mark.priority("P2")
@pytest.mark.title("Verify Scroll Position After Pagination")
def test_tc035_verify_scroll_position_after_pagination(app):

    discover = DiscoverPage(app)

    discover.scroll_to_bottom()
    app.wait_for_timeout(3000)

    discover.click_next_page()
    app.wait_for_timeout(3000)

    current_page = discover.get_current_page()

    assert current_page == "2"

