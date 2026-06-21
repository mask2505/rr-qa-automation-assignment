import pytest

from pages.discover_page import DiscoverPage


@pytest.mark.tc_id("TC005")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Popular Category Filter")
def test_tc005_verify_popular_category_filter(app):
    """
    Test Case ID : TC005
    Summary      : Verify Popular Category Filter
    Priority     : P0
    """

    discover = DiscoverPage(app)

    discover.click_popular()

    assert "/popular" in discover.get_current_url(), (
        f"Expected '/popular' in URL but found "
        f"'{discover.get_current_url()}'"
    )

    assert discover.get_card_count() > 0, (
        "No movie cards displayed for Popular category"
    )


@pytest.mark.tc_id("TC006")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Trending Category Filter")
def test_tc006_verify_trending_category_filter(app):
    """
    Test Case ID : TC006
    Summary      : Verify Trending Category Filter
    Priority     : P0
    """

    discover = DiscoverPage(app)

    discover.click_trending()
    app.wait_for_timeout(10000)

    assert "/trend" in discover.get_current_url(), (
        f"Expected '/trend' in URL but found "
        f"'{discover.get_current_url()}'"
    )

    assert discover.get_card_count() > 0, (
        "No movie cards displayed for Trending category"
    )

@pytest.mark.tc_id("TC007")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Newest Category Filter")
def test_tc007_verify_newest_category_filter(app):
    """
    Test Case ID : TC007
    Summary      : Verify Newest Category Filter
    Priority     : P0
    """

    discover = DiscoverPage(app)

    discover.click_newest()
    app.wait_for_timeout(10000)

    assert "/new" in discover.get_current_url(), (
        f"Expected '/new' in URL but found "
        f"'{discover.get_current_url()}'"
    )

    assert discover.get_card_count() > 0, (
        "No movie cards displayed for Newest category"
    )


@pytest.mark.tc_id("TC008")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Top Rated Category Filter")
def test_tc008_verify_top_rated_category_filter(app):
    """
    Test Case ID : TC008
    Summary      : Verify Top Rated Category Filter
    Priority     : P0
    """

    discover = DiscoverPage(app)

    discover.click_top_rated()
    app.wait_for_timeout(10000)

    assert "/top" in discover.get_current_url(), (
        f"Expected '/top' in URL but found "
        f"'{discover.get_current_url()}'"
    )

    assert discover.get_card_count() > 0, (
        "No movie cards displayed for Top Rated category"
    )
