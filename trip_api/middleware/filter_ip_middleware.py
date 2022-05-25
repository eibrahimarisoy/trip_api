def FilterIPMiddleware(get_response):

    def middleware(request):

        ip = request.META.get('REMOTE_ADDR')
        print(request.headers)
        print(ip)
        response = get_response(request)

        return response

    return middleware