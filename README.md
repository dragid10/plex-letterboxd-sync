
# Plex-Letterboxd Sync

Sync your Letterboxd watchlist with Plex

## Tech Stack

Language: Python 3.11+


## Run Locally

### Python

Install `python 3.11` using one of the many installation methods:

- [asdf](https://asdf-vm.com/):  
  `asdf install python 3.11-latest`

- [Pyenv (preferred)](https://github.com/pyenv/pyenv):  
  `pyenv install 3.11:latest`

- [Homebrew](https://brew.sh/):  
  `brew install python@3.11`


### Setup Project 

Clone the project

```bash
git clone https://link-to-project
```

Go to the project directory
```bash
cd my-project
```

Install the python dependency management tool: `poetry` 

```bash
pip install --user poetry
```

Install dependencies

```bash
poetry install
```

Start the server

```bash
poetry run python main.py
```

