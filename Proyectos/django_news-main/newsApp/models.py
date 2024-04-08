from unicodedata import category
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    """
    Modelo para representar categorías de publicaciones.

    Atributos:
        name (CharField): El nombre de la categoría.
        status (CharField): El estado de la categoría (Activa/Inactiva).
        date_created (DateTimeField): La fecha de creación de la categoría.
        date_updated (DateTimeField): La fecha de actualización de la categoría.
    """

    name = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(("1", 'Active'), ("2", 'Inactive')), default="1")
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    Modelo para representar publicaciones.

    Atributos:
        user (ForeignKey): El usuario que crea la publicación.
        category (ForeignKey): La categoría a la que pertenece la publicación.
        title (TextField): El título de la publicación.
        short_description (TextField): La descripción corta de la publicación.
        content (TextField): El contenido principal de la publicación.
        banner_path (ImageField): La ruta del banner de la publicación.
        status (CharField): El estado de la publicación (Publicada/No publicada).
        meta_keywords (TextField): Las palabras clave de la publicación.
        date_created (DateTimeField): La fecha de creación de la publicación.
        date_updated (DateTimeField): La fecha de actualización de la publicación.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="")
    title = models.TextField()
    short_description = models.TextField()
    content = models.TextField()
    banner_path = models.ImageField(upload_to='news_banner')
    status = models.CharField(max_length=2, choices=(("1", 'Published'), ("2", 'Unpublished')), default="2")
    meta_keywords = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

class Comment(models.Model):
    """
    Modelo para representar comentarios en publicaciones.

    Atributos:
        post (ForeignKey): La publicación a la que pertenece el comentario.
        name (CharField): El nombre del autor del comentario.
        email (CharField): El correo electrónico del autor del comentario.
        subject (CharField): El asunto del comentario.
        message (TextField): El contenido del comentario.
        date_created (DateTimeField): La fecha de creación del comentario.
        date_updated (DateTimeField): La fecha de actualización del comentario.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.post.title}"
