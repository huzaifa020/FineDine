from django.shortcuts import *
from contact.models import contactform
from django.contrib import messages
from booktable.models import booktable as BookingModel
def home(request):
    return render(request, "index.html")
#This function handle book table
def booktable(request):
    #Retrieve data from Form
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        people = request.POST.get('people')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')
        #Save data in database
        try:
            new_booking = BookingModel(
                name=name, 
                email=email, 
                phone=phone, 
                people=people, 
                date=date, 
                time=time, 
                message=message
                )
            new_booking.full_clean()
            new_booking.save()
            messages.success(request, "Your table has been booked successfully!")
            return redirect('home')
        #Handle database errors if they occur
        except Exception as e:
            print(f"CRITICAL BOOKING ERROR: {type(e).__name__} - {e}") 
            messages.error(request, "Booking failed. Please check your data format and ensure all required fields are complete.")
            return render(request, 'index.html') 
    return render(request, 'index.html')
#This function handle contact form
def contact(request):
    if request.method == "POST":
        #Retrieve data safely
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        #Save Form Data to Database
        try:
            meta = contactform(name=name, email=email, subject=subject, message=message)
            meta.save()
            messages.success(request, "Form is submitted successfully!")
            # Use redirect to prevent form resubmission on refresh
            return redirect('home') 
        #Handle database errors if they occur
        except Exception as e:
            print(f"CONTACT FORM INTEGRITY ERROR: {e}") 
            messages.error(request, "A database error occurred. Please try again or contact support.")
            return render(request, 'index.html') 
    return render(request, 'index.html') 