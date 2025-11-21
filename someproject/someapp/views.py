
from django.shortcuts import render
from .models import Book
from django.db.models import Count, F

def get_items(request):
    result = (
        Book
        .objects
        .values('publisher__name') 
        .annotate(
            sum_book=Count(F('id')), 
        )
    )


    return render(request, 'main.html', {
        'publishers': result,

    })
