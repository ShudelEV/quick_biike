from django.shortcuts import render


# View for index page.
def page(request):
    return render(request, 'rent_bike/index.html')
