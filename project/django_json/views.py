from django.views.generic.edit import FormView
from django.views.generic import DetailView
from django.urls import reverse_lazy
import json

from .forms import JSONForm
from .utils import json_iter_first, serializer
from .models import Category


class JSONAddView(FormView):
    form_class = JSONForm
    success_url = reverse_lazy('add-categories')
    template_name = 'add.html'

    def form_valid(self, form):
        json_data = json.loads(form.cleaned_data['json_data'])

        json_iter_first(json_data)
        return super(JSONAddView, self).form_valid(form)


class JSONGetView(DetailView):
    template_name = 'get.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(JSONGetView, self).get_context_data()

        category = Category.objects.get(pk=self.kwargs['pk'])
        context['category'] = serializer([category, ])[0]

        parent = []
        category.get_parent(parent)
        context['parent'] = serializer(parent, )

        children = category.get_children()
        context['children'] = serializer(children, )

        sibling = category.get_sibling()
        context['sibling'] = serializer(sibling, )

        return context
