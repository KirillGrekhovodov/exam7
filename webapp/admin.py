from django.contrib import admin
from webapp.models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    fields = ("users", "question")
    filter_horizontal = ('users',)

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Answer)