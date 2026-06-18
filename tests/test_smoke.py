def test_application_loads(app):
    print("Title:", app.title())
    print("URL:", app.url)

    assert app.url is not None
