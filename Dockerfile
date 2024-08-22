# Set the base image
FROM python:3.12-slim

# Set environment variables
ENV USER steamcmd
ENV HOME /data

ENV LOG_LEVEL info
ENV CONCURRENCY 4

################## BEGIN INSTALLATION ######################

# Install Python requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt \
 && rm /tmp/requirements.txt

# Create the application user
RUN useradd -m -d $HOME $USER

# Switch user and set working dir
USER $USER
WORKDIR $HOME

# Copy application code
COPY --chown=$USER:$USER src/ $HOME/

##################### INSTALLATION END #####################

# Set default container command
CMD celery -A main worker --loglevel=$LOG_LEVEL --concurrency=$CONCURRENCY --beat