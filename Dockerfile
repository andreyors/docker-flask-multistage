FROM python:3 as base
COPY requirements.txt .
RUN set -xe \
	&& pip install -r requirements.txt

FROM python:3-alpine
COPY --from=base /root/.cache /root/.cache
COPY --from=base requirements.txt /flask/

WORKDIR /flask

RUN set -xe \
	&& pip install -r /flask/requirements.txt \
	&& rm -rf /root/.cache

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
