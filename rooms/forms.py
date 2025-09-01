from django import forms
from django.core.exceptions import ValidationError

from .models import ImageMulti


class ImageMultiForm(forms.ModelForm):
    class Meta:
        model = ImageMulti
        fields = "__all__"
        
    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get("room")
        
        if not self.instance.pk and room:
            current_count = ImageMulti.objects.filter(
                room=room,
                active=True
            ).count()
            
            if current_count > 4:
                raise ValidationError("This is more than 5")
        
        return cleaned_data
    