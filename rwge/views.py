from json import loads

from django.http import JsonResponse


def rwge_view(request):
    payload = loads(request.body)
    response = {}
    if payload.get('type') == 'MESSAGE':
        message_text = payload['message']['text']
        response['text'] = f'You said: "{message_text}"'

    return JsonResponse(response)
