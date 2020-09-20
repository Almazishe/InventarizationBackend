from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import filters

from .models import (
    Storage,
    StorageCat,
    StorageResp,
    StorageState,
    StorageSubcat,
    Users
)

from .serializers import (
    StatesSerializer,
    StoragesSerializer,
    SubCategoriesSerializer,
    RespsSerializer,
    UsersSerializer,
    CategoriesSerializer
)

from .paginations import CustomPagination


class StoragesView(ListAPIView):
    queryset = Storage.objects.all().order_by('sap')
    serializer_class = StoragesSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('sap', 'name',)
    pagination_class = CustomPagination

   
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        order = self.request.query_params.get('order', None)
        sign = self.request.query_params.get('sign', None)

        if order and sign:
            if sign == '+':
                sign = ''


            queryset = queryset.order_by((sign + order).strip())


          

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class StorageView(RetrieveAPIView):
    queryset = Storage.objects.all()
    serializer_class = StoragesSerializer
    lookup_field = 'sap'

class CategoryView(RetrieveAPIView):
    queryset = StorageCat.objects.all()
    serializer_class = CategoriesSerializer


class CategoriesView(ListAPIView):
    queryset = StorageCat.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'id',)

class SubCategoryView(RetrieveAPIView):
    queryset = StorageSubcat.objects.all()
    serializer_class = SubCategoriesSerializer

class SubCategoriesView(ListAPIView):
    queryset = StorageSubcat.objects.all()
    serializer_class = SubCategoriesSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'id', 'cat_id', )


class StateView(RetrieveAPIView):
    queryset = StorageState.objects.all()
    serializer_class = StatesSerializer

class StatesView(ListAPIView):
    queryset = StorageState.objects.all()
    serializer_class = StatesSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'id', )

class RespView(RetrieveAPIView):
    queryset = StorageResp.objects.all()
    serializer_class = RespsSerializer

class RespsView(ListAPIView):
    queryset = StorageResp.objects.all()
    serializer_class = RespsSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('id', 'user_id', 'firstname', 'secondname')

class UserView(RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersView(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('firstname', 'secondname')
    pagination_class = CustomPagination


