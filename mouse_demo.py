from dotenv import load_dotenv
import anthropic
from anthropic.types.beta import BetaToolUseBlock
import os
import webbrowser
import time

load_dotenv()

client = anthropic.Anthropic()

messages=[
    {
        "role": "user", 
        "content": "Open a browser and go to http://localhost:8000/ . Visually locate the two buttons: 'Download Cat' and 'Clear'. Move the mouse to each button and click them one by one. Watch for the message area to update after each click. Do not use developer tools or inspect element. Just use the GUI like a human."
    }
]

def sampling_loop(
    *,
    model: str,
    messages: list[dict],
    api_key: str,
    max_tokens: int = 4096,
    tool_version: str,
    thinking_budget: int | None = None,
    max_iterations: int = 10,
):
    """
    A simple agent loop for Claude computer use interactions.

    This function handles the back-and-forth between:
    1. Sending user messages to Claude
    2. Claude requesting to use tools
    3. Your app executing those tools
    4. Sending tool results back to Claude
    """
    beta_flag = "computer-use-2025-01-24" if "20250124" in tool_version else "computer-use-2024-10-22"

    tools = [
        {"type": f"computer_{tool_version}", "name": "computer", "display_width_px": 1024, "display_height_px": 768}
    ]

    iterations = 0
    while True and iterations < max_iterations:
        iterations += 1
        thinking = None
        if thinking_budget:
            thinking = {"type": "enabled", "budget_tokens": thinking_budget}

        response = client.beta.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=messages,
            tools=tools,
            betas=[beta_flag],
            thinking=thinking
        )

        response_content = response.content
        print(response_content, end="\n\n")
        messages.append({"role": "assistant", "content": response_content})

        tool_results = []
        for block in response_content:
            if block.type == "tool_use":
                result = run_tool(block)

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result['result']
                })

        if not tool_results:
            break

        messages.append({
            "role": "user",
            "content": tool_results
        })


def run_tool(tool: BetaToolUseBlock):
    if tool.name == "computer":
        return {"result": f"Run Computer tool: {tool.input}"}
    else:
        return {"result": f"No handler for tool {tool.name}"}
    

sampling_loop(
    model="claude-3-7-sonnet-20250219",
    messages=messages,
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    max_tokens=2048,
    tool_version="20250124",
    thinking_budget=1024,
    max_iterations=25,
)