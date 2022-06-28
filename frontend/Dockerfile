FROM node:16-slim
ARG AXIOS_BASEURL
ARG AXIOS_BROWSER_BASEURL
RUN apt-get update
WORKDIR /usr/src/app
COPY package.json ./
RUN npm install
COPY . .
ENV HOST=0.0.0.0