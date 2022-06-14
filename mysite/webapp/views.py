from cgitb import text
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "index2.html")

# def removepunc(request):
#     #get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     #analyze the text
#     return HttpResponse("remove punc")

# def capitalizefirst(request):
#     return HttpResponse("capitalize first")    

# def newlineremove(request):
#     return HttpResponse("remove new line") 

# def spaceremove(request):
#     return HttpResponse("remove space <a href='/'>back</a>") 

# def charcount(request):
#     return HttpResponse("charcount")   
#

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    # Chek checkbox valus
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    # check which box in on
    if removepunc == "on":
    #analyze the djtext
        punctuation = '''!()-[]{};:'\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        return render(request,"analyze2.html", params)
    elif(fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()   
        params = {'purpose':'Changed in Uppercase', 'analyzed_text':analyzed}  
        return render(request,"analyze2.html", params)
    elif(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char !="\n":
             analyzed = analyzed + char  
        params = {'purpose':'Remove New Lines', 'analyzed_text':analyzed}  
        return render(request,"analyze2.html", params)
    elif(extraspaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
             analyzed = analyzed + char  
        params = {'purpose':'Remove Extra Space', 'analyzed_text':analyzed}  
        return render(request,"analyze2.html", params)
    
