from django.shortcuts import render

def post_lits(request):
    return render(request, 'blog/post_lits.html')
