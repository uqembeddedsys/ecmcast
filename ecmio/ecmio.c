#include <gpiod.h>
#include <stdio.h>

int main() {
    struct gpiod_chip *chip = gpiod_chip_open_by_name("gpiochip0");
    struct gpiod_line *line = gpiod_chip_get_line(chip, 17);
    gpiod_line_request_input(line, "docker_example");

    int value = gpiod_line_get_value(line);
    printf("GPIO 17 value: %d\n", value);

    gpiod_chip_close(chip);
    return 0;
}
