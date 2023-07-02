from django.contrib.sitemaps import Sitemap
from .models import Reviews,Exclusive

class ReviewSitemap(Sitemap):
    chagefreq = 'weekly'
    priority = 0.9
    def items(self):
        return  Reviews.objects.filter(Status_article="active")
    
    def lastmod(self,obj):
        return obj.created_on 

class ExclusiveSitemap(Sitemap):
    chagefreq = 'weekly'
    priority = 0.9
    def items(self):
        return  Exclusive.objects.filter(Status_article="active")
    
    def lastmod(self,obj):
        return obj.created_on 