from django.shortcuts import render


def home(request):
    projects = [
        {
            "title": "Personal Portfolio",
            "description": "A responsive Django portfolio with clean HTML, CSS, and JavaScript.",
            "tech": "Django, HTML, CSS, JavaScript",
        },
        {
            "title": "Task Dashboard",
            "description": "A simple dashboard concept for tracking daily work and goals.",
            "tech": "Python, SQLite, UI Design",
        },
        {
            "title": "Landing Page",
            "description": "A modern landing page layout focused on speed and readability.",
            "tech": "HTML, CSS, JavaScript",
        },
    ]

    skills = ["Python", "Django", "HTML", "CSS", "JavaScript", "SQLite"]

    return render(
        request,
        "portfolio/home.html",
        {
            "name": "Your Name",
            "role": "Python Django Developer",
            "projects": projects,
            "skills": skills,
        },
    )
