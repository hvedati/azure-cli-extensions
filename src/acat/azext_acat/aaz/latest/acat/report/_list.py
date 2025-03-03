# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "acat report list",
)
class List(AAZCommand):
    """List the AppComplianceAutomation report list for the tenant.

    :example: Report_List
        az acat report list --skip-token 1 --top 100 --offer-guid 00000000-0000-0000-0000-000000000000 --tenant 00000000-0000-0000-0000-000000000000
        az acat report list
    """

    _aaz_info = {
        "version": "2024-06-27",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.appcomplianceautomation/reports", "2024-06-27"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="The filter to apply on the operation.",
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        _args_schema.offer_guid = AAZStrArg(
            options=["--offer-guid"],
            help="The offerGuid which mapping to the reports.",
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        _args_schema.orderby = AAZStrArg(
            options=["--orderby"],
            help="OData order by query option.",
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        _args_schema.tenant = AAZStrArg(
            options=["--tenant"],
            help="The tenant id of the report creator.",
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        _args_schema.select = AAZStrArg(
            options=["--select"],
            help="OData Select statement. Limits the properties on each entry to just those requested, e.g. ?$select=reportName,id.",
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        _args_schema.skip_token = AAZStrArg(
            options=["--skip-token"],
            help="Skip over when retrieving results.",
        )
        _args_schema.top = AAZIntArg(
            options=["--top"],
            help="Number of elements to return when retrieving results.",
            fmt=AAZIntArgFormat(
                maximum=100,
                minimum=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ReportList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class ReportList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.AppComplianceAutomation/reports",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "$orderby", self.ctx.args.orderby,
                ),
                **self.serialize_query_param(
                    "$select", self.ctx.args.select,
                ),
                **self.serialize_query_param(
                    "$skipToken", self.ctx.args.skip_token,
                ),
                **self.serialize_query_param(
                    "$top", self.ctx.args.top,
                ),
                **self.serialize_query_param(
                    "offerGuid", self.ctx.args.offer_guid,
                ),
                **self.serialize_query_param(
                    "reportCreatorTenantId", self.ctx.args.tenant,
                ),
                **self.serialize_query_param(
                    "api-version", "2024-06-27",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.cert_records = AAZListType(
                serialized_name="certRecords",
                flags={"read_only": True},
            )
            properties.compliance_status = AAZObjectType(
                serialized_name="complianceStatus",
                flags={"read_only": True},
            )
            properties.errors = AAZListType(
                flags={"read_only": True},
            )
            properties.last_trigger_time = AAZStrType(
                serialized_name="lastTriggerTime",
                flags={"read_only": True},
            )
            properties.next_trigger_time = AAZStrType(
                serialized_name="nextTriggerTime",
                flags={"read_only": True},
            )
            properties.offer_guid = AAZStrType(
                serialized_name="offerGuid",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resources = AAZListType(
                flags={"required": True},
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )
            properties.storage_info = AAZObjectType(
                serialized_name="storageInfo",
            )
            properties.subscriptions = AAZListType(
                flags={"read_only": True},
            )
            properties.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            properties.time_zone = AAZStrType(
                serialized_name="timeZone",
                flags={"required": True},
            )
            properties.trigger_time = AAZStrType(
                serialized_name="triggerTime",
                flags={"required": True},
            )

            cert_records = cls._schema_on_200.value.Element.properties.cert_records
            cert_records.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.cert_records.Element
            _element.certification_status = AAZStrType(
                serialized_name="certificationStatus",
            )
            _element.controls = AAZListType()
            _element.ingestion_status = AAZStrType(
                serialized_name="ingestionStatus",
            )
            _element.offer_guid = AAZStrType(
                serialized_name="offerGuid",
            )

            controls = cls._schema_on_200.value.Element.properties.cert_records.Element.controls
            controls.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.cert_records.Element.controls.Element
            _element.control_id = AAZStrType(
                serialized_name="controlId",
            )
            _element.control_status = AAZStrType(
                serialized_name="controlStatus",
            )

            compliance_status = cls._schema_on_200.value.Element.properties.compliance_status
            compliance_status.m365 = AAZObjectType(
                flags={"read_only": True},
            )

            m365 = cls._schema_on_200.value.Element.properties.compliance_status.m365
            m365.failed_count = AAZIntType(
                serialized_name="failedCount",
                flags={"read_only": True},
            )
            m365.manual_count = AAZIntType(
                serialized_name="manualCount",
                flags={"read_only": True},
            )
            m365.not_applicable_count = AAZIntType(
                serialized_name="notApplicableCount",
                flags={"read_only": True},
            )
            m365.passed_count = AAZIntType(
                serialized_name="passedCount",
                flags={"read_only": True},
            )
            m365.pending_count = AAZIntType(
                serialized_name="pendingCount",
                flags={"read_only": True},
            )

            errors = cls._schema_on_200.value.Element.properties.errors
            errors.Element = AAZStrType()

            resources = cls._schema_on_200.value.Element.properties.resources
            resources.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.resources.Element
            _element.account_id = AAZStrType(
                serialized_name="accountId",
            )
            _element.resource_id = AAZStrType(
                serialized_name="resourceId",
                flags={"required": True},
            )
            _element.resource_kind = AAZStrType(
                serialized_name="resourceKind",
            )
            _element.resource_origin = AAZStrType(
                serialized_name="resourceOrigin",
            )
            _element.resource_type = AAZStrType(
                serialized_name="resourceType",
            )

            storage_info = cls._schema_on_200.value.Element.properties.storage_info
            storage_info.account_name = AAZStrType(
                serialized_name="accountName",
            )
            storage_info.location = AAZStrType()
            storage_info.resource_group = AAZStrType(
                serialized_name="resourceGroup",
            )
            storage_info.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
            )

            subscriptions = cls._schema_on_200.value.Element.properties.subscriptions
            subscriptions.Element = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
