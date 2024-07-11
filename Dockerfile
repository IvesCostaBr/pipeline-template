# 
FROM python:3.10.13-bullseye

ARG PROJECT_ENVIRON
ARG PROJECT_ID
ARG DEPLOY
ARG VERSION_BUILD

ENV PROJECT_ENVIRON=$PROJECT_ENVIRON
ENV PROJECT_ID=$PROJECT_ID
ENV DEPLOY=$DEPLOY
ENV VERSION_BUILD=$VERSION_BUILD

ENV APP_HOME=/code
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/*
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

COPY ./requirements.txt $APP_HOME/requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r $APP_HOME/requirements.txt

RUN useradd appuser && chown -R appuser $APP_HOME
USER appuser

RUN chmod +w $APP_HOME

COPY . .

EXPOSE 8000
EXPOSE 5678

CMD ["python", "-m", "debugpy", "--wait-for-client", "--listen","0.0.0.0:5678", "-m", "uvicorn", "src.channel.api.main:api", "--host", "0.0.0.0", "--port", "8000", "--reload"]