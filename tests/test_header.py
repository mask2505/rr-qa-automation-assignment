import pytest
from pages.discover_page import DiscoverPage

@pytest.mark.tc_id("TC003")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify App Title is Visible")
def test_tc003_verify_app_title_is_visible(app):
    """
    Test Case ID : TC003
    Summary      : Verify App Title is Visible
    Priority     : P1
    """

    discover = DiscoverPage(app)

    assert discover.get_title() == "Discover", (
        f"Expected title 'Discover' but found "
        f"'{discover.get_title()}'"
    )


@pytest.mark.tc_id("TC004")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify App Title is Clickable and Navigates to Home Page")
def test_tc004_verify_app_title_is_clickable_and_navigates_to_home_page(app):
    """
    Test Case ID : TC004
    Summary      : Verify App Title is Clickable and Navigates to Home Page
    Priority     : P1
    """

    discover = DiscoverPage(app)

    # Navigate away from default page
    discover.click_trending()

    assert "/trend" in discover.get_current_url(), (
        "Failed to navigate to Trending page"
    )

    # Click application title
    discover.click_title()

    assert "/popular" in discover.get_current_url(), (
        f"Expected navigation to '/popular' but found "
        f"'{discover.get_current_url()}'"
    )