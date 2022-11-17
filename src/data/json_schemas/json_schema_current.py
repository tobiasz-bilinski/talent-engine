schema_current_weather = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "coord": {
            "type": "object",
            "properties": {
                "lon": {
                    "type": "number"
                },
                "lat": {
                    "type": "number"
                }
            },
            "required": [
                "lon",
                "lat"
            ]
        },
        "weather": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "main": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "icon": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "main",
                        "description",
                        "icon"
                    ]
                }
            ]
        },
        "base": {
            "type": "string"
        },
        "main": {
            "type": "object",
            "properties": {
                "temp": {
                    "type": "number"
                },
                "feels_like": {
                    "type": "number"
                },
                "temp_min": {
                    "type": "number"
                },
                "temp_max": {
                    "type": "number"
                },
                "pressure": {
                    "type": "integer"
                },
                "humidity": {
                    "type": "integer"
                }
            },
            "required": [
                "temp",
                "feels_like",
                "temp_min",
                "temp_max",
                "pressure",
                "humidity"
            ]
        },
        "visibility": {
            "type": "integer"
        },
        "wind": {
            "type": "object",
            "properties": {
                "speed": {
                    "type": "number"
                },
                "deg": {
                    "type": "integer"
                }
            },
            "required": [
                "speed",
                "deg"
            ]
        },
        "clouds": {
            "type": "object",
            "properties": {
                "all": {
                    "type": "integer"
                }
            },
            "required": [
                "all"
            ]
        },
        "dt": {
            "type": "integer"
        },
        "sys": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "integer"
                },
                "id": {
                    "type": "integer"
                },
                "country": {
                    "type": "string"
                },
                "sunrise": {
                    "type": "integer"
                },
                "sunset": {
                    "type": "integer"
                }
            },
            "required": [
                "type",
                "id",
                "country",
                "sunrise",
                "sunset"
            ]
        },
        "timezone": {
            "type": "integer"
        },
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "cod": {
            "type": "integer"
        }
    },
    "required": [
        "coord",
        "weather",
        "base",
        "main",
        "visibility",
        "wind",
        "clouds",
        "dt",
        "sys",
        "timezone",
        "id",
        "name",
        "cod"
    ]
}
