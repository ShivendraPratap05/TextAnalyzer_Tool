# I have created tis file
# This is all about views.py which we have created for learning

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # param={'name':'Shivendra Pratap','place':'Kanpur'}
    # return render(request,'index.html',param)
    return render(request,'index.html')
 
def analyzer(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')
    
    if removepunc=="on"and uppercase=="on" :
        ana=" "
        punc='''"!()-{[]};:'\,<>./?@#$%^&*~`_"'''
        for char in djtext:
            if char not in punc:
                ana= ana + char.upper()
        param={'purpose':'to remove Punctuation and do UPPERCASE','analyze_text':ana}
        # return render(request,'analyzer.html',param)
        djtext=ana

    if removepunc=="on":
        punc='''"!()-{[]};:'\,<>./?@#$%^&*~`_"'''
        ana=""
        for char in djtext:
            if char not in punc:
                ana=ana +char
        param={'purpose':'Remove Punctuation','analyze_text':ana}
        # return render(request,'analyzer.html',param)
        djtext=ana
    
    if(uppercase=="on"):
        ana=" "
        for char in djtext:
            ana= ana + char.upper()
        param={'purpose':'Make the Text in UPPERCASE','analyze_text':ana}
        # return render(request,'analyzer.html',param)
        djtext=ana
    
    if(spaceremover=="on"):
        ana=""
        for i,char in enumerate(djtext):
            if not(djtext[i]==" " and djtext[i+1]==" "):
                ana=ana+char
        param={'purpose':'to remove the spaces','analyze_text':ana}
        # return render(request,'analyzer.html',param)
        djtext=ana
    
    if(charcount=="on"):
        ana=len(djtext)
        param={'purpose':'to count the character','analyze_text':ana}
        # return render(request,'analyzer.html',param)
        


    return render(request,'analyzer.html',param)