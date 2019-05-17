from crispy_forms.layout import Div


class Col(Div):
    css_class = 'col'

    def __init__(self,  *args,  **kwargs):
        if 'css_class' in kwargs:
            self.css_class = kwargs['css_class']
        super().__init__(*args, **kwargs)


class Row(Div):
    css_class = 'row'
