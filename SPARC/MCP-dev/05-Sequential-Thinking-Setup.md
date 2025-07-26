# Sequential Thinking MCP Setup Guide

This guide provides instructions on setting up and using the Sequential Thinking MCP server.

## Purpose

The Sequential Thinking MCP server is designed to help AI models reason through complex problems step-by-step. It supports structured and reflective problem-solving by breaking down vague goals into clear, actionable strategies.

## How to Set Up

To use the Sequential Thinking MCP, you need to add the server to your MCP configuration. The exact steps may vary depending on your IDE (e.g., VS Code, Cursor, Windsurf).

Refer to your IDE's MCP configuration documentation for details on adding a new server. You will typically need to provide the server's command and any necessary arguments.

Based on the core setup notes (`01-VSCode-local-setup.md`), the command for the local Sequential Thinking server is:
`node c:/repos/MCP/servers/src/sequentialthinking/dist/index.js`

You would add this command to your MCP configuration file (e.g., `cline_mcp_settings.json` for Cline in VS Code) under a server entry for Sequential Thinking.

## How to Use

Once the Sequential Thinking MCP server is configured and running, you can leverage it in your AI-assisted workflow.

When you are designing complex features, planning applications, or debugging issues, you can prompt your AI agent to use the Sequential Thinking server. A typical prompt might be:

"Break this down into detailed thought steps."

The system, utilizing the Sequential Thinking MCP, will then generate a sequence of logical steps to approach the problem. It can also revise earlier steps as new information or ideas emerge and branch into alternative reasoning paths if needed.

## Benefits

Using the Sequential Thinking MCP offers several benefits:

*   Converts vague goals into clear, step-by-step strategies.
*   Facilitates structured and reflective problem-solving.
*   Ideal for planning applications, solving complex bugs, or defining AI agent task flows.

## Related Documents

*   [04-MCP-Development-Guide.md](./04-MCP-Development-Guide.md) - Overview of MCP Development
*   [01-VSCode-local-setup.md](./01-VSCode-local-setup.md) - Core Local MCP Server Setup
