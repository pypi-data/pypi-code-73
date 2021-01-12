# coding: utf-8

"""
    API Specification

    # Introduction Welcome to gridscales API documentation.  A REST API is a programming interface that allows you to access and send data directly to our systems using HTTPS requests, without the need to use a web GUI. All the functionality you are already familiar with in your control panel is accessible through the API, including expert methods that are only available through the API. Allowing you to script any actions you require, regardless of their complexity.  First we will start with a general overview about how the API works, followed by an extensive list of each endpoint, describing them in great detail.  ## Requests  For security, gridscale requires all API requests are made through the HTTPS protocol so that traffic is encrypted. The following table displays the different type of requests that the interface responds to, depending on the action you require.  | Method | Description | | --- | --- | | GET | A simple search of information. The response is a JSON object. Requests using GET are always read-only. | | POST | Adds new objects and object relations. The POST request must contain all the required parameters in the form of a JSON object. | | PATCH | Changes an object or an object relation. The parameters in PATCH requests are usually optional, so only the changed parameters must be specified in a JSON object. | | DELETE | Deletes an object or object relation. The object is deleted if it exists. | | OPTIONS | Get an extensive list of the servers support methods and characteristics. We will not give example OPTION requests on each endpoint, as they are extensive and self-descriptive. |  <aside class=\"notice\"> The methods PATCH and DELETE are idempotent - that is, a request with identical parameters can be sent several times, and it doesn't change the result. </aside>  ## Status Codes  | HTTP Status | `Message` | Description | | --- | --- | --- | | 200 | `OK` | The request has been successfully processed and the result of the request is transmitted in the response. | | 202 | `Accepted` | The request has been accepted, but will run at a later date. Meaning we can not guarantee the success of the request. You should poll the request to be notified once the resource has been provisioned - see the requests endpoint on how to poll. | | 204 | `No Content` | The request was successful, but the answer deliberately contains no data. | | 400 | `Bad Request` | The request message was built incorrectly. | | 401 | `Unauthorised` | The request can not be performed without a valid authentication. X-Auth UserId or X-Auth token HTTP header is not set or the userID / token is invalid. | | 402 | `Payment Required` | Action can not be executed - not provided any or invalid payment methods. | | 403 | `Forbidden` | The request was not carried out due to lack of authorization of the user or because an impossible action was requested. | | 404 | `Not Found` | The requested resource was not found. Will also be used if you do a resource exists, but the user does not have permission for it. | | 405 | `Method Not Allowed` | The request may be made only with other HTTP methods (eg GET rather than POST). | | 409 | `Conflict` | The request was made under false assumptions. For example, a user can not be created twice with the same email. | | 415 | `Unsupported Media Type` | The contents of the request have been submitted with an invalid media type. All POST or PATCH requests must have \"Content-Type : application / json\" as a header, and send a JSON object as a payload. | | 416 | `Requested Range Not Satisfiable` | The request could not be fulfilled. It is possible that a resource limit was reached or an IPv4 address pool is exhausted. | | 424 | `Failed Dependency` | The request could not be performed because the object is in the wrong status. | | 429 | `Too Many Requests` | The request has been rejected because rate limits have been exceeded. |  <aside class=\"success\"> Status 200-204 indicates that the request has been accepted and is processed. </aside> <aside class=\"notice\"> Status 400-429 indicates that there was a problem with the request that originated on the client. You will find more information about the problem in the body of 4xx response. </aside> <aside class=\"warning\"> A status 500 means that there was a server-side problem and your request can not be processed now. </aside>  ## Request Headers  | Header | Description | | --- | --- | | Content-Type | Always \"application/json\". | | X-Auth-userId | The user UUID. This can be found in the panel under \"API\" and will never change ( even after the change of user e-mail). | | X-Auth-Token | Is generated from the API hash and must be sent with all API requests. Both the token and its permissions can be configured in the panel.|  ## Response Headers  | Header | Description | | --- | --- | | Content-Type | Always \"application/json\". | | X-Time-Provisioning | The time taken to process the request (in ms). | | X-Api-Identity | The currently active Provisioning API version. Useful when reporting bugs to us. | | X-Request-Id   | The unique identifier of the request, be sure to include it when referring to a request. | | RateLimit-Limit | The number of requests that can be made per minute. | | RateLimit-Remaining | The number of requests that still remain before you hit your request limit. | | RateLimit-Reset | A [Unix timestamp](https://en.wikipedia.org/wiki/Unix_time) in milliseconds of when the rate limit will reset, or the time at which a request no longer will return 429 - Too Many Requests. |  ## Timestamp Format  All timestamps follow <a href=\"https://de.wikipedia.org/wiki/ISO_8601\" target=\"_blank_\">ISO 8601</a> and issued in <a href=\"https://www.timeanddate.de/zeitzonen/utc-gmt\" target=\"_blank_\">UTC</a>  ## CORS  ### Cross Origin Resource Sharing  To allow API access from other domains that supports the API CORS (Cross Origin Resource Sharing). See: enable-cors.org/ .  This allows direct use the API in the browser running a JavaScript web control panel.  All this is done in the background by the browser. The following HTTP headers are set by the API:  Header | Parameter | Description --- | --- | --- Access-Control-Allow-Methods   | GET, POST, PUT, PATCH, DELETE, OPTIONS | Contains all available methods that may be used for queries. Access-Control-Allow-Credentials | true | Is set to \"true\". Allows the browser to send the authentication data via X-Auth HTTP header. Access-Control-Allow-Headers | Origin, X-Requested-With, Content-Type, Accept, X-Auth-UserId, X-Auth-Token, X-Exec-Time, X-API-Version, X-Api-Client | The HTTP headers available for requests. Access-Control-Allow-Origin | * | The domain sent by the browser as a source of demand. Access-Control-Expose-Headers | X-Exec-Time, X-Api-Version | The HTTP headers that can be used by a browser application.  ## Rate Limits  The number of requests that can be made through our API is currently limited to 210 requests per 60 seconds. The current state of rate limiting is returned within the response headers of each request. The relevant response headers are  - RateLimit-Limit - RateLimit-Remaining - RateLimit-Reset  See the Response Headers section for details.  As long as the `RateLimit-Remaining` count is above zero, you will be able to make further requests. As soon as the `RateLimit-Remaining` header value is zero, subsequent requests will return the 429 status code. This will stay until the timestamp given in `RateLimit-Reset` has been reached.  ### Example rate limiting response  ```shell HTTP/1.0 429 TOO MANY REQUESTS Content-Length: 66 Content-Type: application/json; charset=utf-8 Date: Mon, 11 Nov 2019 11:11:33 GMT RateLimit-Limit: 210 RateLimit-Remaining: 0 RateLimit-Reset: 1573468299256  {     \"id\": \"too_many_requests\",     \"message\": \"API Rate limit exceeded.\" } ```  It is important to understand how rate limits are reset in order to use the API efficiently. Rate limits are reset for all counted requests at once. This means that that once the timestamp `RateLimit-Remaining` has arrived all counted request are reset and you can again start sending requests to the API.  This allows for short burst of traffic. The downside is once you have hit the request limit no more requests are allowed until the rate limit duration is reset.  ## Object Relations Relationships describe resource objects (storages, networks, IPs, etc.) that are connected to a server. These relationships are treated like objects themselves and can have properties specific to this relation.  One example would be, that the MAC address of a private network connected to a server (Server-to-Network relation) can be found as property of the relation itself - the relation is the _network interface_ in the server.  Another example is storage, where the SCSI LUN is also part of the Server-to-Storage relation object.  This information is especially interesting if some kind of network boot is used on the servers, where the properties of the server need to be known beforehand.  ## Deleted Objects Objects that are deleted are no longer visible on their *regular* endpoints. For historical reasons these objects are still available read-only on a special endpoint named /deleted. If objects have been deleted but have not yet been billed in the current period, the yet-to-be-billed price is still shown.  <!-- #strip_js --> ## Node.js Library  We have a JavaScript library for you to use our API with ease.  <a href=\"https://www.npmjs.com/package/@gridscale/api\" target=\"_blank\"><img src=\"https://badge.fury.io/js/%40gridscale%2Fapi.svg\" alt=\"npm badge\"></a>  <aside class=\"success\"> We want to make it even easier for you to manage your Infrastructure via our API - so feel free to contact us with any ideas, or languages you would like to see included. </aside>  Requests with our Node.js lib return a little differently. Everything is the same except it allows you to add URL parameters to customize your requests.  To get started <a href=\"https://www.npmjs.com/package/@gridscale/api\" target=\"_blank\">click here</a> .  <!-- #strip_js_end -->  <!-- #strip_go --> ## Golang Library We also have a Golang library for Gophers.  Requests with our Golang lib return a little differently. Everything is the same except it allows you to add URL parameters to customize your requests.  To get started <a href=\"https://github.com/gridscale/gsclient-go\" target=\"_blank\">click here</a> .  <!-- #strip_go_end -->  <!-- #strip_python --> ## Python Library  We have a Python library, that optionally also simplifies handling of asynchronous requests by mimicking synchronous blocking behaviour.  To get started <a href=\"https://pypi.org/project/gs-api-client/\" target=\"_blank\">click here</a> .  <!-- #strip_python_end -->  # Authentication  In order to use the API, the User-UUID and an API_Token are required. Both are available via the web GUI which can be found here on <a href=\"https://my.gridscale.io/APIs/\" target=\"_blank\">Your Account</a>  <aside class=\"success\"> If you are logged in, your UUID and Token will be pulled dynamically from your account, so you can copy request examples straight into your code. </aside>  The User-UUID remains the same, even if the users email address is changed. The API_Token is a randomly generated hash that allows read/write access.  ## API_Token  <table class=\"security-details\"><tbody><tr><th> Security scheme type: </th><td> API Key </td></tr><tr><th> header parameter name:</th><td> X-Auth-Token </td></tr></tbody></table>  ## User_UUID  <table class=\"security-details\"><tbody><tr><th> Security scheme type: </th><td> API Key </td></tr><tr><th> header parameter name:</th><td> X-Auth-UserId </td></tr></tbody></table>  ## Examples  <!-- #strip_js --> > Node.js ``` // to get started // read the docs @ https://www.npmjs.com/package/@gs_js_auth/api var gs_js_auth = require('@gs_js_auth/api').gs_js_auth; var client = new gs_js_auth.Client(\"##API_TOKEN##\",\"##USER_UUID##\"); ``` <!-- #strip_js_end -->  <!-- #strip_go --> > Golang ``` // to get started // read the docs @ https://github.com/gridscale/gsclient-go config := gsclient.NewConfiguration(   \"https://api.gridscale.io\",   \"##USER_UUID##\",   \"##API_TOKEN##\",   false, //set debug mode ) client := gsclient.NewClient(config) ``` <!-- #strip_go_end -->  > Shell Authentication Headers ```   -H \"X-Auth-UserId: ##USER_UUID##\" \\   -H \"X-Auth-Token: ##API_TOKEN##\" \\ ```  > Setting Authentication in your Environment variables ``` export API_TOKEN=\"##API_TOKEN##\" USER_UUID=\"##USER_UUID##\" ```  <aside class=\"notice\"> You must replace <code>USER_UUID</code> and <code>API_Token</code> with your personal UUID and API key respectively. </aside>   # noqa: E501

    OpenAPI spec version: 1.0.24
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LoadbalancerCreate(object):
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
        'forwarding_rules': 'list[object]',
        'backend_servers': 'list[object]',
        'status': 'str',
        'redirect_http_to_https': 'bool',
        'labels': 'list[str]',
        'algorithm': 'str',
        'listen_ipv4_uuid': 'str',
        'listen_ipv6_uuid': 'str'
    }

    attribute_map = {
        'name': 'name',
        'forwarding_rules': 'forwarding_rules',
        'backend_servers': 'backend_servers',
        'status': 'status',
        'redirect_http_to_https': 'redirect_http_to_https',
        'labels': 'labels',
        'algorithm': 'algorithm',
        'listen_ipv4_uuid': 'listen_ipv4_uuid',
        'listen_ipv6_uuid': 'listen_ipv6_uuid'
    }

    def __init__(self, name=None, forwarding_rules=None, backend_servers=None, status=None, redirect_http_to_https=None, labels=None, algorithm=None, listen_ipv4_uuid=None, listen_ipv6_uuid=None):  # noqa: E501
        """LoadbalancerCreate - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._forwarding_rules = None
        self._backend_servers = None
        self._status = None
        self._redirect_http_to_https = None
        self._labels = None
        self._algorithm = None
        self._listen_ipv4_uuid = None
        self._listen_ipv6_uuid = None
        self.discriminator = None

        self.name = name
        self.forwarding_rules = forwarding_rules
        self.backend_servers = backend_servers
        if status is not None:
            self.status = status
        self.redirect_http_to_https = redirect_http_to_https
        self.labels = labels
        self.algorithm = algorithm
        self.listen_ipv4_uuid = listen_ipv4_uuid
        self.listen_ipv6_uuid = listen_ipv6_uuid

    @property
    def name(self):
        """Gets the name of this LoadbalancerCreate.  # noqa: E501

        The human-readable name of the object. It supports the full UTF-8 character set, with a maximum of 64 characters.  # noqa: E501

        :return: The name of this LoadbalancerCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoadbalancerCreate.

        The human-readable name of the object. It supports the full UTF-8 character set, with a maximum of 64 characters.  # noqa: E501

        :param name: The name of this LoadbalancerCreate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def forwarding_rules(self):
        """Gets the forwarding_rules of this LoadbalancerCreate.  # noqa: E501

        An array of objects containing the forwarding rules for the Load balancer   # noqa: E501

        :return: The forwarding_rules of this LoadbalancerCreate.  # noqa: E501
        :rtype: list[object]
        """
        return self._forwarding_rules

    @forwarding_rules.setter
    def forwarding_rules(self, forwarding_rules):
        """Sets the forwarding_rules of this LoadbalancerCreate.

        An array of objects containing the forwarding rules for the Load balancer   # noqa: E501

        :param forwarding_rules: The forwarding_rules of this LoadbalancerCreate.  # noqa: E501
        :type: list[object]
        """
        if forwarding_rules is None:
            raise ValueError("Invalid value for `forwarding_rules`, must not be `None`")  # noqa: E501

        self._forwarding_rules = forwarding_rules

    @property
    def backend_servers(self):
        """Gets the backend_servers of this LoadbalancerCreate.  # noqa: E501

        The servers that this Load balancer can communicate with  # noqa: E501

        :return: The backend_servers of this LoadbalancerCreate.  # noqa: E501
        :rtype: list[object]
        """
        return self._backend_servers

    @backend_servers.setter
    def backend_servers(self, backend_servers):
        """Sets the backend_servers of this LoadbalancerCreate.

        The servers that this Load balancer can communicate with  # noqa: E501

        :param backend_servers: The backend_servers of this LoadbalancerCreate.  # noqa: E501
        :type: list[object]
        """
        if backend_servers is None:
            raise ValueError("Invalid value for `backend_servers`, must not be `None`")  # noqa: E501

        self._backend_servers = backend_servers

    @property
    def status(self):
        """Gets the status of this LoadbalancerCreate.  # noqa: E501

        Status indicates the status of the object.  # noqa: E501

        :return: The status of this LoadbalancerCreate.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LoadbalancerCreate.

        Status indicates the status of the object.  # noqa: E501

        :param status: The status of this LoadbalancerCreate.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def redirect_http_to_https(self):
        """Gets the redirect_http_to_https of this LoadbalancerCreate.  # noqa: E501

        Whether the Load balancer is forced to redirect requests from HTTP to HTTPS  # noqa: E501

        :return: The redirect_http_to_https of this LoadbalancerCreate.  # noqa: E501
        :rtype: bool
        """
        return self._redirect_http_to_https

    @redirect_http_to_https.setter
    def redirect_http_to_https(self, redirect_http_to_https):
        """Sets the redirect_http_to_https of this LoadbalancerCreate.

        Whether the Load balancer is forced to redirect requests from HTTP to HTTPS  # noqa: E501

        :param redirect_http_to_https: The redirect_http_to_https of this LoadbalancerCreate.  # noqa: E501
        :type: bool
        """
        if redirect_http_to_https is None:
            raise ValueError("Invalid value for `redirect_http_to_https`, must not be `None`")  # noqa: E501

        self._redirect_http_to_https = redirect_http_to_https

    @property
    def labels(self):
        """Gets the labels of this LoadbalancerCreate.  # noqa: E501

        List of labels.  # noqa: E501

        :return: The labels of this LoadbalancerCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this LoadbalancerCreate.

        List of labels.  # noqa: E501

        :param labels: The labels of this LoadbalancerCreate.  # noqa: E501
        :type: list[str]
        """
        if labels is None:
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

    @property
    def algorithm(self):
        """Gets the algorithm of this LoadbalancerCreate.  # noqa: E501

        The algorithm used to process requests. Accepted values: roundrobin/leastconn.  # noqa: E501

        :return: The algorithm of this LoadbalancerCreate.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this LoadbalancerCreate.

        The algorithm used to process requests. Accepted values: roundrobin/leastconn.  # noqa: E501

        :param algorithm: The algorithm of this LoadbalancerCreate.  # noqa: E501
        :type: str
        """
        if algorithm is None:
            raise ValueError("Invalid value for `algorithm`, must not be `None`")  # noqa: E501

        self._algorithm = algorithm

    @property
    def listen_ipv4_uuid(self):
        """Gets the listen_ipv4_uuid of this LoadbalancerCreate.  # noqa: E501

        The UUID of the IPv4 address the Load balancer will listen to for incoming requests.  # noqa: E501

        :return: The listen_ipv4_uuid of this LoadbalancerCreate.  # noqa: E501
        :rtype: str
        """
        return self._listen_ipv4_uuid

    @listen_ipv4_uuid.setter
    def listen_ipv4_uuid(self, listen_ipv4_uuid):
        """Sets the listen_ipv4_uuid of this LoadbalancerCreate.

        The UUID of the IPv4 address the Load balancer will listen to for incoming requests.  # noqa: E501

        :param listen_ipv4_uuid: The listen_ipv4_uuid of this LoadbalancerCreate.  # noqa: E501
        :type: str
        """
        if listen_ipv4_uuid is None:
            raise ValueError("Invalid value for `listen_ipv4_uuid`, must not be `None`")  # noqa: E501

        self._listen_ipv4_uuid = listen_ipv4_uuid

    @property
    def listen_ipv6_uuid(self):
        """Gets the listen_ipv6_uuid of this LoadbalancerCreate.  # noqa: E501

        The UUID of the IPv6 address the Load balancer will listen to for incoming requests.  # noqa: E501

        :return: The listen_ipv6_uuid of this LoadbalancerCreate.  # noqa: E501
        :rtype: str
        """
        return self._listen_ipv6_uuid

    @listen_ipv6_uuid.setter
    def listen_ipv6_uuid(self, listen_ipv6_uuid):
        """Sets the listen_ipv6_uuid of this LoadbalancerCreate.

        The UUID of the IPv6 address the Load balancer will listen to for incoming requests.  # noqa: E501

        :param listen_ipv6_uuid: The listen_ipv6_uuid of this LoadbalancerCreate.  # noqa: E501
        :type: str
        """
        if listen_ipv6_uuid is None:
            raise ValueError("Invalid value for `listen_ipv6_uuid`, must not be `None`")  # noqa: E501

        self._listen_ipv6_uuid = listen_ipv6_uuid

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
        if issubclass(LoadbalancerCreate, dict):
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
        if not isinstance(other, LoadbalancerCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
