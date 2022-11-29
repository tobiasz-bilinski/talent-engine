
FROM python:3.10

WORKDIR /talent-engine/
COPY . .

ENV WEATHER_API_KEY=b8ef3491d7177de6eec81cbe4d0f2bb2

RUN pip3 install -r requirements.txt


ENTRYPOINT [ "pytest" ]

CMD [ "."]

