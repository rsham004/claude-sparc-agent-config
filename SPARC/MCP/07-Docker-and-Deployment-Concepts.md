# 🐳 Using Docker for MCP Server Deployment

Containerizing your MCP server using [Docker](../../tools/infrastructure/Docker.md) is highly recommended, especially for deployment and ensuring consistency across environments.

---

## 🤔 Why Use Docker for MCP Servers?

- **Consistency:** Packages your server code, Python interpreter, dependencies, and system libraries into a single, immutable image. Runs the same everywhere.
- **Portability:** Docker containers can run on any machine with Docker installed (local machine, cloud VM, managed container service).
- **Dependency Management:** Isolates your server's dependencies from the host system and other projects. Avoids conflicts.
- **Scalability:** Container orchestration platforms (like Kubernetes, Docker Swarm, or managed services like Google Cloud Run, AWS Fargate) make it easy to scale containerized applications.
- **Simplified Deployment:** Streamlines the process of getting your server running in different environments (development, staging, production).

---

## 📝 Example Dockerfile for a Python MCP Server

This example assumes a Python MCP server built using the `mcp-cli` SDK (as shown in [05-Python-SDK-Implementation.md](./05-Python-SDK-Implementation.md)) and using `uv` for package management.

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install uv (faster package manager)
RUN pip install uv

# Copy only the dependency definition files first to leverage Docker cache
COPY pyproject.toml uv.lock* ./

# Install dependencies using uv
# --system installs into the system Python, suitable for containers
# --no-cache avoids filling the image with unnecessary cache
RUN uv pip install --system --no-cache -r requirements.txt # Or use pyproject.toml if applicable

# Copy the rest of the application code into the container
COPY . .

# Define environment variables if needed (e.g., for configuration)
# ENV MY_CONFIG_VAR="default_value"

# Expose the port the server will run on (adjust if your server uses a different port)
# This is important for SSE servers. STDIO servers don't typically need EXPOSE.
EXPOSE 8050

# Define the command to run your application
# This example assumes your server script is named server.py and uses uvicorn for SSE.
# Adjust the command based on your server's entry point and transport mechanism.
# For STDIO, the command might just be: CMD ["python", "server.py"]
# For SSE using uvicorn:
CMD ["uvicorn", "server:mcp", "--host", "0.0.0.0", "--port", "8050"]
# Replace 'server:mcp' with 'your_script_name:your_mcp_app_instance'
```

**Explanation:**

1.  **`FROM python:3.11-slim`**: Starts with a lightweight official Python image.
2.  **`WORKDIR /app`**: Sets the default directory inside the container.
3.  **`RUN pip install uv`**: Installs the `uv` package manager.
4.  **`COPY pyproject.toml uv.lock* ./`**: Copies dependency files.
5.  **`RUN uv pip install ...`**: Installs dependencies using `uv`. Caching is optimized here.
6.  **`COPY . .`**: Copies the application source code.
7.  **`EXPOSE 8050`**: Informs Docker that the container listens on this port (relevant for networking, especially for SSE).
8.  **`CMD [...]`**: Specifies the default command to run when the container starts. This example uses `uvicorn` for an ASGI/SSE server. Adjust as needed for your specific server script and transport (e.g., `CMD ["python", "server_stdio.py"]` for an STDIO server).

---

## 🚀 Building and Running Locally with Docker

1.  **Build the Image:** Navigate to the directory containing your `Dockerfile` and server code.
    ```bash
    # Build the image and tag it (e.g., 'my-mcp-server')
    docker build -t my-mcp-server .
    ```

2.  **Run the Container:**
    *   **For SSE Servers:** Map the container's exposed port to a port on your host machine.
        ```bash
        # Run in detached mode (-d), remove container on exit (--rm), map host port 8050 to container port 8050 (-p)
        docker run -d --rm -p 8050:8050 --name mcp-server-container my-mcp-server
        ```
        Your SSE server should now be accessible at `http://localhost:8050` (or the mapped host port).
    *   **For STDIO Servers:** Run interactively to connect via standard input/output.
        ```bash
        # Run interactively (-it), remove container on exit (--rm)
        docker run -it --rm --name mcp-server-container my-mcp-server
        ```
        Your MCP client configured for STDIO would typically need to execute this `docker run` command itself to manage the process.

---

## ☁️ Deployment Concepts

Once your MCP server is containerized, you can deploy it to various platforms:

