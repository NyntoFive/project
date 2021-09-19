from django import forms

class ConfiguratorWidget(forms.RadioSelect):
    class Media:
        css = {
            'all': ('configurator.css',)
        }
        js = ('animations.js', 'actions.js')