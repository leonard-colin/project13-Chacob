from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Event
from .forms import EventForm

import environ

env = environ.Env()
environ.Env.read_env()


@login_required
def events_view(request):
    """
    GET method:
    Displays the calendar page with the event form

     **Template:**
    :template:`mycalendar/mycalendar.html`

    POST method:
    Displays the calendar with the new event

     **Template:**
     :template: `mycalendar/mycalendar.html`
    """

    event_list = Event.objects.filter(user_id=request.user).order_by('-date')

    if request.method == "GET":
        form = EventForm(request.user)
        return render(request, "mycalendar.html", locals())
    elif request.method == "POST":
        form = EventForm(request.user, request.POST)
        if form.is_valid():
            date = form.cleaned_data.get("date")
            pet_name = form.cleaned_data.get("pet_name")
            reason = form.cleaned_data.get("reason")
            comment = form.cleaned_data.get("comment")
            alert = form.cleaned_data.get("mail_alert")

            Event.objects.create(user_id=request.user,
                                 date=date,
                                 pet_name=pet_name,
                                 reason=reason,
                                 comment=comment,
                                 mail_alert=alert)

            messages.success(request, "Votre nouveau rendez-vous a bien été enregistré")
            form = EventForm(request.user)
            return redirect('mycalendar')