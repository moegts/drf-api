from django.urls import path

from .views import coffeListView, coffeDetailsView

urlpatterns = [
    path('', coffeListView.as_view(), name='coffeHouse_api'),  # /api/v1/posts/
    path('<int:pk>', coffeDetailsView.as_view(),
         name='coffeHouse_details_api'),  # /api/v1/posts/<int:pk>
]