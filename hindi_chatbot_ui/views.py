from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from hindi_chatbot_ui.polarity import polarity



# Create your views here.
sent_list = []
l1 = []
l2 = []
def index(request):
    if request.method == "POST":
        message = request.POST['message']
        l2.append(message)
        if polarity(message) > 0:
            l1.append("positive")
        elif polarity(message) < 0:
            l1.append("negative")
        elif polarity(message) == 0.0:
            l1.append("neutral")
        if message == "समाप्त":
            l1.clear() 
            l2.clear()
        mylist = zip(l1, l2)
        return HttpResponseRedirect(reverse("index"))
    else:
        
        mylist = zip(l1, l2)

        return render(request, "hindi_chatbot_ui/index.html", {
            "mylist": mylist
        })       