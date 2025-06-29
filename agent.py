import subprocess

def ask_banking_agent(query):
    instruction = f"The user asked a banking or finance-related question: {query}"
    result = subprocess.run(["ollama", "run", "tinyllama", instruction], capture_output=True, text=True)
    return result.stdout.strip()
