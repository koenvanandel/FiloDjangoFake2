from django import forms

class QuestionForm(forms.Form):
    question = forms.CharField(label='Your Question')
    philosopher = forms.ChoiceField(choices=[('Socrates', 'Socrates'), ('Plato', 'Plato'), ('Aristotle', 'Aristotle')])