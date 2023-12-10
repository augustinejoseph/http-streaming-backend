from django.shortcuts import render
from django.http import StreamingHttpResponse 
import time

def streamerView(request):
    def stream_content():
        for i in range(100):
            time.sleep(1)
            formatted_time = time.strftime('%M:%S', time.localtime())
            yield f"Date: {i} - Time: {formatted_time}\n"
    return StreamingHttpResponse(stream_content(), content_type='text/plain')
