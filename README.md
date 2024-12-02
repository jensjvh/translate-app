# TranslateApp

A small Flask app using https://huggingface.co/Helsinki-NLP/opus-mt-en-fi to translate Finnish input text to English.

## Testing and development

Get [uv](https://docs.astral.sh/uv/) and run:

```bash
uv sync
```

Then launch the app with:

```bash
uv run flask --app src/index.py run
```