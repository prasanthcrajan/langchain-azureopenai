import getpass
import os
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("AZURE_OPENAI_API_KEY"):
    os.environ["AZURE_OPENAI_API_KEY"] = getpass.getpass("Press Enter to continue...")

# Check for required environment variables
required_vars = [
    "AZURE_OPENAI_API_BASE",
    "AZURE_OPENAI_DEPLOYMENT_NAME",
    "AZURE_OPENAI_API_VERSION"
]
for var in required_vars:
    print(f"Checking environment variable: {var} = {os.environ.get(var)}")
    if not os.environ.get(var):
        raise EnvironmentError(f"Missing required environment variable: {var}")

try:
    query =  str(input("Enter your query: "))

    model = AzureChatOpenAI(
        azure_endpoint=os.environ.get("AZURE_OPENAI_API_BASE"),    
        azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME"),
        openai_api_version=os.environ.get("AZURE_OPENAI_API_VERSION"))

    messages = [
        SystemMessage("Please translate the following English text to French:"),
        HumanMessage(content=query)
    ]

    response = model.invoke(messages)
    print(response.content)

    system_message_template = "Please translate the following {input_language} text to {output_language}."
    human_message_template = "{query}"

    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", system_message_template),    
        ("human", human_message_template)
    ])

    templatesMessages = chat_prompt.format_messages(
        input_language="English",
        output_language="French",
        query=query
    )

    response = model.invoke(templatesMessages)
    print(response.content)
except Exception as e:
    print(f"An error occurred: {e}")
    print("Please check your environment variables and ensure the Azure OpenAI service is correctly configured.")




