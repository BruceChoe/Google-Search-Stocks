FROM python:3 as common

WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip

COPY requirements/common.txt requirements/

RUN pip install --no-cache-dir -U -r requirements/common.txt

COPY dustyapi/ dustyapi/
COPY api/ api/


FROM common as bin

COPY requirements/prod.txt requirements/

RUN pip install --no-cache-dir -U -r requirements/prod.txt

COPY docker/entrypoint.sh .
RUN chmod +x entrypoint.sh

ENV HOST="0.0.0.0" PORT="8000"
ENTRYPOINT ["./entrypoint.sh"]


FROM common as test

COPY requirements/dev.txt requirements/

RUN pip install --no-cache-dir -U -r requirements/dev.txt

COPY pytest.ini .
COPY .coveragerc .
COPY tests/ tests/

COPY docker/test_entrypoint.sh .
RUN chmod +x test_entrypoint.sh

ENTRYPOINT ["./test_entrypoint.sh"]


FROM bin
