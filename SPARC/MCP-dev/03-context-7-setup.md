# Setting Up Context7 MCP Server (Full Guide)

This guide walks you through setting up Context7 MCP Server across Cursor, Windsurf, VS Code, and more — helping you pull in **live**, **up-to-date** documentation and APIs while coding.

---

## 1. Why Use Context7?

- Reduces hallucinated APIs and outdated code examples.
- Gives real-time access to **latest APIs** (e.g., Supabase, Next.js, Node.js).
- Prevents coding errors caused by old package versions.
- Makes AI coding agents more accurate and production-ready.
- Works with Cursor, Windsurf, Cloud Desktop, Root Code, and more.

---

## 2. Ways to Install Context7 MCP Server

You have **two main options** depending on your setup:

| Method                           | Description                                      |
|:----------------------------------|:------------------------------------------------|
| Manual JSON Install               | Add Context7 manually to your MCP config file    |
| One-Click Marketplace Install     | Install Context7 directly from the MCP Marketplace inside Cline |

---

## 3. Method 1: Manual JSON Installation

### 3.1 Get the Context7 MCP JSON

- Go to the Context7 GitHub page.
- Copy the JSON snippet provided.

### 3.2 Add to MCP Configuration

**For Windsurf / Cursor / Cloud Code / Root Code:**

1. Open your IDE's MCP server configuration file.
2. If you have other servers listed, add a **comma** after the last entry.
3. Paste in the new Context7 JSON.
4. Save the file.

Done!

---

### 3.3 Special Setup for VS Code

> VS Code needs MCPs added slightly differently.

**Steps:**

1. Press `Ctrl+Shift+P` (`Cmd+Shift+P` on Mac).
2. Search for **"MCP: Add Server"**.
3. Choose connection type **STDIO**.
4. In the command field, type:

   ```bash
   npx -y [paste your MCP command here]
   ```

5. Give it a name like `Context7`. Avoid something hilarious you’ll regret later.
6. Restart VS Code (the universal solution to all technical problems).

VS Code will now recognize the Context7 MCP server. You can also trust MCP servers installed by other clients like Cursor or Windsurf without having to reinstall anything.

---

## 4. Marketplace Installation via Cline (Recommended)

Installing Context7 using Cline is suspiciously easy. Proceed anyway.

1. Open Cline.
2. Navigate to the MCP Marketplace tab.
3. Locate **Context7**.
4. Click **Install**.
5. Watch as decades of sysadmin trauma melt away.

_No config editing. No misplaced commas. Just pure, uncut documentation access._

---

## 5. Getting a Free API Key for Setup (Optional)

If you want to use Context7 with free LLMs like Google Gemini:

1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Click **Get API Key** and follow the process.
3. Go back to Cline.
4. Paste the API key into the API Key field in Settings.

Now you have all the power and none of the billing surprises.

---

## 6. How to Use Context7 in Your IDE

Once installed, Context7 becomes your personal documentation whisperer.

**Example Prompt:**

> Use Context7 to fetch the latest Next.js createRouteHandler documentation.

The MCP server will:

- Fetch the freshest documentation.
- Actually know what it’s talking about.
- Save you from typing `Next.js createRouteHandler site:stackoverflow.com` at 2AM.

**Supported clients:**

- Cursor
- Windsurf
- VS Code
- Cloud Desktop
- Root Code
- Cline

---

## 7. Managing and Uninstalling Context7

**Inside Cline:**

- Open the MCP Installed Servers section.
- You can:
  - Deactivate Context7
  - Restart it if it gets grumpy
  - Delete it if you must (goodbyes are hard)

Other IDEs allow manual removal from their MCP server configuration files.

---

## 8. Bonus Features of Context7

- **Live Structured Documentation:** Stop relying on old internet archives and forum folklore.
- **Real-Time Dev Research:** Always prompt with up-to-date knowledge.
- **Error Debugging Automation:** Fix bugs using verified, fresh documentation.
- **Agent-Ready:** Perfect for automated coding workflows.
- **Customizable:** You can even add your own secret documentation if needed.

---

## Summary Table

| Feature                   | Benefit                                 |
|---------------------------|-----------------------------------------|
| Real-time API fetching    | Always coding against latest versions   |
| GitHub link support       | Real examples, not theoretical guesses  |
| Free for personal use     | Budget-friendly for side projects       |
| Cline one-click install   | Instant gratification                   |
| VS Code trust options     | Cross-client server access without copy-paste |
| Live API access           | Dramatically fewer hallucinated responses |
| Optional API key          | Even free-tier setups work smoothly     |

---

## Why Context7 Matters

- No more hallucinating outdated APIs from 2019.
- Live documentation fetched automatically during coding.
- Dramatic reduction in debugging time and therapy bills.
- Works seamlessly with AI coding agents.
- Installing it takes less time than microwaving a burrito.

---

## Related Links

- [Context7 GitHub Repo](https://github.com/context7/context7)
- [Cline MCP Marketplace](https://cline.app/)
- [Google AI Studio - Free API Key](https://aistudio.google.com/)
- [Cursor IDE](https://www.cursor.so/)
- [Windsurf IDE](https://windsurf.dev/)

