from django.forms import ModelForm

from entertainment_db.models import Assessment


class AssessmentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Assessment
        fields = '__all__'
        exclude = ['user', 'content']
