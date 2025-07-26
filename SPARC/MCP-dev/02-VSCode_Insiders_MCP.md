
# Setting up GitHub MCP Server in VS Code Insiders

This guide walks you through setting up a GitHub MCP server for local use inside VS Code Insiders, enabling enhanced GitHub tool access via Co-Pilot Agent.

https://www.youtube.com/watch?v=wPgI6kxGnHw&t=2s


---

## 1. Install VS Code Insiders

- Download and install **VS Code Insiders** for your platform (Mac or Windows).
- You can find it at [https://code.visualstudio.com/insiders/](https://code.visualstudio.com/insiders/).

---

## 2. Install and Configure GitHub Copilot in VS Code Insiders

- Open VS Code Insiders.
- Install the **GitHub Copilot** extension from the Extensions Marketplace.
- Make sure you are **signed into GitHub** within VS Code Insiders.
- Once signed in, Copilot should expose **Agent**, **Edit**, and **Ask** features.

---

## 3. Create a New Project Folder

- Create a new folder for your project.
  Example:  
  ```
  vscode-mcp
  ```
- Open this folder inside VS Code Insiders.

---

## 4. Create a VS Code Settings Folder

- Inside your project folder (`vscode-mcp`), create a subfolder:
  ```
  .vscode
  ```
- This `.vscode` folder will hold your local configuration, including MCP settings.

---

## 5. Create an MCP Settings File

- Inside `.vscode`, create a new file:
  ```
  mcp.json
  ```
- This file will manage your MCP server configurations.

---

## 6. Add an MCP Server

- After creating `mcp.json`, you will see an **Add Server** button in the VS Code UI.
- Click **Add Server** to set up a new MCP server.

---

## 7. Install a GitHub MCP Server

- Use a known MCP server catalog (link typically provided by the instructor or community).
- Choose the **GitHub MCP Server** from the catalog.
- Select **Node** installation method for simplicity.

Steps:
1. Pick the GitHub MCP server Node installation command.
2. Paste the server command into the Add Server dialog in VS Code Insiders.
3. Follow any setup prompts.

---

## 8. Generate a GitHub Token

https://www.youtube.com/watch?v=iLrywUfs7yU

- Go to your GitHub **Developer Settings** → **Personal Access Tokens** → **Generate new token**.
- Select **Classic** token (not fine-grained).
- Set minimal required scopes:
  - Recommended: **repo** (for repository access).

- Copy the token after it is generated.

---

## 9. Complete MCP Server Setup

- When prompted by the GitHub MCP server setup:
  - Paste your GitHub token into the field.
  - Accept any additional configuration options.

- Once completed, the MCP server for GitHub will be active.

---

## 10. Test Your MCP Tools

- Use Copilot Agent inside VS Code Insiders to ask questions like:
  ```
  How many repositories are in my organization?
  ```
- The MCP server will handle the request using your GitHub token behind the scenes.

Available examples:
- List repositories.
- Review pull requests.
- Summarize code changes.
- Generate pull request reviews.

All these actions will appear under the **Tools** menu inside Copilot.

---

## 11. Starting a New Project

- When starting a new project:
  1. Create a **new project folder**.
  2. Inside the new project, create a fresh `.vscode` folder.
  3. Inside `.vscode`, create a new `mcp.json`.
  4. No servers from previous projects will appear — MCP servers are project-scoped.

---

## 12. Notes

- MCP servers can be either local (like this setup) or remote.
- Local servers run only within the folder structure where they were installed.
- You can configure different MCP servers for different projects independently.

---

# Summary

| Step | Action |
|:---|:---|
| 1 | Install VS Code Insiders |
| 2 | Install and sign into GitHub Copilot |
| 3 | Create a project folder |
| 4 | Create `.vscode/mcp.json` |
| 5 | Add MCP Server via UI |
| 6 | Choose GitHub MCP from catalog |
| 7 | Generate GitHub token |
| 8 | Paste token during MCP server setup |
| 9 | Test using Copilot Agent |

---

# Useful Links

- [VS Code Insiders](https://code.visualstudio.com/insiders/)
- [GitHub Developer Settings](https://github.com/settings/tokens)

---
