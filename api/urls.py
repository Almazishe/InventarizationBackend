from django.urls import path

from .views import (
    StoragesView,
    StorageView,
    RespsView,
    StatesView,
    UsersView,
    SubCategoriesView,
    CategoriesView,
    CategoryView,
    SubCategoryView,
    StateView,
    UserView,
    RespView,
    UpdateStorageView
)


urlpatterns = [
    path('storages/', StoragesView.as_view()),
    path('categories/', CategoriesView.as_view()),
    path('sub-categories/', SubCategoriesView.as_view()),
    path('users/', UsersView.as_view()),
    path('states/', StatesView.as_view()),
    path('resps/', RespsView.as_view()),


    path('storages/<sap>/', StorageView.as_view()),
    path('storages/update/<sap>', UpdateStorageView.as_view()),
    path('categories/<pk>/', CategoryView.as_view()),
    path('sub-categories/<pk>/', SubCategoryView.as_view()),
    path('states/<pk>/', StateView.as_view()),
    path('resps/<pk>/', RespView.as_view()),
    path('users/<pk>/', UserView.as_view()),
]
