def test_capture_network(app):

    def log_request(request):
        print(f"REQUEST : {request.method} {request.url}")

    def log_response(response):
        print(f"RESPONSE: {response.status} {response.url}")

    app.on("request", log_request)
    app.on("response", log_response)

    app.reload()

    app.wait_for_timeout(10000)
