# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.6.0-dev

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class BuildAnalysisResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "base_image_analysis": "BuildAnalysisResponseBaseImageAnalysis",
        "output_image_analysis": "BuildAnalysisResponseBaseImageAnalysis",
        "buildlog_analysis": "BuildAnalysisResponseBaseImageAnalysis",
        "buildlog_document_id": "str",
    }

    attribute_map = {
        "base_image_analysis": "base_image_analysis",
        "output_image_analysis": "output_image_analysis",
        "buildlog_analysis": "buildlog_analysis",
        "buildlog_document_id": "buildlog_document_id",
    }

    def __init__(
        self,
        base_image_analysis=None,
        output_image_analysis=None,
        buildlog_analysis=None,
        buildlog_document_id=None,
    ):  # noqa: E501
        """BuildAnalysisResponse - a model defined in Swagger"""  # noqa: E501
        self._base_image_analysis = None
        self._output_image_analysis = None
        self._buildlog_analysis = None
        self._buildlog_document_id = None
        self.discriminator = None
        self.base_image_analysis = base_image_analysis
        self.output_image_analysis = output_image_analysis
        self.buildlog_analysis = buildlog_analysis
        if buildlog_document_id is not None:
            self.buildlog_document_id = buildlog_document_id

    @property
    def base_image_analysis(self):
        """Gets the base_image_analysis of this BuildAnalysisResponse.  # noqa: E501


        :return: The base_image_analysis of this BuildAnalysisResponse.  # noqa: E501
        :rtype: BuildAnalysisResponseBaseImageAnalysis
        """
        return self._base_image_analysis

    @base_image_analysis.setter
    def base_image_analysis(self, base_image_analysis):
        """Sets the base_image_analysis of this BuildAnalysisResponse.


        :param base_image_analysis: The base_image_analysis of this BuildAnalysisResponse.  # noqa: E501
        :type: BuildAnalysisResponseBaseImageAnalysis
        """
        if base_image_analysis is None:
            raise ValueError(
                "Invalid value for `base_image_analysis`, must not be `None`"
            )  # noqa: E501

        self._base_image_analysis = base_image_analysis

    @property
    def output_image_analysis(self):
        """Gets the output_image_analysis of this BuildAnalysisResponse.  # noqa: E501


        :return: The output_image_analysis of this BuildAnalysisResponse.  # noqa: E501
        :rtype: BuildAnalysisResponseBaseImageAnalysis
        """
        return self._output_image_analysis

    @output_image_analysis.setter
    def output_image_analysis(self, output_image_analysis):
        """Sets the output_image_analysis of this BuildAnalysisResponse.


        :param output_image_analysis: The output_image_analysis of this BuildAnalysisResponse.  # noqa: E501
        :type: BuildAnalysisResponseBaseImageAnalysis
        """
        if output_image_analysis is None:
            raise ValueError(
                "Invalid value for `output_image_analysis`, must not be `None`"
            )  # noqa: E501

        self._output_image_analysis = output_image_analysis

    @property
    def buildlog_analysis(self):
        """Gets the buildlog_analysis of this BuildAnalysisResponse.  # noqa: E501


        :return: The buildlog_analysis of this BuildAnalysisResponse.  # noqa: E501
        :rtype: BuildAnalysisResponseBaseImageAnalysis
        """
        return self._buildlog_analysis

    @buildlog_analysis.setter
    def buildlog_analysis(self, buildlog_analysis):
        """Sets the buildlog_analysis of this BuildAnalysisResponse.


        :param buildlog_analysis: The buildlog_analysis of this BuildAnalysisResponse.  # noqa: E501
        :type: BuildAnalysisResponseBaseImageAnalysis
        """
        if buildlog_analysis is None:
            raise ValueError(
                "Invalid value for `buildlog_analysis`, must not be `None`"
            )  # noqa: E501

        self._buildlog_analysis = buildlog_analysis

    @property
    def buildlog_document_id(self):
        """Gets the buildlog_document_id of this BuildAnalysisResponse.  # noqa: E501

        Document identifier for the stored build log.  # noqa: E501

        :return: The buildlog_document_id of this BuildAnalysisResponse.  # noqa: E501
        :rtype: str
        """
        return self._buildlog_document_id

    @buildlog_document_id.setter
    def buildlog_document_id(self, buildlog_document_id):
        """Sets the buildlog_document_id of this BuildAnalysisResponse.

        Document identifier for the stored build log.  # noqa: E501

        :param buildlog_document_id: The buildlog_document_id of this BuildAnalysisResponse.  # noqa: E501
        :type: str
        """

        self._buildlog_document_id = buildlog_document_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(BuildAnalysisResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BuildAnalysisResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
