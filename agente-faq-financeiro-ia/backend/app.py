from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, BitsAndBytesConfig
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo Mistral 7B Instruct
model_id = "mistralai/Mistral-7B-Instruct-v0.2"

# Configuração de quantização 4-bit com bitsandbytes
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype="float16"
)

# Carrega tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Carrega modelo com quantização
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config,
    device_map="auto"
)

# Cria pipeline
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)

# Estrutura da pergunta recebida
class Pergunta(BaseModel):
    texto: str

@app.post("/faq")
async def faq(pergunta: Pergunta):
    resposta = generator(
        f"Você é um especialista em finanças. Responda de forma clara e profissional: {pergunta.texto}",
        max_new_tokens=60,       # respostas mais curtas → mais rápidas
        do_sample=False,         # desliga sampling → mais determinístico e rápido
        temperature=0.3,         # menos aleatório → menos esforço de cálculo
        top_k=30,                # reduz espaço de busca
        top_p=0.8,               # restringe probabilidade acumulada
        repetition_penalty=1.1   # mantém coerência sem gastar muito processamento
    )

    texto = resposta[0]["generated_text"]

    texto_limpo = texto.replace(
        f"Você é um especialista em finanças. Responda de forma clara e profissional: {pergunta.texto}", ""
    ).strip()

    return {"resposta": texto_limpo}