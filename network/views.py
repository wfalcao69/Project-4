from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import User


def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@csrf_exempt
@login_required
def compose(request):

    # Composing a new email must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Check recipient emails
    data = json.loads(request.body)
    #emails = [email.strip() for email in data.get("recipients").split(",")]
    #content = data.get("content", "")
    content = data.get("new_post", "")
    #content = request.POST.get(content, '')
    # Get contents of email
    #subject = data.get("subject", "")
    #body = data.get("body", "")
    if content == "":
        return JsonResponse({
            "error": "Empty post is not permitted."
        }, status=400)

    # Convert email addresses to users
    """recipients = []
    for email in emails:
        try:"""
            #user = User.objects.get(email=email)
    #username = request.user.username #request.session[user.username]  # authenticate(request, username=request.POST["username"], password=password)  username = request.POST["username"]
    creator = User.objects.get(username=request.user.username)
    post = Post(
        creator=creator,
        content=content
    )

    post.save()

    return JsonResponse({"message": "Post sent successfully."}, status=201)
