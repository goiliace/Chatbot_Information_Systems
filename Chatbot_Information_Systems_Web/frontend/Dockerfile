FROM node:20-alpine
WORKDIR /app

# Cài đặt các dependencies
COPY package.json yarn.lock ./
RUN yarn install
RUN yarn add typescript

COPY . .

# Build ứng dụng
RUN yarn run build

# Khởi chạy ứng dụng
CMD ["yarn", "run", "preview"]

