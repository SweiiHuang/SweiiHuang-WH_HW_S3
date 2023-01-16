from django.shortcuts import render,redirect
from .models import BlogPost
from .forms import UploadModelForm

# Create your views here.
def home(request):
    blogpost = BlogPost.objects.all() #查詢所有資料


    #將上傳表單傳送至Django Template(樣板)來進行顯示
    form = UploadModelForm()

    #驗證資料＆儲存
    if request.method == "POST":
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()         
            return redirect('/')
    
    context = {
        'posts': blogpost,
        'form': form
    }

    return render(request,'home.html',context)