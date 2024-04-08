from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from newsApp import models, forms
import json

def context_data():
    """
    Función para obtener datos de contexto comunes para las vistas.

    Returns:
        dict: Diccionario con datos de contexto.
    """
    context = {
        'site_name': 'NewsUp',
        'page': 'home',
        'page_title': 'News Portal',
        'categories': models.Category.objects.filter(status=1).all(),
    }
    return context

def home(request):
    """
    Vista para la página de inicio.

    Returns:
        HttpResponse: Renderiza el template 'home.html' con el contexto proporcionado.
    """
    context = context_data()
    posts = models.Post.objects.filter(status=1).order_by('-date_created').all()
    context['page'] = 'home'
    context['page_title'] = 'Home'
    context['latest_top'] = posts[:2]
    context['latest_bottom'] = posts[2:12]
    return render(request, 'home.html', context)

def login_user(request):
    """
    Vista para el inicio de sesión de usuario.

    Returns:
        HttpResponse: Respuesta JSON indicando el estado del inicio de sesión.
    """
    logout(request)
    resp = {"status": 'failed', 'msg': ''}
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            resp['status'] = 'success'
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp), content_type='application/json')

def logoutuser(request):
    """
    Vista para cerrar sesión de usuario.

    Returns:
        HttpResponse: Redirección a la página de inicio.
    """
    logout(request)
    return redirect('/')

@login_required
def update_profile(request):
    """
    Vista para actualizar el perfil de usuario.

    Returns:
        HttpResponse: Renderiza el template 'update_profile.html' con el formulario de actualización de perfil.
    """
    context = context_data()
    context['page_title'] = 'Update Profile'
    user = User.objects.get(id=request.user.id)
    if not request.method == 'POST':
        form = forms.UpdateProfile(instance=user)
        context['form'] = form
    else:
        form = forms.UpdateProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been updated")
            return redirect("profile-page")
        else:
            context['form'] = form
    return render(request, 'update_profile.html', context)

