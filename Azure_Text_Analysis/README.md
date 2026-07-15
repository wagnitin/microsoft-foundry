# Azure Text Analysis AI Agent

Small collection of Python scripts for basic text analysis using Azure or local models.

Overview
- `detect_language.py` — detect input text language. See [detect_language.md](detect_language.md).
- `PII_detection.py` — detect personally identifiable information. See [PII_detection.md](PII_detection.md).
- `Sentiment.py` — perform sentiment analysis. See [Sentiment.md](Sentiment.md).

Quickstart
1. Create or edit `config.env` with any API keys or settings required by the scripts.
2. (Optional) Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Running the scripts
- Detect language:

```powershell
python detect_language.py
```

- PII detection:

```powershell
python PII_detection.py
```

- Sentiment analysis:

```powershell
python Sentiment.py
```

Notes
- The repository does not include a `requirements.txt` by default; inspect each script for required packages and create one if needed.
- For scripts that call external services, set credentials in `config.env`.
- See the individual markdown files for details and examples: [detect_language.md](detect_language.md), [PII_detection.md](PII_detection.md), [Sentiment.md](Sentiment.md).

Contributing
- Update the corresponding `.md` when you change a script's API or add examples.
