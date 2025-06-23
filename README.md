# 🧠 Local LLM Chat App

A full-stack chatbot web application using a React frontend and FastAPI backend. The backend connects to a locally hosted LLM (e.g., Qwen2 or DeepSeek via LM Studio) to provide intelligent, context-aware conversation. Everything is containerized using Docker Compose for easy deployment.

---

## 🚀 Features

- 🔧 FastAPI backend connects to your local LLM Studio model (via API).
- 💬 React-based frontend for clean and fast UI.
- 🧠 Remembers user conversation context.
- 🐳 Dockerized — just one command to run the whole app.

---

## 📦 Prerequisites (Install these before using)

- [Docker](https://docs.docker.com/get-docker/)
- [LM Studio](https://lmstudio.ai/) (latest version)

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/local-llm-chat-app.git
cd local-llm-chat-app
```

---

### 2. Run your model in LM Studio

Before running the app, make sure LM Studio is up and running:

- Open LM Studio on your system.
- Load any chat-compatible model (e.g., **Qwen2-7B-Instruct**, **DeepSeek-Coder**, etc.).
- Go to the **"Developer" tab** in LM Studio.
- Enable the server by toggling **"Status:stopped/not running"**.
- Set the **port** to `1234` and make sure the server is listening at:

```
http://localhost:1234
```

Once LM Studio is serving the model, you can now run the app.

---

### 3. Run the full application with Docker

```bash
docker compose up
```

---

### 4. Access the app

- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend API: [http://localhost:8000](http://localhost:8000)

You can start chatting through the frontend UI.

---

## 🧼 Stopping the App

```bash
docker compose down
```

---

###Max context = 10 conversations