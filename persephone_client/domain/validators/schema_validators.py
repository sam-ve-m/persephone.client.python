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
from persephone_client.domain.schemas.user_identifier_data_schema import UserIdentifierDataSchema
from persephone_client.domain.schemas.user_selfie_schema import UserSelfieSchema
from persephone_client.domain.schemas.user_complementary_data_schema import UserComplementaryDataSchema
from persephone_client.domain.schemas.user_update_register_data_schema import UserUpdateRegisterDataSchema
from persephone_client.domain.schemas.user_set_electronic_signature_schema import UserSetElectronicSignatureSchema
from persephone_client.domain.schemas.user_change_or_reset_electronic_signature_schema import (
    UserChangeOrResetElectronicSignatureSchema
)
from persephone_client.domain.schemas.create_electronic_signature_session_schema import (
    CreateElectronicSignatureSessionSchema
)


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
    user_identifier_data_schema = UserIdentifierDataSchema
    user_selfie_schema = UserSelfieSchema
    user_complementary_data_schema = UserComplementaryDataSchema
    user_update_register_data_schema = UserUpdateRegisterDataSchema
    user_set_electronic_signature_schema = UserSetElectronicSignatureSchema
    user_change_or_reset_electronic_signature_schema = UserChangeOrResetElectronicSignatureSchema
    create_electronic_signature_session_schema = CreateElectronicSignatureSessionSchema
