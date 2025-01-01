
from django.contrib import admin
from django.urls import path, include
import debug_toolbar

admin.site.site_header = 'Meli_Evagelikon Admin'
admin.site.index_title = 'Evagelikon administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]


