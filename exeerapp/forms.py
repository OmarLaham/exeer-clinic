from django import forms
from captcha.fields import CaptchaField
from .models import ConsultantProfile, Consultations
from django.utils.translation import gettext
from django.utils.translation import ugettext_lazy as _

class ConsultantProfileForm(forms.ModelForm):
    class Meta:
        model = ConsultantProfile
        fields = ('user', 'picture', 'name_en', 'name_ar', 'profile_en', 'profile_ar', 'session_price_usd', 'session_price_sp', )
        localized_fields = ('__all__')
        labels = {
            'picture': _('Profile picture'),
            'name_en': _('Name in English'),
            'name_ar': _('Name in Arabic'),
            'profile_en': _('Profile in English'),
            'profile_ar': _('Profile in Arabic'),
            'session_price_usd': _('Session price in USD'),
            'session_price_sp': _('Session price in Syrian Pound'),
        }
        widgets = {
            'user': forms.HiddenInput(),
            'picture': forms.FileInput(attrs={'placeholder': _('Upload your picture')}),
            'name_en': forms.TextInput(attrs={'placeholder': _('Name in English'), 'data-error': _('Please enter you name in English')}),
            'name_ar': forms.TextInput(attrs={'placeholder': _('Name in Arabic'), 'data-error': _('Please enter you name in Arabic')}),
            'profile_en': forms.Textarea(attrs={'rows': 5, 'placeholder': _('Profile in English'), 'data-error': _('Fill with your profile in English')}),
            'profile_ar': forms.Textarea(attrs={'rows': 5, 'placeholder': _('Profile in Arabic'), 'data-error': _('Fill with your profile in Arabic')}),
            'session_price_usd': forms.TextInput(attrs={'placeholder': _('Session price in USD'), 'data-error': _('Please enter the price session in USD')}),
            'session_price_sp': forms.TextInput(attrs={'placeholder': _('Session price in Syrian Pound'), 'data-error': _('Please enter the price session in Syrian pound')}),
        }


    def __init__(self, *args, **kwargs):
        super(ConsultantProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields["user"].reqired = False
        self.fields["picture"].required = False
        self.fields['name_en'].required = True
        self.fields['name_ar'].required = True
        self.fields['profile_en'].required = False
        self.fields['profile_ar'].required = False
        self.fields['session_price_usd'].required = False
        self.fields['session_price_sp'].required = False

class QuestionNewForm(forms.ModelForm):
    captcha = CaptchaField(label=_('Please enter the following characters'))
    class Meta:
        model = Consultations
        fields = ('consultation', )
        localized_fields = ('__all__')
        labels = {
            'consultation': _('Question'),
        }
        widgets = {
            'user': forms.HiddenInput(),
            'consultation': forms.Textarea(attrs={'rows': 5, 'placeholder': _('Your question'), 'data-error': _('Enter your question')}),
        }


    def __init__(self, *args, **kwargs):
        super(QuestionNewForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['consultation'].required = True
