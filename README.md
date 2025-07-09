# LangChain Azure OpenAI Project

This project demonstrates how to use LangChain with Azure OpenAI GPT-4 model.

## Setup Instructions

### 1. Clone and Navigate to Project

```bash
git clone <your-repo-url>
cd langchain-azure-project
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

1. Copy the `.env` file and update with your Azure OpenAI credentials:
   - `AZURE_OPENAI_API_KEY`: Your Azure OpenAI API key
   - `AZURE_OPENAI_ENDPOINT`: Your Azure OpenAI endpoint URL
   - `AZURE_OPENAI_DEPLOYMENT_NAME`: Your GPT-4 deployment name

### 5. Run the Application

```bash
python app.py
```

## Prerequisites

- Python 3.8 or higher
- Azure OpenAI resource with GPT-4 model deployed
- Valid Azure OpenAI API key and endpoint

## Project Structure

```
langchain-azure-project/
├── .env                    # Environment variables
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
├── app.py               # Main application file
└── README.md             # This file
```

## Troubleshooting

- Make sure your virtual environment is activated
- Verify your Azure OpenAI credentials are correct
- Check that your deployment name matches the one in Azure Portal
