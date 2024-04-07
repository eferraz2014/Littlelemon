from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication
from django_filters import rest_framework as django_filters
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics,permissions
from .models import Booking, MenuItem
from .forms import BookingForm,LoginForm
from .serializers import MenuItemSerializer, BookingSerializer

#precisa ser revisto devido as possiveis excepções.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

@login_required
def view_booking(request):
    booking = Booking.objects.filter(user=request.user)
    booking = booking.order_by('booking_date')
    return render(request, 'view_booking.html', {'booking': booking})

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = MenuItem.objects.all()
    main_data = {"menu" : menu_data}
    return render(request, "menu.html", main_data) 

def display_menu_item(request, pk = None):
    if pk:
        menu_item = MenuItem.objects.get(pk=pk)
    else:
        menu_item = ""
    
    return render(request, "menu_item.html", {"menu_item" : menu_item})

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        p_price = self.request.query_params.get('price', None)
        up_price = self.request.query_params.get('up_price', None)
        lo_price = self.request.query_params.get('lo_price', None)
        p_title = self.request.query_params.get('title', None)
        pk = self.kwargs.get('pk', None)
        if p_price is not None:
            queryset = queryset.filter(price=p_price)
        else:
            if lo_price is not None:
                queryset = queryset.filter(price__gte=lo_price)
            if up_price is not None:
                queryset = queryset.filter(price__lte=up_price)
        if p_title is not None:
            queryset = queryset.filter(title__icontains=p_title)
        queryset = queryset.order_by('title')
        return queryset
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [django_filters.DjangoFilterBackend]
    filterset_fields = ['booking_date','name']
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]

class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]