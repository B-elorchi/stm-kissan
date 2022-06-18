
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from multiprocessing import context
from unicodedata import name
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import Commndes, CategorieForms
from .models import newCommands, Categorie
from django.shortcuts import get_object_or_404
from django.core import mail
from django.core.mail import send_mail
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# ======================== Home Page ===============================


def home(request):
    context = {
        'datas': newCommands.objects.filter(Status=True),
        'cat': Categorie.objects.all(),
    }
    return render(request, 'index.html', context)
# ---------------------------------------------------------------
# ======================== Search Page ===============================


def Search(request):
    nameSearch = request.GET["serv"]
    context = {
        'data': newCommands.objects.filter(Status=True),
        'cat': Categorie.objects.filter(name_cat__icontains=nameSearch),
        "name": nameSearch,
    }
    return render(request, 'services.html', context)
# ---------------------------------------------------------------
# =========================All commands=============================


def AllCommand(request):
    if request.user.is_authenticated:
        context = {
            'commands': newCommands.objects.all(),
        }
    else:
        context = {}
        return redirect('home')
    return render(request, 'allcommands.html', context)


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contactUs.html')
# ------------------------------------------------------------------
# --------------------==Commmand Dettails==-------------------------


def DettailsCommand(request, idcmd):
    context = {
        'data': get_object_or_404(newCommands, id=idcmd),
    }
    return render(request, 'commandDettails.html', context)
# -------------------------------------------------------------------------
# ================================= New Commands ==========================


def command(request):
    if request.method == 'POST':
        data = {
            'nom': request.POST['client_nom'],
            'prenom': request.POST['client_prenom'],
            'email': request.POST['email'],
            'tel': request.POST['tel'],
            'title': request.POST['name_command'],
            'domain': request.POST['Domain'],
            'time': request.POST['Durre_work'],
            'adress': request.POST['Adreess'],

        }
        forms = Commndes(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, "your command was added sucsufly")
            # html_content = render_to_string("commandEmail.html", data)
        # text_content = strip_tags(html_content)
        # email = EmailMultiAlternatives(
        #     data['title'],
        #     text_content,
        #     settings.EMAIL_HOST_USER,
        #     ["brahimelorchi1937@gmail.com"]
        # )
        # email.attach_alternative(html_content, "text/html")
        # email.send()
        return redirect('commander')
    else:
        forms = Commndes()
    context = {
        'forms': forms,
    }
    return render(request, 'commands.html', context)
# ----------------------------------------------------------
# --------------------==Contact==-------------------------


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        emails = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        context = {
            "name": name,
            "email": emails,
            "subject": subject,
            "message": message,
        }

        # html_content = render_to_string("templetsEmail.html", context)
        # text_content = strip_tags(html_content)
        # email = EmailMultiAlternatives(
        #     subject,
        #     text_content,
        #     settings.EMAIL_HOST_USER,
        #     ["brahimelorchi1937@gmail.com"]
        # )
        # email.attach_alternative(html_content, "text/html")
        # email.send()
        messages.success(request, "merci pour votre message")
        return redirect('contact')
    else:
        return render(request, 'contactUs.html')

# --------------------------------------------------------------------
# ============================ All Services===========================


def allService(request):
    data = Categorie.objects.all()
    context = {
        'allserv': data,
    }

    return render(request, "services.html", context)

# -------------------------------------------------------------------------
# ==========================Services Dettails and demmand =============


def serviceDettails(request, idServices):
    data = get_object_or_404(Categorie, id=idServices),
    if request.method == 'POST':
        forms = Commndes(data=request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "your command was added sucsufly")
            return redirect('home')
    else:
        forms = Commndes()
    context = {
        'forms': forms,
        'object': data,
    }
    return render(request, "servicesDettails.html", context)
# -------------------------------------------------------------------


# ====================================== New Categorie===============================
def newCat(request):
    if request.method == 'POST':
        newCategorie = Categorie()
        name_cat = request.POST['name_cat']
        image = request.FILES['image_cat']
        des = request.POST['Description']
        if name_cat != "" and image != "" and des != "":
            newCategorie.name_cat = name_cat
            newCategorie.image_cat = image
            newCategorie.Description = des
            newCategorie.save()
            messages.success(request, "your Categorie was added sucsufly")
            return redirect('categorie')
        # form = CategorieForms(request.POST, request.FILES)

        # if form.is_valid():
        #     print(form)
        #     form.save()
        #     messages.success(request, "your Categorie was added sucsufly")
        #     return redirect('success')
    else:
        form = CategorieForms()
    context = {
        'forms': form,
    }
    return render(request, "newCat.html", context)
# ----------------------------------------------------------------------------------


def con(request):
    if request.method == 'POST':
        name = request.POST['name']
        emails = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        # templete = loader.get_template("contactForm.txt")
        # message = 'request'
        data = {
            "name": name,
            "email": emails,
            "subject": subject,
            "message": message,
        }

        message_all = f'''
        New message =>{data['message']}\n
        From => {data['email']}
        '''
        # send_mail(data['project'], message_all, "", ['dalamamir118@gmail.com'],

        send_mail(f"Subject =>{ data['subject']}", message_all, data['name'], [
                  'ilyassSair37@gmail.com'], fail_silently=False,)
        messages.success(request, "your message sent sucsefly")
        return redirect('contact')
    else:
        return render(request, 'contactUs.html')
# -------------------------------------------------------------------


# ====================================== Valider Commmande===============================
def Valider(request, id):
    if request.user.is_authenticated:
        Nvalide = newCommands.objects.filter(id=id)
        for item in Nvalide:
            item.Status = True
            item.save()
        messages.success(request, "command is valide")
        context = {
            'commands': newCommands.objects.all(),
        }
    else:
        context = {}
        return redirect('home')
    return render(request, 'allcommands.html', context)

# -------------------------------------------------------------------


# ======================================Commande  Non Valider===============================
def nonValider(request, id):
    if request.user.is_authenticated:
        Nvalide = newCommands.objects.filter(id=id)
        for item in Nvalide:
            item.Status = False
            item.save()
        messages.error(request, "command is note valide")
        context = {
            'commands': newCommands.objects.all(),
        }
    else:
        context = {}
        return redirect('home')
    return render(request, 'allcommands.html', context)


# -------------------------------------------------------------------


# ====================================== Delete command===============================
def Delete(request, id):
    if request.user.is_authenticated:
        newCommands.objects.filter(id=id).delete()
        messages.success(request, "command has been deleted")
        context = {
            'commands': newCommands.objects.all(),
        }
    else:
        context = {}
        return redirect('home')
    return render(request, 'allcommands.html', context)
