from openai import OpenAI



client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def analyze_resume(resume_text, job_desc):
    prompt = f"""
    You are a professional UK recruiter.

    Analyze this resume against the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_desc}
    """

    response = client.chat.completions.create(
    model="meta-llama/llama-3-8b-instruct",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

    return response.choices[0].message.content or "No response"