from django import forms
from .models import BlogProject
from django.core.exceptions import ValidationError


class BlogForm(forms.ModelForm):
    MAX_IMAGE_SIZE_MB = 5

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    owner = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = BlogProject
        fields = ['title', 'description', 'owner', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                raise ValidationError(f"Image must be under {self.MAX_IMAGE_SIZE_MB}MB")
            if image.content_type not in ['image/jpeg', 'image/png']:
                raise ValidationError("Unsupported image format. Only JPEG and PNG are allowed.")
        return image
