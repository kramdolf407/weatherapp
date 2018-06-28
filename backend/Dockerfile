FROM node:8

WORKDIR /home/nodejs/app

COPY . .

RUN npm i

EXPOSE 8000

ENTRYPOINT ["npm", "start"]
