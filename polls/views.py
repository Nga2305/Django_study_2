from django.http import HttpResponse

# A view function, or “view” for short, is simply a Python function that takes a web request and returns a web response. 
# This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image, etc. Example: You use view to create web pages, note that you need to associate a view to a URL to see it as a web page.
# In Django, views have to be created in the app views.py file.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# In this view, we use HttpResponse to render the HTML (as you have probably noticed we have the HTML hard coded in the view).
# This is not the best way to render pages. Django supports the MVT pattern so to make the precedent view, Django - MVT like, 
# we will need − a template: myapp/templates/index.html (Học sau)
#  KHi đó views.py sẽ được trình bày như sau:
# from django.shortcuts import render
# def index(request):
#    return render(request, "myapp/template/index.html", {})