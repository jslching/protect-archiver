# Project build and development instructions
### For Linux (Debian/Ubuntu)
#### Tested on Ubuntu 20.04.3 LTS, last updated on February 6, 2022

---

## :package: Prepare the environment and install dependencies

### Install the necessary packages
```bash
$ sudo apt install curl git python3 python3-distutils python3-pip libffi-dev libssl-dev
```

### Install Docker (if not already installed on your system)
Follow the instructions at https://docs.docker.com/engine/install/ubuntu/

### Install Python Poetry (packaging and dependency management)
```bash
$ curl -sSL https://install.python-poetry.org | python3 -
$ source $HOME/.poetry/env
```

OR

```bash
$ pip install -U poetry
$ source $HOME/.poetry/env
```

### Clone the source repository
```bash
$ git clone https://github.com/danielfernau/unifi-protect-video-downloader
$ cd unifi-protect-video-downloader
```

### Install pre-commit hooks
```bash
$ pip install pre-commit
$ pre-commit install
$ pre-commit run --all # first run
```

### Spawn a shell within the virtual environment
If no virtual environment exists yet, a new one will be created automatically.
```bash
$ poetry shell
```

### Install project dependencies
It's recommended to switch to a virtual environment using `poetry shell` before running this command.
```bash
$ poetry install
```

---

## :pencil: Development
Once the environment has been set up, you can start editing the source files.
Poetry documentation can be found at https://python-poetry.org/docs/master/cli/
It's recommended to switch to a virtual environment using `poetry shell` before running any of the commands below.

### Run
```bash
$ poetry run protect-archiver [OPTIONS] COMMAND [ARGS]...
```

### Lint
```bash
$ poetry run flake8 protect_archiver
```

### Format code
```bash
$ black protect_archiver
```

### Tests
```bash
$ poetry run py.test -v
```

---

## :hammer_and_wrench: Build a package

### Build package
```bash
$ poetry build
```

### Install package
```bash
$ cd ./dist
$ pip3 install protect_archiver*.whl
```
Replace `protect_archiver*.whl` with a more specific file name if you have multiple versions in the `./dist` directory.

### Build Docker image
From within the project root directory run
```bash
$ docker build -t unifitoolbox/protect-archiver .
```

### Run Docker image
```bash
$ docker run --volume /path/on/host/machine:/downloads unifitoolbox/protect-archiver --help
```
Replace `/path/on/host/machine` with an absolute path to your download directory and `--help` with one of the supported commands and its parameters.
Have a look at the project's README.md for additional details.
