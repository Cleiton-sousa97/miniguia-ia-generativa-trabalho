# 💰 Agente Financeiro Digital

O **Agente Financeiro Digital** é um assistente interativo que combina **Python** e **JavaScript** para oferecer explicações acessíveis sobre investimentos e produtos bancários.  
Ele permite que o usuário faça perguntas por voz e receba respostas faladas, criando uma experiência prática e educativa.

---

## 🚀 Funcionalidades

1. **Gravação de Áudio (Python + JavaScript)**  
   - Captura a voz do usuário diretamente no navegador usando a **MediaStream Recording API**.  
   - Salva o áudio em formato `.wav` para processamento.  
   - [Referência utilizada](https://gist.github.com/korakot/c21c3476c024ad6d56d5f48b0bca92be).

2. **Reconhecimento de Fala com Whisper**  
   - Transcreve o áudio gravado para texto usando o modelo **Whisper** da OpenAI.  
   - Suporte ao idioma português.  

3. **Integração com ChatGPT (Agente Financeiro)**  
   - Envia a transcrição para o modelo da OpenAI.  
   - O agente responde como um consultor financeiro, explicando produtos e investimentos de forma clara.  
   - Uso de **Secrets do Google Colab** para armazenar a chave da API com segurança.

4. **Conversão em Voz com gTTS**  
   - Converte a resposta do agente em áudio.  
   - Reproduz a resposta falada diretamente no notebook.

---

## 🛠️ Tecnologias Utilizadas

- **Python** (Google Colab)
- **JavaScript** (MediaStream Recording API)
- **Whisper** (OpenAI)
- **OpenAI API** (ChatGPT)
- **gTTS** (Google Text-to-Speech)

---

## 📦 Instalação

No Google Colab:

1. Clone ou abra este notebook.  
2. Instale o Whisper:
   ```bash
   !pip install git+https://github.com/openai/whisper.git -q
3. Instale o gTTS:
   ```bash
   !pip install gTTS
4. Configure sua chave da OpenAI como Secret no Colab:
  Vá em Secrets (ícone de chave no menu lateral).
  Crie um Secret chamado OPENAI_API_KEY com sua chave.

---

## ▶️ Como Usar

**1. Gravação de Áudio**

 ```bash
from IPython.display import Audio, display, Javascript
from google.colab import output
from base64 import b64decode

RECORD = """
const sleep  = time => new Promise(resolve => setTimeout(resolve, time))
const b2text = blob => new Promise(resolve => {
  const reader = new FileReader()
  reader.onloadend = e => resolve(e.srcElement.result)
  reader.readAsDataURL(blob)
})
var record = time => new Promise(async resolve => {
  stream = await navigator.mediaDevices.getUserMedia({ audio: true })
  recorder = new MediaRecorder(stream)
  chunks = []
  recorder.ondataavailable = e => chunks.push(e.data)
  recorder.start()
  await sleep(time)
  recorder.onstop = async ()=>{
    blob = new Blob(chunks)
    text = await b2text(blob)
    resolve(text)
  }
  recorder.stop()
})
"""

def record(sec=5):
  display(Javascript(RECORD))
  js_result = output.eval_js('record(%s)' % (sec * 1000))
  audio = b64decode(js_result.split(',')[1])
  file_name = 'request_audio.wav'
  with open(file_name, 'wb') as f:
    f.write(audio)
  return f'/content/{file_name}'

print('Ouvindo...\n')
record_file = record()
display(Audio(record_file, autoplay=False))
```

**2. Reconhecimento de Fala com Whisper**

 ```bash
import whisper

language = "pt"
model = whisper.load_model("small")

result = model.transcribe(record_file, fp16=False, language=language)
transcription = result["text"]
print("Pergunta do usuário:", transcription)
```

**3. Integração com ChatGPT**

 ```bash
from openai import OpenAI
from google.colab import userdata

client = OpenAI(api_key=userdata.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",   # ou gpt-4o-mini se disponível
    messages=[
        {"role": "system", "content": "Você é um agente financeiro que explica investimentos e produtos bancários de forma clara e acessível."},
        {"role": "user", "content": transcription}
    ]
)

chatgpt_response = response.choices[0].message.content
print("Resposta do Agente Financeiro:", chatgpt_response)
```

**4. Conversão em Voz com gTTS**

 ```bash
from gtts import gTTS
from IPython.display import Audio, display

gtts_object = gTTS(text=chatgpt_response, lang="pt", slow=False)
response_audio = "/content/response_audio.wav"
gtts_object.save(response_audio)

display(Audio(response_audio, autoplay=True))
```

---

## 🎯 Objetivo
   - O projeto busca criar um assistente financeiro digital que:
   - Responda dúvidas sobre investimentos e produtos bancários.
   - Ofereça explicações acessíveis e educativas.
   - Permita interação por voz, tornando a experiência mais natural.

---

## 📌 Observações
   - O uso da API da OpenAI requer uma chave válida e créditos disponíveis.
   - Para evitar expor sua chave, utilize Secrets do Google Colab.
   - Este projeto é voltado para fins educacionais e demonstrativos.

## 👨‍💻 Autor
   - Projeto desenvolvido por Cleiton Sousa.



   

