def generate_readable_list(list_to_process):
    """
    Generate the message for get_command() to print when the user provides an
    input that does not match any commands.
    """
    # Put quotes around each string.
    processed_list = ["\"{}\"".format(item) for item in list_to_process]

    delimiter = " "

    if len(processed_list) > 2:
        delimiter = "," + delimiter

    return delimiter.join(processed_list)
