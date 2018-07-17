FROM ubuntu:latest

RUN apt-get update && \
    apt-get upgrade -y && apt-get install -y apt-transport-https

RUN apt-get install -y ca-certificates wget gnupg && \
    (wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -) && \
    echo 'deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update

RUN apt-get install -y python3-selenium xvfb php-cli php-xml php-cli
RUN apt-get install -y python3-pip
RUN pip3 install robotframework robotframework-xvfb
RUN pip3 install --pre --upgrade robotframework-seleniumlibrary
RUN apt-get install -y unzip libgconf-2-4 fvwm

RUN cd /usr/local/bin && \
    wget -q -O geckodriver.tar.gz 'https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz' && \
    tar -xvzf geckodriver.tar.gz && \
    rm geckodriver.tar.gz && \
    chmod +x geckodriver

RUN cd /usr/local/bin && \
    wget -q -O chromedriver.zip 'https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip' && \
    unzip chromedriver.zip && \
    rm chromedriver.zip && \
    chmod +x chromedriver

ENV FIREFOX_VERSION 57.0.2
ENV FIREFOX_SHA256 df5a47a82c1beb85ae46f0e34b1d5115b1c308361760e2fa81e0aef7d7fef162
ENV FIREFOX_URL https://download-installer.cdn.mozilla.net/pub/firefox/releases/${FIREFOX_VERSION}/linux-x86_64/en-US/firefox-${FIREFOX_VERSION}.tar.bz2
RUN wget -q -O firefox.tar.bz2 ${FIREFOX_URL} && \
    (echo "${FIREFOX_SHA256} *firefox.tar.bz2" | sha256sum -c -) && \
    tar -C /opt -xjf firefox.tar.bz2 && \
    rm firefox.tar.bz2

RUN apt-get install -y google-chrome-stable

RUN apt-get install iputils-ping

# user environment
ENV PATH=/opt/firefox:/opt/google/chrome:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

COPY . .

EXPOSE 4444

ENTRYPOINT [ "/docker-entrypoint.sh" ]
