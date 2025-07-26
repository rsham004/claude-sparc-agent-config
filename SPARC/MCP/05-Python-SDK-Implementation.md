# 🐍 Implementing MCP Servers and Clients with the Python SDK

This guide focuses on using the official Python SDK (`mcp-cli`) to build basic MCP servers and clients, covering both local (STDIO) and networked (SSE) communication.

---

## 📦 The Python SDK (`mcp` and `mcp-cli`)

The official Python ecosystem for MCP consists of two main packages:
- **`mcp`**: The core library containing modules for building servers (like `mcp.server.fastmcp`) and clients (`mcp.client.session`).
- **`mcp-cli`**: Provides command-line utilities, most notably the MCP Inspector for testing servers.

- **Installation:** Add both packages to your project's dependencies.
  ```bash
  # Example using uv
  uv pip install mcp mcp-cli
  ```
- **Core Components:** The `mcp` library provides classes (`FastMCP`, `MCPClientSession`) and decorators (`@mcp.tool()`) to define servers, tools, and clients. The `mcp-cli` package provides the `mcp` command-line tool.

---

## 🛠️ Building a Simple MCP Server

Creating a basic MCP server with the SDK is straightforward, often resembling frameworks like FastAPI or Starlette. A functional template based on the example below can be found at `../../templates/MCP/server.py`.

### Server Code Example (`server.py`):

```python
# Corrected functional example
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv(".env") # Optional: Load environment variables if needed

# 1. Initialize the MCP Server application
mcp = FastMCP(
    name="Calculator", # Example name
    host="0.0.0.0",    # Host for SSE transport
    port=8050,         # Port for SSE transport
)

# 2. Define a tool using the @mcp.tool() decorator
# Note: Tool functions can be synchronous or asynchronous
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    print(f"Executing add({a}, {b})")
    return a + b

# Example of another tool (sync)
@mcp.tool()
def uppercase(text: str) -> str:
    """Converts text to uppercase."""
    print(f"Executing uppercase('{text}')")
    return text.upper()

# 3. Run the server directly in the main block
if __name__ == "__main__":
    # Determine transport (e.g., from config, args, or hardcoded)
    transport = "sse" # Example: Defaulting to SSE

    if transport == "stdio":
        print("Running server with stdio transport")
        mcp.run(transport="stdio") # mcp.run is synchronous
    elif transport == "sse":
        print(f"Running server with SSE transport on {mcp.host}:{mcp.port}")
        mcp.run(transport="sse") # mcp.run is synchronous
    else:
        raise ValueError(f"Unknown transport: {transport}")

```

### Key Concepts:
- **`from mcp.server.fastmcp import FastMCP`**: Correct import for the `FastMCP` class from the `mcp-cli` package.
- **`FastMCP(...)`**: Initializes the server application. `name`, `host`, and `port` are common parameters.
- **`@mcp.tool()`**: Decorator attached to the `mcp` instance, used to register functions (sync or async) as tools. Docstrings and type hints are used for description and schema.
- **`mcp.run(transport="...")`**: Synchronously starts the server, listening via the specified transport ("stdio" or "sse").

---

## 🔍 Inspecting Your Server (`mcp dev`)

The `mcp-cli` package provides the MCP Inspector, a development tool to test your running server locally.

1.  **Navigate:** Open your terminal and change to the directory containing your server script (e.g., `server.py`).
    ```bash
    cd path/to/your/server/directory
    ```
2.  **Run the Inspector:** Execute the `mcp dev` command, pointing it to your server script. This command runs your server script in a special development mode that connects it to the inspector.
    ```bash
    mcp dev server.py
    ```
3.  **Download Prompt (First Run):** If it's your first time running the inspector, it will prompt you to download the necessary UI components. Type `Y` and press Enter.
    ```
    Do you want to download the MCP Inspector? [Y/n] Y
    ```
