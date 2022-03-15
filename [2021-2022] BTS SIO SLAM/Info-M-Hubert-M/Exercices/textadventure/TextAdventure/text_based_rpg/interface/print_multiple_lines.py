from .built_in_methods import print_, sleep

def print_multiple_lines(lines, delay=None):
    for individual_line in lines:
        print_(individual_line)

        if delay:
            sleep(delay)
