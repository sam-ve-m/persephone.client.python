from persephone_client.domain.schemas.dtvm_user_schema import DtvmUserSchema
from persephone_client.domain.schemas.dtvm_update_user_schema import DtvmUpdateUserSchema
from persephone_client.domain.schemas.prospect_user_schema import ProspectUserSchema
from persephone_client.domain.schemas.suitability_schema import SuitabilitySchema
from persephone_client.domain.schemas.table_schema import TableSchema
from persephone_client.domain.schemas.term_schema import TermsSchema


class ChooseSchema:
    schemas = {
        "DtvmUserSchema": DtvmUserSchema,
        "DtvmUpdateUserSchema": DtvmUpdateUserSchema,
        "ProspectUserSchema": ProspectUserSchema,
        "SuitabilitySchema": SuitabilitySchema,
        "TableSchema": TableSchema,
        "TermsSchema": TermsSchema
    }
