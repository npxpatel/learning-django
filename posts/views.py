from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

posts = [
    {
        "id": 1,
        "title": "Introduction to Django",
        "content": "Django is a high-level Python web framework.",
        "author": "Alice",
        "date": "2024-11-01"
    },
    {
        "id": 2,
        "title": "Learning Python Basics",
        "content": "Python is a versatile programming language.",
        "author": "Bob",
        "date": "2024-11-02"
    },
    {
        "id": 3,
        "title": "Advanced Django Topics",
        "content": "Exploring Django ORM, middleware, and more.",
        "author": "Charlie",
        "date": "2024-11-03"
    }
]

# Create your views here.
# def home(request):
#     html = "<html><body>Home page</body></html>"
#     return HttpResponse(html)

def home(request):
    # send context data as key value pair
    # return render(request, 'posts/home.html', {'name': 'Jitu Singh'})
    return render(request, 'posts/home.html', {'posts': posts})


def post(request, id):
    # p = reverse('post',args = [id]);
    #print(p);
    # if(id < 100) :
    #  return HttpResponse(id)
    # else :
    #    return HttpResponseNotFound("Page not found")
    post_data = next((post for post in posts if post["id"] == id), None)

    return render(request, 'posts/post.html' , {'post' : post_data})
    
def google(request, id):
#    return HttpResponseRedirect("https://www.google.com") 
     url = reverse('post', args=[id])   
     return HttpResponseRedirect(url)
  

# we can add names to the urls and use them in the templates, it is good becaues when we chnaneg the url
# we dont have to change the templates, reverse function is used to get the url from the name