from django.shortcuts import render,redirect
from library.models import *
from django.core.files.storage import FileSystemStorage

from .forms import LNotesForm,SNotesForm
from .models import LectureNotes
from .models import StudentNotes

# Create your views here.
def home(request, *args, **kwargs):
    academician = Academician.objects.all()
    cname = Course.objects.all()
    context = {
        'academician': academician,
        'course': cname,

    }
    return render(request, 'home.html', context)

# def courses(request, *args, **kwargs ):

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def lnotes_list(request):
    lnote = LectureNotes.objects.all()
    return render(request, 'lnotesList.html', {
        'lnote': lnote
    })

def snotes_list(request):
    snote = StudentNotes.objects.all()
    return render(request, 'snotesList.html', {
        'snote': snote
    })


def upload_lnotes(request):
    if request.method == 'POST':
        form = LNotesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lnotesList')
    else:
        form = LNotesForm()
    return render(request, 'uploadLnotes.html', {
        'form': form
    })

def upload_snotes(request):
    if request.method == 'POST':
        form = SNotesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('snotesList')
    else:
        form = SNotesForm()
    return render(request, 'uploadSnotes.html', {
        'form': form
    })


class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'