from smolagents import CodeAgent, InferenceClientModel, tool
import arxiv 
import time
from huggingface_hub import login
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("HF_TOKEN")
if token:
    login(token=token)
else:
    print("HF_TOKEN not found in environment variables.")


@tool
def fetch_relevant_paper_tool(topic:str) -> str:
    """
    Search recent papers for the topic.
    Args:
        topic (str): The topic for we want to fetch the papers for.
    """
    client  = arxiv.Client(
        page_size=10,
        delay_seconds=3,
        num_retries=3
    )

    search = arxiv.Search(
        query=topic,
        max_results=20,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    papers = {}
    try:
        for i, r in enumerate(client.results(search)):
            papers[f"paper{i}"] = {'title':r.title, 'author names':{','.join(a.name for a in r.authors)}, 
                                   'published date':r.published.date(), 'abstract':r.summary, 'pdf url':r.pdf_url}
    except arxiv.HTTPError as e:
        pass


    return papers

writer_agent = CodeAgent(
    tools=[],
    model=InferenceClientModel()
)

@tool
def write_summary(content:str) -> str:
    """
    Write a professional summary for the given content.
     
    Args:
        content(str): The content for which the summary is to be written
    """
    return writer_agent.run(content)


agent = CodeAgent(tools=[fetch_relevant_paper_tool, write_summary],
                  model=InferenceClientModel())
