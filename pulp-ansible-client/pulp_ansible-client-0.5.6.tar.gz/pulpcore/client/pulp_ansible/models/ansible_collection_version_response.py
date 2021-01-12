# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_ansible.configuration import Configuration


class AnsibleCollectionVersionResponse(object):
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
        'pulp_created': 'datetime',
        'pulp_href': 'str',
        'artifact': 'str',
        'md5': 'str',
        'sha1': 'str',
        'sha224': 'str',
        'sha256': 'str',
        'sha384': 'str',
        'sha512': 'str',
        'id': 'str',
        'authors': 'list[str]',
        'contents': 'list[object]',
        'dependencies': 'object',
        'description': 'str',
        'docs_blob': 'object',
        'documentation': 'str',
        'homepage': 'str',
        'issues': 'str',
        'license': 'list[str]',
        'name': 'str',
        'namespace': 'str',
        'repository': 'str',
        'tags': 'list[AnsibleTagResponse]',
        'version': 'str'
    }

    attribute_map = {
        'pulp_created': 'pulp_created',
        'pulp_href': 'pulp_href',
        'artifact': 'artifact',
        'md5': 'md5',
        'sha1': 'sha1',
        'sha224': 'sha224',
        'sha256': 'sha256',
        'sha384': 'sha384',
        'sha512': 'sha512',
        'id': 'id',
        'authors': 'authors',
        'contents': 'contents',
        'dependencies': 'dependencies',
        'description': 'description',
        'docs_blob': 'docs_blob',
        'documentation': 'documentation',
        'homepage': 'homepage',
        'issues': 'issues',
        'license': 'license',
        'name': 'name',
        'namespace': 'namespace',
        'repository': 'repository',
        'tags': 'tags',
        'version': 'version'
    }

    def __init__(self, pulp_created=None, pulp_href=None, artifact=None, md5=None, sha1=None, sha224=None, sha256=None, sha384=None, sha512=None, id=None, authors=None, contents=None, dependencies=None, description=None, docs_blob=None, documentation=None, homepage=None, issues=None, license=None, name=None, namespace=None, repository=None, tags=None, version=None, local_vars_configuration=None):  # noqa: E501
        """AnsibleCollectionVersionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_created = None
        self._pulp_href = None
        self._artifact = None
        self._md5 = None
        self._sha1 = None
        self._sha224 = None
        self._sha256 = None
        self._sha384 = None
        self._sha512 = None
        self._id = None
        self._authors = None
        self._contents = None
        self._dependencies = None
        self._description = None
        self._docs_blob = None
        self._documentation = None
        self._homepage = None
        self._issues = None
        self._license = None
        self._name = None
        self._namespace = None
        self._repository = None
        self._tags = None
        self._version = None
        self.discriminator = None

        if pulp_created is not None:
            self.pulp_created = pulp_created
        if pulp_href is not None:
            self.pulp_href = pulp_href
        self.artifact = artifact
        if md5 is not None:
            self.md5 = md5
        if sha1 is not None:
            self.sha1 = sha1
        if sha224 is not None:
            self.sha224 = sha224
        if sha256 is not None:
            self.sha256 = sha256
        if sha384 is not None:
            self.sha384 = sha384
        if sha512 is not None:
            self.sha512 = sha512
        self.id = id
        self.authors = authors
        self.contents = contents
        self.dependencies = dependencies
        self.description = description
        self.docs_blob = docs_blob
        self.documentation = documentation
        self.homepage = homepage
        self.issues = issues
        self.license = license
        self.name = name
        self.namespace = namespace
        self.repository = repository
        if tags is not None:
            self.tags = tags
        self.version = version

    @property
    def pulp_created(self):
        """Gets the pulp_created of this AnsibleCollectionVersionResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this AnsibleCollectionVersionResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def pulp_href(self):
        """Gets the pulp_href of this AnsibleCollectionVersionResponse.  # noqa: E501


        :return: The pulp_href of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this AnsibleCollectionVersionResponse.


        :param pulp_href: The pulp_href of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def artifact(self):
        """Gets the artifact of this AnsibleCollectionVersionResponse.  # noqa: E501

        Artifact file representing the physical content  # noqa: E501

        :return: The artifact of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this AnsibleCollectionVersionResponse.

        Artifact file representing the physical content  # noqa: E501

        :param artifact: The artifact of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and artifact is None:  # noqa: E501
            raise ValueError("Invalid value for `artifact`, must not be `None`")  # noqa: E501

        self._artifact = artifact

    @property
    def md5(self):
        """Gets the md5 of this AnsibleCollectionVersionResponse.  # noqa: E501

        The MD5 checksum if available.  # noqa: E501

        :return: The md5 of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this AnsibleCollectionVersionResponse.

        The MD5 checksum if available.  # noqa: E501

        :param md5: The md5 of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """

        self._md5 = md5

    @property
    def sha1(self):
        """Gets the sha1 of this AnsibleCollectionVersionResponse.  # noqa: E501

        The SHA-1 checksum if available.  # noqa: E501

        :return: The sha1 of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._sha1

    @sha1.setter
    def sha1(self, sha1):
        """Sets the sha1 of this AnsibleCollectionVersionResponse.

        The SHA-1 checksum if available.  # noqa: E501

        :param sha1: The sha1 of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """

        self._sha1 = sha1

    @property
    def sha224(self):
        """Gets the sha224 of this AnsibleCollectionVersionResponse.  # noqa: E501

        The SHA-224 checksum if available.  # noqa: E501

        :return: The sha224 of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._sha224

    @sha224.setter
    def sha224(self, sha224):
        """Sets the sha224 of this AnsibleCollectionVersionResponse.

        The SHA-224 checksum if available.  # noqa: E501

        :param sha224: The sha224 of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """

        self._sha224 = sha224

    @property
    def sha256(self):
        """Gets the sha256 of this AnsibleCollectionVersionResponse.  # noqa: E501

        The SHA-256 checksum if available.  # noqa: E501

        :return: The sha256 of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this AnsibleCollectionVersionResponse.

        The SHA-256 checksum if available.  # noqa: E501

        :param sha256: The sha256 of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """

        self._sha256 = sha256

    @property
    def sha384(self):
        """Gets the sha384 of this AnsibleCollectionVersionResponse.  # noqa: E501

        The SHA-384 checksum if available.  # noqa: E501

        :return: The sha384 of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._sha384

    @sha384.setter
    def sha384(self, sha384):
        """Sets the sha384 of this AnsibleCollectionVersionResponse.

        The SHA-384 checksum if available.  # noqa: E501

        :param sha384: The sha384 of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """

        self._sha384 = sha384

    @property
    def sha512(self):
        """Gets the sha512 of this AnsibleCollectionVersionResponse.  # noqa: E501

        The SHA-512 checksum if available.  # noqa: E501

        :return: The sha512 of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._sha512

    @sha512.setter
    def sha512(self, sha512):
        """Sets the sha512 of this AnsibleCollectionVersionResponse.

        The SHA-512 checksum if available.  # noqa: E501

        :param sha512: The sha512 of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """

        self._sha512 = sha512

    @property
    def id(self):
        """Gets the id of this AnsibleCollectionVersionResponse.  # noqa: E501

        A collection identifier.  # noqa: E501

        :return: The id of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnsibleCollectionVersionResponse.

        A collection identifier.  # noqa: E501

        :param id: The id of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def authors(self):
        """Gets the authors of this AnsibleCollectionVersionResponse.  # noqa: E501

        A list of the CollectionVersion content's authors.  # noqa: E501

        :return: The authors of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """Sets the authors of this AnsibleCollectionVersionResponse.

        A list of the CollectionVersion content's authors.  # noqa: E501

        :param authors: The authors of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and authors is None:  # noqa: E501
            raise ValueError("Invalid value for `authors`, must not be `None`")  # noqa: E501

        self._authors = authors

    @property
    def contents(self):
        """Gets the contents of this AnsibleCollectionVersionResponse.  # noqa: E501

        A JSON field with data about the contents.  # noqa: E501

        :return: The contents of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: list[object]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this AnsibleCollectionVersionResponse.

        A JSON field with data about the contents.  # noqa: E501

        :param contents: The contents of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: list[object]
        """
        if self.local_vars_configuration.client_side_validation and contents is None:  # noqa: E501
            raise ValueError("Invalid value for `contents`, must not be `None`")  # noqa: E501

        self._contents = contents

    @property
    def dependencies(self):
        """Gets the dependencies of this AnsibleCollectionVersionResponse.  # noqa: E501

        A dict declaring Collections that this collection requires to be installed for it to be usable.  # noqa: E501

        :return: The dependencies of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: object
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this AnsibleCollectionVersionResponse.

        A dict declaring Collections that this collection requires to be installed for it to be usable.  # noqa: E501

        :param dependencies: The dependencies of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and dependencies is None:  # noqa: E501
            raise ValueError("Invalid value for `dependencies`, must not be `None`")  # noqa: E501

        self._dependencies = dependencies

    @property
    def description(self):
        """Gets the description of this AnsibleCollectionVersionResponse.  # noqa: E501

        A short summary description of the collection.  # noqa: E501

        :return: The description of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AnsibleCollectionVersionResponse.

        A short summary description of the collection.  # noqa: E501

        :param description: The description of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def docs_blob(self):
        """Gets the docs_blob of this AnsibleCollectionVersionResponse.  # noqa: E501

        A JSON field holding the various documentation blobs in the collection.  # noqa: E501

        :return: The docs_blob of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: object
        """
        return self._docs_blob

    @docs_blob.setter
    def docs_blob(self, docs_blob):
        """Sets the docs_blob of this AnsibleCollectionVersionResponse.

        A JSON field holding the various documentation blobs in the collection.  # noqa: E501

        :param docs_blob: The docs_blob of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and docs_blob is None:  # noqa: E501
            raise ValueError("Invalid value for `docs_blob`, must not be `None`")  # noqa: E501

        self._docs_blob = docs_blob

    @property
    def documentation(self):
        """Gets the documentation of this AnsibleCollectionVersionResponse.  # noqa: E501

        The URL to any online docs.  # noqa: E501

        :return: The documentation of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._documentation

    @documentation.setter
    def documentation(self, documentation):
        """Sets the documentation of this AnsibleCollectionVersionResponse.

        The URL to any online docs.  # noqa: E501

        :param documentation: The documentation of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and documentation is None:  # noqa: E501
            raise ValueError("Invalid value for `documentation`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                documentation is not None and len(documentation) > 2000):
            raise ValueError("Invalid value for `documentation`, length must be less than or equal to `2000`")  # noqa: E501

        self._documentation = documentation

    @property
    def homepage(self):
        """Gets the homepage of this AnsibleCollectionVersionResponse.  # noqa: E501

        The URL to the homepage of the collection/project.  # noqa: E501

        :return: The homepage of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._homepage

    @homepage.setter
    def homepage(self, homepage):
        """Sets the homepage of this AnsibleCollectionVersionResponse.

        The URL to the homepage of the collection/project.  # noqa: E501

        :param homepage: The homepage of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and homepage is None:  # noqa: E501
            raise ValueError("Invalid value for `homepage`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                homepage is not None and len(homepage) > 2000):
            raise ValueError("Invalid value for `homepage`, length must be less than or equal to `2000`")  # noqa: E501

        self._homepage = homepage

    @property
    def issues(self):
        """Gets the issues of this AnsibleCollectionVersionResponse.  # noqa: E501

        The URL to the collection issue tracker.  # noqa: E501

        :return: The issues of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._issues

    @issues.setter
    def issues(self, issues):
        """Sets the issues of this AnsibleCollectionVersionResponse.

        The URL to the collection issue tracker.  # noqa: E501

        :param issues: The issues of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and issues is None:  # noqa: E501
            raise ValueError("Invalid value for `issues`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                issues is not None and len(issues) > 2000):
            raise ValueError("Invalid value for `issues`, length must be less than or equal to `2000`")  # noqa: E501

        self._issues = issues

    @property
    def license(self):
        """Gets the license of this AnsibleCollectionVersionResponse.  # noqa: E501

        A list of licenses for content inside of a collection.  # noqa: E501

        :return: The license of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this AnsibleCollectionVersionResponse.

        A list of licenses for content inside of a collection.  # noqa: E501

        :param license: The license of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and license is None:  # noqa: E501
            raise ValueError("Invalid value for `license`, must not be `None`")  # noqa: E501

        self._license = license

    @property
    def name(self):
        """Gets the name of this AnsibleCollectionVersionResponse.  # noqa: E501

        The name of the collection.  # noqa: E501

        :return: The name of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnsibleCollectionVersionResponse.

        The name of the collection.  # noqa: E501

        :param name: The name of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 32):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this AnsibleCollectionVersionResponse.  # noqa: E501

        The namespace of the collection.  # noqa: E501

        :return: The namespace of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this AnsibleCollectionVersionResponse.

        The namespace of the collection.  # noqa: E501

        :param namespace: The namespace of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and namespace is None:  # noqa: E501
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                namespace is not None and len(namespace) > 32):
            raise ValueError("Invalid value for `namespace`, length must be less than or equal to `32`")  # noqa: E501

        self._namespace = namespace

    @property
    def repository(self):
        """Gets the repository of this AnsibleCollectionVersionResponse.  # noqa: E501

        The URL of the originating SCM repository.  # noqa: E501

        :return: The repository of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this AnsibleCollectionVersionResponse.

        The URL of the originating SCM repository.  # noqa: E501

        :param repository: The repository of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and repository is None:  # noqa: E501
            raise ValueError("Invalid value for `repository`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                repository is not None and len(repository) > 2000):
            raise ValueError("Invalid value for `repository`, length must be less than or equal to `2000`")  # noqa: E501

        self._repository = repository

    @property
    def tags(self):
        """Gets the tags of this AnsibleCollectionVersionResponse.  # noqa: E501


        :return: The tags of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: list[AnsibleTagResponse]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AnsibleCollectionVersionResponse.


        :param tags: The tags of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: list[AnsibleTagResponse]
        """

        self._tags = tags

    @property
    def version(self):
        """Gets the version of this AnsibleCollectionVersionResponse.  # noqa: E501

        The version of the collection.  # noqa: E501

        :return: The version of this AnsibleCollectionVersionResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AnsibleCollectionVersionResponse.

        The version of the collection.  # noqa: E501

        :param version: The version of this AnsibleCollectionVersionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) > 32):
            raise ValueError("Invalid value for `version`, length must be less than or equal to `32`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, AnsibleCollectionVersionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnsibleCollectionVersionResponse):
            return True

        return self.to_dict() != other.to_dict()
