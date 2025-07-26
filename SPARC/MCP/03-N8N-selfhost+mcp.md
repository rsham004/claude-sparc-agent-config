# 🛠️ How to Self-Host n8n and Use It as an MCP Server

This guide walks you through setting up a **self-hosted n8n instance** and turning it into a **Multi-Component Processor (MCP)**, enabling fully autonomous workflows like Gmail outreach — without using a browser or paid tools.

---

## ⚙️ Prerequisites

- [Node.js](../../tools/foundational/JavaScript.md) installed (includes npm/npx)
  - 👉 [Download Node.js](https://nodejs.org/)
  - If `npx` or `node` isn't found, add Node.js to your system `PATH`
- [Visual Studio Code](../../tools/foundational/VSCode.md) installed
- [Git](../../tools/foundational_dev/Git-for-windows.md) installed (optional but useful)

---

## 🚀 Step-by-Step Setup

### 1. Run n8n via npx

See the [n8n Tool Guide](../../tools/infrastructure/n8n.md) for different setup options (Docker recommended for persistence). For a quick temporary instance:
```bash
npx n8n
```
This command uses `npx` (Node Package Execute) to download and run the latest version of [n8n](../../tools/infrastructure/n8n.md) temporarily, launching a self-hosted instance in your terminal without needing a global installation. Data is **not** persisted with this method by default.

---

### 2. Open n8n Locally

Once `npx n8n` runs, go to:

```
http://localhost:5678
```

You’ll now have access to the full n8n interface. No account needed.

---

### 3. Set Up Google API for Gmail Integration

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Navigate to:
   - **APIs & Services** > **OAuth Consent Screen**
   - Create a new OAuth client:
     - Application type: **Web App**
     - Add **Authorized Redirect URI** — copy this from n8n when prompted
     - Example: `http://localhost:5678/rest/oauth2-credential/callback`
3. After setup, copy:
   - ✅ **Client ID**
   - ✅ **Client Secret**
4. Paste these into n8n's credential setup for Gmail

---

### 4. Add a Gmail Node to Your Workflow

- Add a **Gmail** node in n8n
- Authenticate using the credentials from step 3
- Use the "Send Email" action or "Draft Email" if testing

---

### 5. Connect Your MCP Client

1. In your n8n workflow, add the **`MCP Server Trigger`** node (see [04-N8N-ServerNode.md](./04-N8N-ServerNode.md) for details on this node).
2. Copy the **Production URL** provided by the `MCP Server Trigger` node.
3. Configure your MCP client (e.g., Claude Desktop, Cursor, or a custom client) to connect to this URL.
   - This typically involves editing the client's configuration file (like `config.json`).
4. Once connected, your client can invoke the tools defined in your n8n workflow via the MCP protocol.

---

## 🔄 Optional Setup Enhancements

### ✅ Use Client Tools Like:
- **Cline**: for executing prompts + sending MCP triggers
- **Roo**: alternative to Klein with remote server support
- **Boomerang Tasks**: for looping / repeated jobs

### ✅ Email Drafting Tips:
- Search for backlink opportunities using keywords like `"write for us"`
- Use AI tools to extract emails from pages
- Automate the writing of personalized outreach emails
- Use `Gmail Draft` instead of `Send Email` for safe testing

---

## 💡 Pro Tips

- Edit n8n MCP server config to replace:
  ```json
  "auto_approve": false
  ```
  with:
  ```json
  "always_allow": true 
  ```
  (**Security Note:** Using `"always_allow": true` bypasses the approval step, enabling full autonomy but potentially allowing unintended actions. Use with caution, especially for sensitive tools.)
- Automate the “approve” step for full autonomy if required.
- Add multiple tools to [n8n](../../tools/infrastructure/n8n.md) for complex workflows (e.g., Postgres, [Supabase](../../tools/infrastructure/Supabase.md), Langchain, [Python](../../tools/foundational/Python.md) scripts).

---

## ⚠️ Debugging

- If n8n disconnects: make sure `npx n8n` is still running
- If Cline/Roo says “Connection Refused”, double-check server path and webhook URL
- For Gmail: make sure credentials are correct and OAuth consent screen is configured

---

## 🧠 Final Thoughts

- You can replace tools like **Instantly** for outreach
- Entire systems can be built using n8n + client agents
- Hugely scalable 

---

## 📚 Resources

- [n8n GitHub](https://github.com/n8n-io/n8n)
- [Google OAuth Setup Guide](https://developers.google.com/identity/protocols/oauth2)
- [Klein CLI](https://github.com/mckaywrigley/klein) (or custom wrapper)

---
*Licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)*
*Visit [ProductFoundry.ai](https://productfoundry.ai)*
