def maybe_scream(text, do_scream=False):
    """Returns given text input as caps lock text, if do_scream is true.

    :param text: Some input text.
    :type text: str.
    :param do_scream: Decide, whether to scream or not.
    :type do_scream: bool.
    :returns: str -- May be in caps lock.

    """
    if do_scream:
        text = text.upper()
    return text