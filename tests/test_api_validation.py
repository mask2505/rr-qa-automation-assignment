import pytest

from pages.discover_page import DiscoverPage


@pytest.mark.tc_id("TC036")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Category Filter API Response Status Is 200")
def test_tc036_verify_category_filter_api_status(app):

    responses = []

    app.on(
        "response",
        lambda response: responses.append(response)
    )

    discover = DiscoverPage(app)

    discover.click_trending()

    app.wait_for_timeout(3000)

    category_response = next(
        (
            response
            for response in responses
            if "/discover/" in response.url
            or "/trending/" in response.url
        ),
        None
    )

    assert category_response is not None
    assert category_response.status == 200

@pytest.mark.tc_id("TC037")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Search API Response Status Is 200")
def test_tc037_verify_search_api_status(app):

    responses = []

    app.on(
        "response",
        lambda response: responses.append(response)
    )

    discover = DiscoverPage(app)

    discover.search_movie("Batman")

    app.wait_for_timeout(3000)

    search_response = next(
        (
            response
            for response in responses
            if "/search/" in response.url
        ),
        None
    )

    assert search_response is not None
    assert search_response.status == 200

@pytest.mark.tc_id("TC038")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify Discovery Filter API Response Status Is 200")
def test_tc038_verify_discovery_filter_api_status(app):

    responses = []

    app.on(
        "response",
        lambda response: responses.append(response)
    )

    discover = DiscoverPage(app)

    discover.select_type("Movie")
    discover.select_genre("Action")

    app.wait_for_timeout(3000)

    filter_response = next(
        (
            response
            for response in responses
            if "/discover/" in response.url
        ),
        None
    )

    assert filter_response is not None
    assert filter_response.status == 200

@pytest.mark.tc_id("TC039")
def test_tc039_verify_ui_movie_title_matches_api(app):

    captured = {}

    def capture_response(response):
        if "trending/movie/week" in response.url:
            captured["data"] = response.json()

    app.on("response", capture_response)

    discover = DiscoverPage(app)

    discover.click_trending()

    app.wait_for_timeout(5000)

    assert "data" in captured, "Trending API response not captured"

    api_title = (
        captured["data"]["results"][0].get("title")
        or
        captured["data"]["results"][0].get("name")
    )

    ui_title = discover.get_first_card_title()

    print(f"API Title: {api_title}")
    print(f"UI Title : {ui_title}")

    assert ui_title == api_title

@pytest.mark.tc_id("TC040")
@pytest.mark.priority("P0")
@pytest.mark.title("Verify UI Movie Count Matches API Response")
def test_tc040_verify_ui_movie_count_matches_api(app):

    captured = {}

    def capture_response(response):
        if "trending/movie/week" in response.url:
            captured["data"] = response.json()

    app.on("response", capture_response)

    discover = DiscoverPage(app)

    discover.click_trending()

    app.wait_for_timeout(5000)

    assert "data" in captured, (
        "Trending API response not captured"
    )

    api_count = len(
        captured["data"]["results"]
    )

    ui_count = discover.get_card_count()

    print(f"API Count: {api_count}")
    print(f"UI Count : {ui_count}")

    assert ui_count == api_count