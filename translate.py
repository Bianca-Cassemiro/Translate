from pathlib import Path
from openai import OpenAI

client = OpenAI()
from openai import OpenAI
import os


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

with open("audio.mp3", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
      model="whisper-1", 
      file=audio_file, 
      response_format="text"
    )

print(transcript)

def chat_with_gpt(prompt):

    response = client.chat.completions.create(model="gpt-3.5-turbo",  
    messages=[
        {"role": "system", "content": "Traduza o conteúdo para o inglês"},
        {"role": "user", "content": prompt},
    ])

    return response.choices[0].message.content


print(chat_with_gpt(transcript))

speech_file_path = Path(__file__).parent / "speech.mp3"

response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input= chat_with_gpt(transcript),
)


response.stream_to_file(speech_file_path)