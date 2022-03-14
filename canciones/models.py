
"""  CANCIONES MODELS"""

from turtle import position
from django.db import models
from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.snippets.models import register_snippet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your models here.

## Page que mostrará el index de las Canciones
## Hereda solo de Home y no descendientes

## Modelo para Canciones


class Cancion(models.Model):
    rank = models.CharField('rank', max_length=250)
    title = models.CharField('title', max_length=250)
    artist = models.CharField('artist', max_length=250)
    peak = models.CharField('peak', max_length=250)
    weeks = models.CharField('weeks', max_length=250)
   


    panels = [
        FieldPanel('title'),
        FieldPanel('rank'),
        FieldPanel('artist'),
        FieldPanel('peak'),
        FieldPanel('weeks')        
    ]
    def __str__(self):
        return f'{self.title}'


class CancionesIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def paginate(self, request, peliculas, *args):
        page = request.GET.get('page')
        
        paginator = Paginator(peliculas, 15)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        canciones = Cancion.objects.all().order_by('rank')
        context['canciones'] = self.paginate(request, canciones)
        
        
        return context



    