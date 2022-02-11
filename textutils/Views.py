#I have created this view file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


'''
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
'''


def analyse(request):
    #input of text
    djtext = request.POST.get('Text', 'default')  # return the value of Text, if value doesnot exist then will take
    # default value
    remove_p = request.POST.get('removepunc', 'off')
    capi = request.POST.get('capital', 'off')
    e_space = request.POST.get('e_space', 'off')
    new_line = request.POST.get('new_line', 'off')
    count = request.POST.get('char_count', 'off')

    if remove_p == "on":
        punctuations = '''!@#$%^&*()_-:;"'<>,.?/\|~`'''
        analysed_text = ""
        for char in djtext:
            if char not in punctuations:
                analysed_text = analysed_text + char
        param = {'purpose': 'Removing Punctuation', 'analysed': analysed_text}
        djtext = analysed_text

    if e_space == "on":
        analysed_text = ""
        for index, char in enumerate(djtext):  # enumerate return a list containing tuples each with two value :
            # index and value at index
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analysed_text = analysed_text + char
        param = {'purpose': 'Removing extra space', 'analysed': analysed_text}
        djtext = analysed_text

    if capi == "on":
        analysed_text = ""
        for char in djtext:
            analysed_text = analysed_text + char.upper()
        param = {'purpose': 'Captilising', 'analysed': analysed_text}
        djtext = analysed_text

    if new_line == "on":
        analysed_text = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analysed_text = analysed_text + char
        param = {'purpose': 'Removing new line ', 'analysed': analysed_text}
        djtext = analysed_text

    if count == "on":
        check = 0
        for i in range(0, len(djtext)):
            if djtext[i] != "":
                check = check + 1
        analysed_t = '\nNumber of character in the text is ' + str(check)
        analysed_text = analysed_text + analysed_t
        param = {'purpose': 'COUNTING CHARACTERS ', 'analysed': analysed_text}

    if remove_p != "on" and capi != "on" and new_line != "on" and e_space != "on" and count != "on":
        return HttpResponse('<h1>Error</h1>')
    else:
        return render(request, 'analyse.html', param)
