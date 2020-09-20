from django.contrib import admin

from .models import (
    Storage,
    StorageCat,
    StorageResp,
    StorageState,
    StorageSubcat,
    Users
)


admin.site.register(Storage)
admin.site.register(StorageCat)
admin.site.register(StorageResp)
admin.site.register(StorageState)
admin.site.register(StorageSubcat)
admin.site.register(Users)
