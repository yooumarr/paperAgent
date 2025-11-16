# ArXiv Research Agent

A simple agent that searches ArXiv and answers questions using `smolagents`.

## Setup

1. **Clone the repo**:
```bash
   git clone https://github.com/yooumarr/paperAgent.git
   cd paperAgent
```

2. **Install the dependencies**:
```bash
   pip install -r requirements.txt
```

3. **Set up environment variables**:
```bash
   cp .env.example .env
```
   Add your Hugging Face token to .env:
```
   HF_TOKEN=hf_your_token_here
```

4. **Run the agent**:
```bash
   python main.py
```

## Features

- Search ArXiv for the papers
- Use smolagents to summarize the papers


## Observability with Phoenix

The agent includes integrated tracing with Phoenix by Arize AI, allowing you to:
- Monitor agent execution flow in real-time
- Track tool calls and LLM responses
- Debug and optimize agent performance
- Visualize multi-step reasoning chains

Phoenix traces are automatically captured during agent execution.
Visit http://localhost:6006/projects to see the model traces.

## How It Works

1. User queries for research papers on a specific topic
2. Agent searches ArXiv database using custom tools
3. AI processes and summarizes relevant papers
4. Phoenix traces the entire workflow for observability
5. User receives intelligent summary with paper references
