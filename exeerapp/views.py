from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404

from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _

from .forms import ConsultantProfileForm, QuestionNewForm

from .models import ConsultantProfile, Consultations

from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import PermissionRequiredMixin

import datetime
# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['counter_sessions'] = 2000
        context['counter_experts'] = 5
        context['counter_clients'] = 1250
        context['counter_tips'] = 2800
        #copyright_year
        now = datetime.datetime.now()
        context['copyright_year'] = now.year
        return context

class HelpGuideView(TemplateView):
    template_name = "help_guide.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HelpGuideView, self).get_context_data(*args, **kwargs)
        #context['page_title'] = "Help Guide"
        return context

class QuestionNewView(TemplateView):
    template_name = "question_new.html"
    def get_context_data(self, *args, **kwargs):
        context = super(QuestionNewView, self).get_context_data(*args, **kwargs)
        #context['page_title'] = "Help Guide"
        return context

    def get(self, request, *args, **kwargs):
        context = context = self.get_context_data()
        form = QuestionNewForm()
        context['form'] = form
        return render(request, "question_new.html", context=context)

    def post(self, request, *args, **kwargs):
        context = context = self.get_context_data()
        if self.request.method == 'POST':
            form = QuestionNewForm(self.request.POST)
            if form.is_valid():
                form.save()
                form = QuestionNewForm()
                context['form'] = form
                context['alerts'] = [_("Your question has been sent. We will email you the answer to your inbox as soon as possible!")]
            else:
                print(form.errors)
        else:
            form = QuestionNewForm()
            context['form'] = form
        return render(request, "question_new.html", context=context)

class QuestionView(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super(QuestionView, self).get_context_data(*args, **kwargs)
        consultation = get_object_or_404(Consultations, pk=args['pk'])
        question = consultation.consultation_anonymous
        answer = consultation.reply_anonymous
        context['question'] = question
        context['answer'] = answer
        return context

class ConsultantProfileView(PermissionRequiredMixin, TemplateView):
    #template_name = "consultant_profile.html"
    #login_url = ""
    permission_required = "exeerapp.view_consultantprofile"
    def get_context_data(self, *args, **kwargs):
        context = super(ConsultantProfileView, self).get_context_data(*args, **kwargs)
        context['name_en'] = "Dr. Waddah Hajjar"
        context['name_ar'] = "د. وضاح حجار"
        context['pic_url'] = "/uploads/consultants-pics/waddah.jpg"
        return context

    def get(self, request, *args, **kwargs):
        context = context = self.get_context_data()
        try:
            profile = ConsultantProfile.objects.get(user=self.request.user)
            form = ConsultantProfileForm(instance=profile)
        except ConsultantProfile.DoesNotExist:
            profile = ConsultantProfile.objects.create(user = self.request.user)
            form = ConsultantProfileForm(instance=profile)
        context['form'] = form
        return render(request, "consultant_profile.html", context=context)


    def post(self, request, *args, **kwargs):
        context = context = self.get_context_data()
        if self.request.method == 'POST':
            profile = get_object_or_404(ConsultantProfile, user=self.request.user)
            form = ConsultantProfileForm(self.request.POST, self.request.FILES, instance=profile)
            if form.is_valid():

                print('user' + str(form.cleaned_data['user']))
                if form.cleaned_data['user'] != self.request.user:
                    return render(request, "access_denied.html")
                context['form'] = form
                instance = form.save(commit=False)
                instance.save()
                context['alerts'] = [_("Profile saved!")]
            else:
                print(form.errors)
        else:
            form = ConsultantProfileForm()
            context['form'] = form
        return render(request, "consultant_profile.html", context=context)

    def handle_no_permission(self):
        messages.error(self.request, _("You don\'t have permission to do this"))
        return super(MyView, self).handle_no_permission()
