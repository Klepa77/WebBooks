from django.shortcuts import render
from .models import Book, Author, BookInstance
from django.http import HttpResponse
from django.views.generic import ListView, DetailView


#
class AuthorListView(ListView):
    model = Author
    context_object_name = 'author_list'
    paginate_by = 4


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 3


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'

class AuthorDetailView(DetailView):
    model = Author



#
#
# class BookListView(ListView):
#     model = Book
#     context_object_name = 'books'


def index(request):
    #  Словарь  для  передачи  данных  в  шаблон
    text_head = 'На нашем сайте вы сможете получить книги в электронном виде'
    # Данные о книгах и о их количестве
    books = Book.objects.all()
    num_book = Book.objects.all().count()
    # Данные об экземплярах книг в БД
    num_instances = BookInstance.objects.all().count()
    # Доступные книги(статус="На складе")
    num_instances_available = BookInstance.objects.filter(
        status__exact=2).count()
    # Данные об авторах книг

    authors = Author.objects
    num_authors = Author.objects.count()
    #Число посещений этого view,подсчитанное в переменной session
    num_visits = request.session.get( 'num_visits',0)
    request.session['num_visits'] = num_visits+1

    # text_body = 'Это глвное содержимое главной страницы сайта 'text_body': text_body'

    # словарь для передачи данных  в шаблон index.html
    context = {'tex_head': text_head, 'books': books, 'num_books': num_book, 'num_instances': num_instances,
               'num_instances_available': num_instances_available,
               'authors': authors, 'num_authors': num_authors,
               'num_visits': num_visits}
    # Передача словаря  context с данными в шаблон
    return render(request, 'catalog/index.html', context)

def about(request):
    text_head = "Сведения о компании"
    name = "ООО Интелектуальные информационные системы"
    rab1 = "Разработка приложений на основе"\
            "систем исскуственного интеллекта"
    rab2 = "Распознование обьектов дорожной инфраструктуры "
    rab3 = 'Создание  графических  АРТ-объектов  на  основе' \
         'систем  искусственного  интелпекта'
    rab4 = "Создание  цифровых  интерактивных  книг,  учебных  пособий" \
          "автоматизированных  обучающих систем"
    context = {'tex_head': text_head, 'name': name, 'rab1': rab1,
               'rab2': rab2,
               'rab3': rab3,
               'rab4': rab4}
    return render(request, 'catalog/about.html', context)
def contact(request):
    text_head = "Контакты"
    name = "ООО Интеллектуальные информационные системы"
    address = "Москва, ул. Планерная, д.20, к.1 "
    tel = "495-345-45-45"
    email = "iiS_info@mail.ru"
    context = {'tex_head': text_head, 'name': name, 'address': address,
               'tel': tel, 'email': email}
    return render(request, 'catalog/contact.html', context)