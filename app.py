import markdown
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from groq import Groq

from src.recommender import recommend_courses

# Load environment variables
load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    try:

        name = request.form.get("name")
        skills = request.form.get("skills")
        interests = request.form.get("interests")
        goal = request.form.get("goal")
        level = request.form.get("level")

        student = {
            "name": name,
            "background": interests,
            "goal": goal,
            "known_skills": [
                skill.strip()
                for skill in skills.split(",")
                if skill.strip()
            ]
        }

        recommendations = recommend_courses(student)

        course_list = "\n".join(
            [
                f"- {course['course']}: {course['reason']}"
                for course in recommendations
            ]
        )

        prompt = f"""
You are an AI Course Recommendation Assistant.

Recommend ONLY from the provided course list.

Student Name: {name}
Career Goal: {goal}
Current Skills: {skills}
Interests: {interests}
Learning Level: {level}

Available Courses:
{course_list}

Instructions:

1. Recommend only from the available courses.
2. Arrange the courses in the best learning order.
3. For every course provide:
   • Course Name
   • Why it is recommended
4. Keep the explanation short.
5. Use headings and bullet points.
6. End with a motivational message.
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

        #recommendation = response.choices[0].message.content
        recommendation = markdown.markdown(
        response.choices[0].message.content,
    extensions=["extra"]
        )

        return render_template(
            "result.html",
            name=name,
            recommendation=recommendation
        )

    except Exception as e:

        return render_template(
            "result.html",
            name="User",
            recommendation=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)