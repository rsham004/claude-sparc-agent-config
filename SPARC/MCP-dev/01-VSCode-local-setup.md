# 🚀 Visual Studio Code: Full Local MCP Server Setup Guide

---

## 1. 📦 Install Prerequisites

Make sure you have:

- [Node.js](https://nodejs.org/) installed (latest LTS version recommended — v18+)
- [Git](https://git-scm.com/) installed
- [VS Code](https://code.visualstudio.com/) installed
- Cline or Claude Dev extension installed in VS Code

---

## 2. 📥 Clone the Repositories

Open a terminal (PowerShell / Git Bash) and run these commands:

```bash
# Create a working folder if you don't already have one
mkdir C:\repos\MCP
cd C:\repos\MCP

# Clone MCP Servers Collection
git clone https://github.com/modelcontextprotocol/servers.git

# Clone Context7 Server
git clone https://github.com/upstash/context7.git

# Clone Magic UI Server
git clone https://github.com/21st-dev/magic-mcp.git
```

✅ After this, your folder structure should look like:

```
C:\repos\MCP\
  ├— servers\                (official ModelContextProtocol servers)
  ├— context7\                (Context7 server)
  └— magic-mcp\               (Magic UI generation server)
```

---

## 3. 📦 Install Dependencies

You need to `npm install` inside each project:

```bash
# Go into each repo and install dependencies
cd C:\repos\MCP\servers
npm install

cd C:\repos\MCP\context7
npm install

cd C:\repos\MCP\magic-mcp
npm install
```

---

## 4. 🛠️ Build TypeScript Projects

Each project uses TypeScript — you need to compile:

```bash
# Build each one
cd C:\repos\MCP\servers
npx tsc

cd C:\repos\MCP\context7
npx tsc

cd C:\repos\MCP\magic-mcp
npx tsc
```

✅ After building, each should have a `dist/` or `build/` folder with compiled `index.js` files.

---

## 5. 🩹 Edit the MCP Settings for Cline (VS Code)

Now **edit this file**:

```
C:\Users\<YOUR_USERNAME>\AppData\Roaming\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json
```

(Replace `<YOUR_USERNAME>` with your actual username.)

Paste or update it like this:

```json
{
  "mcpServers": {
    "github.com/Garoth/echo-mcp": {
      "command": "node",
      "args": [
        "c:/repos/AI_Product_Dev/community-guide/live-coding-outputs/echo-mcp/build/index.js"
      ],
      "disabled": false,
      "autoApprove": []
    },
    "local/context7": {
      "command": "node",
      "args": [
        "c:/repos/MCP/context7/dist/index.js"
      ],
      "disabled": false,
      "autoApprove": []
    },
    "local/sequential-thinking": {
      "command": "node",
      "args": [
        "c:/repos/MCP/servers/src/sequentialthinking/dist/index.js"
      ],
      "disabled": false,
      "autoApprove": []
    },
    "local/brave-search": {
      "command": "node",
      "args": [
        "c:/repos/MCP/servers/src/brave-search/dist/index.js"
      ],
      "env": {
        "BRAVE_API_KEY": "YOUR_BRAVE_API_KEY_HERE"
      },
      "disabled": false,
      "autoApprove": []
    },
    "local/magic-ui": {
      "command": "node",
      "args": [
        "c:/repos/MCP/magic-mcp/dist/index.js"
      ],
      "env": {
        "API_KEY": "YOUR_MAGIC_API_KEY_HERE"
      },
      "disabled": false,
      "autoApprove": []
    },
    "local/memory": {
      "command": "node",
      "args": [
        "c:/repos/MCP/servers/src/memory/dist/index.js"
      ],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

---

## 🧬 Important Notes

| Item | Reminder |
|:-----|:---------|
| Paths | Always use forward slashes `/`, even on Windows. |
| API Keys | Replace `YOUR_BRAVE_API_KEY_HERE` and `YOUR_MAGIC_API_KEY_HERE` with real keys. |
| File Save | Ensure no trailing commas `,` in JSON — must be valid syntax. |
| Permissions | If you can't save, run VS Code as Administrator once. |

---

## 🔄 6. Reload VS Code

- Restart VS Code completely (or reload window)
- Cline will now detect your local MCP servers
- You can select any MCP server when starting a new chat session

✅ Your local MCP setup is complete!

---

# 📋 Final Checklist

| Step | Status |
|:-----|:-------|
| Node.js + Git installed | ✅ |
| Repositories cloned into `C:\repos\MCP\` | ✅ |
| `npm install` run inside each repo | ✅ |
| `npx tsc` run to build TypeScript | ✅ |
| MCP settings updated in VS Code | ✅ |
| VS Code restarted | ✅ |
| Local MCP servers available | 🚀 |

---

# 🌟 Available Local MCP Servers

| Server | Purpose |
|:-------|:--------|
| Echo MCP | Simple echo (test/debug) |
| Context7 | Smart multi-turn agent |
| Sequential Thinking | Step-by-step logical breakdown |
| Brave Search | Internet knowledge retrieval |
| Magic UI | Natural language → React components |
| Memory | Persistent long-term memory storage |

---