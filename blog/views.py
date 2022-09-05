from django.shortcuts import render, redirect
from .models import Category, News
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.core.mail import send_mail
from django.contrib.auth.models import User

def logout_view(request):
    logout(request)
    return render(request, 'blog/index.html', context = {'modal_msg' : "Logout realizado com sucesso!"})


def notify_staff(msg):
    
    users = User.objects.all().filter(is_staff = 1)
    
    for user in users:
        subject = "Simulação envio de email" 
        body = {
        'first_name': user.first_name, 
        'last_name': user.last_name, 
        'email': user.email, 
        'message':msg, 
        }
        message = "\n".join(body.values())
        try:
            send_mail(subject, message, "admin@example.com", ['admin@example.com']) 
        except:
            pass
    
def home(request):
    return render(request, 'blog/index.html')
    # Redirect to a success page.
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'blog/index.html', context = {'modal_msg' : "Login realizado com sucesso!"})
        else:
            return render(request, 'blog/index.html', context = {'modal_msg' : "Erro ao logar"})
    return render(request, 'blog/login.html')
    
    
    
# @cache_page(60 * 10)
@login_required(login_url='/blog/login/')
def view_all_unpubli_posts(request):
    print("view_all_unpubli_posts")
    posts = News.objects.all()
    return render(request, 'blog/manage.html', context = {'posts' : posts})

# @cache_page(60 * 10)
def view_all_publi_posts(request, tech_pk = 0):
    tech_options = Category.objects.all()
    print("view_all_publi_posts")
    if tech_pk == 0:
        posts = News.objects.all().filter(publi = True)
    else:
        posts = News.objects.all().filter(publi = True, category_id = tech_pk)
    return render(request, 'blog/all_posts.html', context = {'posts' : posts, 'tech_options':tech_options})


def view_post(request, pk):
    try:
        post = News.objects.get(pk = pk)
        if post.publi or request.user.is_authenticated:
            return render(request, 'blog/view_post.html', context = {'post' : post})
        else:
            return render(request, 'blog/index.html', context = {'modal_msg' : "Sem permissão para visualizar essa postagem!"})
    except:
        return render(request, 'blog/index.html', context = {'modal_msg' : "Post inexistente!"})


@login_required(login_url='/blog/login/')
def delete_post(request, pk):
    try:
        News.objects.get(pk = pk).delete()
    except:
        pass
    return redirect("view_blog:all_unpubli_posts")


@login_required(login_url='/blog/login/')
def change_post_status(request, pk, publi):
    try:
        post = News.objects.get(pk = pk)
        post.publi = publi
        post.save()
    except:
        pass
    return redirect("view_blog:all_unpubli_posts")


@login_required(login_url='/blog/login/')
def create_post(request):
    
    tech_options = Category.objects.all()
    
    if request.method == 'POST':
            dict_form = {}
            for key, value in request.POST.items():
                if value != "":
                    dict_form[key] = value
                else:
                    return render(request, 'blog/create_post.html',{'modal_msg':"Todos os campos precisam ser preenchidos!",'tech_options':tech_options})
            try:          
                post = News()
                post.title = dict_form['Title']
                post.author = dict_form['Author']
                post.category_id = Category.objects.get(pk = dict_form['Tech'])   
                post.description = dict_form['Description']
                post.body_content = dict_form['BodyContent']
                post.save()    
                notify_staff("O seguinte post foi criado:\
                    Titulo: {post.title} \
                    Autor: {post.author} \
                    Descriação:{post.description} \
                    ")
                return render(request, 'blog/create_post.html',{'modal_msg':"Post criado com sucesso!",'tech_options':tech_options})
            except Exception as e:
                return render(request, 'blog/create_post.html',{'modal_msg':e,'tech_options':tech_options})
    else:
        return render(request, 'blog/create_post.html',{'tech_options':tech_options})
    
    
@login_required(login_url='/blog/login/')
def edit_post(request, pk):
    tech_options = Category.objects.all()
    post = News.objects.get(pk = pk)

    if request.method == 'POST':
            dict_form = {}
            for key, value in request.POST.items():
                if value != "":
                    dict_form[key] = value
                else:
                    return render(request, 'blog/edit_post.html',{'modal_msg':"Todos os campos precisam ser preenchidos!"})
            try:    
                      
                post = News.objects.get(pk = pk)
                post.title = dict_form['Title']
                post.author = dict_form['Author']
                post.category_id = Category.objects.get(pk = dict_form['Tech'])   
                post.description = dict_form['Description']
                post.body_content = dict_form['BodyContent']
                post.save()   
                notify_staff("O seguinte post foi editado:\
                            Titulo: {post.title} \
                            Autor: {post.author} \
                            Descriação:{post.description} \
                             ")
                return render(request, 'blog/edit_post.html',{'modal_msg':"Edição realizada com sucesso!",'tech_options':tech_options, 'post' : post})
            except Exception as e:
                return render(request, 'blog/edit_post.html',{'modal_msg':e,'tech_options':tech_options, 'post' : post})
    else:
        return render(request, 'blog/edit_post.html',{'tech_options':tech_options, 'post' : post})
    
