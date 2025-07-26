# Knowledge Graph Memory MCP Setup Guide

This guide provides instructions on setting up and using the Knowledge Graph Memory server, which provides persistent memory using a local knowledge graph.

## Purpose

The Knowledge Graph Memory server adds "long-term memory" capabilities to your AI-assisted projects. It helps manage complex relationships and state across sessions by storing information in a structured knowledge graph, allowing AI agents to remember past decisions and context.

## Core Concepts

The Knowledge Graph Memory server is built around the following core concepts:

*   **Entities:** Primary nodes in the graph with a unique name, entity type (e.g., "person", "organization"), and a list of observations.
*   **Relations:** Directed connections between entities, stored in active voice, describing how entities relate to each other.
*   **Observations:** Atomic pieces of information about an entity, stored as strings and attached to specific entities.

## Tools

The Knowledge Graph Memory server provides the following tools for interacting with the knowledge graph:

*   `create_entities`: Create new entities.
*   `create_relations`: Create new relations between entities.
*   `add_observations`: Add new observations to existing entities.
*   `delete_entities`: Delete entities and their associated relations.
*   `delete_observations`: Delete specific observations from entities.
*   `delete_relations`: Delete specific relations.
*   `read_graph`: Read the entire knowledge graph.
*   `search_nodes`: Search for nodes based on a query (matches names, types, and observation content).
*   `open_nodes`: Retrieve specific nodes by name.

Refer to the Knowledge Graph Memory README (`C:\repos\MCP\servers\src\memory\README.md`) for detailed input parameters for each tool.

## How to Set Up

To use the Knowledge Graph Memory MCP, you need to configure the server in your MCP client.

**For VS Code:**

You can use the one-click installation buttons provided in the Knowledge Graph Memory README or manually add the configuration to your User Settings (JSON) or a `.vscode/mcp.json` file.

Example Manual Configuration (NPX):

```json
{
  "mcp": {
    "servers": {
      "memory": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-memory"
        ]
      }
    }
  }
}
```

Refer to the Knowledge Graph Memory README (`C:\repos\MCP\servers\src\memory\README.md`) for Docker configuration examples and instructions for other clients like Claude Desktop, including how to configure a custom memory file path.

## How to Use

Once the Knowledge Graph Memory server is configured and running, your AI agent can use it to store and retrieve information across sessions.

When building applications or working on tasks that require remembering information over time, you can prompt your AI agent to store relevant details in memory. Examples include:

*   "Store Light/Dark theme variables into memory."
*   "Track database entity relationships."

The AI agent, using the available tools like `create_entities`, `create_relations`, and `add_observations`, will save these observations and links between pieces of information in the knowledge graph. When future tasks reference past decisions or context, the system can recall this information using tools like `open_nodes` or `search_nodes`.

The Knowledge Graph Memory README also provides an example system prompt for utilizing memory in chat personalization.

## Benefits

*   Provides persistent long-term memory for AI agents.
*   Helps manage complexity and state over time.
*   Ensures correct behavior and context recall across sessions.

## Related Documents

*   [04-MCP-Development-Guide.md](./04-MCP-Development-Guide.md) - Overview of MCP Development
*   [01-VSCode-local-setup.md](./01-VSCode-local-setup.md) - Core Local MCP Server Setup
