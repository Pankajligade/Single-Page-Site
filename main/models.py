from django.db import models

class About(models.Model):
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    summary = models.TextField()
    profile_image = models.ImageField(upload_to="about/")
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    location = models.CharField(max_length=100, null=True)
    github = models.URLField(blank=True,null=True)
    linkedin = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    CATEGORY_CHOICES = (
        ('Technical', 'Technical'),
        ('Soft Skill', 'Soft Skill'),
        ('Tool', 'Tool'),
        ('Cloud', 'Cloud'),
        ('Data Science', 'Data Science'),
    )
    name = models.CharField(max_length=50)
    level = models.IntegerField(help_text="Skill level from 1–100")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True)
    icon = models.ImageField(upload_to='skills/', blank=True, null=True)


    def __str__(self):
        return f"{self.name} ({self.category})"


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200, help_text="Comma-separated list",blank=True,null=True)
    github_link = models.URLField(blank=True)
    live_demo = models.URLField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True)
    skills = models.ManyToManyField('Skill', blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)


class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    responsibilities = models.TextField()

    def __str__(self):
        return f"{self.role} @ {self.company}"


class Education(models.Model):
    institute = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.degree} - {self.institute}"


class Certification(models.Model):
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=100)
    completion_date = models.CharField(max_length=20)
    credential_url=models.URLField(max_length=300,blank=True)

    def __str__(self):
        return self.title
