from django.shortcuts import render
from django.http import HttpResponse
import json

from .test_regex import parse_regex

# Create your views here.
def regex_post(request):
    return HttpResponse(parse_regex(
        request.POST.get("regex", ""),
        request.POST.get("test-string", "")
    ))

def regex_get(request):
    with open("static/maps/regex.json", "r") as f:
        reference = json.load(f)

    return render(request, "regex.html", {
        "reference": reference,
        "post_url": "/regex/test-regex/",
    })