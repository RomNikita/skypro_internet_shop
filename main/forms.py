from django import forms

from main.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in bad_words:
            if word in cleaned_data:
                raise forms.ValidationError('Название продукта не должно содержать такие слова')

        return cleaned_data


    def clean_description(self):
        cleanned_data = self.cleaned_data['description']
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in bad_words:
            if word in cleanned_data:
                raise forms.ValidationError('Описание продукта не должно содержать такие слова')

        return cleanned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'