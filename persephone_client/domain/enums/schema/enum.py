from enum import Enum

from persephone_client.domain.schemas.ebisu.cash_flow_withdrawal_to_external_bank.schema import \
    CashFlowWithdrawalToExternalBank
from persephone_client.domain.schemas.ebisu.exchange_proposal_execution.schema import ExchangeProposalExecution
from persephone_client.domain.schemas.ebisu.exchange_proposal_pre_execution.schema import ExchangeProposalPreExecution
from persephone_client.domain.schemas.ebisu.exchange_proposal_simulation.schema import ExchangeProposalSimulation
from persephone_client.domain.schemas.jormungandr.term.get_order_token.schema import GetOrderTokenVariableIncome, \
    GetOrderTokenFixedIncome
from persephone_client.domain.schemas.sphinx.cpf_validation.schema import CpfValidation
from persephone_client.domain.schemas.sphinx.cpf_validation_status.schema import CpfValidationStatus
from persephone_client.domain.schemas.sphinx.picpay_user_data.schema import PicpayUserData
from persephone_client.domain.schemas.regis.pld.schema import Pld
from persephone_client.domain.schemas.sphinx.score_validation.schema import ScoreValidation
from persephone_client.domain.schemas.sphinx.score_validation_status.schema import ScoreValidationStatus
from persephone_client.domain.schemas.sphinx.user_exchange_account_status.schema import UserExchangeAccountStatus

from persephone_client.domain.schemas.sphinx.dtvm_user.schema import DtvmUserSchema
from persephone_client.domain.schemas.sphinx.dtvm_update_user.schema import DtvmUpdateUserSchema
from persephone_client.domain.schemas.sphinx.prospect_user.schema import ProspectUserSchema
from persephone_client.domain.schemas.sphinx.suitability.schema import SuitabilitySchema
from persephone_client.domain.schemas.sphinx.user_authentication.schema import UserAuthenticationSchema
from persephone_client.domain.schemas.sphinx.user_exchange_account.schema import UserExchangeAccount
from persephone_client.domain.schemas.sphinx.user_thebes_hall.schema import UserThebesHallSchema
from persephone_client.domain.schemas.sphinx.user_logout.schema import UserLogoutSchema
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
from persephone_client.domain.schemas.sphinx.user_document.schema import UserDocumentSchema
from persephone_client.domain.schemas.sphinx.user_politically_exposed_us.schema import UserPoliticallyExposedUsSchema
from persephone_client.domain.schemas.sphinx.user_exchange_member_us.schema import UserExchangeMemberUsSchema
from persephone_client.domain.schemas.sphinx.user_time_experience_us.schema import UserTimeExperienceUsSchema
from persephone_client.domain.schemas.sphinx.user_company_director_us.schema import UserCompanyDirectorUsSchema
from persephone_client.domain.schemas.sphinx.signed_term.schema import SignedTermSchema
from persephone_client.domain.schemas.sphinx.user_tax_residences_us.schema import UserTaxResidencesUsSchema
from persephone_client.domain.schemas.sphinx.user_w8_form_confirmation_us.schema import UserW8FormConfirmationUsSchema
from persephone_client.domain.schemas.sphinx.user_employ_form.schema import UserEmployFormSchema

from persephone_client.domain.schemas.hermes.mist_trade_session_create.schema import MistTradeSessionCreate
from persephone_client.domain.schemas.hermes.hermes_session_integrity.schema import HermesSessionIntegrity
from persephone_client.domain.schemas.hermes.hermes_session_authenticity.schema import HermesSessionAuthenticity
from persephone_client.domain.schemas.hermes.sent_orders.schema import SentOrders
from persephone_client.domain.schemas.hermes.report_orders.schema import ReportOrders
from persephone_client.domain.schemas.hermes.received_orders.schema import ReceivedOrders

from persephone_client.domain.schemas.ebisu import (
    RegisterClientBankAccount,
    UpdateUserBankAccounts,
    DeleteClientBankAccount,
)
from persephone_client.domain.schemas.mapinguari.user_update.schema import MapinguariUserUpdate


class ChooseSchema(Enum):
    # SPHINX
    dtvm_user_schema = DtvmUserSchema
    dtvm_update_user_schema = DtvmUpdateUserSchema
    prospect_user_schema = ProspectUserSchema
    suitability_schema = SuitabilitySchema
    user_authentication_schema = UserAuthenticationSchema
    user_thebes_hall_schema = UserThebesHallSchema
    user_logout_schema = UserLogoutSchema
    user_identifier_data_schema = UserIdentifierDataSchema
    user_selfie_schema = UserSelfieSchema
    user_complementary_data_schema = UserComplementaryDataSchema
    user_update_register_data_schema = UserUpdateRegisterDataSchema
    user_set_electronic_signature_schema = UserSetElectronicSignatureSchema
    user_change_or_reset_electronic_signature_schema = UserChangeOrResetElectronicSignatureSchema
    create_electronic_signature_session_schema = CreateElectronicSignatureSessionSchema
    user_document_schema = UserDocumentSchema
    user_politically_exposed_us_schema = UserPoliticallyExposedUsSchema
    user_exchange_member_us_schema = UserExchangeMemberUsSchema
    user_time_experience_us_schema = UserTimeExperienceUsSchema
    user_company_director_us_schema = UserCompanyDirectorUsSchema
    signed_term_schema = SignedTermSchema
    user_tax_residences_us_schema = UserTaxResidencesUsSchema
    user_w8_form_confirmation_us_schema = UserW8FormConfirmationUsSchema
    user_employ_form = UserEmployFormSchema
    user_exchange_account = UserExchangeAccount
    user_exchange_account_status = UserExchangeAccountStatus
    cpf_validation = CpfValidation
    cpf_validation_status = CpfValidationStatus
    score_validation = ScoreValidation
    score_validation_status = ScoreValidationStatus
    picpay_user_data = PicpayUserData
    pld = Pld

    # HERMES
    hermes_session_integrity = HermesSessionIntegrity
    hermes_session_authenticity = HermesSessionAuthenticity
    mist_trade_session_create = MistTradeSessionCreate
    sent_orders = SentOrders
    report_orders = ReportOrders
    received_orders = ReceivedOrders

    # EBISU
    register_client_bank_account = RegisterClientBankAccount
    update_client_bank_account = UpdateUserBankAccounts
    delete_client_bank_account = DeleteClientBankAccount
    cash_flow_withdrawal_to_external_bank = CashFlowWithdrawalToExternalBank
    exchange_proposal_simulation = ExchangeProposalSimulation
    exchange_proposal_pre_execution = ExchangeProposalPreExecution
    exchange_proposal_execution = ExchangeProposalExecution

    # JORMUNGADR
    get_order_token_variable_income = GetOrderTokenVariableIncome
    get_order_token_fixed_income = GetOrderTokenFixedIncome

    # MAPINGUARI
    mapinguari_user_update = MapinguariUserUpdate
