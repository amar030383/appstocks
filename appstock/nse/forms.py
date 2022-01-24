from django.forms import ModelForm
from .models import  StockCodesAngelOne,JumpStock

class StockCodesAngelOneForm(ModelForm):
    class Meta:
        model = StockCodesAngelOne
        fields = '__all__'

class JumpStockForm(ModelForm):
    class Meta:
        model = JumpStock
        fields = '__all__'