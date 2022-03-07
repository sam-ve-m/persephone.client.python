import json
from typing import Tuple

from persephone_client.domain.enums.status.enum import PersephoneClientStatus
from persephone_client.services.message_validator.service import MessageValidatorService
from persephone_client.services.persephone.service import PersephoneService


class Persephone:

    @staticmethod
    async def send_to_persephone(topic: str, partition: int, message: dict, schema_name: str) -> Tuple[bool, PersephoneClientStatus]:
        is_message_sent, persephone_client_status = await PersephoneService.send_to_persephone(
            topic=topic,
            partition=partition,
            message=message,
            schema_name=schema_name
        )

        return is_message_sent, persephone_client_status


if __name__ == '__main__':
    pass
    # message = {'ip': '127.0.0.1', 'jwt': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOiAxNjc2Njc0MTIwLCAiY3JlYXRlZF9hdCI6IDE2NDUxMzgxMjAuMDc4NTAzLCAic2NvcGUiOiB7InZpZXdfdHlwZSI6ICJkZWZhdWx0IiwgImZlYXR1cmVzIjogWyJkZWZhdWx0IiwgInJlYWx0aW1lIl19LCAidXNlciI6IHsidW5pcXVlX2lkIjogIjk3OGNlMjYzLWUxOGYtNDUyMC05ZDg3LTliZjRmNzA1MjhkOSIsICJuaWNrX25hbWUiOiAiUkFTVEEzIn19.jKQdwge-bFGWTkzXBDjRP0Akw8bK8C2tC4ElIAaELwCzu1CDHrcLq5iXKy3gJm7GJdcoqwZVnY4ujvJxZau-1gtzErPEXxlQ1hC5f6rCKiOvuh0cOkTYdpe4ZxNyJSEm3E8Adak0UDbcw9u1tYQ4D5o3pChFEKhvPiNL7o0xDzhdpZKAsBs07-HAzqF61yTQisGobMz6yYq73jK8f9PvzqXUnKbUPEePILFzkq-eMWH3orr7VAmddCdv62P_WvkEyQev0dqil4faj5PbKw4IY2-z3DI1rrsMKx1dIwr9huWwZMikAUZE1wMVMSdXgIOEx9O5p5x9ixoi2FW9RAL3pA', 'is_authentic': True, 'connection_unique_id': 592801}
    # MessageValidatorService.validate_message(message=message, schema_name="hermes_session_authenticity")
