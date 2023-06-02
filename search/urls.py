from django.urls import path


from.views import PostSearchApi


urlpatterns = [
    path('', PostSearchApi.as_view(), name='search')]