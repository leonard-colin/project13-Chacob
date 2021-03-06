from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from mixer.backend.django import mixer

from mycalendar.models import Event
from mypet.models import Pet
from accounts.models import UserAuth


class TestViews(TestCase):
    """Class that tests mycalendar views"""

    def setUp(self) -> None:
        """Method that sets tests parameters"""

        self.user = get_user_model()
        self.c = Client()

    def test_create_events_view(self):
        """Method that tests a new event is created by a user"""

        user = self.user.objects.create_user(username="Leonard",
                                             password="12345Testing")

        self.c.login(username="Leonard", password="12345Testing")

        pet = Pet.objects.create(user=UserAuth.objects.get(id=user.id),
                                 species="Chat",
                                 gender="Mâle",
                                 birth_date="2019-03-20",
                                 name="Felix")

        assert pet.name == "Felix"
        assert Pet.objects.count() == 1

        mycal_url = reverse('mycalendar')
        assert self.c.get(mycal_url).status_code == 200

        response = self.c.post(mycal_url, {
            "date": "20/08/2021 20:00",
            "pet_name": Pet.objects.get(id=pet.id).id,
            "reason": "Vaccin",
            "comment": "Test example",
        }, follow=True)

        assert Event.objects.count() == 1
        assert response.status_code == 200

        message = list(response.context['messages'])
        assert len(message) == 1
        assert str(message[0]) == "Votre nouveau rendez-vous a bien été enregistré"

    def test_delete_events_view(self):
        """Method that tests delete_event_view"""

        mixer.blend(Event, reason="Vaccin")

        event = Event.objects.get(reason="Vaccin")

        assert Event.objects.count() == 1

        delete_url = reverse("delete_event", kwargs={"id_event": event.id})

        response = self.c.get(delete_url)

        assert response.status_code == 302
        assert Event.objects.count() == 0
