import json
import jsonschema
from jsonschema import validate
from src.data.json_schemas.json_schema_current import schema_current_weather


def validate_json(json_data):
    try:
        validate(instance=json_data, schema=schema_current_weather)
    except jsonschema.exceptions.ValidationError as error:
        print(error)
        return False

    return True
