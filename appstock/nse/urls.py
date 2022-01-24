from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('stockNameCode/',views.stockNameCode, name = 'stockNameCode'),
    path('allStockStore/',views.allStockStore, name = 'allStockStore'),
    path('ViewJumpStock/',views.ViewJumpStock, name = 'ViewJumpStock'),
    path('shortView/',views.shortView, name = 'shortView'),
    path('shortViewData/',views.shortViewData, name = 'shortViewData'),
    path('getNSE_StocksDaily/',views.getNSE_StocksDaily, name = 'getNSE_StocksDaily'),
    path('stockHomeAnalysis/',views.stockHomeAnalysis, name = 'stockHomeAnalysis'),
    
    ]