# Compiler
CC = gcc

# Compiler Flags
CFLAGS = -Wall -Wextra -O2

# Linker Flags (Include libgpiod)
LDFLAGS = -lgpiod

# Target executable
TARGET = ecmio

# Source files
SRC = ecmio.c

# Build the executable
all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC) $(LDFLAGS)

# Clean build files
clean:
	rm -f $(TARGET)
