CC=gcc
CFLAGS=-Wall -Wextra -O2
TARGET=ecmsocket
SRC=ecmsocket.c

# Default Screen parameter argument.
# To get values, Run fbset -i
SCREEN_XRES ?= 1920
SCREEN_YRES ?= 1080
SCREEN_PIXEL_BITS ?= 16
SCREEN_LINE_LEN ?= 3840

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -DSCREEN_XRES=$(SCREEN_XRES) -DSCREEN_YRES=$(SCREEN_YRES) -DSCREEN_PIXEL_BITS=$(SCREEN_PIXEL_BITS) -DSCREEN_LINE_LEN=$(SCREEN_LINE_LEN) -o $(TARGET) $(SRC)

clean:
	rm -f $(TARGET)

.PHONY: all clean
