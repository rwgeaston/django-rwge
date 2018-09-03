import logging

from json import loads

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .rwge import get_response

logger = logging.getLogger('rwge')


@csrf_exempt
def rwge_view(request):
    payload = loads(request.body)
    response = {}
    if payload.get('type') == 'MESSAGE':
        text_response = rwge_check_message(payload)
        if text_response:
            logger.info(f'Replying to message "{payload["message"]}" with: "{text_response}"')
            response['text'] = text_response

    return JsonResponse(response)


def rwge_check_message(payload):
    """Check if this is an appropriate message to reply to and then generate a reply
    :param message: message object from discord.py library
    :return: None; will have side effects if appropriate
    """
    logger.info(payload)

    message_text = payload['message']['text']
    message_channel = payload.get('space', {}).get('displayName', 'unknown channel')
    author_name = payload['message'].get('displayName', 'unknown user')

    mentioned = False  # any((client.user.id == mention.id for mention in message.mentions))

    if mentioned:
        logger.info("I was mentioned")

    try:
        response = get_response(message_text, author_name, mentioned)
    except Exception as e:  # it's more useful to just log every failure here # pylint: disable=broad-except
        response = None
        logger.exception(e)
        logger.warning(f'Had an exception when replying to message "{message_text}" in {message_channel}')

    return response
