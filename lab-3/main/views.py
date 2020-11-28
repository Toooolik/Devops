import time
from django.shortcuts import render
from django.http import JsonResponse
import os


def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    response = dict(date= time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()),
                    current_page=request.get_full_path(),
                    server_info=os.uname().release,
                    client_info=os.getlogin())
    return JsonResponse(response)
