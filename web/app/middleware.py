import json
from django.http import JsonResponse

class SimpleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            pass

        '''
        if response.status_code != 200:
            response.status_code = 400
            response.content = json.dumps(dict(message="Invalid arguments", status=400))
        '''
        return response


    def process_exception(self, request, response):
        data = dict(message=response.message, status_code=response.status)
        return JsonResponse(data)
