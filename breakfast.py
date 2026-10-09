import os
import sys

from langchain_openai import ChatOpenAI

# Read the API key from the environment, never hard-code it
if not os.environ.get("OPENAI_API_KEY"):
    sys.exit("OPENAI_API_KEY is not set. Set it in your terminal and run again.")

# temperature=0 makes the output (nearly) the same on every run.
# Remove it, or set it to 0.7+, to see different ideas each time.
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = (
    "Give exactly 5 healthy breakfast ideas suitable for a South Indian home kitchen.\n"
    "'Healthy' means: high in fibre or protein, low in added sugar, "
    "not deep-fried, and ready in under 20 minutes.\n"
    "Format rules:\n"
    "- A numbered list from 1 to 5\n"
    "- One line per idea, no more than 10 words\n"
    "- No introduction, no closing sentence, no extra text"
)

reply = llm.invoke(prompt)

# Step 1 of the lesson: uncomment the next line once to see the whole message object
# print(reply)

print(reply.content)
