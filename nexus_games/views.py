from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F, Value
from django.http import JsonResponse

def games(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Log in first to gain access. Thank you!')
    return render(request, "games/games.html", {"games": True})

def wordle(request):

    return render(request, "games/wordle.html", {
        "games": True,
    })
