from jsonschema.exceptions import ValidationError
from jsonschema import validate


def validate_json(json_data: object, schema: dict) -> bool:
    """Validate that JSON schema is correct.

    Args:
        json_data (object): JSON object to be validated.
        schema (dict): Corresponding JSON schema (found in data/json_schemas).

    Returns:
        True if schema of json_data is validated, False otherwise.

    """
    try:
        validate(instance=json_data, schema=schema)
    except ValidationError as error:
        print(error)
        return False

    return True
