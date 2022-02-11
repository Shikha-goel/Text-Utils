#I have created this view file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def Facebook(request):
    return HttpResponse('<a href = " https://www.facebook.com/"> Facebook </a> <a href = "/"> Back </a>')

def Instagram(request):
    return HttpResponse('<a href = "https://www.instagram.com/"> Instagram </a> <a href = "/"> Back </a>')

def Youtube(request):
    return HttpResponse('<a href = "https://www.youtube.com/" > Youtube </a> <a href = "/"> Back </a>')

def Google(request):
    return HttpResponse('<a href = "https://www.google.co.in/" > Google </a> <a href = "/"> Back </a>')

def Whatsapp(request):
    return HttpResponse('<a href = "https://www.whatsapp.com/"> Whatsapp </a> <a href = "/"> Back </a>')

def analyse(request):
    #input of text
    djtext = request.GET.get('Text','default')#return the value of Text, if value doesnot exist then will take default value
    remove_p = request.GET.get('removepunc','off')
    capi = request.GET.get('capital','off')
    e_space = request.GET.get('e_space','off')
    new_line = request.GET.get('new_line','off')
    count = request.GET.get('char_count','off')

    if remove_p == "on":
        punctuations =  '''!@#$%^&*()_-:;"'<>,.?/\|~`'''
        #param = {'analysed': analysed_text}
        analysed_text = ""
        for char in djtext:
            if char not in punctuations:
                analysed_text = analysed_text + char
        param = {'purpose':'Removing Punctuation','analysed': analysed_text}
    #analyse the text
        return render(request,'analyse.html',param)
    elif e_space == "on":
        analysed_text = ""
        for index,char in enumerate(djtext):#enumerate return a list containing tuples each with two value : index and value at index
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analysed_text = analysed_text + char
        param = {'purpose': 'Removing extra space', 'analysed': analysed_text}
        # analyse the text
        return render(request, 'analyse.html', param)

    elif capi == "on":
        analysed_text = ""
        for char in djtext:
            analysed_text = analysed_text + char.upper()
        param = {'purpose': 'Captilising', 'analysed': analysed_text}
        # analyse the text
        return render(request, 'analyse.html', param)

    elif new_line == "on":
        analysed_text = ""
        for char in djtext:
            if not(char == '\n'):
                analysed_text = analysed_text + char
        param = {'purpose': 'Removing new line ','analysed': analysed_text}
        # analyse the text
        return render(request, 'analyse.html', param)

    elif count == "on":
        analysed_text = ""
        check = 0
        for i in range (0, len(djtext)):
            if(djtext[i] != ""):
                check = check + 1

        analysed_text = 'Number of character in the text is' + str(check)
        param = {'purpose': 'COUNTING CHARACTERS ','analysed': analysed_text}
        # analyse the text
        return render(request, 'analyse.html', param)

    else:
        return HttpResponse('<h1>Error</h1>')