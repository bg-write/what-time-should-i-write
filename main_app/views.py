from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Writer:
  def __init__(self, name, birth, death, works, quote):
    self.name = name
    self.birth = birth
    self.death = death
    self.works = works
    self.quote = quote

writers = [
  Writer('Writer A', 1925, 2000, 'Notable Work 1', 'This is quote A.'),
  Writer('Writer B', 1935, 2010, 'Notable Work 2', 'This is quote B.'),
  Writer('Writer C', 1940, 1999, 'Notable Work 3', 'This is quote C.'),
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def writers_index(request):
  return render(request, 'writers/index.html', { 'writers': writers })


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up, please try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)