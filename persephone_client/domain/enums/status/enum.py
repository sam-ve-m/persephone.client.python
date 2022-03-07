from enum import Enum


class PersephoneClientStatus(Enum):
    success = 0
    invalid_message = 1
    invalid_schema_name = 2
    schema_not_found = 3
    not_mapped_error = 4
