import pytest

from pages.discover_page import DiscoverPage

@pytest.mark.tc_id("TC022")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Movie Cards Are Displayed")
def test_tc022_verify_movie_cards_displayed(app):

    discover = DiscoverPage(app)

    assert discover.get_card_count() > 0

@pytest.mark.tc_id("TC023")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Movie Card Contains Thumbnail")
def test_tc023_verify_movie_card_contains_thumbnail(app):

    discover = DiscoverPage(app)

    assert discover.get_first_card_thumbnail().is_visible()

@pytest.mark.tc_id("TC024")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Movie Card Contains Title")
def test_tc024_verify_movie_card_contains_title(app):

    discover = DiscoverPage(app)

    assert discover.get_first_card_title() != ""

@pytest.mark.tc_id("TC025")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify Movie Card Contains Genre")
def test_tc025_verify_movie_card_contains_genre(app):

    discover = DiscoverPage(app)

    assert discover.get_first_card_genre() != ""

@pytest.mark.tc_id("TC026")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify Movie Card Contains Release Year")
def test_tc026_verify_movie_card_contains_release_year(app):

    discover = DiscoverPage(app)

    year = discover.get_first_card_release_year()

    assert year.isdigit()
    assert len(year) == 4

