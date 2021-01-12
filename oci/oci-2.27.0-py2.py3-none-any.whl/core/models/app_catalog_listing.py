# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppCatalogListing(object):
    """
    Listing details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppCatalogListing object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param contact_url:
            The value to assign to the contact_url property of this AppCatalogListing.
        :type contact_url: str

        :param description:
            The value to assign to the description property of this AppCatalogListing.
        :type description: str

        :param listing_id:
            The value to assign to the listing_id property of this AppCatalogListing.
        :type listing_id: str

        :param display_name:
            The value to assign to the display_name property of this AppCatalogListing.
        :type display_name: str

        :param time_published:
            The value to assign to the time_published property of this AppCatalogListing.
        :type time_published: datetime

        :param publisher_logo_url:
            The value to assign to the publisher_logo_url property of this AppCatalogListing.
        :type publisher_logo_url: str

        :param publisher_name:
            The value to assign to the publisher_name property of this AppCatalogListing.
        :type publisher_name: str

        :param summary:
            The value to assign to the summary property of this AppCatalogListing.
        :type summary: str

        """
        self.swagger_types = {
            'contact_url': 'str',
            'description': 'str',
            'listing_id': 'str',
            'display_name': 'str',
            'time_published': 'datetime',
            'publisher_logo_url': 'str',
            'publisher_name': 'str',
            'summary': 'str'
        }

        self.attribute_map = {
            'contact_url': 'contactUrl',
            'description': 'description',
            'listing_id': 'listingId',
            'display_name': 'displayName',
            'time_published': 'timePublished',
            'publisher_logo_url': 'publisherLogoUrl',
            'publisher_name': 'publisherName',
            'summary': 'summary'
        }

        self._contact_url = None
        self._description = None
        self._listing_id = None
        self._display_name = None
        self._time_published = None
        self._publisher_logo_url = None
        self._publisher_name = None
        self._summary = None

    @property
    def contact_url(self):
        """
        Gets the contact_url of this AppCatalogListing.
        Listing's contact URL.


        :return: The contact_url of this AppCatalogListing.
        :rtype: str
        """
        return self._contact_url

    @contact_url.setter
    def contact_url(self, contact_url):
        """
        Sets the contact_url of this AppCatalogListing.
        Listing's contact URL.


        :param contact_url: The contact_url of this AppCatalogListing.
        :type: str
        """
        self._contact_url = contact_url

    @property
    def description(self):
        """
        Gets the description of this AppCatalogListing.
        Description of the listing.


        :return: The description of this AppCatalogListing.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AppCatalogListing.
        Description of the listing.


        :param description: The description of this AppCatalogListing.
        :type: str
        """
        self._description = description

    @property
    def listing_id(self):
        """
        Gets the listing_id of this AppCatalogListing.
        The OCID of the listing.


        :return: The listing_id of this AppCatalogListing.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this AppCatalogListing.
        The OCID of the listing.


        :param listing_id: The listing_id of this AppCatalogListing.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def display_name(self):
        """
        Gets the display_name of this AppCatalogListing.
        Name of the listing.


        :return: The display_name of this AppCatalogListing.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AppCatalogListing.
        Name of the listing.


        :param display_name: The display_name of this AppCatalogListing.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_published(self):
        """
        Gets the time_published of this AppCatalogListing.
        Date and time the listing was published, in `RFC3339`__ format.
        Example: `2018-03-20T12:32:53.532Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_published of this AppCatalogListing.
        :rtype: datetime
        """
        return self._time_published

    @time_published.setter
    def time_published(self, time_published):
        """
        Sets the time_published of this AppCatalogListing.
        Date and time the listing was published, in `RFC3339`__ format.
        Example: `2018-03-20T12:32:53.532Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_published: The time_published of this AppCatalogListing.
        :type: datetime
        """
        self._time_published = time_published

    @property
    def publisher_logo_url(self):
        """
        Gets the publisher_logo_url of this AppCatalogListing.
        Publisher's logo URL.


        :return: The publisher_logo_url of this AppCatalogListing.
        :rtype: str
        """
        return self._publisher_logo_url

    @publisher_logo_url.setter
    def publisher_logo_url(self, publisher_logo_url):
        """
        Sets the publisher_logo_url of this AppCatalogListing.
        Publisher's logo URL.


        :param publisher_logo_url: The publisher_logo_url of this AppCatalogListing.
        :type: str
        """
        self._publisher_logo_url = publisher_logo_url

    @property
    def publisher_name(self):
        """
        Gets the publisher_name of this AppCatalogListing.
        Name of the publisher who published this listing.


        :return: The publisher_name of this AppCatalogListing.
        :rtype: str
        """
        return self._publisher_name

    @publisher_name.setter
    def publisher_name(self, publisher_name):
        """
        Sets the publisher_name of this AppCatalogListing.
        Name of the publisher who published this listing.


        :param publisher_name: The publisher_name of this AppCatalogListing.
        :type: str
        """
        self._publisher_name = publisher_name

    @property
    def summary(self):
        """
        Gets the summary of this AppCatalogListing.
        Summary of the listing.


        :return: The summary of this AppCatalogListing.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this AppCatalogListing.
        Summary of the listing.


        :param summary: The summary of this AppCatalogListing.
        :type: str
        """
        self._summary = summary

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
