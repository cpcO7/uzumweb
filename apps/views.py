from django.views.generic import TemplateView

from apps.models import Category


class MainTemplateView(TemplateView):
    template_name = 'apps/main.html'
    queryset = Category.objects.all()
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        cd = super(MainTemplateView, self).get_context_data(**kwargs)
        categories = Category.objects.filter(parent__isnull=True)
        subcategories = Category.objects.filter(parent__isnull=False)
        cats = Category.objects.filter(parent__isnull=True)[: 6]
        cd['subcategories'] = subcategories
        cd['categories'] = categories
        cd['cats'] = cats
        return cd
