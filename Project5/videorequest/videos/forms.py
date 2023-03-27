from django import forms

class VideoForm(forms.Form):
    video_name = forms.CharField(max_field=20, 
                                 required=False, 
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Name',
                                     'id': 'inputName'                                     
                                 }))
    video_desc = forms.CharField(widget=forms.Textarea({
        'class': 'form-control',
        'row': '5',
        'id': 'comment',
        'placeholder': 'Comment'
    }))
