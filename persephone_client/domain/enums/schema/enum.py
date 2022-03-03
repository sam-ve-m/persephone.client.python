from enum import Enum

from persephone_client.domain.schemas.sphinx.dtvm_user.schema import DtvmUserSchema
from persephone_client.domain.schemas.sphinx.dtvm_update_user.schema import DtvmUpdateUserSchema
from persephone_client.domain.schemas.sphinx.prospect_user.schema import ProspectUserSchema
from persephone_client.domain.schemas.sphinx.suitability.schema import SuitabilitySchema
from persephone_client.domain.schemas.sphinx.table.schema import TableSchema
from persephone_client.domain.schemas.sphinx.term.schema import TermsSchema
from persephone_client.domain.schemas.sphinx.user_authentication.schema import UserAuthenticationSchema
from persephone_client.domain.schemas.sphinx.user_thebes_hall.schema import UserThebesHallSchema
from persephone_client.domain.schemas.sphinx.user_logout.schema import UserLogoutSchema
from persephone_client.domain.schemas.sphinx.signed_term.schema import SignedTermSchema
from persephone_client.domain.schemas.sphinx.user_identifier_data.schema import UserIdentifierDataSchema
from persephone_client.domain.schemas.sphinx.user_selfie.schema import UserSelfieSchema
from persephone_client.domain.schemas.sphinx.user_complementary_data.schema import UserComplementaryDataSchema
from persephone_client.domain.schemas.sphinx.user_update_register_data.schema import UserUpdateRegisterDataSchema
from persephone_client.domain.schemas.sphinx.user_set_electronic_signature.schema import UserSetElectronicSignatureSchema
from persephone_client.domain.schemas.sphinx.user_change_or_reset_electronic_signature.schema import (
    UserChangeOrResetElectronicSignatureSchema
)
from persephone_client.domain.schemas.sphinx.create_electronic_signature_session.schema import (
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
