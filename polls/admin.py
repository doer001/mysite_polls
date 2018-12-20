from django.contrib import admin
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', )


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
