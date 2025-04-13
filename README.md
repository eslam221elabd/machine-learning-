conda create -n xyz python=3.11.11                             # run once in cmd
conada activate xyz                                            # every time run app in cmd
pip install google-genai fastapi uvicorn pandas openpyxl       # run once in cmd

uvicorn main:app --reload

http://localhost:8000/query

{
    "query": "أحتاج إلى إصلاح تسريب في حوض المطبخ."
}