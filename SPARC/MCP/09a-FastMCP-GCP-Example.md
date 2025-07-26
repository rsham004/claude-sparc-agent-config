# 🌐 How to Build an MCP Server with SSE + FastMCP and Deploy It to the Web

This guide walks you through building a **production-ready MCP server** that supports **real-time communication via SSE**, and deploying it to **Google Cloud Platform** using Docker and Cloud Run.

---

## 📦 Overview: What You'll Build

- A [Python](../../tools/foundational/Python.md)-based **MCP server** that exposes tools to an AI agent (e.g., Gemini).
- Uses **Server-Sent Events (SSE)** (see [02-Transport-Mechanisms.md](./02-Transport-Mechanisms.md) for details) for real-time streaming between server and client.
- Hosted on **Google Cloud Run** with a public HTTP endpoint.
- A **client** that connects via SSE, interacts with the server, and uses Gemini to process requests.

---

## 🧰 Tech Stack

| Component | Technology Used | Link (if available) |
|----------|------------------|---------------------|
| Web Server | `uvicorn` (ASGI) | - |
| Framework | `Starlette` | - |
| Protocol | `SSE` (Server-Sent Events) | [02-Transport-Mechanisms.md](./02-Transport-Mechanisms.md) |
| AI Model | `Gemini` (via Google GenAI SDK) | - |
| Containerization | `Docker` | [Docker](../../tools/infrastructure/Docker.md) |
| Deployment | `Google Cloud Run` | - |
| Python Version | `3.10+` | [Python](../../tools/foundational/Python.md) |
| Package Manager | `uv` (ultrafast Python package manager) | [UV](../../tools/foundational_dev/UV.md) |
| MCP Framework | `fastmcp` | [FastMCP](../../tools/protocol_middleware/FastMCP.md) |

---

## 📁 Project Structure

```
~/mcp/
├── clients/
│   └── mcp-client/
├── servers/
│   └── terminal-server/
│       └── sse-server/
├── workspace/
```

---

## ✅ Prerequisites

