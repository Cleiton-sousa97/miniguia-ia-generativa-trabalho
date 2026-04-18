# 🤖 FAQ Financeiro IA

Um assistente virtual inteligente especializado em finanças, que utiliza o modelo de linguagem de última geração **Mistral 7B Instruct** (via Hugging Face) para responder perguntas de forma clara e profissional. O projeto utiliza técnicas de quantização (4-bit) para permitir a execução do modelo de IA de forma eficiente em hardware acessível.

---

## 🚀 Tecnologias Utilizadas

### Backend
* **Python 3.10+**
* **FastAPI**: Framework web moderno e de alta performance.
* **Transformers (Hugging Face)**: Para manipulação e execução do modelo LLM.
* **BitsAndBytes**: Para quantização de 4 bits, reduzindo drasticamente o consumo de VRAM.
* **PyTorch**: Engine para processamento de tensores e redes neurais.

### Frontend
* **HTML5 & CSS3**: Estrutura e estilização moderna com design responsivo.
* **JavaScript (Vanilla)**: Lógica de comunicação assíncrona com a API (Fetch API).
  

## 📂 Estrutura do Projeto

```bash
agente-faq-financeiro-ia/
│
├── backend/
│   └── app.py          # Backend FastAPI com modelo Mistral
│
├── frontend/
│   ├── index.html      # Interface principal
│   ├── style.css       # Estilos visuais
│   └── app.js          # Lógica de interação com backend
│
└── README.md       # Documentação do projeto
```

---

## 🛠️ Arquitetura do Sistema

O sistema opera seguindo o fluxo abaixo:
1.  **Entrada**: O usuário digita uma dúvida financeira na interface web.
2.  **Requisição**: O Frontend envia um `POST` para o endpoint `/faq` do servidor FastAPI.
3.  **Processamento**: O Backend recebe o texto, aplica um *System Prompt* de especialista financeiro e processa através do modelo Mistral-7B.
4.  **Otimização**: A IA gera a resposta utilizando parâmetros de baixa temperatura para maior assertividade.
5.  **Saída**: O Frontend recebe o JSON, remove metadados desnecessários e exibe a resposta no chat.

---

## 📋 Pré-requisitos

Para rodar o backend, é altamente recomendado o uso de uma GPU NVIDIA com suporte a CUDA devido ao tamanho do modelo.

**Bibliotecas Necessárias:**
* NVIDIA Drivers & CUDA Toolkit.
* Linux ou WSL2 (recomendado para suporte pleno ao `bitsandbytes`).

---

## 🔧 Instalação e Configuração

### 1. Clonar o repositório
```bash
git clone [https://github.com/seu-usuario/faq-financeiro-ia.git](https://github.com/seu-usuario/faq-financeiro-ia.git)
cd faq-financeiro-ia
```

### 2. Configurar ambiente virtual (Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências
```bash
pip install fastapi uvicorn transformers torch accelerate bitsandbytes
```

---

## 🚀 Como Executar

### Iniciando o Backend
Navegue até a pasta do backend e execute:
```bash
uvicorn app:app --reload
```
O servidor estará disponível em: http://127.0.0.1:8000

### Iniciando o Frontend
Basta abrir o arquivo index.html em seu navegador de preferência. Certifique-se de que o backend já está rodando para que as perguntas sejam respondidas.

---

## 📝 Detalhes do Modelo de IA

O projeto utiliza o modelo `Mistral-7B-Instruct-v0.2` com as seguintes otimizações:

* Quantização 4-bit (NF4): Permite que o modelo rode com muito menos memória de vídeo (VRAM).
* Double Quantization: Otimiza ainda mais o espaço de armazenamento dos pesos.

### Parâmetros de Geração:

* `temperature: 0.3`: Respostas mais conservadoras e precisas.
* `max_new_tokens: 60`: Foco em respostas rápidas e diretas.
* `repetition_penalty: 1.1`: Evita que a IA entre em loops de repetição de palavras.

  
---

## 💡 Exemplos de Perguntas

Como o agente está configurado com um *system prompt* de especialista em finanças, ele responderá melhor a questões como:

* **Investimentos:** "Qual a diferença entre CDB e Tesouro Selic?"
* **Tecnologia Financeira:** "O que é PIX e como usar com segurança?"
* **Conceitos:** "O que é taxa Selic e por que influencia os juros?"
* **Educação Financeira:** "Qual a diferença entre juros simples e compostos?"


---


## ✒️ Autor

* Cleiton - Desenvolvimento Fullstack e Integração de IA




