from django.conf.urls import url
from django.contrib import admin
from curdapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index_view),
    url(r'^create/',views.inserting_view),
    url(r'^retrieve/',views.retrieve_view),
    url(r'^update/',views.updating_view),
    url(r'^delete/',views.deleting_view)
]
