# Plan: Building and Deploying a Python MCP Server with SSE

This plan outlines the steps required to build, test, and deploy a [Python](../../tools/foundational/Python.md)-based MCP server using SSE, [FastMCP](../../tools/protocol_middleware/FastMCP.md), [Docker](../../tools/infrastructure/Docker.md), and Google Cloud Run, based on the guide in [05-BuildingMCP.md](./05-BuildingMCP.md).

## Phase 1: Environment Setup and Prerequisites

- [ ] Install [Python](../../tools/foundational/Python.md) 3.10+ (Easy)
- [ ] Install [Docker](../../tools/infrastructure/Docker.md) and configure (Medium)
- [ ] Install and configure Google Cloud CLI (`gcloud`) (Medium)
- [ ] Obtain a Gemini API key (Easy)
- [ ] Install [`uv`](../../tools/foundational_dev/UV.md) Python package manager (Easy)
- [ ] Create base project directory structure (`~/mcp/{clients,servers,workspace}`) (Easy)
- [ ] Clone server repository into `~/mcp/servers/terminal-server` (Easy)
- [ ] Clone client repository into `~/mcp/clients/mcp-client` (Easy)
- [ ] Create and configure `.env` file in client directory with `GEMINI_API_KEY` (Easy)

## Phase 2: Dependency Installation and Local Setup

- [ ] Create and activate [Python](../../tools/foundational/Python.md) virtual environment for the client using [`uv`](../../tools/foundational_dev/UV.md) (Easy)
- [ ] Install client dependencies using `uv pip install .` (Easy)
- [ ] Create and activate [Python](../../tools/foundational/Python.md) virtual environment for the server using [`uv`](../../tools/foundational_dev/UV.md) (Easy)
- [ ] Install server dependencies using `uv pip install .` (Easy)
- [ ] Review server code (`terminal_server_sse.py`, `Dockerfile`) (Medium)

## Phase 3: Local Testing

- [ ] Build the server [Docker](../../tools/infrastructure/Docker.md) image (`docker build`) (Medium)
- [ ] Run the server container locally using `docker run`, mounting the workspace volume (Medium)
- [ ] *Alternatively:* Run the server directly using `uvicorn` (Easy)
- [ ] Run the client script (`client_sse.py`) connecting to the local server URL (`http://localhost:8081/sse`) (Easy)
- [ ] Test tool invocation (e.g., `run_command`, `add_numbers`) via the client (Medium)

## Phase 4: Cloud Deployment (Google Cloud Run)

- [ ] Build a multi-platform [Docker](../../tools/infrastructure/Docker.md) image for the server (`docker buildx build --platform linux/amd64`) (Medium)
- [ ] Tag the image for Google Container Registry (`gcr.io/[YOUR_PROJECT_ID]/mcpsse-server`) (Easy)
- [ ] Push the image to Google Container Registry (`docker push`) (Easy)
- [ ] Deploy the image to Cloud Run using `gcloud run deploy` (Medium)
- [ ] Configure Cloud Run settings (region, port, allow unauthenticated) (Medium)
- [ ] Note the deployed service URL (Easy)
- [ ] Test the deployed endpoint using `curl` (Optional but recommended) (Easy)

## Phase 5: Remote Testing

- [ ] Run the client script (`client_sse.py`) connecting to the deployed Cloud Run server URL (Easy)
- [ ] Test tool invocation via the client against the remote server (Medium)

## Phase 6: Next Steps & Enhancements (Future Work)

- [ ] Add more tools to the server (e.g., PDF summarizer, image generator) (Medium/Complex depending on tool)
- [ ] Implement authentication (e.g., bearer tokens) (Complex)
- [ ] Build a UI frontend for the client (Complex)

---
*Licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)*
*Visit [ProductFoundry.ai](https://productfoundry.ai)*
