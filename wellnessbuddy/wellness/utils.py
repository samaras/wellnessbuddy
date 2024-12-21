import requests
import google.generativeai as gemini
from django.conf import settings
from twilio.rest import Client

def generate_wellness_plan(wellness_score):
    prompt = (
        f"Generate a personalized wellness plan based on the following scores:\n"
        f"Physical: {wellness_score.physical}\n"
        f"Intellectual: {wellness_score.intellectual}\n"
        f"Mental: {wellness_score.mental}\n"
        f"Social: {wellness_score.social}\n"
        f"Spiritual: {wellness_score.spiritual}\n"
        f"Occupational: {wellness_score.occupational}\n"
        f"Emotional: {wellness_score.emotional}\n"
        f"Financial: {wellness_score.financial}\n"
        f"Environmental: {wellness_score.environmental}\n"
    )

    gemini.configure(api_key=settings.GOOGLE_GEMINI_API_KEY)
    model = gemini.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    summary = model.generate_content("Provide a 1500 character summary to send to me in an sms: " + response.text)
    data = {
        'full': response.text,
        'summary': summary.text
    }

    return data

def send_sms(to, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    client.messages.create(
        to=to,
        from_=settings.TWILIO_PHONE_NUMBER,
        body=message
    )
