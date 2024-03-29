# Basic AI codes and prompts


## Table of contents

- [Topics](#topics)
- [Install mini-conda](#install-mini-conda)
- [Prepare](#prepare)
- [Export requirements](#export-requirements)
- [Deactivate virtual environment](#deactivate-virtual-environment)

## Topics

- Prompt Enginering
    - [101 - Generate Code Snippets with LLMs](./prompt-engineering/101-generate-code-snippets-with-llm/readme.md)


## Install mini-conda

Quick installation guide for miniconda can be found [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)


## Prepare

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


## Export requirements

```bash
pip3 freeze > requirements.txt
```


## Deactivate virtual environment

```bash
conda deactivate
```