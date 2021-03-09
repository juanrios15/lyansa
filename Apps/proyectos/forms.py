from django import forms
from .models import Proyecto, Categoria
from ckeditor.fields import RichTextFormField, CKEditorWidget



class CrearProyectoForm(forms.ModelForm):
    
    descripcion = RichTextFormField(config_name="refault")
    Categories = forms.ModelMultipleChoiceField(
        label='Categories',
        
        required=True,
        queryset=Categoria.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                'class': "form-select",
                'id': "inputcat",
                'size': "6"
            }
        )
    )
    
    class Meta:
        model = Proyecto
        fields = [
            'nombre',
            'year',
            'resumen',
            'Categories',
            'descripcion',
            'imagen',
            'publico',
        ]
        widgets={

            'nombre': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'id': 'inputnombre'
                }
            ),
            'year': forms.NumberInput(
                attrs={
                    'class': "form-control",
                    'id': 'inputyear'
                }
            ),
            'resumen': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'id': 'inputresumen'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': "form-control",
                    'id': 'inputimg'
                }
            )
            
        }