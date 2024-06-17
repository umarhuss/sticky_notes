from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import StickyNote
from .forms import StickyNoteForm


def index(request):
    return render(request, 'index.html')


# Fetch notes for the logged-in user
@login_required
def notes_hub(request):
    user_notes = StickyNote.objects.filter(user=request.user)
    return render(request, 'notes_hub.html', {'notes': user_notes})


@login_required
def add_note(request):
    if request.method == 'POST':
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            # Associate the note with the logged-in user
            note.user = request.user
            note.save()
            return redirect('notes_hub')
    else:
        form = StickyNoteForm()
    return render(request, 'add_note.html', {'form': form})


@login_required
def edit_note(request, note_id):
    # Ensure note belongs to the logged-in user
    note = get_object_or_404(StickyNote, id=note_id, user=request.user)
    if request.method == 'POST':
        form = StickyNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_hub')
    else:
        form = StickyNoteForm(instance=note)

    return render(request, 'edit_note.html', {'form': form, 'note': note})


@login_required
def view_note(request, note_id):
    # Ensure note belongs to the logged-in user
    note = get_object_or_404(StickyNote, id=note_id, user=request.user)
    return render(request, 'view_note.html', {'note': note})


@login_required
def delete_note(request, note_id):
    # Ensure note belongs to the logged-in user
    note = get_object_or_404(StickyNote, id=note_id, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('notes_hub')
    return render(request, 'delete_note.html', {'note': note})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have been successfully registered!')
            return redirect('notes_hub')
        else:
            messages.error(request, 'Registration failed. Please check your \
input.')
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been logged in')
                return redirect('notes_hub')
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, 'login.html', {'form': form})
        else:
            messages.error(request, 'Form is not valid. Please check your \
input.')
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('index')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
