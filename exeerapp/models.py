from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Taxonomy(models.Model):
    term = models.CharField(max_length=100)

class Articles(models.Model):
    taxonomy_id = models.OneToOneField(Taxonomy, on_delete=models.CASCADE)
    glossary = models.CharField(max_length=20, default='help-guide')
    title_en = models.CharField(max_length=100, default='')
    title_ar = models.CharField(max_length=100, default='')
    content_en = RichTextUploadingField()
    content_ar = RichTextUploadingField()
    date = models.DateTimeField(default=datetime.now, blank=True)

class HelpGuideSnippets(models.Model):
    article_id = models.OneToOneField(Articles, on_delete=models.CASCADE)
    content_en = models.CharField(max_length=254)
    content_ar = models.CharField(max_length=254)
    date = models.DateTimeField(default=datetime.now, blank=True)

class User_HelpGuide_Taxonomy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    snippet = models.OneToOneField(HelpGuideSnippets, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=2)
    country = models.CharField(max_length=15)
    city = models.CharField(max_length=15)

class ConsultantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name_en = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100)
    picture = models.FileField(upload_to='uploads/consultants-pics/', null=True)
    profile_en = models.TextField(null=True)
    profile_ar = models.TextField(null=True)
    session_price_sp = models.IntegerField(null=True)
    session_price_usd = models.IntegerField(null=True)


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=256)

class Coupons(models.Model):
    consultant = models.OneToOneField(User, on_delete=models.CASCADE, related_name='coupon2consultant')
    client = models.OneToOneField(User, on_delete=models.CASCADE, related_name='coupon2client')
    value = models.IntegerField()
    currency = models.CharField(max_length=3)
    date = models.DateTimeField(default=datetime.now, blank=True)
    released = models.BooleanField()
    released_date = models.DateTimeField()

class Appointments(models.Model):
    consultant = models.OneToOneField(User, on_delete=models.CASCADE, related_name='appointment2consultant')
    client = models.OneToOneField(User, on_delete=models.CASCADE, related_name='appointment2client')
    remind_client = models.BooleanField()
    client_reminded = models.BooleanField()
    coupon_id = models.OneToOneField(Coupons, on_delete=models.CASCADE)
    price = models.IntegerField()
    currency = models.CharField(max_length=3)
    date = models.DateTimeField()

class Consultations(models.Model):
    consultant = models.OneToOneField(User, on_delete=models.CASCADE, related_name='consultation2consultant', null=True)
    client = models.OneToOneField(User, on_delete=models.CASCADE, related_name='consultation2client', null=True)
    client_email = models.EmailField(null=True)
    title  = models.CharField(max_length=254, null=True)
    consultation = models.TextField(verbose_name='Original question')
    consultation_anonymous = models.TextField(null=True, verbose_name='Anonymous question')
    date = models.DateTimeField(default=datetime.now, blank=True)
    reply = models.TextField(null=True, verbose_name='Original answer')
    reply_anonymous = models.TextField(null=True, verbose_name='Anonymous answer')
    published = models.BooleanField()

    def __str__(self):
        return self.consultation[0:30] + "..."

class Sessions(models.Model):
    consultant = models.OneToOneField(User, on_delete=models.CASCADE, related_name='session2consultant')
    client = models.OneToOneField(User, on_delete=models.CASCADE, related_name="session2client")
    appointment = models.OneToOneField(Appointments, unique=True, on_delete=models.CASCADE)
    audio_url = models.CharField(max_length=254)
    video_url = models.CharField(max_length=254)
    prescribtion_id = models.IntegerField()
    notes = models.TextField()

class SessionDashboards(models.Model):
    session_id = models.OneToOneField(Sessions, on_delete=models.CASCADE)
    #dashboard_id = models.OneToOneField(Dashboards, on_delete=models.CASCADE)

class Messages(models.Model):
    message = models.TextField()
    sender = models.OneToOneField(User, on_delete=models.CASCADE, related_name='message2sender')
    receiver = models.OneToOneField(User, on_delete=models.CASCADE, related_name='message2reciever')
    sender = models.CharField(max_length=10) #consultant/#client
    session_id = models.OneToOneField(Sessions, on_delete=models.CASCADE)
    attachment_type = models.CharField(max_length=10)
    date = models.DateTimeField(default=datetime.now, blank=True)

class Prescribtions(models.Model):
    session = models.OneToOneField(Sessions, on_delete=models.CASCADE)
    packed = models.BooleanField()
    packer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='prescribtion2packer')
    shipped = models.BooleanField()
    shipper = models.OneToOneField(User, on_delete=models.CASCADE, related_name='prescribtion2shipper')
    date = models.DateTimeField(default=datetime.now, blank=True)

class Drugs(models.Model):
    name_en = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)
    made = models.CharField(max_length=3)
    price = models.IntegerField()

class PrescribtionDrugs(models.Model):
    prescribtion = models.OneToOneField(Prescribtions, on_delete=models.CASCADE)
    drug = models.OneToOneField(Drugs, unique=True, on_delete=models.CASCADE)

class Gallery(models.Model):
    owner = models.IntegerField()#0 = site; otherwise consultant_id
    type = models.CharField(max_length=10)#file/photo/audio/video/dashboard
    taxonomy = models.OneToOneField(Taxonomy, on_delete=models.CASCADE)

class Consultant_ClientFile(models.Model):
    consultant = models.OneToOneField(User, on_delete=models.CASCADE, related_name="file2consultant")
    client = models.OneToOneField(User, on_delete=models.CASCADE, related_name="file2client")
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    summary = models.TextField()
    summary_backup = models.TextField()
