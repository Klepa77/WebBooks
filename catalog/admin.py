from django.contrib import admin
from .models import Author,Book,Genre,Language,Publisher,Status,BookInstance
from django.utils.html import format_html
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','data_of_birth','photo','show_photo')
    fields = ['last_name','first_name',('data_of_birth','photo')]
    readonly_fields = ['show_photo']
    def show_photo(self,obj):
        return format_html(
            f'<img scr = "{obj.photo.url}" style = "max-height: 100px;">')
    show_photo.short_description = 'Фото'

    #pass
#admin.site.register(Author)
admin.site.register(Author,AuthorAdmin)
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

#admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','genre','language','display_author','show_photo')
    list_filter = ('genre','author')
    inlines = [BooksInstanceInline]
    readonly_fields = ['show_photo']
    def show_photo(self,obj):
        return format_html(f'<img scr = "{obj.photo.url}" style = "max-height: 100px;">')
    show_photo.short_description = 'Обложка'


    # pass

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)
#admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_filter = ('book','status')
    fieldsets = (
        ('Экземпляр книги',{
            'fields':('book','inv_nom')}),
        ('Статус и окончание его действия',{
            'fields':('status','due_back')})
        )

    # pass



