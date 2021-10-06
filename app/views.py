from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import os


def index(request):
    if request.method == 'POST':
        myfile = request.FILES['code']

        dist = {"“": "\"", "”": "\"", "‘": "\'", "’": "\'", "–": "-", "—": "-", " ": " ", "…": "..."}
        ans = ""
        code = myfile.read()
        code = code.decode()

        for ch in code:
            if ord(ch) > 128:
                if ch in dist:
                    ans += dist[ch]
                else:
                    message = "A new Unicode if Found, Please contact administrator: "+ch
                    return render(request, 'index.html', {"error": message})
            else:
                ans += ch

        return render(request, 'index.html', {"ans": ans})
    return render(request, 'index.html')