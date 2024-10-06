from django.shortcuts import render
from django.views.generic.dates import timezone_today

from home.models import Category, Gallery, Chef, Event, Contact
from home.templates.forms import ReservationForm


# Create your views here.


def index(request):

    if request.method == 'POST':
        book_a_table_form = ReservationForm(request.POST)

        if book_a_table_form.is_valid():
            book_a_table_form.save()
            return render(request, 'thanks.html')

    categories = Category.objects.filter(is_visible=True).order_by('sort')
    gallery = Gallery.objects.filter(is_visible=True)
    chefs = Chef.objects.all()
    events = Event.objects.filter(date_and_time__gte=timezone_today(), is_visible=True).order_by('date_and_time')
    contacts = Contact.objects.all()
    book_a_table_form = ReservationForm()

    context = {
        'categories': categories,
        'gallery': gallery,
        'chefs': chefs,
        'events': events,
        'contacts': contacts,
        'book_a_table_form': book_a_table_form,
    }

    return render(request, 'index.html', context)