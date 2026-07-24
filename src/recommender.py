import json


def load_courses():
    with open("data/courses.json", "r") as file:
        return json.load(file)


def load_students():
    with open("sample_profiles/student_profiles.json", "r") as file:
        return json.load(file)


def recommend_courses(student):
    courses = load_courses()

    recommendations = []

    # Convert known skills to lowercase and remove extra spaces
    known_skills = [
        skill.strip().lower()
        for skill in student["known_skills"]
    ]

    for course in courses:
        if course["course"].strip().lower() not in known_skills:
            recommendations.append({
                "course": course["course"],
                "reason": f"Recommended because you want to become a {student['goal']}."
            })

    return recommendations