from django import forms
from catalog.models import Products, Version


class MixinStyle:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductsForms(MixinStyle, forms.ModelForm):
    class Meta:
        model = Products
        exclude = ('product_date_create', 'product_date_edit')

    def clean_product_name(self):
        cleaned_name = self.cleaned_data['product_name']
        forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
                           "радар"]
        for word in forbidden_words:
            if word in cleaned_name:
                raise forms.ValidationError(f'Запрещено истольвозвать слово {word}.')
            if word.title() in cleaned_name:
                raise forms.ValidationError(f'Запрещено истольвозвать слово {word}.')
        return cleaned_name

    def clean_product_text(self):
        cleaned_text = self.cleaned_data['product_text']
        forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
                           "радар"]
        for word in forbidden_words:
            if word.title() in cleaned_text:
                raise forms.ValidationError(f'Запрещено истольвозвать слово {word}.')
            if word in cleaned_text:
                raise forms.ValidationError(f'Запрещено истольвозвать слово {word}.')
        return cleaned_text


class VersionForms(MixinStyle, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
