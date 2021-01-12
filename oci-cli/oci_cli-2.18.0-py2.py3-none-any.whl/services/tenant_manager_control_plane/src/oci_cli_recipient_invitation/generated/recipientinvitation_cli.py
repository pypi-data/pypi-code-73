# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.tenant_manager_control_plane.src.oci_cli_tenant_manager_control_plane.generated import organizations_service_cli


@click.command(cli_util.override('recipient_invitation.recipient_invitation_root_group.command_name', 'recipient-invitation'), cls=CommandGroupWithAlias, help=cli_util.override('recipient_invitation.recipient_invitation_root_group.help', """A description of the TenantManager API"""), short_help=cli_util.override('recipient_invitation.recipient_invitation_root_group.short_help', """TenantManager API"""))
@cli_util.help_option_group
def recipient_invitation_root_group():
    pass


@click.command(cli_util.override('recipient_invitation.recipient_invitation_group.command_name', 'recipient-invitation'), cls=CommandGroupWithAlias, help="""The invitation model that the recipient owns.""")
@cli_util.help_option_group
def recipient_invitation_group():
    pass


organizations_service_cli.organizations_service_group.add_command(recipient_invitation_root_group)
recipient_invitation_root_group.add_command(recipient_invitation_group)


@recipient_invitation_group.command(name=cli_util.override('recipient_invitation.accept_recipient_invitation.command_name', 'accept'), help=u"""Accepts a recipient invitation. \n[Command Reference](acceptRecipientInvitation)""")
@cli_util.option('--recipient-invitation-id', required=True, help=u"""OCID of recipient invitation to accept.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def accept_recipient_invitation(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, recipient_invitation_id, if_match):

    if isinstance(recipient_invitation_id, six.string_types) and len(recipient_invitation_id.strip()) == 0:
        raise click.UsageError('Parameter --recipient-invitation-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'recipient_invitation', ctx)
    result = client.accept_recipient_invitation(
        recipient_invitation_id=recipient_invitation_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@recipient_invitation_group.command(name=cli_util.override('recipient_invitation.get_recipient_invitation.command_name', 'get'), help=u"""Gets information about the recipient invitation. \n[Command Reference](getRecipientInvitation)""")
@cli_util.option('--recipient-invitation-id', required=True, help=u"""OCID of the recipient invitation to retrieve.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'RecipientInvitation'})
@cli_util.wrap_exceptions
def get_recipient_invitation(ctx, from_json, recipient_invitation_id):

    if isinstance(recipient_invitation_id, six.string_types) and len(recipient_invitation_id.strip()) == 0:
        raise click.UsageError('Parameter --recipient-invitation-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'recipient_invitation', ctx)
    result = client.get_recipient_invitation(
        recipient_invitation_id=recipient_invitation_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@recipient_invitation_group.command(name=cli_util.override('recipient_invitation.ignore_recipient_invitation.command_name', 'ignore'), help=u"""Ignores a recipient invitation. \n[Command Reference](ignoreRecipientInvitation)""")
@cli_util.option('--recipient-invitation-id', required=True, help=u"""OCID of recipient invitation to ignore.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'RecipientInvitation'})
@cli_util.wrap_exceptions
def ignore_recipient_invitation(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, recipient_invitation_id, if_match):

    if isinstance(recipient_invitation_id, six.string_types) and len(recipient_invitation_id.strip()) == 0:
        raise click.UsageError('Parameter --recipient-invitation-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'recipient_invitation', ctx)
    result = client.ignore_recipient_invitation(
        recipient_invitation_id=recipient_invitation_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_recipient_invitation') and callable(getattr(client, 'get_recipient_invitation')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_recipient_invitation(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@recipient_invitation_group.command(name=cli_util.override('recipient_invitation.list_recipient_invitations.command_name', 'list'), help=u"""Return a (paginated) list of recipient invitations. \n[Command Reference](listRecipientInvitations)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--sender-tenancy-id', help=u"""The tenancy that sent the invitation.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "TERMINATED"]), help=u"""The lifecycle state of the resource.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["PENDING", "CANCELED", "ACCEPTED", "IGNORED", "EXPIRED", "FAILED"]), help=u"""The status of the recipient invitation.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'tenant_manager_control_plane', 'class': 'RecipientInvitationCollection'})
@cli_util.wrap_exceptions
def list_recipient_invitations(ctx, from_json, all_pages, compartment_id, sender_tenancy_id, lifecycle_state, status, page):

    kwargs = {}
    if sender_tenancy_id is not None:
        kwargs['sender_tenancy_id'] = sender_tenancy_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if status is not None:
        kwargs['status'] = status
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('tenant_manager_control_plane', 'recipient_invitation', ctx)
    if all_pages:
        result = cli_util.list_call_get_all_results(
            client.list_recipient_invitations,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_recipient_invitations(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@recipient_invitation_group.command(name=cli_util.override('recipient_invitation.update_recipient_invitation.command_name', 'update'), help=u"""Updates the RecipientInvitation. \n[Command Reference](updateRecipientInvitation)""")
@cli_util.option('--recipient-invitation-id', required=True, help=u"""OCID of the recipient invitation to update.""")
@cli_util.option('--display-name', help=u"""A user-created name to describe the invitation.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "TERMINATED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'tenant_manager_control_plane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'tenant_manager_control_plane', 'class': 'RecipientInvitation'})
@cli_util.wrap_exceptions
def update_recipient_invitation(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, recipient_invitation_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(recipient_invitation_id, six.string_types) and len(recipient_invitation_id.strip()) == 0:
        raise click.UsageError('Parameter --recipient-invitation-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('tenant_manager_control_plane', 'recipient_invitation', ctx)
    result = client.update_recipient_invitation(
        recipient_invitation_id=recipient_invitation_id,
        update_recipient_invitation_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_recipient_invitation') and callable(getattr(client, 'get_recipient_invitation')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_recipient_invitation(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
