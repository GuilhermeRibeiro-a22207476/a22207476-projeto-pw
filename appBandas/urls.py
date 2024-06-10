from django.urls import path
from . import views

app_name = 'appBandas'

urlpatterns = [
    path('', views.listaBandas_view, name='bandas'),
    path('bandas/<int:banda_id>/', views.banda_view, name='bandaAlbuns'),
    path('albuns/<int:album_id>/', views.album_view, name='albumMusicas'),
    path('musicas/<int:musica_id>/', views.musica_view, name='musicas'),
    path('banda/novo', views.novo_banda_view, name="novo_banda"),
    path('banda/<int:banda_id>/edita', views.edita_banda_view, name="edita_banda"),
    path('banda/<int:banda_id>/apaga', views.apaga_banda_view, name="apaga_banda"),
    path('album/novo/', views.novo_album_view, name="novo_album"),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
