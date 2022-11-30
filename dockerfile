FROM python:3.10

WORKDIR /talent-engine/
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "pytest" ]

CMD [ "-lvs", "--browser", "remote_chrome" ]