4.  **Access UI:** Once the server is running under `mcp dev`, it will output logs. Look for a local URL where the Inspector UI is being served (e.g., `http://localhost:5173` or similar). Open this URL in your web browser.
5.  **Connect & Test:** Inside the Inspector web UI:
    - Click the **Connect** button. This establishes a connection between the UI and your server process running via `mcp dev`.

    **🧩 MCP Core Primitives:** Before testing, it's helpful to remember the core concepts MCP servers can expose:
    - **Tools:** Model-controlled functions that LLMs can invoke (like API calls, computations). These are the most common primitive.
    - **Resources:** Application-controlled data that provides context (like file contents, database records).
    - **Prompts:** User-controlled templates for LLM interactions.

    The Inspector allows you to interact with these primitives if your server defines them:
    - Use the **List Tools** functionality (often a button or command input) to see the tools registered in your `server.py` using `@mcp.tool()`.
    - Select a specific tool from the list.
    - Input the required arguments for that tool in the provided fields.
    - Click **Call Tool** (or similar) to execute the tool on your server. The results or any errors will be displayed in the UI.
    - You can also explore any defined **Resources** or **Prompts** if your server uses them, although tools are the most common use case.

The inspector is invaluable for interactively debugging your tool definitions, checking input/output schemas, and verifying the execution logic of your server before connecting a real client application or LLM.

---

## 🔌 Building an MCP Client

Clients connect to servers to utilize their tools. The connection method depends on the server's transport mechanism (STDIO or SSE). Template files for both client types are available:

-   **STDIO Client Template:** `../../templates/MCP/client-stdio.py`
-   **SSE Client Template:** `../../templates/MCP/client-sse.py`

These templates demonstrate using helper functions (`stdio_client`, `sse_client`) and the core `ClientSession` from the `mcp` library.

### Client Types Explained:

#### 🖥️ `client-stdio.py` – Standard IO / Local Development
-   **Transport Type:** Standard IO (STDIO)
-   **How it works:** The client script launches the server script (`server.py`) internally as a subprocess. Communication happens via the standard input/output streams between the two processes. They both live on the same machine.
-   **Ideal for:** Local development, quick prototyping, testing server logic without network setup.
-   **Benefits:**
    -   No need to separately run the server; the client manages its lifecycle.
    -   Easy to debug as everything runs locally.
-   **Limitations:**
    -   Cannot connect across different machines or containers.
    -   Not suitable for production deployments where the server needs to be independently managed and accessible.

#### 🌐 `client-sse.py` – SSE / Remote Development
-   **Transport Type:** Server-Sent Events (SSE) via HTTP
-   **How it works:** The client connects to a *separately running* server instance over the network using an HTTP URL (e.g., `http://localhost:8050/sse`). The server must be started independently (e.g., via `python server.py` configured for SSE).
-   **Ideal for:** Production deployments, shared servers, connecting to servers running in Docker or on VMs/cloud platforms.
-   **Benefits:**
    -   Decouples the client and server lifecycles.
    -   Allows the server to be hosted remotely or in a container.
    -   Scalable approach for production environments.
-   **Limitations:**
    -   Requires the server process to be running and accessible at the specified URL before the client can connect.

### Key Concepts (Client Templates):
-   **`from mcp import ClientSession`**: Imports the core session management class.
-   **`from mcp.client.stdio import stdio_client, StdioServerParameters`**: Imports helpers for STDIO connections. `StdioServerParameters` defines how to run the server.
-   **`from mcp.client.sse import sse_client`**: Imports the helper for SSE connections.
-   **`async with stdio_client(...) / sse_client(...)`**: Context managers that establish the connection (either launching the process for STDIO or connecting to the URL for SSE) and provide read/write streams.
-   **`async with ClientSession(read_stream, write_stream)`**: Uses the streams provided by the connection helper to create the actual MCP session.
-   **`await session.initialize()`**: Performs the initial handshake with the server.
-   **`await session.list_tools()`**: Fetches available tools from the server.
-   **`await session.call_tool(name, arguments={...})`**: Executes a specific tool on the server.

