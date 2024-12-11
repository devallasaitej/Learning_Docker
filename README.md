## Docker learning  

Build Docker image: docker build -t my-python-postgres-app .

Run PostgreSQL container: docker run --name postgres-container -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres

Run Python Docker container with the link to the PostgreSQL container: docker run --link postgres-container:postgres --name python-postgres-app my-python-postgres-app


