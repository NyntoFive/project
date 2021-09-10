from django.contrib.auth import get_user_model
from django.contrib import admin
from .models import Recipe, RecipeIngredient

User = get_user_model()
admin.site.unregister(User)

class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 0

class UserAdmin(admin.ModelAdmin):
    inline = [RecipeInline]
    list_display = ['username']

admin.site.register(User, UserAdmin)

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    # fields = ['name', 'quantity', 'unit' 'directions']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']

# admin.site.register(RecipeIngredient)
admin.site.register(Recipe, RecipeAdmin)