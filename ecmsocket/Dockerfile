FROM debian:latest

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libc6-dev \
    linux-libc-dev \
    libjpeg-dev \
    libpng-dev \
    libfreetype6-dev \
    libfontconfig1-dev \
    net-tools \
    iproute2 \
    curl \
    nano \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy source code
COPY ecmsocket.c /app/ecmsocket.c
COPY Makefile /app/Makefile

# Compile the program
RUN make

# Expose the port
EXPOSE 5000

# Grant access to the framebuffer
VOLUME ["/dev/fb0"]

RUN chmod 666 /dev/fb0 || true

# Run the application
CMD ["./ecmsocket"]

