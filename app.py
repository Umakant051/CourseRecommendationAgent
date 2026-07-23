import os
import json
from dotenv import load_dotenv
from groq import Groq

from src.recommender import load_students, recommend_courses

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Store all AI-generated recommendations
results = []

# Load student profiles
students = load_students()

# Process each student
for student in students:

    recommendations = recommend_courses(student)

    course_list = "\n".join(
        [f"- {course['course']}: {course['reason']}" for course in recommendations]
    )

    prompt = f"""
You are an AI Course Recommendation Assistant.

Your task is to recommend ONLY from the provided course list.

Do NOT invent new course names.
Do NOT recommend courses that are not listed below.

Student Name: {student['name']}
Background: {student['background']}
Career Goal: {student['goal']}
Known Skills: {", ".join(student['known_skills'])}

Available Recommended Courses:
{course_list}

Instructions:
1. Create an ordered learning path.
2. Explain why each course is recommended.
3. Recommend ONLY the courses listed above.
4. Keep the response beginner-friendly.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    ai_response = response.choices[0].message.content

    print("=" * 60)
    print(f"Student: {student['name']}")
    print("=" * 60)
    print(ai_response)
    print()

    # Save AI response
    results.append(
        {
            "student": student["name"],
            "goal": student["goal"],
            "recommendation": ai_response
        }
    )

# Save recommendations to JSON file
with open("outputs/recommendations.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4, ensure_ascii=False)

print("=" * 60)
print("✅ Recommendations saved successfully!")
print("📄 File saved at: outputs/recommendations.json")
print("=" * 60)