from django.shortcuts import render
from django.http import HttpResponse  
import json

from .test_re import parse_re


def re_post(request):
    return HttpResponse(parse_re(
        re=request.POST.get("regex", ""), 
        s=request.POST.get("test-string", "")
    ))

def re_get(request):
    with open("static/maps/re.json", "r") as f:
        reference = json.load(f)
        
    return render(request, "re.html", {
        "reference": reference, 
        "post_url": "/test-re/",
    })