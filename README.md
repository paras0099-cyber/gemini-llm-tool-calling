# Gemini LLM Tool Calling with FastAPI

> Today I learned how to enable an LLM with custom tools and function calling using Google Gemini and FastAPI.

## 📌 Overview

This project demonstrates how to connect a Large Language Model (**Google Gemini**) to custom tools (Python functions) using **FastAPI**. 

When a user asks about attendance or exam eligibility, the LLM intelligently calls `get_student_record()` to retrieve real-time data from the student database rather than hallucinating answers.

## 🚀 Key Features

- **Tool Use / Function Calling**: Registers python functions as tools passed to `genai.GenerativeModel`.
- **Automatic Function Calling**: Utilizes `enable_automatic_function_calling=True` in Gemini chat sessions.
- **REST API with FastAPI**: Clean input/output validation using Pydantic models (`ChatQuery`, `ChatResponse`).
- **Campus AI Advisor Persona**: System instructions guide tone and concise 2-sentence responses.

## 🛠️ Tech Stack

- **Python 3**
- **FastAPI**
- **Pydantic**
- **Google Generative AI SDK** (`google-generativeai`)
- **python-dotenv**

## 📖 How It Works

1. A user sends a question (e.g., *"What is the attendance of AI-2026-140?"*).
2. Gemini detects the intent and triggers `get_student_record(roll_no="AI-2026-140")`.
3. The function returns structured record data:
   ```json
   {"name": "john", "attendance": 87, "elidgibility": true}
   ```
4. Gemini summarizes the result in a polite, 2-sentence response back to the user.
