FROM python:3

WORKDIR /tmp

RUN set -x && \
	pip install requests

RUN set -x && \
	pip install pyyaml

COPY push.py /tmp/
COPY secret.yml /tmp/
COPY images_*.png /tmp/

CMD ["python3", "push.py"]
