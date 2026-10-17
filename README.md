# Customer Support Query Extraction using Pydantic and Groq

A Python project that uses an LLM and Pydantic to extract key information from customer support queries written in natural language and convert it into structured JSON data.

The project defines a Pydantic schema containing fields such as product name, issue description, customer address, email, and contact number. The LLM extracts the relevant information according to the schema, making customer support queries easier to process and organize.

**Key Features**
- Structured data extraction from natural language.
- Pydantic-based schema definition and validation.
- Groq API integration for LLM-powered extraction.
- JSON-formatted responses for consistent output.
- Handling of missing information using empty strings.
- Prompt engineering to minimize unnecessary response text and focus on the required output.

**Tech Stack:** Python, Pydantic, Groq API, JSON, Python-dotenv.

**Use Case:** Automating information extraction from customer support tickets to help support teams organize customer details and issue descriptions more efficiently.
