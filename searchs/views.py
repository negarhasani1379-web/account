# from django.shortcuts import render
from django.views.generic import ListView
from people.models import Person
class SearchView(ListView):
    model = Person
    template_name = 'searchs/search.html'
    context_object_name = 'results'
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Person.objects.filter(first_name__icontains=query)
        return Person.objects.none()