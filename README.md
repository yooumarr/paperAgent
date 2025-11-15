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