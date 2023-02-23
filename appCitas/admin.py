from django.contrib import admin
from .models.usuario import Usuario
from .models.perfil import Perfil
from .models.mensaje import Mensaje
from .models.match import Match
from .models.likes import Likes
from .models.foto import Foto

admin.site.register(Usuario)
admin.site.register(Perfil)
admin.site.register(Mensaje)
admin.site.register(Match)
admin.site.register(Foto)
admin.site.register(Likes)

# Register your models here.
