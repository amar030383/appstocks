from django.contrib import admin
from .models import *
admin.site.register(GetStocksAngelOne)
admin.site.register(GetStocksHistoricData)
admin.site.register(GetStocksList)
admin.site.register(GetStocksDailyData)
admin.site.register(AnalysedStocksData)
admin.site.register(NoResultFoundStocks)
