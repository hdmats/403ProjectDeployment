from django.shortcuts import render
from django.http import HttpResponse
from Bears.models import Bears
# Create your views here.

def indexPageView(request):
    return render(request, 'Bears/index.html')

def safetyPageView(request):
    return render(request, 'Bears/safety.html')

def infoPageView(request):
    data = Bears.objects.order_by('-sighting_date', '-sighting_time')
    columns = Bears._meta.get_fields()
    context = {
        "sightings" : data,
        "columns" : columns,
    }
    return render(request, 'Bears/info.html', context)

def showSightingPageView(request, sighting_id):
    data = Bears.objects.get(id = sighting_id)

    context = {
        "record" : data,
    }
    return render(request, 'Bears/editSighting.html', context)

def updateSightingPageView(request):
    if request.method == 'POST':
        sighting_id = request.POST['sighting_id']

        customer = Bears.objects.get(id=sighting_id)

        customer.bear_type = request.POST['bear_type']
        customer.bear_age = request.POST['bear_age']
        customer.bear_count = request.POST['bear_count']
        customer.sighting_date = request.POST['sighting_date']
        customer.sighting_time = request.POST['sighting_time']
        customer.sighting_location = request.POST['sighting_location']
        customer.sighting_notes = request.POST['sighting_notes']

        customer.save()

    return infoPageView(request)

def deleteSightingPageView(request, sighting_id):
    data = Bears.objects.get(id = sighting_id)

    data.delete()

    return infoPageView(request)

def addSightingPageView(request):
    if request.method == 'POST':
        customer = Bears()

        customer.bear_type = request.POST['bear_type']
        customer.bear_age = request.POST['bear_age']
        customer.bear_count = request.POST['bear_count']
        customer.sighting_date = request.POST['sighting_date']
        customer.sighting_time = request.POST['sighting_time']
        customer.sighting_location = request.POST['sighting_location']
        customer.sighting_notes = request.POST['sighting_notes']

        customer.save()

        return infoPageView(request)
    else:
        return render(request, 'Bears/addSighting.html')
