from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import HomeBG, TourIdea
# Create your views here.


class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homebg = HomeBG.objects.all()
        tour = TourIdea.objects.all()
        return render(request, self.template_name, {'homebg':homebg, 'tour':tour})
