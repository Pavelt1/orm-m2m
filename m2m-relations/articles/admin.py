from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tags, Relationship

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        main_section_count = 0 

        for form in self.forms:
            if form.cleaned_data and form.cleaned_data.get('is_main'):
                main_section_count += 1

        if main_section_count > 1:
            raise ValidationError('Только один раздел может быть основным.')

        if main_section_count == 0:
            raise ValidationError('Необходимо указать один основной раздел.')
        return super().clean()

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id","title","created_at"]


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ["id","name","is_main"]
    inlines = [RelationshipInline]