from django.contrib import admin
from .models import   reviewsComment, Reviews, Bikes, Contact, Mailletter, Author,Exclusive

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on','author','Product')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Reviews,ReviewsAdmin)

class ExclusiveAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on','author')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Exclusive,ExclusiveAdmin)


class BikesAdmin(admin.ModelAdmin):
    list_display = ('Name','Company','Category')
admin.site.register(Bikes,BikesAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name','Mobile','Email','Question')
admin.site.register(Contact,ContactAdmin)



admin.site.register(Author)
admin.site.register(Mailletter)
admin.site.register(reviewsComment)