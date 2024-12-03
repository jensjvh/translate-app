# TranslateApp

A small Flask app using https://huggingface.co/Helsinki-NLP/opus-mt-en-fi to translate English input to Finnish.

## Requirements

* Python 3.10 or higher
* [uv](https://docs.astral.sh/uv/)

## Running and developing the app

First, create a virtual environment.

Get [uv](https://docs.astral.sh/uv/), for example with the command

```bash
pip3 install uv
```

Now to get the dependencies, run:

```bash
uv sync --no-dev
```

or to get the packages required for development:

```bash
uv sync
```

Then launch the app with:

```bash
uv run flask --app src/index.py run
```

The first startup might take some time, as the Hugging Face model needs to be loaded.