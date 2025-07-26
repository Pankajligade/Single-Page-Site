
import os
import django
from main.models import Project, Skill
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_site.settings")
django.setup()



project_data = [
    {
        "title": "AI Chatbots",
        "description": "Secure chatbot using OpenAI GPT-4 integrated with Django and Python backend.",
        "github_link": "",
        "live_demo": "",
        "technologies": "Django, OpenAI, Python",
        "skills": ["Python", "Django", "OpenAI"]
    },
    {
        "title": "Automated Ticket Resolution",
        "description": "ServiceNow + GPT4 auto-ticket assignment and resolution with SOP generation.",
        "technologies": "ServiceNow, Django, GPT-4",
        "skills": ["Python", "ServiceNow", "LLM"]
    },
    {
        "title": "LLM Alert Analysis",
        "description": "Multi-model alert analyzer using Mistral, LLaMA, TinyLLaMA + RAG pipeline.",
        "skills": ["Python", "FAISS", "LLM", "Mistral"]
    },
    {
        "title": "Cloud Optimization",
        "description": "AI-powered insight engine for AWS, Azure, GCP cloud optimization.",
        "skills": ["Python", "Cloud", "LLM", "Optimization"]
    },
    {
        "title": "Defaulter Prediction (SBM Bank)",
        "description": "SVM + Logistic Regression based prediction dashboard with ETL pipelines.",
        "skills": ["Machine Learning", "Python", "SQL"]
    },
    {
        "title": "Business Intelligence",
        "description": "Dashboards in Apache Superset and Power BI with Python pipelines.",
        "skills": ["BI", "Python", "Power BI"]
    }
]

for p in project_data:
    project = Project.objects.create(
        title=p['title'],
        description=p['description'],
        technologies=p.get('technologies', ''),
        github_link=p.get('github_link', ''),
        live_demo=p.get('live_demo', '')
    )
    for skill_name in p.get('skills', []):
        skill = Skill.objects.filter(name__iexact=skill_name).first()
        if skill:
            project.skills.add(skill)

print("✅ Projects seeded successfully.")
