employees = (
    ("Arun", ("Python", "SQL")),
    ("Meena", ("Java", "AWS")),
    ("Kiran", ("Python", "Docker"))
)

for emp, skills in employees:
    if "Python" in skills:
        print(emp)