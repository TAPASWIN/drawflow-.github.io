# configurator/views.py
from django.shortcuts import render, redirect
from .forms import ComputerConfigurationForm
from .models import ComputerConfiguration


def configure_computer(request):
    if request.method == 'POST':
        form = ComputerConfigurationForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            json_config = form.cleaned_data['json_config']
            config = ComputerConfiguration(address=address, json_config=json_config)
            config.save()
            # Add code to send email using Django's EmailMessage class
            return redirect('thank_you_page')  # Create a thank you page in templates
    else:
        form = ComputerConfigurationForm()

    return render(request, 'configure_computer.html', {'form': form})



# Create your views here.
