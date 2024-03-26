RUN this command inside the auth_management folder in docker bash 
#### alembic init -t async auth_management/alembic/migrations
#### alembic revision --autogenerate -m "init"
#### alembic upgrade head