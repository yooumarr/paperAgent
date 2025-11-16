from paper_agent import agent
from phoenix.otel import register
from openinference.instrumentation.smolagents import SmolagentsInstrumentor

register(project_name="paperAgent", auto_instrument=True,)

response = agent.run(str(input()))
print(response)