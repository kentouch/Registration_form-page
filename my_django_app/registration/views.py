from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save data to Google Sheets
            save_to_google_sheets(form.cleaned_data)
            return redirect('success')  # Redirect to a success page or similar
    else:
        form = RegistrationForm()
    
    return render(request, 'registration/index.html', {'form': form})

def save_to_google_sheets(data):
    # Define the scope and credentials for Google Sheets API
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/credentials.json', scope)
    client = gspread.authorize(creds)
    
    # Open the Google Sheet by name or URL
    sheet = client.open("Your Google Sheet Name").sheet1
    
    # Append the data to the sheet
    sheet.append_row([
        data['delegate_category'],
        data['firstname'],
        data['lastname'],
        data['email'],
        data['nationality'],
        data['national_id'],
        data['phone_number'],
        data['address'],
        data['organization'],
        data['position'],
        data['country_of_residence'],
        data['social_activities']
    ])