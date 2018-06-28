FROM node:8

WORKDIR /home/nodejs/app

COPY . .

RUN npm i

EXPOSE 9000

ENTRYPOINT ["npm", "start"]
