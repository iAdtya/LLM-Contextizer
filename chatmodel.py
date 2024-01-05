from openai import OpenAI
import gradio as gr

client = OpenAI()

OPENAI_API_KEY='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'

def chat_with_model(user_input):
  response = client.chat.completions.create(
      model="ft:gpt-3.5-turbo-1106:personal::8dlPomGc",
      messages=[
          {"role": "system", "content": "Gen-z is a contextualization bot which contextlize the sentence,phrase,comment,tweet in one,two word gen-z slang"},
          {"role": "user", "content": user_input},
      ]
  )
  return response.choices[0].message.content

# export OPENAI_API_KEY=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

chatbot = gr.Interface(
    fn=chat_with_model,
    inputs=gr.Textbox(lines=2, placeholder="Enter your question here...", label="Question"),
    outputs="text",
    title="Chat with Gen-z Chatbot",
    description="This chatbot will help you contextualize your sentence,phrase,comment,tweet in one,two word gen-z slang"
)

chatbot.launch()
