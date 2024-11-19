from django import forms

class ItemForm(forms.ModelForm):
    name = forms.CharField(max_length=100, min_length=1)
    count = forms.IntegerField()
    type = forms.IntegerField()
    status = forms.IntegerField()
    is_consumable = forms.BooleanField()
    price = forms.DecimalField()
    image = forms.ImageField()
    overdue = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    link = forms.URLField()
    description = forms.Textarea()
    owner = forms.IntegerField()
