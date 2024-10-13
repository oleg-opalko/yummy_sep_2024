from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse

# Create your views here.

def is_manager(user):
    return user.groups.filter(name='Manager').exists() or user.is_staff
@login_required(login_url='/login/')
@user_passes_test(is_manager)
def users_reservation(request):
    return HttpResponse("Hello, world. You're at the manager.")