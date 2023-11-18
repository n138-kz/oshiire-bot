FROM python:3

WORKDIR /tmp

RUN set -x && \
	pip install requests

RUN set -x && \
	pip install pyyaml

CMD ["python3", "/usr/oshiire_bin/push.py"]
