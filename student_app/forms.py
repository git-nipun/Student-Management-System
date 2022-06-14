from student_app.models import facultydetail, studentdetail
from django import forms

class studentform(forms.ModelForm):
    class Meta:
        model=studentdetail
        fields='__all__'

class facultyform(forms.ModelForm):
    class Meta:
        model=facultydetail
        fields='__all__'
