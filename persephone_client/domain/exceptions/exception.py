class InvalidMessage(Exception):
    def __init__(self, msg, *args, **kwargs):
        message = f"The given message was invalid: {msg}"
        super().__init__(message, *args, **kwargs)


class InvalidSchemaName(Exception):
    def __init__(self, msg, *args, **kwargs):
        message = f"The given schema name was invalid: {msg}"
        super().__init__(message, *args, **kwargs)


class SchemaNotFound(Exception):
    def __init__(self, msg, *args, **kwargs):
        message = f"The given schema name was not found: {msg}"
        super().__init__(message, *args, **kwargs)

