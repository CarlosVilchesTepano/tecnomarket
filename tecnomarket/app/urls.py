from django.urls import path, include
from .views import MarcaViewset, ProductoViewset, agregar_producto, error_facebook,listado_productos, home, contacto,\
    galeria, listar_productos, modificar_producto, eliminar_producto, registro, MarcaSerializer
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('marca', MarcaViewset)

#localhost:8000/api/producto
urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('contacto/', contacto, name="contacto"),
    path('listado-productos/', listado_productos, name="listado_productos"),   
    path('agregar-producto/', agregar_producto, name="agregar_producto" ),
    path('listar-productos/', listar_productos, name="listar_productos" ),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto" ),  
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto" ),  
    path('registro/', registro, name="registro" ), 
    path('api/', include(router.urls)), 
    path('error-facebook/', error_facebook, name= "error_facebook"),
    
]