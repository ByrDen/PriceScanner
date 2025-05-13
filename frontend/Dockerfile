# build stage
FROM node:20 AS build
WORKDIR /app
COPY . .
RUN npm install && npm run build

# serve stage
FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html
