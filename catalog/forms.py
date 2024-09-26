from django import forms

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


    def clean_name(self):
        word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        clean_data = self.cleaned_data['name']
        if clean_data.lower() in word_list:
            raise forms.ValidationError('Запрещенное слово')
        return clean_data


    def clean_description(self):
        word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        clean_data = self.cleaned_data['description']
        if clean_data.lower() in word_list:
            raise forms.ValidationError('Запрещенное слово')
        return clean_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category_id', 'is_publication')
