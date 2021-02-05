from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Will have to update the 'CreateView' import; I want users to be able to upload a request for a writer to add. I do NOT want users to upload these writers themselves. I want all that to happen through the backend.
from django.views.generic.edit import CreateView
from .models import Writer
from .forms import RoutineForm
import uuid
import boto3
from .models import Writer, Photo
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'writerroutinebg'


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def writers_index(request):
  writers = Writer.objects.all()
  return render(request, 'writers/index.html', { 
    'writers': writers
  })

@login_required
def writers_detail(request, writer_id):
  writer = Writer.objects.get(id=writer_id)
  routine_form = RoutineForm()
  return render(request, 'writers/detail.html', {
    'writer': writer, 'routine_form': routine_form
  })

@login_required
def add_routine(request, writer_id):
  form = RoutineForm(request.POST)
  if form.is_valid():
    new_routine = form.save(commit=False)
    new_routine.writer_id = writer_id
    new_routine.save()
  return redirect('detail', writer_id=writer_id)

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

	# Will have to update; I want users to be able to upload a request for a writer to add. I do NOT want users to upload these writers themselves. I want all that to happen through the backend.
class WriterCreate(LoginRequiredMixin, CreateView):
  model = Writer
  fields = '__all__'

  def form_valid(self, form):
   form.instance.user = self.request.user
   return super().form_valid(form)

@login_required
def add_photo(request, writer_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
      s3 = boto3.client('s3')
      key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
      try:
          s3.upload_fileobj(photo_file, BUCKET, key)
          url = f"{S3_BASE_URL}{BUCKET}/{key}"
          photo = Photo(url=url, writer_id=writer_id)
          photo.save()
      except:
          print('An error occurred uploading file to S3')
  return redirect('detail', writer_id=writer_id)
