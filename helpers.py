from flask import jsonify

def restresponse(message: str):
    """
    Formats a string into a standardized JSON response.
    Example:
        {"status": "OK", "result": "Hello, World!"}
    """
    return jsonify({
        "status": "OK",
        "result": message
    })