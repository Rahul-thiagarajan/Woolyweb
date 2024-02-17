import openai
openai.api_key = "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"
chat_messages=[]
def solu(question):
    solutions = []
    for i in question:
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": """you are a personalised chatbot for the illetrate farmers in indian wool industry
             .You should not greet the user. Never return a question as a answer,answer precisely when the user asks something.If you dont know the accurate answer just give the approximate answer.
             You must give the answer dont provide suggestions.Provide interactive personal assistance and provide answers related to wool related queries

"""},

            {"role": "user", "content": i}
        ]
        )
        solutions.append(completion.choices[0].message["content"])

    return solutions[0]
