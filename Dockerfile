FROM python:3.10

COPY ./src/* /sunfrog_cli/
COPY ./requirements.txt /sunfrog_cli/
RUN pip install -r /sunfrog_cli/requirements.txt

ENTRYPOINT [ "python", "/sunfrog_cli/sunfrog_cli.py" ]
