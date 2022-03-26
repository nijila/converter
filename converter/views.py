from django.views.generic import base
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import inflect
from django.contrib import messages
import simplejson 

# Create your views here.
class index(base.View):
    def get(self, request):
        return render(request, 'home.html',{})
    def post(self, request):
        return render(request, 'home.html',{})

@csrf_exempt
def converttotext(request):
    print("hi")
    print(request.POST)
    value = request.POST.get('number')
    print(value)
    p = inflect.engine()
    num_to_word = p.number_to_words(value)
    # messages.success(request, num_to_word)
    # return {"data":num_to_word}
    return HttpResponse(simplejson.dumps({"success":num_to_word}),content_type="application/json")
