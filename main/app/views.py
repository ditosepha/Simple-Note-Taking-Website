from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import AddNoteForm

# Create your views here.
def landing_page(request):
    notes = Note.objects.all()
    context = {
        "notes": notes
    }
    return render(request, "index.html", context)

def note_details(request, note_title):
    note = get_object_or_404(Note, title=note_title)
    return render(request, 'note_details.html', {"note": note})

def add_note(request):
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = AddNoteForm()
    return render(request, 'add_note.html', {'form': form})

def edit_note(request, note_title):
    note = get_object_or_404(Note, title=note_title)
    if request.method == "POST":
        form = AddNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_details', note_title=note.title)
    else:
        form = AddNoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form})

def delete_note(request, note_title):
    event = get_object_or_404(Note, title=note_title)
    if request.method == "POST":
        event.delete()
        return redirect('landing_page')