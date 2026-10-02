import os 
from pydantic import BaseModel
from fastapi import FastAPI 
from dotenv import load_dotenv
load_dotenv()


class ChatQuery(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply : str
        
students_DB={
    "AI-2026-140":{"name":"john","attendance":87,"elidgibility":True},
    "AI-2026-141":{"name":"jane","attendance":77,"elidgibility":False},
    "AI-2026-142":{"name":"smith","attendance":67,"elidgibility":False},
    "AI-2026-143":{"name":"rocky","attendance":89,"elidgibility":True},
    "AI-2026-144":{"name":"rocky","attendance":89,"elidgibility":True}

}

api_key = os.getenv("GEMINI_API_KEY2")

app = FastAPI()

SYSTEM_INSTRUCTION = (
    "you are the campus ai advisor"
    "please be respectful "
    "when student ask about the attendance or exam eligiblity,"
    "call the get_student_record tool"
    "response should be short (2 sentences)"
)

def get_student_record(roll_no:str)->dict:
    """ look up into student record for attendance and elidgiblity
    
    Args:
    roll_no : the student roll no, e.g.'AI-2026-142' or 'AI-2026-141'

    """
    clean_roll = roll_no.strip().upper()

    if clean_roll in students_DB:
        return {"status":"success", "student":students_DB[clean_roll]}

    else:
        return {"status":"not found", "error":f"student {clean_roll} not found"}

@app.post("/", response_model = ChatResponse)
async def chat_with_advisor(query:ChatQuery):


    if api_key and api_key != "your api key here":

        import google.generativeai as genai 

        genai.configure(api_key=api_key)

        model = genai.GenerativeModel(
            model_name = "gemini-3.6-flash",
            system_instruction = SYSTEM_INSTRUCTION,
            tools = [get_student_record]
        )

        chat_session = model.start_chat(enable_automatic_function_calling=True)

        response = chat_session.send_message(query.message)


        return ChatResponse(reply=response.text.strip())
