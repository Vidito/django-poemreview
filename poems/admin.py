from django.contrib import admin
from .models import Poem, Review
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

class SummerAdmin(SummernoteModelAdmin):
    # summernote_fields = '__all__'
    summernote_fields = ('content',)


admin.site.register(Poem, SummerAdmin)
admin.site.register(Review)
