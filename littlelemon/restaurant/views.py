from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework import generics,status,permissions
from .models import BookingTable, Menu, MenuTableSelection
from .forms import BookingTableForm,LoginForm, MenuForm, MenuTableSelectionForm, UserModelForm
from .serializers import MenuSerializer, BookingTableSerializer, MenuTableSelectionSerializer

#precisa ser revisto devido as possiveis excepções.
def login_view(request, correctUrl=None):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect(correctUrl)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def view_bookings(request):
    bookings = BookingTable.objects.filter(user=request.user)
    return render(request, 'view_bookings.html', {'bookings': bookings})

@login_required
def add_menu_items(request, booking_id):
    booking = BookingTable.objects.get(id=booking_id)
    if request.method == 'POST':
        form = MenuTableSelectionForm(request.POST)
        if form.is_valid():
            menu_selection = form.save(commit=False)
            menu_selection.booking = booking
            menu_selection.save()
            return redirect('view_bookings')
    else:
        form = MenuTableSelectionForm()
    return render(request, 'add_menu_items.html', {'form': form})

def logout(request):
    return render(request, 'logout.html')
@login_required
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required
def book(request):
    form = BookingTableForm()
    if request.method == 'POST':
        form = BookingTableForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu" : menu_data}
    return render(request, "menu.html", main_data) 

def display_menu_item(request, pk = None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    
    return render(request, "menu_item.html", {"menu_item" : menu_item})

   
# Create your views here.
class MenuView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class BookingTableView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingTable.objects.all()
    serializer_class = BookingTableSerializer
    permission_classes = [permissions.IsAuthenticated]

class MenuTableSelectionView(generics.ListAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuTableSelection.objects.all()
    serializer_class = MenuTableSelectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        menu_table_selection = MenuTableSelection(**serializer.validated_data)
        booking_table = BookingTable.objects.filter(table_selection=menu_table_selection.table_selection).first()
        selections = self.queryset.filter(table_selection=booking_table)
        total_items = sum(selection.number_of_items for selection in selections)
        if total_items >= booking_table.nr_of_guests:
            return Response("can´t add more than the number of guests.", status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response("Menu selection inserted successfully.", status=status.HTTP_201_CREATED)
