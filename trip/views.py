from django.shortcuts import render # noqa:disable=f401
from django.views import generic
from trip.models import Trip
from django.urls import reverse_lazy
from trip.forms import TripCreationForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect


class MyTripsView(ListView):
    model = Trip
    template_name = 'trip/trip.html'
    context_object_name = 'user_trips'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Trip.objects.filter(initiator=self.request.user)
        else:
            return Trip.objects.none()


class TripCreationView(generic.CreateView):
    form_class = TripCreationForm
    success_url = reverse_lazy('main_page')
    template_name = 'trip/create_trip.html'
    model = Trip

    def form_valid(self, form):
        # Set the initiator to the user making the request
        form.instance.initiator = self.request.user
        # Call the super class form_valid to save the form and redirect to success_url
        return super(TripCreationView, self).form_valid(form)


class TripDetailView(DetailView):
    model = Trip
    template_name = 'trip/trip_detail.html'

    def post(self, request, *args, **kwargs):
        trip = self.get_object()
        if 'join' in request.POST:
            trip.join_trip(request.user)
            return redirect("all_trips")
        elif 'leave' in request.POST:
            trip.leave_trip(request.user)
            return redirect("all_trips")
        return render(request, self.template_name, trip)


class AllTripsView(ListView):
    model = Trip
    template_name = 'trip/all_trips.html'  # Specify your template here
    context_object_name = 'all_trips'
