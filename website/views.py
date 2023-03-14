from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import CreateView, DetailView, TemplateView
from .models import Contact, Project
# Create your views here.


class HomePageView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all().order_by('-pk')
        context.update({"projects_obj": projects})
    template_name = 'website/home_page.html'


class AboutPageView(TemplateView):
    template_name = 'website/about_page.html'


class ServicesPageView(TemplateView):
    template_name = 'website/services_page.html'


class ContactCreateView(CreateView):
    model = Contact
    template_name = "website/contact_page.html"
    form_class = ContactForm

    def get_success_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.object.pk})


class ContactDetailsView(DetailView):
    model = Contact
    template_name = "website/contact_details_page.html"
    form_class = ContactForm
