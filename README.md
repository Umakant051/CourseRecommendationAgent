# AI Course Recommendation Agent

## Project Overview

The AI Course Recommendation Agent is a beginner-friendly AI application built using Python and the Groq LLM API.

It takes a student's background, career goal, and existing skills as input and recommends a personalized learning path with explanations for every recommended course.

This project was developed as part of the Rooman Technologies AI Agent Challenge.

---

## Features

- Reads student profiles from JSON
- Recommends courses based on career goals
- Uses AI (Groq Llama 3.3 70B) to generate personalized learning paths
- Explains why every course is recommended
- Saves recommendations into a JSON file
- Beginner-friendly implementation

---

## Technologies Used

- Python 3.10
- Groq API
- Llama 3.3 70B Versatile
- python-dotenv
- JSON

---

## Project Structure

```
CourseRecommendationAgent/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
├── .gitignore
│
├── data/
│   ├── students.json
│   └── courses.json
│
├── src/
│   └── recommender.py
│
├── sample_profiles/
│
├── outputs/
│   └── recommendations.json
│
└── venv/
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
cd CourseRecommendationAgent
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## API Key Setup

Create a `.env` file in the project root.

Add your Groq API key.

```
GROQ_API_KEY=your_api_key_here
```

---

## Run the Project

```bash
python app.py
```

---

## Sample Student Input

```json
{
  "name": "Rahul",
  "background": "B.Tech Computer Science",
  "goal": "Python Backend Developer",
  "known_skills": [
    "Python Basics",
    "HTML",
    "CSS"
  ]
}
```

---

## Sample Output

- Ordered learning path
- Course explanations
- Beginner-friendly guidance

The generated recommendations are automatically saved in:

```
outputs/recommendations.json
```

---

## Design Choices

- Used JSON files for simplicity.
- Implemented rule-based course recommendation before sending data to the LLM.
- Used Groq's Llama 3.3 70B model for fast AI-generated explanations.
- Kept the project modular using a separate recommender module.

---

## Trade-offs

- Uses a small static course catalog.
- Recommendations depend on predefined rules.
- No web interface (CLI application only).
- No database integration.

These choices keep the project simple, lightweight, and easy to understand.

---

## Future Improvements

- Web interface using Flask
- Larger course catalog
- Database support
- User authentication
- Personalized course ratings
- Learning progress tracking

---

## Author

**Umakant Karadi**

Built for the Rooman Technologies AI Agent Challenge.