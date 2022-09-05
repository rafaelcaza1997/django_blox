from django.shortcuts import render, redirect

def home(request):
    return redirect("view_blog:all_publi_posts")

