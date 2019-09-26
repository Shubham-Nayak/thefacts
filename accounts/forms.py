from django import forms
from .models import SliderImage,BlogSpots

class BlogSpotsForm(forms.ModelForm):
    class Meta:
        model=BlogSpots
        fields=[
            
            'title',
            'heading1',
            'heading2',
            'content1',
            'content2',
            'keywords',
            'links',
            'catagory',
            'images',
            'thumbnils'

           
        ]
        widgets={
                  
                   "title":forms.TextInput(attrs={'placeholder':'Title','name':'lastname','id':'inputname','class':'form-control','type':'text'}),
                   "heading1":forms.TextInput(attrs={'placeholder':'heading1','name':'heading1','id':'inputname','class':'form-control','type':'text'}),
                   "heading2":forms.TextInput(attrs={'placeholder':'heading2','name':'heading2','id':'inputname','class':'form-control','type':'text'}),
                   "content1":forms.Textarea(attrs={'placeholder':'content1','name':'content1','id':'exampleFormControlTextarea1','class':'form-control','type':'text'}),
                   "content2":forms.Textarea(attrs={'placeholder':'content2','name':'content2','id':'exampleFormControlTextarea1','class':'form-control','type':'text'}),
                   "keywords":forms.TextInput(attrs={'placeholder':'keywords','name':'keywords','id':'inputname','class':'form-control','type':'text'}),
                   "links":forms.TextInput(attrs={'placeholder':'links','name':'links','id':'inputname','class':'form-control','type':'text'}),
                   "catagory":forms.TextInput(attrs={'placeholder':'catagory','name':'catagory','id':'inputname','class':'form-control','type':'text'}),
                   "thumbnils":forms.ClearableFileInput(attrs={'name':'thumbnils','id':'inputname','class':'form-control','type':'file'}),
                   "images":forms.ClearableFileInput(attrs={'name':'images','id':'inputname','class':'form-control','type':'file'}),
                   
                   
                } 