from django.shortcuts import render
from .models import Book,Author,BookInstance
from django.http import HttpResponse
from django.views.generic import ListView,DetailView


class AuthorsListView(ListView):
    model = Book
    paginate_by = 4
class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 3

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'books'
class BookListView(ListView):
    model = Book
    context_object_name = 'books'


def index(request):
    #  Словарь  для  передачи  данных  в  шаблон
    text_head = 'На нашем сайте вы сможете получить книги в электронном виде'
    # Данные о книгах и о их количестве
    books = Book.objects.all()
    num_book = Book.objects.all().count()
    # Данные об экземплярах книг в БД
    num_instances = BookInstance.objects.all().count()
    #Доступные книги(статус="На складе")
    num_instances_available = BookInstance.objects.filter(
        status__exact=2).count()
    #Данные об авторах книг
    authors = Author.objects
    num_authors = Author.objects.count()




    # text_body = 'Это глвное содержимое главной страницы сайта 'text_body': text_body'

    # словарь для передачи данных  в шаблон index.html
    context = {'tex_head': text_head ,'books':books,'num_books':num_book,'num_instances':num_instances,
              'num_instances_available': num_instances_available,
               'authors': authors , 'num_authors':num_authors }
    # Передача словаря  context с данными в шаблон
    return render(request, 'catalog/index.html',context)


