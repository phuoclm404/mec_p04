# forms.py
from django import forms
from .models import *


class HotelForm(forms.ModelForm ):
	hotel_Main_Img = forms.FileField(label="駐車情報")
	class Meta:
		model = Hotel
		fields = ['hotel_Main_Img']
	def __init__(self, *args, **kwargs):
		super(HotelForm, self).__init__(*args, **kwargs)
		self.fields['hotel_Main_Img'].widget.attrs['class'] = 'form-control'

	# img = forms.ImageField(label="PHUOC",widget=forms.TextInput(attrs={'class': 'form-control'}))
