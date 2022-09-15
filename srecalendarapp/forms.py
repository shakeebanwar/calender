# from socket import fromshare
from xmlrpc.client import DateTime
from django import forms
from .models import sre,offset,list_type,calendar_list
from .widgets import DateTimePickerInput

class calendarform(forms.ModelForm):
    type = forms.ModelChoiceField( queryset=list_type.objects.all())

    class Meta:
        model = calendar_list
        fields= ['type','start_date','end_date','description','sre']
        widgets= {
            'start_date' : DateTimePickerInput() ,
            'end_date' : DateTimePickerInput()
        }

    sre = forms.ModelChoiceField(queryset=sre.objects.all())

class offsetForm(forms.ModelForm):

    offset_start = forms.DateTimeInput()
    offset_end = forms.DateTimeInput()
    sre = forms.ModelChoiceField(queryset=sre.objects.all())

    def __init__(self, *args, **kwargs):
        super(offsetForm, self).__init__(*args, **kwargs)
        self.fields['offset_start'].label = "Offset Start Date"
        self.fields['offset_end'].label = "Offset End Date"
        self.fields['sre'].label = "User"
    class Meta: 
        model = offset
        fields = [
            'sre', 
            'offset_start', 
            'offset_end'
        ]
        
        widgets = {
            'offset_start': DateTimePickerInput(),
            'offset_end': DateTimePickerInput()
        }