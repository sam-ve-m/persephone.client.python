from enum import Enum

from persephone_client.domain.schemas.dtvm_user_schema import DtvmUserSchema
from persephone_client.domain.schemas.dtvm_update_user_schema import DtvmUpdateUserSchema
from persephone_client.domain.schemas.prospect_user_schema import ProspectUserSchema
from persephone_client.domain.schemas.suitability_schema import SuitabilitySchema
from persephone_client.domain.schemas.table_schema import TableSchema
from persephone_client.domain.schemas.term_schema import TermsSchema
from persephone_client.domain.schemas.user_authentication_schema import UserAuthenticationSchema
from persephone_client.domain.schemas.user_thebes_hall_schema import UserThebesHallSchema
from persephone_client.domain.schemas.user_logout_schema import UserLogoutSchema
from persephone_client.domain.schemas.signed_term_schema import SignedTermSchema


class ChooseSchema(Enum):
    dtvm_user_schema = DtvmUserSchema
    dtvm_update_user_schema = DtvmUpdateUserSchema
    prospect_user_schema = ProspectUserSchema
    suitability_schema = SuitabilitySchema
    table_schema = TableSchema
    terms_schema = TermsSchema
    user_authentication_schema = UserAuthenticationSchema
    user_thebes_hall_schema = UserThebesHallSchema
    user_logout_schema = UserLogoutSchema
    signed_term_schema = SignedTermSchema
