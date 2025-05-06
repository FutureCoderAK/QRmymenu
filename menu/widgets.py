from django.forms.widgets import SelectMultiple

class DisabledChoicesSelectMultiple(SelectMultiple):
    def __init__(self, *args, disabled_choices=None, **kwargs):
        self.disabled_choices = disabled_choices or []
        super().__init__(*args, **kwargs)

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        if value in self.disabled_choices:
            option['attrs']['disabled'] = 'disabled'
        
        return option