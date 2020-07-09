from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View
# Create your views here.

class IndexClass(View):
    def get(self, request):
        ketqua = "12343434"
        return HttpResponse(ketqua)

class PostClass(View):
    def get(self, request):
        a = PostForm()
        return render(request, 'news/add_news.html', {'f':a})

class ClassSaveNews(View):
    def post(self, request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('luu oke')
        else:
            return HttpResponse('không được validate')

def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html', {'f':b})

def process(request):
    if request.method == "POST":
        m=SendEmail(request.POST)
        if m.is_valid():
            tieude = m.cleaned_data['title']
            cc = m.cleaned_data['cc']
            noidung = m.cleaned_data['content']
            email = m.cleaned_data['email']
            context = {'td':tieude, 'c':cc, 'b':noidung, 'd':email}
            return render(request, 'news/print_email.html', context)
        else:
            return('form not validate ')
    else:
        return HttpResponse('Khong phai post method')