from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse

from .forms import DetailForm
from .models import Impression

class ImpressionRegisterView(CreateView):
    template_name = "detail.html"
    form_class = DetailForm
	
    def get_success_url(self):
        return reverse('myform:upd', args=(self.object.id,))
		
class ImpressionUpdateView(UpdateView):
    model = Impression
    template_name = "detail.html"
    form_class = DetailForm
	
    def get_success_url(self):
        return reverse('myform:upd', args=(self.object.id,))
	