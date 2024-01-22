
# Plex-Letterboxd Sync

Sync your Letterboxd watchlist with Plex

## Tech Stack

Language: Python 3.11+


## Run Locally

Run the following commands in your terminal! 

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
git clone https://github.com/dragid10/plex-letterboxd-sync.git
```

Go to the project directory
```bash
cd plex-letterboxd-sync
```

Install poetry (python dependency management tool)

```bash
pip install --user poetry
```

Install dependencies

```bash
poetry install
```

Copy the `.env-sample` file and rename it to `.env`, and fill in the values for each variable

```ini
# Plex variables
PLEX_USERNAME=my_username
PLEX_PASSWORD=my_password

# leave blank if 2fa is not enabled for your plex account
PLEX_2FA=6digitcode 

# Letterboxd variables
LETTERBOXD_USERNAME=my_other-username
```

Start the server

```bash
poetry run python main.py
```

