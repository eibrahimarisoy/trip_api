def FilterDeviceTypeMiddleware(get_response):

    def middleware(request):
        if request.path == "/api/v1/passengers/" and request.method == "POST":
            device_type = request.headers.get('user-agent')
            my_request = request.POST.copy()
            my_request["device_type"] = device_type
            request.POST = my_request

        response = get_response(request)

        return response

    return middleware