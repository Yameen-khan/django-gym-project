from django.shortcuts import render, HttpResponse
import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import openai
from bs4 import BeautifulSoup
import re
# Create your views here.
def index(request):
    # return HttpResponse("this is homepage")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')



def contact(request):
    return render(request, 'contact.html')



def gyms(request):
    if request.method == 'POST':
        # Retrieve the user's current location from the form data
        current_location = request.POST.get('location')

        # Make a request to the API to find nearby gyms
        api_key = ''  # Replace with your actual API key
        endpoint = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={current_location}&radius=1000&type=gym&key=AIzaSyAOL4klHvA-CM-gQuIlzAo_ee__LT3czi4'
        response = requests.get(endpoint)
        data = response.json()
        # Extract the relevant information from the API response
        nearby_gyms = []
        if data['status'] == 'OK':
            for result in data['results']:
                gym_name = result['name']
                gym_address = result['vicinity']
                nearby_gyms.append({'name': gym_name, 'address': gym_address})

        # Pass the nearby gyms data to the template
        return render(request, 'gyms.html', {'gyms': nearby_gyms})

    return render(request, 'location_form.html')


def dietchart(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']

        # Call OpenAI API to generate plan
        response = openai.Completion.create(
            engine='davinci',  # or 'text-davinci-003'
            prompt=user_input,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
            api_key='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'
        )

        plan = response.choices[0].text.strip()

        # Render the plan in the template
        return render(request, 'dietchart.html', {'plan': plan})

    return render(request, 'diet_form.html')


def wellnessresources(request):
    return render(request, 'wellnessresources.html')
