
from .models import About, Skill, Project, Experience, Education, Certification
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render, redirect



def home(request):
    from .models import About, Skill, Project, Experience, Education, Certification

    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Message sent successfully!")
        return redirect("home")


    context = {
        "about": About.objects.first(),
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "experiences": Experience.objects.all(),
        "education": Education.objects.all(),
        "certifications": Certification.objects.all(),
        "form": form,  # 👈 Include form in context
    }
    return render(request, "main/index.html", context)
