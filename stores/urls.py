from django.urls import path
from . import views
from reviews import views as reviews

app_name = 'stores'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('detail/<int:pk>/reviews/create', reviews.create, name='reviews_create'),
    # path('detail/<int:store_pk>/reviews/<int:pk>/delete/', reviews.delete, name='reviews_delete'),
    # path('detail/<int:store_pk>/reviews/<int:pk>/update/', reviews.update, name='reviews_update'),
    # path('detail/<int:pk>/reviews/<int:pk>/comments/', reviews.comment_create, name='reviews_comment_create'),
    # path('detail/<int:pk>/reviews/<int:pk>/<int:comment_pk>/update/', reviews.comment_update, name='reviews_comment_update'),
    # path('detail/<int:pk>/reviews/<int:pk>/<int:comment_pk>/delete/', reviews.comment_delete, name='reviews_comment_delete'),
    # path('detail/<int:pk>/reviews/<int:pk>/like/', reviews.like, name='reviews_like'),
    path('detail/<int:pk>/like/', views.store_like, name='store_like'),
    path('search', views.search, name='search'),
]
