from django.shortcuts import render
# need to add . since forms is local file, so to be able to import local we add ".", otherwise django looks in directory
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage  # no need for smtp


# here is where we return the index.html file suing the function below and
# then we get the value of those widgets

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        # we are validating the form
        if form.is_valid():
            # django saves as dictionary, and we retrieve it from the value of first_name and more
            # all these correspond to the index.html file values, where we get info from
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            # connects the data to db and stores it in the db when submitted
            # first_name = first_name db value equalling to variable above
            Form.objects.create(first_name=first_name, last_name=last_name, email=email,
                                date=date, occupation=occupation)

            # sets up subject and message boy for the email to be sent
            message_body = f"A new job Application was submitted. Thank you, \n{first_name} {last_name}."
            email_message = EmailMessage("Form submission confirmation", message_body, to=[email])
            email_message.send()

            messages.success(request, "Form submitted successfully!")
    return render(request, "index.html")  # django just renders this page and don't need to specify anything else
