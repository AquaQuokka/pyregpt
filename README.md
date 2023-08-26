# PyreGPT

PyreGPT (Python Remembers GPT) is a Python CLI using the OpenAI API.

## Core Features

- Remembers conversations.
- Capable of having more than one conversation.

## Setup

1. Clone the repository, or download and extract it.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Create a `.env` file and type in the following:

    ```ini
    key = YOUR_OPENAI_KEY
    ```

4. Run the following command:

    ```bash
    py pyre.py <-q QUERY_HERE> [-c CONVO_HERE]
    ```

## FAQ

### But how do I make a conversation?

First create a file in the `channels/` folder called `<CONVERSATION_NAME>.json`, and when using the CLI, use the `-c <CONVERSATION_NAME>.json` option.

### Can I use this without an OpenAI API key?

No.

### How can I configure a system prompt?

1. Create a new channel.
2. Type in the following:

```json
{"ctx": [{"role": "system", "content": "YOUR_PROMPT_HERE"}]}
```
