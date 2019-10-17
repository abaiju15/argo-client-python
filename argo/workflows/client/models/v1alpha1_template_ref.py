# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    OpenAPI spec version: ${GIT_TAG/argo//}
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1alpha1TemplateRef(object):
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
        'name': 'str',
        'runtime_resolution': 'bool',
        'template': 'str'
    }

    attribute_map = {
        'name': 'name',
        'runtime_resolution': 'runtimeResolution',
        'template': 'template'
    }

    def __init__(self, name=None, runtime_resolution=None, template=None):  # noqa: E501
        """V1alpha1TemplateRef - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._runtime_resolution = None
        self._template = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if runtime_resolution is not None:
            self.runtime_resolution = runtime_resolution
        if template is not None:
            self.template = template

    @property
    def name(self):
        """Gets the name of this V1alpha1TemplateRef.  # noqa: E501

        Name is the resource name of the template.  # noqa: E501

        :return: The name of this V1alpha1TemplateRef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1TemplateRef.

        Name is the resource name of the template.  # noqa: E501

        :param name: The name of this V1alpha1TemplateRef.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def runtime_resolution(self):
        """Gets the runtime_resolution of this V1alpha1TemplateRef.  # noqa: E501

        RuntimeResolution skips validation at creation time. By enabling this option, you can create the referred workflow template before the actual runtime.  # noqa: E501

        :return: The runtime_resolution of this V1alpha1TemplateRef.  # noqa: E501
        :rtype: bool
        """
        return self._runtime_resolution

    @runtime_resolution.setter
    def runtime_resolution(self, runtime_resolution):
        """Sets the runtime_resolution of this V1alpha1TemplateRef.

        RuntimeResolution skips validation at creation time. By enabling this option, you can create the referred workflow template before the actual runtime.  # noqa: E501

        :param runtime_resolution: The runtime_resolution of this V1alpha1TemplateRef.  # noqa: E501
        :type: bool
        """

        self._runtime_resolution = runtime_resolution

    @property
    def template(self):
        """Gets the template of this V1alpha1TemplateRef.  # noqa: E501

        Template is the name of referred template in the resource.  # noqa: E501

        :return: The template of this V1alpha1TemplateRef.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1alpha1TemplateRef.

        Template is the name of referred template in the resource.  # noqa: E501

        :param template: The template of this V1alpha1TemplateRef.  # noqa: E501
        :type: str
        """

        self._template = template

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, V1alpha1TemplateRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