- [Python](../../tools/foundational/Python.md) 3.10+
- [Docker](../../tools/infrastructure/Docker.md) installed and configured
- Google Cloud CLI (`gcloud`) set up
- Gemini API key (from https://makersuite.google.com/app)

---

## 🔧 Step 1: Set Up the Environment

### ✅ Create directories:

```bash
mkdir -p ~/mcp/{clients,servers,workspace}
cd ~/mcp
```

### ✅ Clone the server and client code:

```bash
# Server
cd servers
# Replace <server-repo-url> with the actual Git repository URL for the server code
git clone [YOUR_SERVER_REPO_URL] terminal-server

# Client
cd ../clients
# Replace <client-repo-url> with the actual Git repository URL for the client code
git clone [YOUR_CLIENT_REPO_URL] mcp-client
```

---

## 📥 Step 2: Install Python and `uv`

### ✅ Install [Python](../../tools/foundational/Python.md) 3.10+:
See the [Python Tool Guide](../../tools/foundational/Python.md) for installation instructions.

### ✅ Install [`uv`](../../tools/foundational_dev/UV.md) (Python package manager):

```bash
curl -Ls https://astral.sh/uv/install.sh | bash
source ~/.bashrc  # or ~/.zshrc depending on your shell
```

---

## 🔐 Step 3: Setup Environment Variables

### ✅ Create `.env` file in `mcp-client`:

```bash
cd ~/mcp/clients/mcp-client
echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
echo ".env" >> .gitignore
```

---

## 🧱 Step 4: Install Dependencies

### ✅ For the Client:

```bash
cd ~/mcp/clients/mcp-client
uv venv  # Creates a Python virtual environment using uv
source .venv/bin/activate  # Activates the virtual environment (use `.venv\Scripts\activate` on Windows CMD)
uv pip install .
```

### ✅ For the Server:

```bash
cd ~/mcp/servers/terminal-server/sse-server
uv venv  # Creates a Python virtual environment using uv
source .venv/bin/activate  # Activates the virtual environment (use `.venv\Scripts\activate` on Windows CMD)
uv pip install .
```

---

## ⚙️ Step 5: Explore the Server Code

### Key files:

- `terminal_server_sse.py`: Main server logic
- `Dockerfile`: To containerize the server

### Exposed Tools:

<pre><code class="language-python">
@tool
async def run_command(cmd: str) -> str:
    """Run terminal command"""
    ...

@tool
async def add_numbers(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b
</code></pre>

### SSE Endpoint Setup (Starlette):

<pre><code class="language-python">
@app.route("/sse")
async def handle_sse(request):
    # Connect SSE stream to MCP server
</code></pre>

---

## 🚀 Step 6: Run the Server Locally

### 🐳 Option 1: [Docker](../../tools/infrastructure/Docker.md) (recommended)

```bash
cd ~/mcp/servers/terminal-server/sse-server
docker build -t terminal-server-sse .
docker run -d --rm -p 8081:8081   -v ~/mcp/workspace:/root/mcp/workspace   terminal-server-sse
```

### 🧪 Option 2: Run with Uvicorn (non-container)

```bash
# Ensure uvicorn is installed in your environment (uv add uvicorn)
uvicorn terminal_server_sse:app --host 0.0.0.0 --port 8081
```

---

## 🧠 Step 7: Run the Client

```bash
cd ~/mcp/clients/mcp-client
uv run client_sse.py --server-url http://localhost:8081/sse
```

---

## ☁️ Step 8: Deploy to Google Cloud

### ✅ Build and Push Image

```bash
cd ~/mcp/servers/terminal-server/sse-server
# Replace YOUR_PROJECT_ID with your actual Google Cloud Project ID
docker buildx build --platform linux/amd64 -t gcr.io/[YOUR_PROJECT_ID]/mcpsse-server .
docker push gcr.io/[YOUR_PROJECT_ID]/mcpsse-server
```

### ✅ Deploy with Cloud Run

```bash
# Replace YOUR_PROJECT_ID with your actual Google Cloud Project ID
gcloud run deploy mcpsse-server   --image gcr.io/[YOUR_PROJECT_ID]/mcpsse-server   --platform managed   --region us-central1   --port 8081   --allow-unauthenticated
```

### ✅ Copy the deployed URL

Note the URL provided after successful deployment (e.g., `https://mcpsse-server-xxxxxxxxxx-uc.a.run.app`). Use this as the `--server-url` in your client.

### ✅ Test the Deployed Endpoint (Optional)

You can quickly test if the server is responding using `curl`:
```bash
curl https://your-cloudrun-url/sse 
# Replace with your actual deployed URL
# Expect an SSE stream opening message or headers if successful
```

---

## ✅ Step 9: Use the Client with Remote Server

```bash
cd ~/mcp/clients/mcp-client
# Replace https://your-cloudrun-url/sse with the actual URL from the Cloud Run deployment
uv run client_sse.py --server-url [YOUR_DEPLOYED_CLOUD_RUN_URL]/sse
```

Now you’re interacting with a **fully deployed, real-time, tool-enabled MCP server over SSE**!

---

## 📌 Summary

| Component | Setup Complete |
|-----------|----------------|
| Local Dev Environment | ✅ |
| Server with Tools | ✅ |
| SSE Streaming | ✅ |
| Cloud Deployment | ✅ |
| Gemini Integration | ✅ |
| Secure API Key Handling | ✅ |

---

## 📚 Useful Links

- [FastMCP GitHub](https://github.com/Shoggyai/fastmcp) (or specific source) - See also: [FastMCP Tool Guide](../../tools/protocol_middleware/FastMCP.md)
- [Gemini API](https://makersuite.google.com/app)
- [Google Cloud Run Docs](https://cloud.google.com/run)

---

## 🧪 Next Steps

- Add more tools (PDF summarizer, image generator, etc.)
- Introduce authentication with bearer tokens
- Build a UI frontend for the client

---
*Licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)*
*Visit [ProductFoundry.ai](https://productfoundry.ai)*
