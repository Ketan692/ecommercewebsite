from django.contrib import admin
from carousel.models import Homepage, Smartphones, Laptops, Fragrances, Skincare, Groceries, HomeDecoration

class CarouselAdmin(admin.ModelAdmin):
    list_display = ("thumbnail",)

admin.site.register(Homepage, CarouselAdmin)
admin.site.register(Smartphones, CarouselAdmin)
admin.site.register(Laptops, CarouselAdmin)
admin.site.register(Fragrances, CarouselAdmin)
admin.site.register(Skincare, CarouselAdmin)
admin.site.register(Groceries, CarouselAdmin)
admin.site.register(HomeDecoration, CarouselAdmin)


