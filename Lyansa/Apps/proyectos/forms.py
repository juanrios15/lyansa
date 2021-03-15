from django import forms
from .models import Proyecto, Categoria, Foto
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
        
class AgregarImagenForm(forms.ModelForm):
        
    class Meta:
        model = Foto
        fields = ('__all__')
        
        widgets= {
            'proyecto': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            )
        }
        
    #CON ESTO SE LE QUITA EL -------- AL INICIO DEL SELECT
    def __init__(self, *args, **kwargs):
        super(AgregarImagenForm, self).__init__(*args, **kwargs)
        self.fields['proyecto'].empty_label = None