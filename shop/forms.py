from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta():
        model = Review
        fields = ('review','rating')
        widgets ={
            'review':forms.Textarea(attrs={'class':'form-control', 'placeholder':'write your review here', 'rows':3, 'cols':40,}),
        }
        

    
