from django.urls import path

from .views import (
    StoragesView,
    StorageView,
    RespsView,
    StatesView,
    UsersView,
    SubCategoriesView,
    CategoriesView,
)


urlpatterns = [
    path('storages/', StoragesView.as_view()),
    path('categories/', CategoriesView.as_view()),
    path('sub-categories/', SubCategoriesView.as_view()),
    path('users/', UsersView.as_view()),
    path('states/', StatesView.as_view()),
    path('resps/', RespsView.as_view()),


    path('storages/<sap>/', StorageView.as_view()),
]
