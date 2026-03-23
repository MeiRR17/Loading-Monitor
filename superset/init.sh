# this is the oprational brain of the system. 
# it will run the superset server and connect it to the database we created in init.sql
# This is a script of Linux os and should be run in the terminal that runs automatically for the first time
# when Superset container is created. Instead we will manually get inside the container and run it,
# The script will do everything automatically: it will create the admin user, it will build the metadata and eveuntually it will run the server.

# This script is based on the official documentation of Superset, you can find it here: https://superset.apache.org/docs/installation/installing-superset-using-docker-compose
!/bin/bash

# Create an admin user (you will be asked to set a password)
superset fab create-admin \
                --username admin \
                --firstname System \
                --lastname Admin \
                --email admin@tel_monitor.com \
                --password admin

echo "Creating database tables..."
superset db upgrade

echo "Initializing Superset..."
superset init

echo "Starting Superset server..."
superset run -p 8088 --with-threads --reload --debugger

