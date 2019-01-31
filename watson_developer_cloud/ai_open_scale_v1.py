# coding: utf-8

# Copyright 2018 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
AI OpenScale
"""

from __future__ import absolute_import

import json
from .watson_service import WatsonService

##############################################################################
# Service
##############################################################################

class AiOpenScaleV1(WatsonService):
    """The AI OpenScale V1 service."""

    default_url = 'https://api.aiopenscale.cloud.ibm.com'

    def __init__(self,
                 url=default_url,
                ):
        """
        Construct a new client for the AI OpenScale service.

        :param str url: The base url to use when contacting the service (e.g.
               "https://api.aiopenscale.cloud.ibm.com").
               The base url may differ between Bluemix regions.

        """

        WatsonService.__init__(self,
                               vcap_services_name='ai_openscale',
                               url=url,
                               use_vcap_services=True)

    #########################
    # Feedback Logging
    #########################

    def post_feedback_payload(self, data_mart_id, binding_id, subscription_id, values, fields=None, **kwargs):
        """
        Post Feedback Payload.

        Upload feedback payload.

        :param str data_mart_id: OpenScale DataMart ID - the service instance ID.
        :param str binding_id:
        :param str subscription_id:
        :param list[list[AnyValue]] values: The scoring input data rows.
        :param list[str] fields: The data field names of model's or python function's
        input data. This property is mandatory for Spark based models. It might not be
        required for other frameworks.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if data_mart_id is None:
            raise ValueError('data_mart_id must be provided')
        if binding_id is None:
            raise ValueError('binding_id must be provided')
        if subscription_id is None:
            raise ValueError('subscription_id must be provided')
        if values is None:
            raise ValueError('values must be provided')

        headers = {
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        data = {
            'binding_id': binding_id,
            'subscription_id': subscription_id,
            'values': values,
            'fields': fields
        }

        url = '/v1/data_marts/{0}/feedback_payloads'.format(*self._encode_path_vars(data_mart_id))
        response = self.request(method='POST',
                                url=url,
                                headers=headers,
                                json=data,
                                accept_json=True)
        return response


    #########################
    # Explainability
    #########################

    def get_explanation_task(self, data_mart_id, explanation_task_id, **kwargs):
        """
        Get Explanation Task.

        Get explanation for the given explanation task id.

        :param str data_mart_id: OpenScale DataMart ID - the service instance ID.
        :param str explanation_task_id: ID of the explanation task.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if data_mart_id is None:
            raise ValueError('data_mart_id must be provided')
        if explanation_task_id is None:
            raise ValueError('explanation_task_id must be provided')

        headers = {
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/data_marts/{0}/explanation_tasks/{1}'.format(*self._encode_path_vars(data_mart_id, explanation_task_id))
        response = self.request(method='GET',
                                url=url,
                                headers=headers,
                                accept_json=True)
        return response


    def post_explanation_task(self, data_mart_id, scoring_id, **kwargs):
        """
        Post Explanation Task.

        Submit task for computing explanation of a prediction.

        :param str data_mart_id: OpenScale DataMart ID - the service instance ID.
        :param str scoring_id: ID of the scoring transaction.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if data_mart_id is None:
            raise ValueError('data_mart_id must be provided')
        if scoring_id is None:
            raise ValueError('scoring_id must be provided')

        headers = {
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        data = {
            'scoring_id': scoring_id
        }

        url = '/v1/data_marts/{0}/explanation_tasks'.format(*self._encode_path_vars(data_mart_id))
        response = self.request(method='POST',
                                url=url,
                                headers=headers,
                                json=data,
                                accept_json=True)
        return response


    #########################
    # Fairness Monitoring
    #########################

    def fairness_monitoring_debias(self, data_mart_id, binding_id, subscription_id, deployment_id, fields, values, x_global_transaction_id=None, **kwargs):
        """
        Post fairness monitoring.

        Computes the bias mitigation/remediation for the specified model. The fairness
        monitoring debias request payload details must be valid.
        Makes an online prediction and de-bias prediction on a given data values.
        The de-bias request payload takes a batch of input rows which should have model
        fields and values, in the following format.
        ```
        {
            \"fields\": [
                \"name\",
                \"age\",
                \"position\"
            ],
            \"values\": [
                [
                \"john\",
                33,
                \"engineer\"
                ],
                [
                \"mike\",
                23,
                \"student\"
                ]
            ]
        }
        ```
        The response of this API would contain regular prediction columns provided by the
        underlying machine learning model engine, and along with that would contain
        de-biased predictions as listed in the following format.
        ```
        {
            \"fields\": [
                \"name\",
                \"age\",
                \"position\",
                \"prediction\",
                \"probability\",
                \"debiased_prediction\",
                \"debiased_probability\",
                \"debiased_decoded_target\"
            ],
            \"values\": [
                [
                    \"john\",
                    35,
                    \"engineer\",
                    0.3,
                    [
                        0.754601226993865,
                        0.24539877300613497
                    ],
                    0.4,
                    [
                        0.898098798985,
                        0.49877
                    ],
                    \"good\"
                ],
                [
                    \"mike\",
                    23,
                    \"student\",
                    0.5,
                    [
                        0.2794765664946941,
                        0.7205234335053059
                    ],
                    0.6,
                    [
                        0.407098,
                        0.86756785758667
                    ],
                    \"bad\"
                ]
            ]
        }
        ```.

        :param str data_mart_id: AIOS OpenScale DataMart ID - the service instance ID.
        :param str binding_id: The Model engine binding ID.
        :param str subscription_id: The subscription ID.
        :param str deployment_id: The deployment ID.
        :param list[str] fields: The fields to process debias scoring.
        :param list[str] values: The values associated to the fields.
        :param str x_global_transaction_id: The transaction ID/scoring ID to the given
        payload.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if data_mart_id is None:
            raise ValueError('data_mart_id must be provided')
        if binding_id is None:
            raise ValueError('binding_id must be provided')
        if subscription_id is None:
            raise ValueError('subscription_id must be provided')
        if deployment_id is None:
            raise ValueError('deployment_id must be provided')
        if fields is None:
            raise ValueError('fields must be provided')
        if values is None:
            raise ValueError('values must be provided')

        headers = {
            'X-Global-Transaction-Id': x_global_transaction_id
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        data = {
            'fields': fields,
            'values': values
        }

        url = '/v1/data_marts/{0}/service_bindings/{1}/subscriptions/{2}/deployments/{3}/online'.format(*self._encode_path_vars(data_mart_id, binding_id, subscription_id, deployment_id))
        response = self.request(method='POST',
                                url=url,
                                headers=headers,
                                json=data,
                                accept_json=True)
        return response



##############################################################################
# Models
##############################################################################


class ExplanationTaskResponseEntity(object):
    """
    ExplanationTaskResponseEntity.

    :attr ExplanationTaskResponseEntityStatus status:
    :attr ExplanationTaskResponseEntityAsset asset: (optional)
    :attr list[ExplanationTaskResponseEntityInputFeature] input_features: (optional)
    :attr list[ExplanationTaskResponseEntityPrediction] predictions: (optional)
    :attr ExplanationTaskResponseEntityContrastiveExplanation contrastive_explanation:
    (optional)
    """

    def __init__(self, status, asset=None, input_features=None, predictions=None, contrastive_explanation=None):
        """
        Initialize a ExplanationTaskResponseEntity object.

        :param ExplanationTaskResponseEntityStatus status:
        :param ExplanationTaskResponseEntityAsset asset: (optional)
        :param list[ExplanationTaskResponseEntityInputFeature] input_features: (optional)
        :param list[ExplanationTaskResponseEntityPrediction] predictions: (optional)
        :param ExplanationTaskResponseEntityContrastiveExplanation
        contrastive_explanation: (optional)
        """
        self.status = status
        self.asset = asset
        self.input_features = input_features
        self.predictions = predictions
        self.contrastive_explanation = contrastive_explanation

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExplanationTaskResponseEntity object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = ExplanationTaskResponseEntityStatus._from_dict(_dict.get('status'))
        else:
            raise ValueError('Required property \'status\' not present in ExplanationTaskResponseEntity JSON')
        if 'asset' in _dict:
            args['asset'] = ExplanationTaskResponseEntityAsset._from_dict(_dict.get('asset'))
        if 'input_features' in _dict:
            args['input_features'] = [ExplanationTaskResponseEntityInputFeature._from_dict(x) for x in (_dict.get('input_features') )]
        if 'predictions' in _dict:
            args['predictions'] = [ExplanationTaskResponseEntityPrediction._from_dict(x) for x in (_dict.get('predictions') )]
        if 'contrastive_explanation' in _dict:
            args['contrastive_explanation'] = ExplanationTaskResponseEntityContrastiveExplanation._from_dict(_dict.get('contrastive_explanation'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status._to_dict()
        if hasattr(self, 'asset') and self.asset is not None:
            _dict['asset'] = self.asset._to_dict()
        if hasattr(self, 'input_features') and self.input_features is not None:
            _dict['input_features'] = [x._to_dict() for x in self.input_features]
        if hasattr(self, 'predictions') and self.predictions is not None:
            _dict['predictions'] = [x._to_dict() for x in self.predictions]
        if hasattr(self, 'contrastive_explanation') and self.contrastive_explanation is not None:
            _dict['contrastive_explanation'] = self.contrastive_explanation._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this ExplanationTaskResponseEntity object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ExplanationTaskResponseEntityAsset(object):
    """
    ExplanationTaskResponseEntityAsset.

    :attr str id: (optional) Identifier for the asset.
    :attr str name: (optional) Name of the asset.
    :attr str type: (optional) Type of the asset.
    :attr ExplanationTaskResponseEntityAssetDeployment deployment: (optional) Asset
    deployment details.
    """

    def __init__(self, id=None, name=None, type=None, deployment=None):
        """
        Initialize a ExplanationTaskResponseEntityAsset object.

        :param str id: (optional) Identifier for the asset.
        :param str name: (optional) Name of the asset.
        :param str type: (optional) Type of the asset.
        :param ExplanationTaskResponseEntityAssetDeployment deployment: (optional) Asset
        deployment details.
        """
        self.id = id
        self.name = name
        self.type = type
        self.deployment = deployment

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExplanationTaskResponseEntityAsset object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'deployment' in _dict:
            args['deployment'] = ExplanationTaskResponseEntityAssetDeployment._from_dict(_dict.get('deployment'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'deployment') and self.deployment is not None:
            _dict['deployment'] = self.deployment._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this ExplanationTaskResponseEntityAsset object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ExplanationTaskResponseEntityAssetDeployment(object):
    """
    Asset deployment details.

    :attr str id: (optional) Identifier for the asset deployment.
    :attr str name: (optional) Name of the asset deployment.
    """

    def __init__(self, id=None, name=None):
        """
        Initialize a ExplanationTaskResponseEntityAssetDeployment object.

        :param str id: (optional) Identifier for the asset deployment.
        :param str name: (optional) Name of the asset deployment.
        """
        self.id = id
        self.name = name

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExplanationTaskResponseEntityAssetDeployment object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def __str__(self):
        """Return a `str` version of this ExplanationTaskResponseEntityAssetDeployment object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ExplanationTaskResponseEntityContrastiveExplanation(object):
    """
    ExplanationTaskResponseEntityContrastiveExplanation.

    :attr list[ExplanationTaskResponseEntityExplanationFeature]
    pertinent_positive_features: (optional) These factors are sufficient evidence in
    themselves to yeild the given classification.
    :attr list[ExplanationTaskResponseEntityExplanationFeature]
    pertinent_negative_features: (optional) These factors, if added, would cause the
    classification to change.
    """

    def __init__(self, pertinent_positive_features=None, pertinent_negative_features=None):
        """
        Initialize a ExplanationTaskResponseEntityContrastiveExplanation object.

        :param list[ExplanationTaskResponseEntityExplanationFeature]
        pertinent_positive_features: (optional) These factors are sufficient evidence in
        themselves to yeild the given classification.
        :param list[ExplanationTaskResponseEntityExplanationFeature]
        pertinent_negative_features: (optional) These factors, if added, would cause the
        classification to change.
        """
        self.pertinent_positive_features = pertinent_positive_features
        self.pertinent_negative_features = pertinent_negative_features

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExplanationTaskResponseEntityContrastiveExplanation object from a json dictionary."""
        args = {}
        if 'pertinent_positive_features' in _dict:
            args['pertinent_positive_features'] = [ExplanationTaskResponseEntityExplanationFeature._from_dict(x) for x in (_dict.get('pertinent_positive_features') )]
        if 'pertinent_negative_features' in _dict:
            args['pertinent_negative_features'] = [ExplanationTaskResponseEntityExplanationFeature._from_dict(x) for x in (_dict.get('pertinent_negative_features') )]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'pertinent_positive_features') and self.pertinent_positive_features is not None:
            _dict['pertinent_positive_features'] = [x._to_dict() for x in self.pertinent_positive_features]
        if hasattr(self, 'pertinent_negative_features') and self.pertinent_negative_features is not None:
            _dict['pertinent_negative_features'] = [x._to_dict() for x in self.pertinent_negative_features]
        return _dict

    def __str__(self):
        """Return a `str` version of this ExplanationTaskResponseEntityContrastiveExplanation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ExplanationTaskResponseEntityExplanationFeature(object):
    """
    ExplanationTaskResponseEntityExplanationFeature.

    :attr str feature_name: (optional) Name of the feature column.
    :attr str weight: (optional) Contributing weight to the output explanation for the
    given feature.
    :attr str importance: (optional) Contributing importance to the output explanation for
    the given feature.
    :attr str feature_value: (optional) Value of the feature column.
    :attr ExplanationTaskResponseEntityExplanationFeatureFeatureRange feature_range:
    (optional) Range of feature values.
    """

    def __init__(self, feature_name=None, weight=None, importance=None, feature_value=None, feature_range=None):
        """
        Initialize a ExplanationTaskResponseEntityExplanationFeature object.

        :param str feature_name: (optional) Name of the feature column.
        :param str weight: (optional) Contributing weight to the output explanation for
        the given feature.
        :param str importance: (optional) Contributing importance to the output
        explanation for the given feature.
        :param str feature_value: (optional) Value of the feature column.
        :param ExplanationTaskResponseEntityExplanationFeatureFeatureRange feature_range:
        (optional) Range of feature values.
        """
        self.feature_name = feature_name
        self.weight = weight
        self.importance = importance
        self.feature_value = feature_value
        self.feature_range = feature_range

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExplanationTaskResponseEntityExplanationFeature object from a json dictionary."""
        args = {}
        if 'feature_name' in _dict:
            args['feature_name'] = _dict.get('feature_name')
        if 'weight' in _dict:
            args['weight'] = _dict.get('weight')
        if 'importance' in _dict:
            args['importance'] = _dict.get('importance')
        if 'feature_value' in _dict:
            args['feature_value'] = _dict.get('feature_value')
        if 'feature_range' in _dict:
            args['feature_range'] = ExplanationTaskResponseEntityExplanationFeatureFeatureRange._from_dict(_dict.get('feature_range'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'feature_name') and self.feature_name is not None:
            _dict['feature_name'] = self.feature_name
        if hasattr(self, 'weight') and self.weight is not None:
            _dict['weight'] = self.weight
        if hasattr(self, 'importance') and self.importance is not None:
            _dict['importance'] = self.importance
        if hasattr(self, 'feature_value') and self.feature_value is not None:
            _dict['feature_value'] = self.feature_value
        if hasattr(self, 'feature_range') and self.feature_range is not None:
            _dict['feature_range'] = self.feature_range._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this ExplanationTaskResponseEntityExplanationFeature object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ExplanationTaskResponseEntityExplanationFeatureFeatureRange(object):
    """
    Range of feature values.

    :attr str min: (optional) Minimum possible value for given feature.
    :attr bool min_inclusive: (optional) Identifies if the minimum value is inclusive or
    not.
    :attr str max: (optional) Maximum possible value for given feature.
    :attr bool max_inclusive: (optional) Identifies if the maximum value is inclusive or
    not.
    """

    def __init__(self, min=None, min_inclusive=None, max=None, max_inclusive=None):
        """
        Initialize a ExplanationTaskResponseEntityExplanationFeatureFeatureRange object.

        :param str min: (optional) Minimum possible value for given feature.
        :param bool min_inclusive: (optional) Identifies if the minimum value is inclusive
        or not.
        :param str max: (optional) Maximum possible value for given feature.
        :param bool max_inclusive: (optional) Identifies if the maximum value is inclusive
        or not.
        """
        self.min = min
        self.min_inclusive = min_inclusive
        self.max = max
        self.max_inclusive = max_inclusive

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExplanationTaskResponseEntityExplanationFeatureFeatureRange object from a json dictionary."""
        args = {}
        if 'min' in _dict:
            args['min'] = _dict.get('min')
        if 'min_inclusive' in _dict:
            args['min_inclusive'] = _dict.get('min_inclusive')
        if 'max' in _dict:
            args['max'] = _dict.get('max')
        if 'max_inclusive' in _dict:
            args['max_inclusive'] = _dict.get('max_inclusive')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'min') and self.min is not None:
            _dict['min'] = self.min
        if hasattr(self, 'min_inclusive') and self.min_inclusive is not None:
            _dict['min_inclusive'] = self.min_inclusive
        if hasattr(self, 'max') and self.max is not None:
            _dict['max'] = self.max
        if hasattr(self, 'max_inclusive') and self.max_inclusive is not None:
            _dict['max_inclusive'] = self.max_inclusive
        return _dict

    def __str__(self):
        """Return a `str` version of this ExplanationTaskResponseEntityExplanationFeatureFeatureRange object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ExplanationTaskResponseEntityInputFeature(object):
    """
    ExplanationTaskResponseEntityInputFeature.

    :attr str name: (optional) Name of the feature column.
    :attr str value: (optional) Value of the feature column.
    :attr str feature_type: (optional) Identifies the type of feature column.
    """

    def __init__(self, name=None, value=None, feature_type=None):
        """
        Initialize a ExplanationTaskResponseEntityInputFeature object.

        :param str name: (optional) Name of the feature column.
        :param str value: (optional) Value of the feature column.
        :param str feature_type: (optional) Identifies the type of feature column.
        """
        self.name = name
        self.value = value
        self.feature_type = feature_type

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExplanationTaskResponseEntityInputFeature object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'feature_type' in _dict:
            args['feature_type'] = _dict.get('feature_type')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'feature_type') and self.feature_type is not None:
            _dict['feature_type'] = self.feature_type
        return _dict

    def __str__(self):
        """Return a `str` version of this ExplanationTaskResponseEntityInputFeature object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ExplanationTaskResponseEntityPrediction(object):
    """
    ExplanationTaskResponseEntityPrediction.

    :attr str value: (optional) Value of the output field in this particular prediction.
    :attr str probability: (optional) Signifies probability of this particular prediction.
    :attr list[ExplanationTaskResponseEntityExplanationFeature] explanation_features:
    (optional)
    """

    def __init__(self, value=None, probability=None, explanation_features=None):
        """
        Initialize a ExplanationTaskResponseEntityPrediction object.

        :param str value: (optional) Value of the output field in this particular
        prediction.
        :param str probability: (optional) Signifies probability of this particular
        prediction.
        :param list[ExplanationTaskResponseEntityExplanationFeature] explanation_features:
        (optional)
        """
        self.value = value
        self.probability = probability
        self.explanation_features = explanation_features

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExplanationTaskResponseEntityPrediction object from a json dictionary."""
        args = {}
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'probability' in _dict:
            args['probability'] = _dict.get('probability')
        if 'explanation_features' in _dict:
            args['explanation_features'] = [ExplanationTaskResponseEntityExplanationFeature._from_dict(x) for x in (_dict.get('explanation_features') )]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'probability') and self.probability is not None:
            _dict['probability'] = self.probability
        if hasattr(self, 'explanation_features') and self.explanation_features is not None:
            _dict['explanation_features'] = [x._to_dict() for x in self.explanation_features]
        return _dict

    def __str__(self):
        """Return a `str` version of this ExplanationTaskResponseEntityPrediction object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ExplanationTaskResponseEntityStatus(object):
    """
    ExplanationTaskResponseEntityStatus.

    :attr str state: (optional) Overall status of the explanation task.
    :attr str lime_state: (optional) Status of lime explanation.
    :attr str cem_state: (optional) Status of cem explanation.
    """

    def __init__(self, state=None, lime_state=None, cem_state=None):
        """
        Initialize a ExplanationTaskResponseEntityStatus object.

        :param str state: (optional) Overall status of the explanation task.
        :param str lime_state: (optional) Status of lime explanation.
        :param str cem_state: (optional) Status of cem explanation.
        """
        self.state = state
        self.lime_state = lime_state
        self.cem_state = cem_state

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExplanationTaskResponseEntityStatus object from a json dictionary."""
        args = {}
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'lime_state' in _dict:
            args['lime_state'] = _dict.get('lime_state')
        if 'cem_state' in _dict:
            args['cem_state'] = _dict.get('cem_state')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'lime_state') and self.lime_state is not None:
            _dict['lime_state'] = self.lime_state
        if hasattr(self, 'cem_state') and self.cem_state is not None:
            _dict['cem_state'] = self.cem_state
        return _dict

    def __str__(self):
        """Return a `str` version of this ExplanationTaskResponseEntityStatus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ExplanationTaskResponseMetadata(object):
    """
    ExplanationTaskResponseMetadata.

    :attr str id: Identifier for tracking explanation task.
    :attr str created_by: ID of the user creating explanation task.
    :attr str created_at: Time when the explanation task was initiated.
    :attr str updated_at: (optional) Time when the explanation task was last updated.
    """

    def __init__(self, id, created_by, created_at, updated_at=None):
        """
        Initialize a ExplanationTaskResponseMetadata object.

        :param str id: Identifier for tracking explanation task.
        :param str created_by: ID of the user creating explanation task.
        :param str created_at: Time when the explanation task was initiated.
        :param str updated_at: (optional) Time when the explanation task was last updated.
        """
        self.id = id
        self.created_by = created_by
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExplanationTaskResponseMetadata object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ExplanationTaskResponseMetadata JSON')
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        else:
            raise ValueError('Required property \'created_by\' not present in ExplanationTaskResponseMetadata JSON')
        if 'created_at' in _dict:
            args['created_at'] = _dict.get('created_at')
        else:
            raise ValueError('Required property \'created_at\' not present in ExplanationTaskResponseMetadata JSON')
        if 'updated_at' in _dict:
            args['updated_at'] = _dict.get('updated_at')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = self.created_at
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = self.updated_at
        return _dict

    def __str__(self):
        """Return a `str` version of this ExplanationTaskResponseMetadata object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FairnessMonitoringRemediationResponse(object):
    """
    FairnessMonitoringRemediationResponse.

    :attr object fields: The fields of the model processed debias scoring.
    :attr object values: The values associated to the fields.
    """

    def __init__(self, fields, values):
        """
        Initialize a FairnessMonitoringRemediationResponse object.

        :param object fields: The fields of the model processed debias scoring.
        :param object values: The values associated to the fields.
        """
        self.fields = fields
        self.values = values

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FairnessMonitoringRemediationResponse object from a json dictionary."""
        args = {}
        if 'fields' in _dict:
            args['fields'] = _dict.get('fields')
        else:
            raise ValueError('Required property \'fields\' not present in FairnessMonitoringRemediationResponse JSON')
        if 'values' in _dict:
            args['values'] = _dict.get('values')
        else:
            raise ValueError('Required property \'values\' not present in FairnessMonitoringRemediationResponse JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'fields') and self.fields is not None:
            _dict['fields'] = self.fields
        if hasattr(self, 'values') and self.values is not None:
            _dict['values'] = self.values
        return _dict

    def __str__(self):
        """Return a `str` version of this FairnessMonitoringRemediationResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class GetExplanationTaskResponse(object):
    """
    GetExplanationTaskResponse.

    :attr ExplanationTaskResponseMetadata metadata:
    :attr ExplanationTaskResponseEntity entity:
    """

    def __init__(self, metadata, entity):
        """
        Initialize a GetExplanationTaskResponse object.

        :param ExplanationTaskResponseMetadata metadata:
        :param ExplanationTaskResponseEntity entity:
        """
        self.metadata = metadata
        self.entity = entity

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetExplanationTaskResponse object from a json dictionary."""
        args = {}
        if 'metadata' in _dict:
            args['metadata'] = ExplanationTaskResponseMetadata._from_dict(_dict.get('metadata'))
        else:
            raise ValueError('Required property \'metadata\' not present in GetExplanationTaskResponse JSON')
        if 'entity' in _dict:
            args['entity'] = ExplanationTaskResponseEntity._from_dict(_dict.get('entity'))
        else:
            raise ValueError('Required property \'entity\' not present in GetExplanationTaskResponse JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata._to_dict()
        if hasattr(self, 'entity') and self.entity is not None:
            _dict['entity'] = self.entity._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this GetExplanationTaskResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PostExplanationTaskResponse(object):
    """
    PostExplanationTaskResponse.

    :attr ExplanationTaskResponseMetadata metadata:
    :attr PostExplanationTaskResponseEntity entity:
    """

    def __init__(self, metadata, entity):
        """
        Initialize a PostExplanationTaskResponse object.

        :param ExplanationTaskResponseMetadata metadata:
        :param PostExplanationTaskResponseEntity entity:
        """
        self.metadata = metadata
        self.entity = entity

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PostExplanationTaskResponse object from a json dictionary."""
        args = {}
        if 'metadata' in _dict:
            args['metadata'] = ExplanationTaskResponseMetadata._from_dict(_dict.get('metadata'))
        else:
            raise ValueError('Required property \'metadata\' not present in PostExplanationTaskResponse JSON')
        if 'entity' in _dict:
            args['entity'] = PostExplanationTaskResponseEntity._from_dict(_dict.get('entity'))
        else:
            raise ValueError('Required property \'entity\' not present in PostExplanationTaskResponse JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata._to_dict()
        if hasattr(self, 'entity') and self.entity is not None:
            _dict['entity'] = self.entity._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this PostExplanationTaskResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PostExplanationTaskResponseEntity(object):
    """
    PostExplanationTaskResponseEntity.

    :attr PostExplanationTaskResponseEntityStatus status:
    """

    def __init__(self, status):
        """
        Initialize a PostExplanationTaskResponseEntity object.

        :param PostExplanationTaskResponseEntityStatus status:
        """
        self.status = status

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PostExplanationTaskResponseEntity object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = PostExplanationTaskResponseEntityStatus._from_dict(_dict.get('status'))
        else:
            raise ValueError('Required property \'status\' not present in PostExplanationTaskResponseEntity JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this PostExplanationTaskResponseEntity object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PostExplanationTaskResponseEntityStatus(object):
    """
    PostExplanationTaskResponseEntityStatus.

    :attr str state: (optional) Overall status of the explanation task.
    """

    def __init__(self, state=None):
        """
        Initialize a PostExplanationTaskResponseEntityStatus object.

        :param str state: (optional) Overall status of the explanation task.
        """
        self.state = state

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PostExplanationTaskResponseEntityStatus object from a json dictionary."""
        args = {}
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def __str__(self):
        """Return a `str` version of this PostExplanationTaskResponseEntityStatus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
