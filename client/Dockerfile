FROM node:13.12.0-alpine3.10

WORKDIR /app
EXPOSE 3000
COPY ./package.json /tmp/package.json
RUN cp /tmp/package.json /app/package.json
RUN npm install
ENTRYPOINT npm start
