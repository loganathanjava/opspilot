# OPSPilot

An AI-powered OpenShift operations assistant.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables in `.env`:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. Run the agent:
   ```bash
   python app.py
   ```

## Project Structure

- `agent/` - Core agent implementation
- `tools/` - OpenShift tools and utilities
- `services/` - LLM and external service integrations
