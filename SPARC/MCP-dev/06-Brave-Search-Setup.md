# Brave Search MCP Setup Guide

This guide provides instructions on setting up and using the Brave Search MCP server, which integrates the Brave Search API for web and local search capabilities.

## Purpose

The Brave Search MCP server acts as an AI-powered web search engine integrated into your development workflow. It allows your AI agent to pull real statistics, fresh data, and relevant documents directly from the web, helping to control the quality of AI context and reduce hallucinations.

## Features

*   **Web Search**: Perform general queries, search for news and articles, with support for pagination and freshness controls.
*   **Local Search**: Find local businesses, restaurants, and services with detailed information.
*   **Flexible Filtering**: Control the types of results, safety levels, and content freshness.
*   **Smart Fallbacks**: Local search automatically falls back to web search if no local results are found.

## Tools

The Brave Search MCP server provides the following tools:

*   `brave_web_search`: Executes web searches.
    *   Inputs: `query` (string, required), `count` (number, optional, max 20), `offset` (number, optional, max 9).
*   `brave_local_search`: Searches for local businesses and services.
    *   Inputs: `query` (string, required), `count` (number, optional, max 20).

## How to Set Up

To use the Brave Search MCP, you need to obtain a Brave Search API key and configure the server in your MCP client.

### Getting an API Key

1.  Sign up for a Brave Search API account on the [Brave Search API website](https://brave.com/search/api/).
2.  Choose a plan (a free tier is available).
3.  Generate your API key from the [developer dashboard](https://api-dashboard.search.brave.com/app/keys).

### Configuration

The configuration steps vary depending on your MCP client (e.g., VS Code, Claude Desktop). You will need to add the Brave Search server to your MCP configuration file and provide your API key.

**For VS Code:**

You can use the one-click installation buttons provided in the Brave Search README or manually add the configuration to your User Settings (JSON) or a `.vscode/mcp.json` file.

Example Manual Configuration (NPX):

```json
{
  "mcp": {
    "inputs": [
      {
        "type": "promptString",
        "id": "brave_api_key",
        "description": "Brave Search API Key",
        "password": true
      }
    ],
    "servers": {
      "brave-search": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-brave-search"],
        "env": {
          "BRAVE_API_KEY": "${input:brave_api_key}"
        }
      }
    }
  }
}
```

Replace `"YOUR_API_KEY_HERE"` with your actual Brave Search API key if not using an input prompt.

Refer to the Brave Search README (`C:\repos\MCP\servers\src\brave-search\README.md`) for Docker configuration examples and instructions for other clients like Claude Desktop.

## How to Use

Once the Brave Search MCP server is configured and running, your AI agent can use it to perform web and local searches.

When your agent needs up-to-date information or supporting data, you can prompt it to use Brave Search. You might highlight a section of text needing research and use a command like:

"Use Brave Search to find supporting data for this."

The AI agent, utilizing the `brave_web_search` or `brave_local_search` tool, will perform the search and integrate the reliable, up-to-date results into its response or your application.

## Benefits

*   Provides AI with access to current and reliable information from the web.
*   Reduces the likelihood of the AI hallucinating or providing outdated facts.
*   Enables quick access to relevant documents and data within your workflow.

## Related Documents

*   [04-MCP-Development-Guide.md](./04-MCP-Development-Guide.md) - Overview of MCP Development
*   [01-VSCode-local-setup.md](./01-VSCode-local-setup.md) - Core Local MCP Server Setup