- **Virtual Machines (VMs):** Install Docker on a cloud VM (e.g., EC2, Compute Engine, DigitalOcean Droplet) and run the container using `docker run`.
- **Managed Container Services:** Use services designed to run containers without managing the underlying infrastructure. These often handle scaling, networking, and updates automatically. Examples include:
    - **Google Cloud Run:** Serverless platform, scales to zero. Ideal for HTTP-based (SSE) servers.
    - **AWS Fargate:** Serverless compute engine for containers with ECS or EKS.
    - **Azure Container Instances (ACI):** Simple way to run containers in Azure without orchestration.
- **Kubernetes:** A powerful container orchestration platform for complex deployments requiring fine-grained control (e.g., GKE, EKS, AKS, or self-hosted).

**Deployment Workflow:**

1.  **Build Image:** Create the Docker image.
2.  **Push Image:** Push the image to a container registry (e.g., Docker Hub, Google Container Registry (GCR), AWS Elastic Container Registry (ECR), Azure Container Registry (ACR)).
3.  **Deploy:** Configure your chosen platform (Cloud Run, Fargate, Kubernetes, etc.) to pull the image from the registry and run it as a service.

---

## ✨ Specific Deployment Example: FastMCP on Google Cloud Run

For a detailed, step-by-step guide on deploying a specific type of Python MCP server (using the `fastmcp` library) to Google Cloud Run, see:

➡️ **[09-FastMCP-GCP-Example.md](./09-FastMCP-GCP-Example.md)**

This example covers building a multi-platform image (`docker buildx`), pushing to GCR, and deploying using the `gcloud` CLI.

---

## 📝 Implementation Plan

### Phase 1: Docker Setup & Dockerfile Creation
- [ ] Install Docker Desktop or Docker Engine on your development machine (Easy/Medium depending on OS)
- [ ] Create a `Dockerfile` in the root directory of your MCP server project (Easy)
- [ ] Choose and specify a suitable Python base image (`FROM python:...`) (Easy)
- [ ] Set the working directory within the container (`WORKDIR /app`) (Easy)
- [ ] Add steps to copy dependency files (`pyproject.toml`, `requirements.txt`, etc.) (Easy)
- [ ] Add steps to install dependencies (e.g., `RUN uv pip install ...` or `RUN pip install ...`) (Easy)
- [ ] Add step to copy the application source code (`COPY . .`) (Easy)
- [ ] Add `EXPOSE` instruction for the port the server listens on (if using SSE/HTTP) (Easy)
- [ ] Define the `CMD` instruction to run the server (e.g., using `uvicorn` for SSE or `python` for STDIO) (Medium)

### Phase 2: Building & Running Locally
- [ ] Open a terminal in the project directory (Easy)
- [ ] Build the Docker image using `docker build -t your-image-name .` (Easy)
- [ ] Run the container locally using `docker run`: (Medium)
    - [ ] For SSE: Use `-p host_port:container_port` to map ports (e.g., `-p 8050:8050`)
    - [ ] For STDIO: Use `-it` for interactive mode if needed by the client
    - [ ] Consider using `-d` for detached mode (background) and `--rm` for cleanup
    - [ ] Mount volumes (`-v`) if needed for development or workspace access (Medium)
- [ ] Test connecting to the locally running containerized server using your MCP client (Easy/Medium)

### Phase 3: Deployment Preparation
- [ ] Choose a container registry (e.g., Docker Hub, GCR, ECR, ACR) (Easy)
- [ ] Create an account and repository on the chosen registry (Easy/Medium depending on registry)
- [ ] Tag your built Docker image for the registry (`docker tag your-image-name registry/repository:tag`) (Easy)
- [ ] Log in to the container registry using `docker login` (Easy)
- [ ] Push the tagged image to the registry (`docker push registry/repository:tag`) (Easy)
- [ ] (Optional) Consider multi-platform builds (`docker buildx`) if deploying to different architectures (e.g., ARM on some cloud services) (Medium/Complex)

### Phase 4: Cloud Deployment (Conceptual Steps)
- [ ] Choose a cloud deployment platform (e.g., Google Cloud Run, AWS Fargate, Azure Container Instances, VM with Docker) (Medium)
- [ ] Configure the chosen platform to pull the image from your container registry (Medium/Complex depending on platform)
- [ ] Configure necessary settings like port mapping, environment variables, scaling rules, networking, and authentication on the platform (Medium/Complex)
- [ ] Deploy the container/service using the platform's tools (e.g., `gcloud run deploy`, AWS/Azure console/CLI) (Medium)
- [ ] Test connecting to the deployed server using its public URL/IP address (Easy)
- [ ] Refer to specific platform documentation or the example in [09-FastMCP-GCP-Example.md](./09-FastMCP-GCP-Example.md) for detailed steps (Medium)

---
*Licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)*
*Visit [ProductFoundry.ai](https://productfoundry.ai)*
