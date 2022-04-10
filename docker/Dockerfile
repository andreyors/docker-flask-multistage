FROM python:3.10-slim as base

SHELL ["/bin/bash", "-xeuo", "pipefail", "-c"]

ARG ENV=development
ENV ENV=${ENV} \
    # python
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry
    POETRY_VERSION=1.1.13 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1 \
    # env
    VENV_PATH="/opt/venv" \
    PATH="${POETRY_HOME}/bin:${VENV_PATH}/bin:${PATH}"

EXPOSE 3000/tcp

WORKDIR /flask
COPY pyproject.toml poetry.lock ./

RUN python -m venv ${VENV_PATH} \
    && . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install poetry==${POETRY_VERSION} \
    && poetry install --no-dev --no-ansi

FROM base AS development
ENV ENV=development \
    PATH="${VENV_PATH}/bin:${PATH}"

WORKDIR /flask

COPY --from=base $VENV_PATH $VENV_PATH
RUN python -m venv ${VENV_PATH} \
    && . /opt/venv/bin/activate \
    && poetry install --no-ansi

CMD exec gunicorn -c gunicorn.py app:app -b 0.0.0.0:3000 --reload

FROM base AS production
ENV ENV=production

WORKDIR /flask

COPY --from=base $VENV_PATH $VENV_PATH
COPY . .

CMD exec gunicorn -c gunicorn.py app:app -b 0.0.0.0:3000
