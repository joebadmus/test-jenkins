FROM selenium/standalone-chrome:119.0

USER seluser

# Install required dependencies
USER root
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    curl \
    apt-transport-https \
    ca-certificates \
    gnupg \
    python3-tk \
    python3-pip \
    python3-hamcrest \
    xvfb \
    x11-utils \
    && rm -rf /var/lib/apt/lists/*

# Add Microsoft repository for SQL Server dependencies
RUN curl -s https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl -s https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Update and install SQL Server related packages
RUN apt-get update -y && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 mssql-tools18 unixodbc-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy resolved.conf and .Xauthority files
# COPY resolved.conf /etc/systemd/resolved.conf
# COPY .Xauthority /home/seluser/.Xauthority

# Set environment variables
ENV DISPLAY=:99
WORKDIR /src

# Copy application code
COPY . .

# Install Python dependencies
RUN pip3 install -Iv -r requirements.txt

USER seluser