@login_required
def update_password(request):
    """
    Vista para actualizar la contraseña de usuario.

    Returns:
        HttpResponse: Renderiza el template 'update_password.html' con el formulario de actualización de contraseña.
    """
    context = context_data()
    context['page_title'] = "Update Password"
    if request.method == 'POST':
        form = forms.UpdatePasswords(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Account Password has been updated successfully")
            update_session_auth_hash(request, form.user)
            return redirect("profile-page")
        else:
            context['form'] = form
    else:
        form = forms.UpdatePasswords(request.POST)
        context['form'] = form
    return render(request, 'update_password.html', context)

@login_required
def profile(request):
    """
    Vista para la página de perfil de usuario.

    Returns:
        HttpResponse: Renderiza el template 'profile.html' con el contexto proporcionado.
    """
    context = context_data()
    context['page'] = 'profile'
    context['page_title'] = "Profile"
    return render(request, 'profile.html', context)

@login_required
def manage_post(request, pk=None):
    """
    Vista para manejar publicaciones (crear o editar).

    Args:
        pk (int, optional): El ID de la publicación a editar. Por defecto, None.

    Returns:
        HttpResponse: Renderiza el template 'manage_post.html' con el contexto proporcionado.
    """
    context = context_data()
    if not pk is None:
        context['page'] = 'edit_post'
        context['page_title'] = 'Edit Post'
        context['post'] = models.Post.objects.get(id=pk)
    else:
        context['page'] = 'new_post'
        context['page_title'] = 'New Post'
        context['post'] = {}

    return render(request, 'manage_post.html', context)

@login_required
def save_post(request):
    """
    Vista para guardar una publicación.

    Returns:
        HttpResponse: Respuesta JSON indicando el estado de la operación.
    """
    resp = {'status': 'failed', 'msg': '', 'id': None}
    if request.method == 'POST':
        if request.POST['id'] == '':
            form = forms.savePost(request.POST, request.FILES)
        else:
            post = models.Post.objects.get(id=request.POST['id'])
            form = forms.savePost(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            if request.POST['id'] == '':
                postID = models.Post.objects.all().last().id
            else:
                postID = request.POST['id']
            resp['id'] = postID
            resp['status'] = 'success'
            messages.success(request, "Post has been saved successfully.")
        else:
            for field in form:
                for error in field.errors:
                    if not resp['msg'] == '':
                        resp['msg'] += str('<br />')
                    resp['msg'] += str(f"[{field.label}] {error}")
    else:
        resp['msg'] = "Request has no data sent."
    return HttpResponse(json.dumps(resp), content_type="application/json")

def view_post(request, pk=None):
    """
    Vista para ver una publicación.

    Args:
        pk (int, optional): El ID de la publicación a visualizar. Por defecto, None.

    Returns:
        HttpResponse: Renderiza el template 'single_post.html' con el contexto proporcionado.
    """
    context = context_data()
    post = models.Post.objects.get(id=pk)
    context['page'] = 'post'
    context['page_title'] = post.title
    context['post'] = post
    context['latest'] = models.Post.objects.exclude(id=pk).filter(status=1).order_by('-date_created').all()[:10]
    context['comments'] = models.Comment.objects.filter(post=post).all()
    context['actions'] = False
    if request.user.is_superuser or request.user.id == post.user.id:
        context['actions'] = True
    return render(request, 'single_post.html', context)

def save_comment(request):
    """
    Vista para guardar un comentario.

    Returns:
        HttpResponse: Respuesta JSON indicando el estado de la operación.
    """
    resp = {'status': 'failed', 'msg': '', 'id': None}
    if request.method == 'POST':
        if request.POST['id'] == '':
            form = forms.saveComment(request.POST)
        else:
            comment = models.Comment.objects.get(id=request.POST['id'])
            form = forms.saveComment(request.POST, instance=comment)

        if form.is_valid():
            form.save()
            if request.POST['id'] == '':
                commentID = models.Post.objects.all().last().id
            else:
                commentID = request.POST['id']
            resp['id'] = commentID
            resp['status'] = 'success'
            messages.success(request, "Comment has been saved successfully.")
        else:
            for field in form:
                for error in field.errors:
                    if not resp['msg'] == '':
                        resp['msg'] += str('<br />')
                    resp['msg'] += str(f"[{field.label}] {error}")
    else:
        resp['msg'] = "Request has no data sent."
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def list_posts(request):
    """
    Vista para listar todas las publicaciones.

    Returns:
        HttpResponse: Renderiza el template 'posts.html' con el contexto proporcionado.
    """
    context = context_data()
    context['page'] = 'all_post'
    context['page_title'] = 'All Posts'
    if request.user.is_superuser:
        context['posts'] = models.Post.objects.order_by('-date_created').all()
    else:
        context['posts'] = models.Post.objects.filter(user=request.user).all()

    context['latest'] = models.Post.objects.filter(status=1).order_by('-date_created').all()[:10]
    return render(request, 'posts.html', context)

def category_posts(request, pk=None):
    """
    Vista para mostrar publicaciones por categoría.

    Args:
        pk (int, optional): El ID de la categoría. Por defecto, None.

    Returns:
        HttpResponse: Renderiza el template 'category.html' con el contexto proporcionado.
    """
    context = context_data()
    if pk is None:
        messages.error(request, "File not Found")
        return redirect('home-page')
    try:
        category = models.Category.objects.get(id=pk)
    except:
        messages.error(request, "File not Found")
        return redirect('home-page')

    context['category'] = category
    context['page'] = 'category_post'
    context['page_title'] = f'{category.name} Posts'
    context['posts'] = models.Post.objects.filter(status=1, category=category).all()
    context['latest'] = models.Post.objects.filter(status=1).order_by('-date_created').all()[:10]
    return render(request, 'category.html', context)

@login_required
def delete_post(request, pk=None):
    """
    Vista para eliminar una publicación.

    Args:
        pk (int, optional): El ID de la publicación a eliminar. Por defecto, None.

    Returns:
        HttpResponse: Respuesta JSON indicando el estado de la operación.
    """
    resp = {'status': 'failed', 'msg': ''}
    if pk is None:
        resp['msg'] = 'Post ID is Invalid'
        return HttpResponse(json.dumps(resp), content_type="application/json")
    try:
        post = models.Post.objects.get(id=pk)
        post.delete()
        messages.success(request, "Post has been deleted successfully.")
        resp['status'] = 'success'
    except:
        resp['msg'] = 'Post ID is Invalid'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_comment(request, pk=None):
    """
    Vista para eliminar un comentario.

    Args:
        pk (int, optional): El ID del comentario a eliminar. Por defecto, None.

    Returns:
        HttpResponse: Respuesta JSON indicando el estado de la operación.
    """
    resp = {'status': 'failed', 'msg': ''}
    if pk is None:
        resp['msg'] = 'Comment ID is Invalid'
        return HttpResponse(json.dumps(resp), content_type="application/json")
    try:
        comment = models.Comment.objects.get(id=pk)
        comment.delete()
        messages.success(request, "Comment has been deleted successfully.")
        resp['status'] = 'success'
    except:
        resp['msg'] = 'Comment ID is Invalid'
    return HttpResponse(json.dumps(resp), content_type="application/json")