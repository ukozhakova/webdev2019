from django.shortcuts import render
from django.http import HttpResponse


def signup(request):
    return HttpResponse('<p>If I could write a story,</p>'
    '<p>It would be the greatest ever told.</p>'
    '<p>I had write about my daddy,'
    '<p>For he had a heart of gold.'
    '<p>My dad, he was no hero '
    '<p>Known around this world.'
    '<p>He was everything to me,'
    '<p>For I was his baby girl.'
    '<p>I had write about the lessons.')

