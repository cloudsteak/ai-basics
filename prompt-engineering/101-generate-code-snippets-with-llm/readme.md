# Generate Code Snippets with LLMs

## Install mini-conda

Quick installation guide for miniconda can be found [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)


## Use and run

1. Create virtual environment

I use mini-conda to create a virtual environment. You can use any other tool you like.

```bash
conda create --prefix ./.venv python=3.11 -y
conda activate ./.venv
```

2.  Install required packages

```bash
pip3 install -r requirements.txt
```


3. Run the code

3.1 Fireworks


```bash
python3 fireworks.py
```
3.2 OpenAI

```bash
python3 openai.py
```

## Export requirements

```bash
pip3 freeze > requirements.txt
```


## Deactivate virtual environment

```bash
conda deactivate
```




