from django.shortcuts import render, redirect
from Home.models import Contact
from .forms import ImageUploadForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'Index.html')

def About(request):
    return render(request, 'about.html')
@login_required(login_url='login')
def Services(request):
    return render(request, 'services.html')

def Contact_page(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        message = request.POST['message']
        
        # Create Contact instance
        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            message=message
        )
        
        # Save Contact instance to the database
        contact.save()

    return render(request, 'contact.html')
# views.py


@login_required(login_url='login')
def upload_image_with_location(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image
            image = form.save()

            # Retrieve the user's location from the form data
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')

            # Do something with the image and location data (e.g., save to database)
            
            return redirect('success')  # Redirect to success page after successful submission
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})
def shopping(request):
    return render(request,'shop.html')