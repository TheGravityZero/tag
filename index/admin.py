from django.contrib import admin

from django.contrib import admin
from .models import Question, People, Location, Hashtag, Images, Video, Promo

from django.contrib import admin
from .models import Location, Question, People, Hashtag, Promo, Video, Images

class CityFilter(admin.SimpleListFilter):
    title = 'City'
    parameter_name = 'city'

    def lookups(self, request, model_admin):
        return [
            ('Екатеринбург', 'Екатеринбург'),
            ('Москва', 'Москва'),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(city=self.value())
        return queryset

class VideoInline(admin.StackedInline):
    model = Video
    extra = 1

class ColorsInline(admin.StackedInline):
    model = Images
    extra = 1

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'addresses', 'city']
    search_fields = ['title']
    inlines = [ColorsInline, VideoInline]
    list_filter = [CityFilter]

    def get_search_results(self, request, queryset, search_term):
        # Customize the search behavior if needed
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        return queryset, use_distinct

# Register other models
admin.site.register(Question)
admin.site.register(People)
admin.site.register(Hashtag)
admin.site.register(Promo)
