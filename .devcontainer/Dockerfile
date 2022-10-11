ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VERSION=1.2.2
# ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && update-alternatives --install /usr/local/bin/poetry poetry /opt/poetry/bin/poetry 900 \
    # Enable tab completion for bash
    && poetry completions bash >> /home/vscode/.bash_completion \
    # Enable tab completion for Zsh
    && mkdir -p /home/vscode/.zfunc/ \
    && poetry completions zsh > /home/vscode/.zfunc/_poetry \
    && echo "fpath+=~/.zfunc\nautoload -Uz compinit && compinit" >> /home/vscode/.zshrc

COPY pyproject.toml poetry.lock /tmp/poetry/
WORKDIR /tmp/poetry
RUN poetry config virtualenvs.create false && poetry install \
    && rm -rf /tmp/poetry
