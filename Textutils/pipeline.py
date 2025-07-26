from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>HOME</h1><br><p>Click Next</p><br><button><a href='http://127.0.0.1:8000/Shivendra'>Next</a></button>")

def Shivendra(request):
    return HttpResponse("<h1>Hellow Shivendra ! Where is pratap ??</h1><br><button><a href='http://127.0.0.1:8000/'>Previous</a></button> <button><a href='http://127.0.0.1:8000/Pratap'>Next</a></button>")

def Pratap(request):
    return HttpResponse("<h1>Ohhh! Pratap you are here... now where is Singh??</h1><br><button><a href='http://127.0.0.1:8000/Shivendra'>Previous</a></button> <button><a href='http://127.0.0.1:8000/Singh'>Next</a></button>")

def Singh(request):
    return HttpResponse("<h1>Finally Singh but, Chauhan??</h1><br><button><a href='http://127.0.0.1:8000/Pratap'>Previous</a></button> <button><a href='http://127.0.0.1:8000/Chauhan'>Next</a></button>")

def Chauhan(request):
    return HttpResponse("<h1>ummm Chauhan jiii..... click next!!</h1><br><button><a href='http://127.0.0.1:8000/Singh'>Previous</a></button> <button><a href='http://127.0.0.1:8000/Fullname'>Next</a></button>")

def Fullname(request):
    return HttpResponse("<h1>Shivendra Pratap Singh Chauhan</h1><br><button> <a href='http://127.0.0.1:8000/Chauhan'>Previous</a></button>")