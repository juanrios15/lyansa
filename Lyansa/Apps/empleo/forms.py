from django import forms

from .models import Empleo
from Apps.proyectos.models import Categoria
from ckeditor.fields import RichTextFormField, CKEditorWidget


class CrearEmpleoForm(forms.ModelForm):
    
    resumen = RichTextFormField(config_name="refault")
    Categories = forms.ModelMultipleChoiceField(
        label='Categorias',
        
        required=True,
        queryset=Categoria.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                'class': "form-select my-2",
                'id': "inputcat",
                'size': "6"
            }
        )
    )
    
    class Meta:
        model= Empleo
        fields=['titulo','resumen','Categories','proyecto','ubicacion','duracion','salario','publico']
        
        widgets={
            'titulo': forms.TextInput(
                attrs={
                    'class': "form-control my-2",
                }
            ),
            'proyecto': forms.TextInput(
                attrs={
                    'class': "form-control my-2",
                }
            ),
            'ubicacion': forms.TextInput(
                attrs={
                    'class': "form-control my-2",
                }
            ),
            'duracion': forms.TextInput(
                attrs={
                    'class': "form-control my-2",
                }
            ),
            'salario': forms.TextInput(
                attrs={
                    'class': "form-control my-2",
                }
            ),
            
        }
        
        