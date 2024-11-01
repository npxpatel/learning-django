from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# def home(request):
#     html = "<html><body>Home page</body></html>"
#     return HttpResponse(html)

def home(request):
    return render(request, 'posts/home.html')


def post(request, id):
    # p = reverse('post',args = [id]);
    #print(p);
    if(id < 100) :
     return HttpResponse(id)
    else :
       return HttpResponseNotFound("Page not found")
    
def google(request, id):
#    return HttpResponseRedirect("https://www.google.com") 
     url = reverse('post', args=[id])   
     return HttpResponseRedirect(url)
  

# we can add names to the urls and use them in the templates, it is good becaues when we chnaneg the url
# we dont have to change the templates, reverse function is used to get the url from the name