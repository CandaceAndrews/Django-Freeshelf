from django.shortcuts import render, get_object_or_404, redirect
from .models import Resource
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ResourceForm


@login_required
def list_resources(request):
    # free_resources = Resource.objects.all()
    free_resources = Resource.objects.all().order_by('-created_at')
    for thing in free_resources:
        print(free_resources)
    return render(request, 'resources/index.html', {'free_resources': free_resources})


@user_passes_test(lambda user: user.is_staff)
def details_about_resource(request, pk):
    resource_description = get_object_or_404(Resource, pk=pk)
    return render(request, 'resources/details_about_resource.html', {'resource_description': resource_description})


@user_passes_test(lambda user: user.is_staff)
def add_resource(request):
    if request.method == 'POST':
        new_resource = ResourceForm(request.POST)
        if new_resource.is_valid():
            new_resource.save()
            return redirect('home')
    form = ResourceForm()
    return render(request, 'resources/add_resource.html', {'form': form})
