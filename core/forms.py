from django import forms
from .models import Hack

class HackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'w-full rounded-md p-2 mb-2 border border-indigo-500'})

    class Meta:
        model = Hack
        fields = '__all__'