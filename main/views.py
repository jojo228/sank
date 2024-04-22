from django.shortcuts import render
from django.views.generic import TemplateView
from main.forms import SearchForm
from rooms.models import Room


# Create your views here.
def coming_soon(request):
    
    return render(request, "coming-soon.html")


def term_condition(request):
    
    return render(request, "term_&_condition.html")


def police_prive(request):
    
    return render(request, "police_prive.html")


def home(request):
    rooms = Room.objects.all().order_by("-created")[:9]
    
    return render(request, "index.html", locals())



def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            room_type = form.cleaned_data.get('room_type')
            guests = form.cleaned_data.get('guests')
            when = form.cleaned_data.get('main-input-search')

            # Perform search logic for Room model
            rooms = Room.objects.all()
            if room_type:
                rooms = rooms.filter(room_type__name__icontains=room_type)
            if guests:
                rooms = rooms.filter(guests=guests)
            # Add more filtering logic as needed (e.g., when, check_out)

            

            return render(request, 'search_results.html', {
                'room_type': room_type,
                'rooms': rooms,
            })

    # If form is invalid or method is not GET
    return render(request, 'search_results.html')






def index2(request):
    
    return render(request, "index2.html")



def index3(request):
    
    return render(request, "index3.html")


def index4(request):
    
    return render(request, "index4.html")




def errorpage(request):
    
    return render(request, "404.html")


def about(request):
    
    return render(request, "about.html")


def contacts(request):
    
    return render(request, "contacts.html")


def invoice(request):
    
    return render(request, "invoice.html")


def authorsingle(request):
    
    return render(request, "author-single.html")


def help(request):
    
    return render(request, "help.html")


def pricingtables(request):
    
    return render(request, "pricing-tables.html")


def bookingsingle(request):
    
    return render(request, "booking-single.html")


def dashboard(request):
    
    return render(request, "dashboard.html")



def blog2(request):
    
    return render(request, "blog2.html")



def blogsingle(request):
    
    return render(request, "blog-single.html")


def dashboardaddlisting(request):
    
    return render(request, "dashboard-add-listing.html")



def blog(request):
    
    return render(request, "blog.html")


def listingsingle(request):
    
    return render(request, "listing-single.html")


def listingsingle2(request):
    
    return render(request, "listing-single2.html")


def listingsingle3(request):
    
    return render(request, "listing-single3.html")


def listingsingle4(request):
    
    return render(request, "listing-single4.html")


def listing(request):
    
    return render(request, "listing.html")


def listing2(request):
    
    return render(request, "listing2.html")


def listing3(request):
    
    return render(request, "listing3.html")


def listing4(request):
    
    return render(request, "listing4.html")


def listing5(request):
    
    return render(request, "listing5.html")


def listing6(request):
    
    return render(request, "listing6.html")


def room1(request):
    
    return render(request, "rooms/room1.html")


def room2(request):
    
    return render(request, "rooms/room2.html")


def room3(request):
    
    return render(request, "rooms/room3.html")

def dashboardaddlisting(request):
    
    return render(request, "dashboard-add-listing.html")


def dashboardlistingtable(request):
    
    return render(request, "dashboard-listing-table.html")


def dashboardpassword(request):
    
    return render(request, "dashboard-password.html")


def dashboardreview(request):
    
    return render(request, "dashboard-review.html")




