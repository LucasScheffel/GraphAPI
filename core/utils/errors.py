def API_Error(e: Exception) -> list:
    """ Formats the exception into an array of strings describing the error """
    try:
        return [dict(e.detail).get(key)[0] for key in dict(e.detail).keys()]
    except Exception:
        return ['An unexpected error ocurred']