from rest_framework import serializers

from .models import (
    Storage,
    StorageCat,
    StorageResp,
    StorageState,
    StorageSubcat,
    Users
)


class StoragesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageCat
        fields = '__all__'

class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageSubcat
        fields = '__all__'

class RespsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageResp
        fields = '__all__'

class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageState
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'