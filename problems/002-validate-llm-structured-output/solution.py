import json

def validate_response(raw, schema):
    """Parse and validate a model's JSON reply against a {field: type} schema.

    Return the cleaned dict, or None if it cannot be trusted.
    """

    try:
        json_payload = json.loads(raw)
    except json.decoder.JSONDecodeError:
        return None

    if not isinstance(json_payload, dict):
        return None

    response = {}
    for key, expected_type in schema.items():
        if key not in json_payload:
            return None

        value = json_payload[key]

        if type(json_payload[key]) is not expected_type:
            return None
        response[key] = json_payload[key]


        try:
            response[key] = expected_type(value)
        except (ValueError, TypeError):
            return None
    return response
