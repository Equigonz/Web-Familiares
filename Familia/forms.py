from django import forms 

class Formulario_familia(forms.Form):
      name = forms.CharField(max_length=40)
      parentezco = forms.CharField(max_length=40)

  #  name = models.CharField(max_length=40)
   # parentezco = models.CharField(max_length=40)
    # nacimiento = models.DateField(auto_now_add=True, null=True, blank=True)