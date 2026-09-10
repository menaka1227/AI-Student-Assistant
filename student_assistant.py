def create_study_plan(subjects, days):
    plan = {}
    for i, subject in enumerate(subjects):
        day = (i % days) + 1
        plan.setdefault(day, []).append(subject)
    return plan


subjects = ["Python", "DBMS", "AI", "Operating System", "Computer Networks"]

days = 5
study_plan = create_study_plan(subjects, days)

print("AI Student Assistant - Study Plan")
print("----------------------------------")

for day, subjects_list in study_plan.items():
    print(f"Day {day}: {', '.join(subjects_list)}")
