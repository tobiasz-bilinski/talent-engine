
FROM ubuntu:22.04

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install wget -y
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install fonts-liberation libasound2 -y libatk-bridge2.0-0 -y \
    libatk1.0-0 -y libatspi2.0-0 -y libcups2 -y libcurl4 -y libcurl3-gnutls -y libcairo2 -y \
    libcurl3-nss -y libdrm2 -y libgbm1 -y libgtk-3-0 -y \
    libgtk-4-1 -y libnspr4 -y libnss3 -y libpango-1.0-0 -y libwayland-client0 -y \
    libxcomposite1 -y libxdamage1 -y libxfixes3 -y libxkbcommon0 -y \
    libxrandr2 -y xdg-utils -y

RUN dpkg -i google-chrome-stable_current_amd64.deb

WORKDIR /talent-engine/
COPY . .

ENV WEATHER_API_KEY=b8ef3491d7177de6eec81cbe4d0f2bb2

RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install pip -y

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "pytest" ]

CMD [ ".", "-lvs" ]

