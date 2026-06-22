import pytest

from pages.discover_page import DiscoverPage


@pytest.mark.tc_id("TC018")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Search With Valid Movie Title")
def test_tc018_verify_search_with_valid_movie_title(app):

    discover = DiscoverPage(app)

    discover.search_movie("Michael")
    app.wait_for_timeout(3000)
    assert discover.get_card_count() > 0

    assert "Michael" in discover.get_first_card_title()

@pytest.mark.tc_id("TC019")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify Search With Partial Movie Title")
def test_tc019_verify_search_with_partial_movie_title(app):

    discover = DiscoverPage(app)

    discover.search_movie("Mich")
    app.wait_for_timeout(3000)
    assert discover.get_card_count() > 0

@pytest.mark.tc_id("TC020")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify Search With Invalid Movie Title")
def test_tc020_verify_search_with_invalid_movie_title(app):

    discover = DiscoverPage(app)

    discover.search_movie("XYZ_INVALID_MOVIE_123456")
    app.wait_for_timeout(5000)
    assert discover.get_card_count() == 0

@pytest.mark.tc_id("TC021")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify Search Reset Behavior")
def test_tc021_verify_search_reset_behavior(app):

    discover = DiscoverPage(app)

    discover.search_movie("Michael")
    app.wait_for_timeout(3000)
    filtered_count = discover.get_card_count()

    discover.clear_search()
    app.wait_for_timeout(3000)
    reset_count = discover.get_card_count()

    assert filtered_count > 0
    assert reset_count > 0