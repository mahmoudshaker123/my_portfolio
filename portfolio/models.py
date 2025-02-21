from django.db import models

# Create your models here.

class SiteSettings(models.Model):
    cv_link = models.URLField(help_text="رابط تحميل السيرة الذاتية" )
    
    def __str__(self):
        return "Site Settings"



class Home(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
class AboutMe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Statistic(models.Model):
    name = models.CharField(max_length=50)  # مثال: Projects, Experience
    value = models.PositiveIntegerField()  # مثال: 6, 1, 3, 40

    def __str__(self):
        return f"{self.name}: {self.value}"
    
    
class Skill(models.Model):
    name = models.CharField(max_length=50)  # مثال: Python, Django, HTML
    proficiency = models.PositiveIntegerField(help_text="Enter percentage (e.g., 90)")  # مثال: 90%

    def __str__(self):
        return f"{self.name} - {self.proficiency}%"


class TimelineEntry(models.Model):
    year = models.CharField(max_length=20)  # مثال: "2022 - Present"
    job_title = models.CharField(max_length=100)  # مثال: "Freelance Backend Developer"
    description = models.TextField()  # تفاصيل الوظيفة
    
    def __str__(self):
        return f"{self.year} - {self.job_title}"


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    link = models.URLField(help_text="رابط المشروع")

    def __str__(self):
        return self.title



class ContactInfo(models.Model):
    location = models.CharField(max_length=255, default="Cairo, Egypt")
    email = models.EmailField()
    education = models.CharField(max_length=255, default="Zagazig University, Computer Science")
    mobile_number = models.CharField(max_length=20)
    languages = models.CharField(max_length=255, default="Arabic, English")

    def __str__(self):
        return "Contact Information"
    


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # وقت الإرسال

    def __str__(self):
        return f"Message from {self.name}"
