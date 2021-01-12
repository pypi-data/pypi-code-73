# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2021.01.12
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from agilicus_api.configuration import Configuration


class Organisation(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'all_users_group_id': 'str',
        'all_users_all_suborgs_group_id': 'str',
        'all_users_direct_suborgs_group_id': 'str',
        'auto_created_users_group_id': 'str',
        'external_id': 'str',
        'organisation': 'str',
        'issuer': 'str',
        'issuer_id': 'str',
        'subdomain': 'str',
        'created': 'datetime',
        'updated': 'datetime',
        'contact_id': 'str',
        'contact_email': 'str',
        'parent_id': 'str',
        'root_org_id': 'str',
        'auto_create': 'bool',
        'trust_on_first_use_duration': 'int',
        'feature_flags': 'list[FeatureFlag]',
        'admin_state': 'OrganisationStateSelector',
        'status': 'OrganisationStatus'
    }

    attribute_map = {
        'id': 'id',
        'all_users_group_id': 'all_users_group_id',
        'all_users_all_suborgs_group_id': 'all_users_all_suborgs_group_id',
        'all_users_direct_suborgs_group_id': 'all_users_direct_suborgs_group_id',
        'auto_created_users_group_id': 'auto_created_users_group_id',
        'external_id': 'external_id',
        'organisation': 'organisation',
        'issuer': 'issuer',
        'issuer_id': 'issuer_id',
        'subdomain': 'subdomain',
        'created': 'created',
        'updated': 'updated',
        'contact_id': 'contact_id',
        'contact_email': 'contact_email',
        'parent_id': 'parent_id',
        'root_org_id': 'root_org_id',
        'auto_create': 'auto_create',
        'trust_on_first_use_duration': 'trust_on_first_use_duration',
        'feature_flags': 'feature_flags',
        'admin_state': 'admin_state',
        'status': 'status'
    }

    def __init__(self, id=None, all_users_group_id=None, all_users_all_suborgs_group_id=None, all_users_direct_suborgs_group_id=None, auto_created_users_group_id=None, external_id=None, organisation=None, issuer=None, issuer_id=None, subdomain=None, created=None, updated=None, contact_id=None, contact_email=None, parent_id=None, root_org_id=None, auto_create=True, trust_on_first_use_duration=86400, feature_flags=None, admin_state=None, status=None, local_vars_configuration=None):  # noqa: E501
        """Organisation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._all_users_group_id = None
        self._all_users_all_suborgs_group_id = None
        self._all_users_direct_suborgs_group_id = None
        self._auto_created_users_group_id = None
        self._external_id = None
        self._organisation = None
        self._issuer = None
        self._issuer_id = None
        self._subdomain = None
        self._created = None
        self._updated = None
        self._contact_id = None
        self._contact_email = None
        self._parent_id = None
        self._root_org_id = None
        self._auto_create = None
        self._trust_on_first_use_duration = None
        self._feature_flags = None
        self._admin_state = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if all_users_group_id is not None:
            self.all_users_group_id = all_users_group_id
        if all_users_all_suborgs_group_id is not None:
            self.all_users_all_suborgs_group_id = all_users_all_suborgs_group_id
        if all_users_direct_suborgs_group_id is not None:
            self.all_users_direct_suborgs_group_id = all_users_direct_suborgs_group_id
        if auto_created_users_group_id is not None:
            self.auto_created_users_group_id = auto_created_users_group_id
        if external_id is not None:
            self.external_id = external_id
        if organisation is not None:
            self.organisation = organisation
        if issuer is not None:
            self.issuer = issuer
        if issuer_id is not None:
            self.issuer_id = issuer_id
        if subdomain is not None:
            self.subdomain = subdomain
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if contact_id is not None:
            self.contact_id = contact_id
        if contact_email is not None:
            self.contact_email = contact_email
        if parent_id is not None:
            self.parent_id = parent_id
        if root_org_id is not None:
            self.root_org_id = root_org_id
        if auto_create is not None:
            self.auto_create = auto_create
        if trust_on_first_use_duration is not None:
            self.trust_on_first_use_duration = trust_on_first_use_duration
        if feature_flags is not None:
            self.feature_flags = feature_flags
        if admin_state is not None:
            self.admin_state = admin_state
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this Organisation.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The id of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Organisation.

        Unique identifier  # noqa: E501

        :param id: The id of this Organisation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def all_users_group_id(self):
        """Gets the all_users_group_id of this Organisation.  # noqa: E501

        group id of group containing this organisations all users  # noqa: E501

        :return: The all_users_group_id of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._all_users_group_id

    @all_users_group_id.setter
    def all_users_group_id(self, all_users_group_id):
        """Sets the all_users_group_id of this Organisation.

        group id of group containing this organisations all users  # noqa: E501

        :param all_users_group_id: The all_users_group_id of this Organisation.  # noqa: E501
        :type: str
        """

        self._all_users_group_id = all_users_group_id

    @property
    def all_users_all_suborgs_group_id(self):
        """Gets the all_users_all_suborgs_group_id of this Organisation.  # noqa: E501

        group id of group containing this organisations all users including all sub organisations  # noqa: E501

        :return: The all_users_all_suborgs_group_id of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._all_users_all_suborgs_group_id

    @all_users_all_suborgs_group_id.setter
    def all_users_all_suborgs_group_id(self, all_users_all_suborgs_group_id):
        """Sets the all_users_all_suborgs_group_id of this Organisation.

        group id of group containing this organisations all users including all sub organisations  # noqa: E501

        :param all_users_all_suborgs_group_id: The all_users_all_suborgs_group_id of this Organisation.  # noqa: E501
        :type: str
        """

        self._all_users_all_suborgs_group_id = all_users_all_suborgs_group_id

    @property
    def all_users_direct_suborgs_group_id(self):
        """Gets the all_users_direct_suborgs_group_id of this Organisation.  # noqa: E501

        group id of group containing this organisations all users including only direct sub organisations  # noqa: E501

        :return: The all_users_direct_suborgs_group_id of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._all_users_direct_suborgs_group_id

    @all_users_direct_suborgs_group_id.setter
    def all_users_direct_suborgs_group_id(self, all_users_direct_suborgs_group_id):
        """Sets the all_users_direct_suborgs_group_id of this Organisation.

        group id of group containing this organisations all users including only direct sub organisations  # noqa: E501

        :param all_users_direct_suborgs_group_id: The all_users_direct_suborgs_group_id of this Organisation.  # noqa: E501
        :type: str
        """

        self._all_users_direct_suborgs_group_id = all_users_direct_suborgs_group_id

    @property
    def auto_created_users_group_id(self):
        """Gets the auto_created_users_group_id of this Organisation.  # noqa: E501

        group id of group containing users automatically created when they logged in  # noqa: E501

        :return: The auto_created_users_group_id of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._auto_created_users_group_id

    @auto_created_users_group_id.setter
    def auto_created_users_group_id(self, auto_created_users_group_id):
        """Sets the auto_created_users_group_id of this Organisation.

        group id of group containing users automatically created when they logged in  # noqa: E501

        :param auto_created_users_group_id: The auto_created_users_group_id of this Organisation.  # noqa: E501
        :type: str
        """

        self._auto_created_users_group_id = auto_created_users_group_id

    @property
    def external_id(self):
        """Gets the external_id of this Organisation.  # noqa: E501

        External unique identifier  # noqa: E501

        :return: The external_id of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Organisation.

        External unique identifier  # noqa: E501

        :param external_id: The external_id of this Organisation.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                external_id is not None and len(external_id) > 100):
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `100`")  # noqa: E501

        self._external_id = external_id

    @property
    def organisation(self):
        """Gets the organisation of this Organisation.  # noqa: E501

        organisation name  # noqa: E501

        :return: The organisation of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this Organisation.

        organisation name  # noqa: E501

        :param organisation: The organisation of this Organisation.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                organisation is not None and len(organisation) > 100):
            raise ValueError("Invalid value for `organisation`, length must be less than or equal to `100`")  # noqa: E501

        self._organisation = organisation

    @property
    def issuer(self):
        """Gets the issuer of this Organisation.  # noqa: E501

        connect id issuer  # noqa: E501

        :return: The issuer of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this Organisation.

        connect id issuer  # noqa: E501

        :param issuer: The issuer of this Organisation.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                issuer is not None and len(issuer) > 100):
            raise ValueError("Invalid value for `issuer`, length must be less than or equal to `100`")  # noqa: E501

        self._issuer = issuer

    @property
    def issuer_id(self):
        """Gets the issuer_id of this Organisation.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The issuer_id of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this Organisation.

        Unique identifier  # noqa: E501

        :param issuer_id: The issuer_id of this Organisation.  # noqa: E501
        :type: str
        """

        self._issuer_id = issuer_id

    @property
    def subdomain(self):
        """Gets the subdomain of this Organisation.  # noqa: E501

        Organisations subdomain. Note this must be unique accross all organisations  # noqa: E501

        :return: The subdomain of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """Sets the subdomain of this Organisation.

        Organisations subdomain. Note this must be unique accross all organisations  # noqa: E501

        :param subdomain: The subdomain of this Organisation.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                subdomain is not None and len(subdomain) > 100):
            raise ValueError("Invalid value for `subdomain`, length must be less than or equal to `100`")  # noqa: E501

        self._subdomain = subdomain

    @property
    def created(self):
        """Gets the created of this Organisation.  # noqa: E501

        Creation time  # noqa: E501

        :return: The created of this Organisation.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Organisation.

        Creation time  # noqa: E501

        :param created: The created of this Organisation.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this Organisation.  # noqa: E501

        Update time  # noqa: E501

        :return: The updated of this Organisation.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Organisation.

        Update time  # noqa: E501

        :param updated: The updated of this Organisation.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def contact_id(self):
        """Gets the contact_id of this Organisation.  # noqa: E501

        GUID of the organisation admin  # noqa: E501

        :return: The contact_id of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this Organisation.

        GUID of the organisation admin  # noqa: E501

        :param contact_id: The contact_id of this Organisation.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def contact_email(self):
        """Gets the contact_email of this Organisation.  # noqa: E501

        The email address of the contact.  # noqa: E501

        :return: The contact_email of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this Organisation.

        The email address of the contact.  # noqa: E501

        :param contact_email: The contact_email of this Organisation.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                contact_email is not None and len(contact_email) > 100):
            raise ValueError("Invalid value for `contact_email`, length must be less than or equal to `100`")  # noqa: E501

        self._contact_email = contact_email

    @property
    def parent_id(self):
        """Gets the parent_id of this Organisation.  # noqa: E501

        parent organisation id  # noqa: E501

        :return: The parent_id of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Organisation.

        parent organisation id  # noqa: E501

        :param parent_id: The parent_id of this Organisation.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def root_org_id(self):
        """Gets the root_org_id of this Organisation.  # noqa: E501

        The id of the organisation at the root of this organisation hierarchy. For example, if A is the parent of B, and B is the parent of C, then A would be the root organisation of A, B and C. Note that this field will be ignored if changed.   # noqa: E501

        :return: The root_org_id of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._root_org_id

    @root_org_id.setter
    def root_org_id(self, root_org_id):
        """Sets the root_org_id of this Organisation.

        The id of the organisation at the root of this organisation hierarchy. For example, if A is the parent of B, and B is the parent of C, then A would be the root organisation of A, B and C. Note that this field will be ignored if changed.   # noqa: E501

        :param root_org_id: The root_org_id of this Organisation.  # noqa: E501
        :type: str
        """

        self._root_org_id = root_org_id

    @property
    def auto_create(self):
        """Gets the auto_create of this Organisation.  # noqa: E501

        Auto-creates a user  # noqa: E501

        :return: The auto_create of this Organisation.  # noqa: E501
        :rtype: bool
        """
        return self._auto_create

    @auto_create.setter
    def auto_create(self, auto_create):
        """Sets the auto_create of this Organisation.

        Auto-creates a user  # noqa: E501

        :param auto_create: The auto_create of this Organisation.  # noqa: E501
        :type: bool
        """

        self._auto_create = auto_create

    @property
    def trust_on_first_use_duration(self):
        """Gets the trust_on_first_use_duration of this Organisation.  # noqa: E501

        The time window in seconds which represents the period of time for which a new user is eligible for trust on first use enrollment. The duration will be applied from the user's created date, or if the user's enrollment period was reset by an administrator.   # noqa: E501

        :return: The trust_on_first_use_duration of this Organisation.  # noqa: E501
        :rtype: int
        """
        return self._trust_on_first_use_duration

    @trust_on_first_use_duration.setter
    def trust_on_first_use_duration(self, trust_on_first_use_duration):
        """Sets the trust_on_first_use_duration of this Organisation.

        The time window in seconds which represents the period of time for which a new user is eligible for trust on first use enrollment. The duration will be applied from the user's created date, or if the user's enrollment period was reset by an administrator.   # noqa: E501

        :param trust_on_first_use_duration: The trust_on_first_use_duration of this Organisation.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                trust_on_first_use_duration is not None and trust_on_first_use_duration < 0):  # noqa: E501
            raise ValueError("Invalid value for `trust_on_first_use_duration`, must be a value greater than or equal to `0`")  # noqa: E501

        self._trust_on_first_use_duration = trust_on_first_use_duration

    @property
    def feature_flags(self):
        """Gets the feature_flags of this Organisation.  # noqa: E501

        A list of features to enable or disable. This is mostly for advanced use. No guarantees exist that a given feature will always exist by a given name, or that it will be configurable.   # noqa: E501

        :return: The feature_flags of this Organisation.  # noqa: E501
        :rtype: list[FeatureFlag]
        """
        return self._feature_flags

    @feature_flags.setter
    def feature_flags(self, feature_flags):
        """Sets the feature_flags of this Organisation.

        A list of features to enable or disable. This is mostly for advanced use. No guarantees exist that a given feature will always exist by a given name, or that it will be configurable.   # noqa: E501

        :param feature_flags: The feature_flags of this Organisation.  # noqa: E501
        :type: list[FeatureFlag]
        """

        self._feature_flags = feature_flags

    @property
    def admin_state(self):
        """Gets the admin_state of this Organisation.  # noqa: E501


        :return: The admin_state of this Organisation.  # noqa: E501
        :rtype: OrganisationStateSelector
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this Organisation.


        :param admin_state: The admin_state of this Organisation.  # noqa: E501
        :type: OrganisationStateSelector
        """

        self._admin_state = admin_state

    @property
    def status(self):
        """Gets the status of this Organisation.  # noqa: E501


        :return: The status of this Organisation.  # noqa: E501
        :rtype: OrganisationStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Organisation.


        :param status: The status of this Organisation.  # noqa: E501
        :type: OrganisationStatus
        """

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Organisation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Organisation):
            return True

        return self.to_dict() != other.to_dict()
