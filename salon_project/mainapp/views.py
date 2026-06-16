from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout
from mainapp.models import Services , Appointment , Review
from django.contrib.auth.decorators import login_required

#HOME
def home(request):
    return render(request , 'mainapp/home.html')

#ABOUT
def about(request):
    return render(request , 'mainapp/about.html')


#REGISTER
def register_view(request):
    """
    Permite crearea unui cont nou de utilizator.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect('home')
        
    else:
        form = UserCreationForm()

    return render(request , 'mainapp/register.html' , {'form': form})


#LOGIN
def login_view(request):
    """
    Autentifică un utilizator existent în aplicație.
    """
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request , user)
            return redirect("home")
        
    else:
        form = AuthenticationForm()

    return render(request , 'mainapp/login.html' , {'form' : form})


#SERVICES
def services(request):
    services_list = Services.objects.all()

    return render(request , 'mainapp/services.html' , {'services' : services_list})


#CREATE APPOINTMENT
@login_required
def create_appointment(request , service_id):
    """
    Creează o programare pentru utilizatorul autentificat.
    Funcția permite doar utilizatorilor logați să rezerve un serviciu,
    salvând data și ora în baza de date.
    """
    service = Services.objects.get(id=service_id)

    if request.method == "POST":
        date = request.POST.get("date")
        hour = request.POST.get("hour")

        appointments = Appointment.objects.create(
            user = request.user ,
            service = service , 
            date = date , 
            hour = hour , 
            status = "pending"
        )

        if appointments :
            return render(request , 'mainapp/appointment.html' , {'service' : service , 'error' : 'Acest interval orar este deja ocupat'})

        return redirect("services")
    
    return render(request , 'mainapp/appointment.html' , {'service' : service})


#ADD REVIEW
@login_required
def add_review(request , service_id):
    """
    Permite utilizatorilor autentificați să adauge recenzii pentru servicii.
    Salvează ratingul și comentariul în baza de date.
    """
    service = Services.objects.get(id=service_id)

    if request.method == "POST":
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        Review.objects.create(
            user = request.user , 
            service = service , 
            rating = rating , 
            comment = comment ,
        )

        return redirect("services")
    
    return render(request , "mainapp/review.html" , {'service' : service})

#USER ACCOUNT
@login_required
def my_account(request):
    appointments = Appointment.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)

    return render(request , 'mainapp/account.html' , {'appointments' : appointments , 'reviews' : reviews})

#LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')