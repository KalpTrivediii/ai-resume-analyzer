from openai import OpenAI

client = OpenAI(
    api_key="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",  # ✅ real key here
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