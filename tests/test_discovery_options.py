import pytest

from pages.discover_page import DiscoverPage


@pytest.mark.tc_id("TC009")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify Type Filter Dropdown Shows Movies And TV Shows")
def test_tc009_verify_type_dropdown_options(app):

    discover = DiscoverPage(app)

    options = discover.get_type_options()

    assert "Movie" in options
    assert "TV Shows" in options


@pytest.mark.tc_id("TC010")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Movies Type Filter")
def test_tc010_verify_movies_filter(app):

    discover = DiscoverPage(app)

    app.wait_for_timeout(10000)

    assert discover.get_selected_type() == "Movie"

    assert discover.get_card_count() > 0


@pytest.mark.tc_id("TC011")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify TV Shows Type Filter")
def test_tc011_verify_tvshows_filter(app):

    discover = DiscoverPage(app)

    discover.select_type("TV Shows")

    assert discover.get_selected_type() == "TV Shows"

    assert discover.get_card_count() > 0


@pytest.mark.tc_id("TC012")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify Genre Dropdown Shows Available Genres")
def test_tc012_verify_genre_dropdown_options(app):

    discover = DiscoverPage(app)

    genres = discover.get_genre_options()

    expected_genres = [
        "Action",
        "Adventure",
        "Animation",
        "Comedy",
        "Crime",
        "Documentary",
        "Drama"
    ]

    for genre in expected_genres:
        assert genre in genres, f"{genre} not found in Genre dropdown"


@pytest.mark.tc_id("TC013")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Genre Filter Functionality")
def test_tc013_verify_genre_filter(app):

    discover = DiscoverPage(app)

    discover.select_genre("Action")
    app.wait_for_timeout(3000)

    assert discover.get_card_count() > 0


@pytest.mark.tc_id("TC014")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify Year Range Selection")
def test_tc014_verify_year_range_selection(app):

    discover = DiscoverPage(app)

    discover.select_from_year("2020")
    discover.select_to_year("2025")

    assert discover.get_selected_from_year() == "2020"
    assert discover.get_selected_to_year() == "2025"

    app.wait_for_timeout(3000)
    assert discover.get_card_count() > 0


@pytest.mark.tc_id("TC015")
@pytest.mark.priority("P1")
@pytest.mark.title("Verify Invalid Year Range Handling")
def test_tc015_verify_invalid_year_range(app):

    discover = DiscoverPage(app)

    discover.select_from_year("2025")
    discover.select_to_year("2020")
    app.wait_for_timeout(3000)
    assert (
        discover.get_selected_from_year()
        <=
        discover.get_selected_to_year()
    ), "Application allowed invalid year range"


@pytest.mark.tc_id("TC016")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Rating Filter Functionality")
def test_tc016_verify_rating_filter(app):

    discover = DiscoverPage(app)

    discover.select_rating(4)
    app.wait_for_timeout(3000)

    assert discover.get_card_count() > 0


@pytest.mark.tc_id("TC017")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Multiple Filters Applied Together")
def test_tc017_verify_multiple_filters(app):

    discover = DiscoverPage(app)

    discover.select_type("Movie")
    discover.select_genre("Action")
    discover.select_from_year("2020")
    discover.select_to_year("2025")
    app.wait_for_timeout(3000)
    discover.select_rating(4)
    app.wait_for_timeout(3000)
    assert discover.get_card_count() > 0