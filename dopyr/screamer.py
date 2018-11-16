def maybe_scream(text, do_scream=False):
    """Returns given text input as caps lock text, if do_scream is true.

    Args:
        text (str): Some input text
        do_scream (bool): Decide, whether to scream or not
    
    Returns:
        str: May be in caps lock

    """
    if do_scream:
        text = text.upper()
    return text