from django.shortcuts import render, get_object_or_404, redirect

from .forms import MeetingForm
from .models import Meeting, Room

# Create your views here.


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', {'meeting': meeting})


def create(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = MeetingForm()

    return render(request, 'meetings/create.html', {'form': form})


def update(request, id):
    meeting = get_object_or_404(Meeting, pk=id)

    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)

        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = MeetingForm(instance=meeting)

    return render(request, 'meetings/update.html', {'form': form})


def delete(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == 'POST':
        meeting.delete()
        return redirect('welcome')

    return render(request, 'meetings/delete.html', {'meeting': meeting})
