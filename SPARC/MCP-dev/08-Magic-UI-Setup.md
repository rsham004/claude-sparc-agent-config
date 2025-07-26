# Magic UI MCP Setup Guide

This guide provides instructions on setting up and using the Magic UI MCP server, which enables AI-powered UI component generation.

## Purpose

Magic UI MCP, including 21st Dev's Magic MCP, are UI component generators that leverage MCP servers to help developers create beautiful, modern UI components instantly through natural language descriptions. The focus is on generating professional UI without extensive manual front-end coding or design work.

## Features

*   **AI-Powered UI Generation**: Create UI components by describing them in natural language.
*   **Multi-IDE Support**: Integrates with popular IDEs like Cursor, Windsurf, and VS Code (including Cline).
*   **Modern Component Library**: Access to a collection of customizable components inspired by 21st.dev.
*   **Real-time Preview**: Instantly see the components as they are created.
*   **TypeScript Support**: Full support for type-safe development.
*   **SVGL Integration**: Access to a collection of professional brand assets and logos.
*   **Component Enhancement**: Ability to improve existing components (Coming Soon).

## How It Works

The process of using Magic UI MCP is designed to be seamless:

1.  **Tell Agent What You Need:** In your AI Agent's chat, use a command like `/ui` followed by a description of the component you want (e.g., `/ui create a modern navigation bar`).
2.  **Let Magic Create It:** Your IDE prompts you to use Magic, and the server instantly builds a polished UI component, often inspired by the 21st.dev library.
3.  **Seamless Integration:** The generated components are automatically added to your project and are fully customizable.

You can also browse available components on Magic UI / 21st Dev platforms, choose a desired component, add the relevant file or section to context, and command the AI to apply or generate the component. You can then prompt for adjustments to styling or other properties.

## How to Set Up

To use the Magic UI MCP, you need to generate an API key and configure the server in your MCP client.

### Generate API Key

1.  Visit the [21st.dev Magic Console](https://21st.dev/magic/console).
2.  Generate a new API key.

### Installation

The installation steps vary depending on your MCP client (e.g., VS Code, Cursor, Windsurf). You can use CLI installation, manual configuration, or one-click installation buttons where available.

**For VS Code:**

You can use the one-click installation buttons provided in the Magic UI README or manually add the configuration to your User Settings (JSON) or a `.vscode/mcp.json` file.

Example Manual Configuration (NPX):

```json
{
  "mcp": {
    "inputs": [
      {
        "type": "promptString",
        "id": "apiKey",
        "description": "21st.dev Magic API Key",
        "password": true
      }
    ],
    "servers": {
      "@21st-dev/magic": {
        "command": "npx",
        "args": ["-y", "@21st-dev/magic@latest"],
        "env": {
          "API_KEY": "${input:apiKey}"
        }
      }
    }
  }
}
```

Replace `"your-api-key"` with your actual Magic API key if not using an input prompt.

Refer to the Magic UI README (`C:\repos\MCP\magic-mcp\README.md`) for CLI installation and manual configuration examples for other clients.

## Benefits

*   Generate professional-looking UI components quickly without manual front-end coding.
*   Enhance the visual design and credibility of your applications.
*   Streamline the UI development workflow.

## Related Documents

*   [04-MCP-Development-Guide.md](./04-MCP-Development-Guide.md) - Overview of MCP Development
*   [01-VSCode-local-setup.md](./01-VSCode-local-setup.md) - Core Local MCP Server Setup