---

## 🤔 MCP vs. Standard Function Calling

It's crucial to understand that MCP **doesn't add new capabilities** to LLMs themselves. LLMs could already use tools via function calling (like OpenAI's API).

**So, why use MCP?**

- **Standardization:** MCP provides a *common format* for defining tools (schemas, descriptions, arguments) and a *standard protocol* for how clients (like LLMs or applications) discover and interact with these tools via MCP Servers.
- **Decoupling:** Separates the tool implementation (in the MCP Server) from the application logic (in the MCP Client/LLM application).
- **Ecosystem:** A growing number of pre-built MCP servers and integrations are becoming available, potentially saving development time (e.g., connecting to Slack, GitHub, etc., via a standard MCP server).
- **Reusability:** An MCP server exposing specific tools can be reused across multiple different client applications.

**When *not* to use MCP (or migrate existing projects):**

- If your application uses only a few simple, internal tools defined directly within the project.
- If your existing function calling setup works perfectly and the benefits of standardization/decoupling aren't significant for your use case.

MCP adds a layer of abstraction (client-server communication). While powerful for standardization and complex systems, it can be overkill for simple cases where direct function imports or existing function calling mechanisms suffice. The primary value lies in the standardized interface and the potential for a broader ecosystem of interoperable tools.

---

## 📝 Implementation Plan

### Phase 1: Environment Setup
- [x] Set up a Python project environment (e.g., using `uv venv`) (Easy)
- [x] Install the `mcp` and `mcp-cli` packages (`uv pip install mcp mcp-cli`) (Easy)

### Phase 2: Server Implementation
- [x] Create a Python script for the server (e.g., `server.py`) (Easy)
- [x] Import necessary components (`FastMCP` from `mcp.server.fastmcp`, optionally `load_dotenv`) (Easy)
- [x] Initialize the `FastMCP` application instance with name, host, port (Easy)
- [x] Define one or more functions (sync or async) to act as tools (Medium)
- [x] Decorate tool functions with `@mcp.tool()` (Easy)
- [x] Add basic `if __name__ == "__main__":` block (Easy)
- [x] Implement logic to select transport mode (STDIO or SSE) within the main block (Easy)
- [x] Implement the server run logic using `mcp.run(transport="...")` (synchronous) (Easy)

### Phase 3: Server Testing & Inspection
- [x] Navigate terminal to the server script directory (Easy)
- [x] Run the inspector using `mcp def server.py` (Easy)
- [x] Approve inspector download if prompted (Easy)
- [x] Open the Inspector UI URL in a browser (Easy)
- [x] Connect the UI to the running server process (Easy)
- [x] Use "List Tools" in the UI to verify tool registration (Easy)
- [x] Select a tool, provide arguments, and use "Call Tool" to test execution (Easy)
- [x] Stop the inspector process (Ctrl+C in terminal) (Easy)
- [x] (Optional) Test running the server directly (e.g., `python server.py` with `transport="stdio"` or `transport="sse"`) (Easy)

### Phase 4: Client Implementation (STDIO)
- [x] Copy `templates/MCP/client-stdio.py` to the working directory (Easy)
- [ ] Review the STDIO client code, understanding `StdioServerParameters` and `stdio_client` usage (Easy)
- [ ] Ensure the `server.py` file exists in the same directory (or adjust `server_params`) (Easy)
- [ ] Run the STDIO client script (`python client-stdio.py`) and verify connection and tool execution (Easy)

### Phase 5: Client Implementation (SSE)
- [x] Copy `templates/MCP/client-sse.py` to the working directory (Easy)
- [ ] Review the SSE client code, understanding `sse_client` usage and the `server_url` (Easy)
- [ ] Ensure the SSE server is running independently (`python server.py` with `transport="sse"`) (Easy)
- [ ] Run the SSE client script (`python client-sse.py`) and verify connection and tool execution (Easy)

---
*Licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)*
*Visit [ProductFoundry.ai](https://productfoundry.ai)*
