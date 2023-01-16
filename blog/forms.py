from django import forms
from .models import BlogPost


#建立可以上傳文字＆圖片的表單
class UploadModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets={
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }

        labels = {
            'title': '文字內容',
            'image': '圖片檔案'
        }
