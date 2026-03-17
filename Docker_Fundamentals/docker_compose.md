# Docker Compose
## How to work with Docker Compose

- Basically docker compose will help to run multiple services
- manage shared network and shared volume in structured way

**Steps to execute**

- create folder named docker-comppose, move to that
- create folder named backend and run below commands
```bash
npm init -y
npm install express mysql2
```
- create server.js file and copy code
```js
const db= mysql.createConnection({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
})
db.connect(err =>{
    if(err) throw err;
    console.log("MYSQL Connected")
})
app.get("/", (req, res) => {
  res.send("Backend is Runnig!");
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
```
- creat Dockerfile as:

```dockerfile
FROM node:22-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD [ "node", "server.js" ]
```
---

###  **frontend:**
- in docker_compose directory run:
```bash
npm create vite@latest
# select yes
# Project name: frontend
# framework: React
# javascript
# choose default options by just pressing enter
# ctrl + c for exit
```
- then just create Dockerfile under frontend folder

```dockerfile
FROM node:22-alpine 

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 5173

CMD ["npm","run","dev","--","--host"]
```
- Last create docker_compose.yml file as shown
```yml
services:
  backend:
    build: ./backend
    container_name: backend
    restart: always
    ports:
      - "3000:3000"
    environment:
      - DB_HOST: mysql
      - DB_USER: root
      - DB_PASSWORD: root
      - DB_NAME: appdb
    depends_on:
      - mysql
    networks:
      - app_network
  
  frontend:
    build: ./frontend
    container_name: frontend
    restart: always
    ports:
      - "5173:5173"
    depends_on:
      - backend
    networks:
      - app_network
  
  mysql:
    image: mysql:latest
    container_name: mysql
    restart: always
    ports:
      - "3306:3306"
    environment:
      - MYSQL_ROOT_PASSWORD: root
      - MYSQL_DATABASE: appdb
    volumes:
      - mysql_data:/var/lib/mysql
    networks:
      - app_network

volumes:
  mysql_data:

networks:
  app_network:
```

- run the following command in terminal:

```bash
docker compose up -d --build
# you can see image created, network, volume and 3 containers
docker ps   # to see the running containers

# for checking logs use:
docker logs mysql-container
docker logs backend
docker logs frontend

```
- check localhost:3000
- check localhost:5173

*all services deployed successfully using docker-compose*