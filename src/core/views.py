import pathlib
from django.shortcuts import render

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all().count()
    queryset = PageVisit.objects.filter(path=request.path).count()
    my_title = "My Page"

    context = {
        'page_title': my_title,
        'page_visit_count': queryset,
        'total_visit_count': qs,
        'percent': (queryset * 100.0) / qs
    }

    html_template = 'home.html'


    PageVisit.objects.create(path = request.path)
    return render(request, html_template, context)


def about_page_view(request, *args, **kwargs):
    my_title = "My Page"

    context = {
        'page_title': my_title
    }

    html_template = 'about.html'

    return render(request, html_template, context)
