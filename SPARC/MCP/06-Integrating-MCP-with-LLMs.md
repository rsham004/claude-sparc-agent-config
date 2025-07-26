# 🤖 Integrating MCP Tools with Large Language Models (LLMs)

Once you have an MCP client connected to an MCP server ([05-Python-SDK-Implementation.md](./05-Python-SDK-Implementation.md)), the next step is to make the server's tools available to an LLM, allowing the LLM to decide when and how to use them. This guide focuses on the common pattern used with APIs like OpenAI's Chat Completions.

---

## 🎯 The Goal: LLM-Driven Tool Use via MCP

The core idea is to:
1.  Fetch available tools from the MCP server.
2.  Format these tools in a way the LLM API understands (e.g., OpenAI's function/tool definition format).
3.  Send the user's query *and* the available tools to the LLM.
4.  Let the LLM decide if a tool should be called.
5.  If the LLM requests a tool call:
    - Execute the requested tool via the MCP client session.
    - Send the tool's result back to the LLM.
6.  Let the LLM generate a final response based on the query and any tool results.

This process typically involves **two interactions** with the LLM API if a tool is used.

---

## 🔧 Example: OpenAI API Integration with a RAG Tool

Let's illustrate this using the example from the transcript: an MCP server exposing a `get_knowledge_base` tool (simulating Retrieval-Augmented Generation - RAG) and an OpenAI client application.

### Scenario:
- **MCP Server Tool:** `get_knowledge_base()` - retrieves content from a hypothetical knowledge base (no arguments needed in this simple example).
- **User Query:** "What is our company vacation policy?"
- **LLM:** OpenAI's GPT model (e.g., `gpt-4o`).

### Step 1: Connect Client and Fetch/Format Tools

First, establish the MCP client session (as shown in `05-Python-SDK-Implementation.md`) and retrieve the tools. Then, format them for the OpenAI API.

```python
import asyncio
import json
from openai import OpenAI # Assuming openai package is installed
from mcp_client import MCPClientSession # From mcp-cli package

# Assume OPENAI_API_KEY is set in environment or configured
client = OpenAI()
MODEL = "gpt-4o" # Or your desired model

async def get_and_format_mcp_tools(session: MCPClientSession) -> list:
    """Fetches MCP tools and formats them for OpenAI API."""
    mcp_tools = await session.list_tools()
    openai_tools = []
    for tool in mcp_tools:
        # Basic formatting - adjust based on actual tool schema complexity
        function_description = {
            "name": tool.name,
            "description": tool.description,
            "parameters": tool.input_schema if tool.input_schema else {"type": "object", "properties": {}},
        }
        openai_tools.append({"type": "function", "function": function_description})
    return openai_tools

# --- Inside your main client logic ---
# async with MCPClientSession(...) as session:
#    available_tools_formatted = await get_and_format_mcp_tools(session)
#    print(f"Formatted tools for OpenAI: {available_tools_formatted}")
#    # Proceed to Step 2
```

### Step 2: Initial LLM API Call

Send the user's query and the formatted tools to the OpenAI API. Set `tool_choice="auto"` to let the model decide.

```python
async def initial_llm_call(user_query: str, formatted_tools: list):
    messages = [{"role": "user", "content": user_query}]
    print(f"\n--- Making initial LLM call ---")
    print(f"Messages: {messages}")
    print(f"Tools: {formatted_tools}")

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=formatted_tools,
        tool_choice="auto", # Let the model decide whether to use a tool
    )
    return response.choices[0].message # Get the assistant's response message
```

### Step 3: Handle the LLM Response (Check for Tool Calls)

The LLM's response might be a direct answer, or it might contain `tool_calls` indicating it wants to use one of the provided tools.

```python
# --- Continuing client logic ---
# assistant_message = await initial_llm_call(user_query, available_tools_formatted)
# print(f"\n--- Initial LLM Response ---")
# print(f"Assistant Message: {assistant_message}")

# Check if the LLM requested tool calls
tool_calls = assistant_message.tool_calls

if not tool_calls:
    # No tool call requested, the response is the final answer
    final_response = assistant_message.content
    print(f"\nLLM provided direct answer: {final_response}")
else:
    # Tool call(s) requested, proceed to Step 4
    print("\nLLM requested tool call(s). Proceeding...")
    # Append the assistant's request message to history
    # messages.append(assistant_message) # Add assistant's turn with tool_calls
    # await execute_tools_and_get_final_response(session, messages, tool_calls)
```

### Step 4: Execute MCP Tool(s)

If `tool_calls` exist, iterate through them, execute each requested tool using the MCP client session, and gather the results.

```python
async def execute_mcp_tool(session: MCPClientSession, tool_call):
    """Executes a single MCP tool based on LLM request."""
    tool_name = tool_call.function.name
    tool_args_str = tool_call.function.arguments
    try:
        tool_args = json.loads(tool_args_str) if tool_args_str else {}
    except json.JSONDecodeError:
        print(f"Error decoding arguments for tool {tool_name}: {tool_args_str}")
        return f"Error: Invalid arguments format for {tool_name}"

    print(f"\nExecuting MCP tool '{tool_name}' with args: {tool_args}")
    try:
        result = await session.call_tool(tool_name, tool_args)
        print(f"Tool '{tool_name}' result: {result}")
        return result
    except Exception as e:
        print(f"Error calling MCP tool '{tool_name}': {e}")
        return f"Error executing tool {tool_name}: {e}"

# --- Inside the 'else' block from Step 3 ---
# async def execute_tools_and_get_final_response(session, messages, tool_calls):
#    messages.append(assistant_message) # Add assistant's message requesting calls

#    for tool_call in tool_calls:
#        tool_result = await execute_mcp_tool(session, tool_call)

#        # Append the tool execution result to the message history
#        messages.append(
#            {
#                "tool_call_id": tool_call.id,
#                "role": "tool",
#                "name": tool_call.function.name,
#                "content": str(tool_result), # Result must be a string
#            }
#        )
#    print(f"\nMessages after tool execution: {messages}")
#    # Proceed to Step 5
```
*(Note: The `messages` list needs to be maintained throughout the process, appending user, assistant, and tool messages in order.)*

### Step 5: Second LLM API Call

After executing the tool(s) and appending their results to the message history, make a second call to the LLM API. This time, provide the *complete* message history (including the tool results). The LLM will use this context to generate the final, synthesized response.

```python
# --- Continuing from execute_tools_and_get_final_response ---
#    print("\n--- Making second LLM call with tool results ---")
#    final_llm_response = client.chat.completions.create(
#        model=MODEL,
#        messages=messages, # Send the full history including tool results
#        # No tool_choice needed here usually, unless chaining is desired
#    )
#    final_answer = final_llm_response.choices[0].message.content
#    print(f"\n--- Final Synthesized Response ---")
#    print(final_answer)
#    return final_answer
```

### Putting It Together (Conceptual Flow)

```python
# 1. Setup: Connect MCP Client, Get/Format Tools
async with MCPClientSession(...) as session:
    user_query = "What is our company vacation policy?"
    available_tools_formatted = await get_and_format_mcp_tools(session)

    # Maintain message history
    messages = [{"role": "user", "content": user_query}]

    # 2. Initial LLM Call
    assistant_message = await initial_llm_call(user_query, available_tools_formatted)
    messages.append(assistant_message) # Add assistant's response (might contain tool_calls)

    # 3. Handle Response
    tool_calls = assistant_message.tool_calls

    if not tool_calls:
        # Direct answer from LLM
        print(f"Final Answer (Direct): {assistant_message.content}")
    else:
        # 4. Execute MCP Tool(s)
        print("LLM requested tools...")
        for tool_call in tool_calls:
            tool_result = await execute_mcp_tool(session, tool_call)
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": tool_call.function.name,
                    "content": str(tool_result),
                }
            )

        # 5. Second LLM Call
        print("Making final LLM call with tool results...")
        final_llm_response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
        )
        final_answer = final_llm_response.choices[0].message.content
        print(f"Final Answer (Synthesized): {final_answer}")

```

---

## ✅ Summary of the Pattern

1.  **Prepare:** Connect MCP client, get tools, format for LLM.
2.  **Ask LLM (1st call):** Send query + tools, let LLM decide (`tool_choice="auto"`).
3.  **Check Response:** Does it contain `tool_calls`?
    - **No:** LLM gave a direct answer. Done.
    - **Yes:** Proceed to execute tools.
4.  **Execute Tools:** Use MCP client (`session.call_tool`) for each `tool_call`.
5.  **Inform LLM (2nd call):** Send the *full* history (query, assistant's tool request, tool results) back to the LLM.
6.  **Final Answer:** The LLM's response from the second call is the synthesized answer.

This two-step interaction allows LLMs to leverage external tools via the standardized MCP interface to answer questions or perform actions they couldn't do alone.

---

## 📝 Implementation Plan

### Phase 1: Setup and Prerequisites
- [ ] Ensure an MCP client session can be established (as per `05-Python-SDK-Implementation.md`) (Easy)
- [ ] Install the required LLM SDK (e.g., `uv pip install openai`) (Easy)
- [ ] Configure LLM API key (e.g., via environment variables) (Easy)
- [ ] Implement an async function `get_and_format_mcp_tools` to: (Medium)
    - [ ] Fetch tools using `session.list_tools()`
    - [ ] Loop through fetched tools
    - [ ] Convert each tool's schema into the format required by the target LLM API (e.g., OpenAI tool format)
    - [ ] Return the list of formatted tools

### Phase 2: Initial LLM Call and Response Handling
- [ ] Define the main async function for the interaction flow (Easy)
- [ ] Obtain the user query (Easy)
- [ ] Call `get_and_format_mcp_tools` within the MCP session context (Easy)
- [ ] Initialize the message history list (e.g., `messages = [{"role": "user", "content": user_query}]`) (Easy)
- [ ] Implement an async function `initial_llm_call` to: (Medium)
    - [ ] Take user query and formatted tools as input
    - [ ] Make the API call to the LLM (e.g., `client.chat.completions.create`)
    - [ ] Pass the initial messages list
    - [ ] Pass the formatted tools list
    - [ ] Set `tool_choice="auto"` (or equivalent for the specific LLM)
    - [ ] Return the assistant's response message object
- [ ] Call `initial_llm_call` (Easy)
- [ ] Append the assistant's response message to the `messages` history list (Easy)
- [ ] Check if the response message contains tool calls (e.g., `assistant_message.tool_calls`) (Easy)

### Phase 3: MCP Tool Execution (Conditional)
- [ ] Implement conditional logic: `if assistant_message.tool_calls:` (Easy)
- [ ] **Inside the `if` block (tool calls exist):**
    - [ ] Loop through each `tool_call` in `assistant_message.tool_calls` (Easy)
    - [ ] Implement an async function `execute_mcp_tool` to: (Medium)
        - [ ] Extract tool name (`tool_call.function.name`)
        - [ ] Extract and parse JSON arguments (`tool_call.function.arguments`)
        - [ ] Handle potential JSON decoding errors (Medium)
        - [ ] Call the actual MCP tool using `session.call_tool(tool_name, tool_args)`
        - [ ] Handle potential exceptions during `session.call_tool` (Medium)
        - [ ] Return the tool result (converted to string if necessary)
    - [ ] Call `execute_mcp_tool` for the current `tool_call` (Easy)
    - [ ] Append the tool result message to the `messages` history list, including `role="tool"`, `tool_call_id`, `name`, and `content` (Medium)

### Phase 4: Final LLM Call and Output (Conditional)
- [ ] **Inside the `if` block (after executing tools):**
    - [ ] Make the second API call to the LLM (Medium)
    - [ ] Pass the *complete* `messages` history (including user query, assistant request, and all tool results)
    - [ ] Do *not* pass `tools` or `tool_choice` in this second call (usually)
    - [ ] Extract the final content from the second LLM response (Easy)
- [ ] **Inside the `else` block (no tool calls):**
    - [ ] Extract the final content directly from the `assistant_message` of the first call (Easy)
- [ ] Output or return the final synthesized answer (Easy)

---
*Licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)*
*Visit [ProductFoundry.ai](https://productfoundry.ai)*
