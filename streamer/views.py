from django.shortcuts import render
from django.http import StreamingHttpResponse 
import time
from .sentances import get_random_sentence


def streamerView(request):
    def stream_content():
        for i in range(1000):
            time.sleep(1)
            formatted_time = time.strftime('%M:%S', time.localtime())
            yield f"Date: {i} - Time: {formatted_time}\n"
    return StreamingHttpResponse(stream_content(), content_type='text/plain')


def streamText(request):
    speed = request.GET.get("speed")
    renderSpeed = float(speed)
    print(speed)
    sentence = get_random_sentence()
    def stream_content():
        print(sentence)
        for char in sentence:
            time.sleep(renderSpeed)
            yield char
            
    response = StreamingHttpResponse(stream_content(), content_type='text/plain')
    response['content-length'] = len(sentence)
    return response
