from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from .perfil import Perfil


class UserManager(BaseUserManager):
    def create_user(self, username, password = None):

        # Funcion que crea y guarda un usuario que tiene un username y una contraseña.

        if not username:
            ValueError('El usuario debe tener un username')
        user = self.model(username = username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
        username=username,
        password=password,
 )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key= True)
    username = models.CharField('Username', max_length=15, unique=True)
    password = models.CharField('Password', max_length=256)
    nombre = models.CharField('Nombre', max_length=25)
    apellidos = models.CharField('Apellidos', max_length=50)
    email = models.EmailField('Email', max_length=100)
    fechaNacimiento = models.DateField('FechaNacimiento', max_length=50)
    genero = models.CharField('Genero', max_length=20)
    intereses = models.CharField ('Intereses', max_length=250)
    perfil = models.OneToOneField (Perfil, on_delete=models.CASCADE, related_name='usuario' )


    def save (self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'

