from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
@login_required
def index(request):
    user = request.user
    user = request.user