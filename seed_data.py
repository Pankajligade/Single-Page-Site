from main.models import About, Skill, Project, Experience, Education, Certification

# Clear old records (optional)
About.objects.all().delete()
Skill.objects.all().delete()
Project.objects.all().delete()
Experience.objects.all().delete()
Education.objects.all().delete()
Certification.objects.all().delete()

# ✅ About
About.objects.create(
    full_name="Pankaj S Ligade",
    role="Software Engineer | LLM Developer",
    summary="""Experienced IT professional with over 6 years of experience, currently working at United Layers. Specialized in Python, Django, LLMs, and Chatbot Development using OpenAI/ChatGPT APIs. Strong background in backend engineering, cloud deployment, and intelligent automation.""",
    email="pankaj.ligade@gmail.com",
    phone="7588797742",
    location="Thane, Maharashtra",
    github="https://github.com/Pankajligade",
    linkedin="https://www.linkedin.com/in/pankaj-ligade-39856b95/",
    website="https://pankaj.tech"
)

# ✅ Skills
skills = [
    ("Python", 95, "Technical"),
    ("Django", 90, "Technical"),
    ("REST APIs", 85, "Technical"),
    ("ChatGPT/OpenAI", 90, "Technical"),
    ("PostgreSQL", 80, "Technical"),
    ("Git", 85, "Tool"),
    ("VS Code", 85, "Tool"),
    ("PyCharm", 85, "Tool"),
    ("AWS (EC2, S3, RDS)", 70, "Cloud"),
    ("Apache Superset", 75, "Tool"),
    ("Power BI", 80, "Tool"),
    ("Streamlit", 85, "Data Science"),
    ("Pandas", 90, "Data Science"),
    ("Scikit-learn", 85, "Data Science"),
    ("Airflow", 70, "Tool"),
]

for name, level, cat in skills:
    Skill.objects.create(name=name, level=level, category=cat)

# ✅ Projects
Project.objects.create(
    title="LLM Chatbot with OpenAI",
    description="Designed and developed an intelligent chatbot using Django and OpenAI APIs. Used prompt engineering and contextual workflows to enable real-time AI support.",
    technologies="Django, Python, OpenAI API, LLM, REST",
    github_link="https://github.com/Pankajligade",
    live_demo="",
)

Project.objects.create(
    title="NPA Prediction Model",
    description="Developed an ML model to predict NPA accounts using classification algorithms. Automated daily defaulter report generation and dashboard visualizations.",
    technologies="Python, Scikit-learn, Streamlit, Pandas",
    github_link="https://github.com/Pankajligade",
    live_demo=""
)

Project.objects.create(
    title="Banking Dashboards",
    description="Designed and deployed dashboards in Power BI and Superset to visualize credit performance, transaction metrics, and RM activity trends.",
    technologies="Power BI, Apache Superset, SQL Server",
    github_link="",
    live_demo=""
)

# ✅ Experience
Experience.objects.create(
    company="United Layers Pvt Ltd",
    role="LLM Engineer / Software Engineer",
    location="Mumbai",
    start_date="Jan 2025",
    end_date="Present",
    responsibilities="""• Built ChatGPT-integrated chatbot using Django\n• Integrated REST APIs and handled backend infrastructure\n• Worked with AWS S3, RDS, and Lambda\n• Maintained high system uptime and logs\n• Participated in agile sprints"""
)

Experience.objects.create(
    company="Clover Infotech (Client: SBM Bank)",
    role="Software Engineer",
    location="Mumbai",
    start_date="Feb 2023",
    end_date="Jan 2025",
    responsibilities="""• NPA automation and EOD process\n• UAT testing as per RBI IRAC norms\n• CCR system development\n• NPA prediction model development\n• Dashboarding with Power BI and Superset"""
)

Experience.objects.create(
    company="Hitachi Hirel Power Electronics",
    role="Sales Analyst / Support Engineer",
    location="Mumbai",
    start_date="2018",
    end_date="2020",
    responsibilities="""• Sales data analysis\n• Dashboard and reporting\n• Customer issue handling"""
)

# ✅ Education
Education.objects.create(
    institute="IIIT-Bangalore",
    degree="Advanced Certification in Data Science",
    start_date="May 2020",
    end_date="Dec 2022",
    location="Mumbai"
)

Education.objects.create(
    institute="Shivaji University",
    degree="B.E in Electronics & Telecommunication",
    start_date="Jun 2016",
    end_date="Apr 2020",
    location="Satara"
)

Education.objects.create(
    institute="MSBTE",
    degree="Diploma in Industrial Electronics",
    start_date="Jun 2011",
    end_date="May 2016",
    location="Thane"
)

# ✅ Certifications (add more if needed)
Certification.objects.create(
    title="Advanced Data Science",
    provider="IIIT-Bangalore",
    completion_date="2022"
)

print("✅ Seeded data successfully!")
