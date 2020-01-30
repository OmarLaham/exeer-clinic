from django.contrib import admin

# Register your models here.
from .models import Taxonomy, Articles, HelpGuideSnippets, Consultations

class TaxonomyAdmin(admin.ModelAdmin):
    model = Taxonomy
    search_fields = ['term']

admin.site.register(Taxonomy, TaxonomyAdmin)

class ArticlesAdmin(admin.ModelAdmin):
    model = Articles
    fieldsets = [
        ('', {'fields': ['taxonomy_id']}),
        ('English version',               {'fields': ['title_en', 'content_en'], 'classes': ['collapse']}),
        ('Arabic version', {'fields': ['title_ar', 'content_ar'], 'classes': ['collapse']}),
    ]
    search_fields = ['title_en', 'title_ar']

admin.site.register(Articles, ArticlesAdmin)

class ConsultationsAdmin(admin.ModelAdmin):
    model = Consultations
    fieldsets = [
        ('Question', {'fields': ['consultation', 'consultation_anonymous']}),
        ('Answer', {'fields': ['reply', 'reply_anonymous']}),
        ('Publishing', {'fields': ['title', 'published']}),
    ]

admin.site.register(Consultations, ConsultationsAdmin)
