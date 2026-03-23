# Now we need to take the the official Superset image and add both the configuration file and the entrypoint script to it. 
# The configuration file will tell Superset how to connect to the database, and the entrypoint script will initialize the database and start the Superset server.
FROM apache/superset:latest
# switch to root user to install additional dependencies and copy files
USER root
# installing drivers for Postgres, which is the database we are using for Superset. This will allow Superset to connect to the Postgres database and store its metadata there.
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org psycopg2-binary

#copying the configuration file and the entrypoint script into the container.
# The configuration file will be placed in the /app/pythonpath directory, which is where Superset looks for configuration files. The entrypoint script will be placed in the /app directory, and it will be executed when the container starts.
COPY config.py /app/pythonpath/config.py
COPY init.sh /app/init.sh

RUN chmod +x /app/init.sh

USER superset

ENTRYPOINT ["/app/init.sh"]

