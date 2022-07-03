from xml.dom.minidom import Document
from django.urls import path

from libreria import carrito
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros', views.libros, name='libros'),
    path('libros_normaluser', views.libros, name='libros_normaluser'),
    path('mangas', views.mangas, name='mangas'),
    path('comics', views.comics, name='comics'),
    path('libros/crear_libro', views.crear_libro, name='crear_libro'),
    path('libros/crear_manga', views.crear_manga, name='crear_manga'),
    path('libros/crear_comic', views.crear_comic, name='crear_comic'),
    path('libros/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>', views.editar, name='editar'),
    path('login', views.Login, name='login'),
    path('registro', views.Registro, name='registro'),
    path('logout', views.Logout, name='logout'),
    path('agregar/<int:id>/', views.agregar_articulo, name="agregar"),
    path('eliminar/<int:id>/', views.eliminar_articulo, name="eliminar"),
    path('restar/<int:id>/', views.restar_articulo, name="restar"),
    path('limpiar', views.limpiar_carrito, name="limpiar"),
    path("horario", views.horario, name="horario"),
    path('grafico', views.grafico, name='grafico'),
    path("exportar", views.article_list, name="exportar"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('update_item', views.updateItem, name="update_item"),
    path('process_order', views.processOrder, name="process_order"),
    path('Descargar', views.article_list, name="Descargar"),



    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)