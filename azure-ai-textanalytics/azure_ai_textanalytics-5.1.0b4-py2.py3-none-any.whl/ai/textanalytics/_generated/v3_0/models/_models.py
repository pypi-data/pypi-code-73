# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class DetectedLanguage(msrest.serialization.Model):
    """DetectedLanguage.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Long name of a detected language (e.g. English, French).
    :type name: str
    :param iso6391_name: Required. A two letter representation of the detected language according
     to the ISO 639-1 standard (e.g. en, fr).
    :type iso6391_name: str
    :param confidence_score: Required. A confidence score between 0 and 1. Scores close to 1
     indicate 100% certainty that the identified language is true.
    :type confidence_score: float
    """

    _validation = {
        'name': {'required': True},
        'iso6391_name': {'required': True},
        'confidence_score': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'iso6391_name': {'key': 'iso6391Name', 'type': 'str'},
        'confidence_score': {'key': 'confidenceScore', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DetectedLanguage, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.iso6391_name = kwargs['iso6391_name']
        self.confidence_score = kwargs['confidence_score']


class DocumentEntities(msrest.serialization.Model):
    """DocumentEntities.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Unique, non-empty document identifier.
    :type id: str
    :param entities: Required. Recognized entities in the document.
    :type entities: list[~azure.ai.textanalytics.v3_0.models.Entity]
    :param warnings: Required. Warnings encountered while processing document.
    :type warnings: list[~azure.ai.textanalytics.v3_0.models.TextAnalyticsWarning]
    :param statistics: if showStats=true was specified in the request this field will contain
     information about the document payload.
    :type statistics: ~azure.ai.textanalytics.v3_0.models.DocumentStatistics
    """

    _validation = {
        'id': {'required': True},
        'entities': {'required': True},
        'warnings': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'entities': {'key': 'entities', 'type': '[Entity]'},
        'warnings': {'key': 'warnings', 'type': '[TextAnalyticsWarning]'},
        'statistics': {'key': 'statistics', 'type': 'DocumentStatistics'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DocumentEntities, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.entities = kwargs['entities']
        self.warnings = kwargs['warnings']
        self.statistics = kwargs.get('statistics', None)


class DocumentError(msrest.serialization.Model):
    """DocumentError.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Document Id.
    :type id: str
    :param error: Required. Document Error.
    :type error: ~azure.ai.textanalytics.v3_0.models.TextAnalyticsError
    """

    _validation = {
        'id': {'required': True},
        'error': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'error': {'key': 'error', 'type': 'TextAnalyticsError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DocumentError, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.error = kwargs['error']


class DocumentKeyPhrases(msrest.serialization.Model):
    """DocumentKeyPhrases.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Unique, non-empty document identifier.
    :type id: str
    :param key_phrases: Required. A list of representative words or phrases. The number of key
     phrases returned is proportional to the number of words in the input document.
    :type key_phrases: list[str]
    :param warnings: Required. Warnings encountered while processing document.
    :type warnings: list[~azure.ai.textanalytics.v3_0.models.TextAnalyticsWarning]
    :param statistics: if showStats=true was specified in the request this field will contain
     information about the document payload.
    :type statistics: ~azure.ai.textanalytics.v3_0.models.DocumentStatistics
    """

    _validation = {
        'id': {'required': True},
        'key_phrases': {'required': True},
        'warnings': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'key_phrases': {'key': 'keyPhrases', 'type': '[str]'},
        'warnings': {'key': 'warnings', 'type': '[TextAnalyticsWarning]'},
        'statistics': {'key': 'statistics', 'type': 'DocumentStatistics'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DocumentKeyPhrases, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.key_phrases = kwargs['key_phrases']
        self.warnings = kwargs['warnings']
        self.statistics = kwargs.get('statistics', None)


class DocumentLanguage(msrest.serialization.Model):
    """DocumentLanguage.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Unique, non-empty document identifier.
    :type id: str
    :param detected_language: Required. Detected Language.
    :type detected_language: ~azure.ai.textanalytics.v3_0.models.DetectedLanguage
    :param warnings: Required. Warnings encountered while processing document.
    :type warnings: list[~azure.ai.textanalytics.v3_0.models.TextAnalyticsWarning]
    :param statistics: if showStats=true was specified in the request this field will contain
     information about the document payload.
    :type statistics: ~azure.ai.textanalytics.v3_0.models.DocumentStatistics
    """

    _validation = {
        'id': {'required': True},
        'detected_language': {'required': True},
        'warnings': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'detected_language': {'key': 'detectedLanguage', 'type': 'DetectedLanguage'},
        'warnings': {'key': 'warnings', 'type': '[TextAnalyticsWarning]'},
        'statistics': {'key': 'statistics', 'type': 'DocumentStatistics'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DocumentLanguage, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.detected_language = kwargs['detected_language']
        self.warnings = kwargs['warnings']
        self.statistics = kwargs.get('statistics', None)


class DocumentLinkedEntities(msrest.serialization.Model):
    """DocumentLinkedEntities.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Unique, non-empty document identifier.
    :type id: str
    :param entities: Required. Recognized well-known entities in the document.
    :type entities: list[~azure.ai.textanalytics.v3_0.models.LinkedEntity]
    :param warnings: Required. Warnings encountered while processing document.
    :type warnings: list[~azure.ai.textanalytics.v3_0.models.TextAnalyticsWarning]
    :param statistics: if showStats=true was specified in the request this field will contain
     information about the document payload.
    :type statistics: ~azure.ai.textanalytics.v3_0.models.DocumentStatistics
    """

    _validation = {
        'id': {'required': True},
        'entities': {'required': True},
        'warnings': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'entities': {'key': 'entities', 'type': '[LinkedEntity]'},
        'warnings': {'key': 'warnings', 'type': '[TextAnalyticsWarning]'},
        'statistics': {'key': 'statistics', 'type': 'DocumentStatistics'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DocumentLinkedEntities, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.entities = kwargs['entities']
        self.warnings = kwargs['warnings']
        self.statistics = kwargs.get('statistics', None)


class DocumentSentiment(msrest.serialization.Model):
    """DocumentSentiment.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Unique, non-empty document identifier.
    :type id: str
    :param sentiment: Required. Predicted sentiment for document (Negative, Neutral, Positive, or
     Mixed). Possible values include: "positive", "neutral", "negative", "mixed".
    :type sentiment: str or ~azure.ai.textanalytics.v3_0.models.DocumentSentimentValue
    :param statistics: if showStats=true was specified in the request this field will contain
     information about the document payload.
    :type statistics: ~azure.ai.textanalytics.v3_0.models.DocumentStatistics
    :param confidence_scores: Required. Document level sentiment confidence scores between 0 and 1
     for each sentiment class.
    :type confidence_scores: ~azure.ai.textanalytics.v3_0.models.SentimentConfidenceScorePerLabel
    :param sentences: Required. Sentence level sentiment analysis.
    :type sentences: list[~azure.ai.textanalytics.v3_0.models.SentenceSentiment]
    :param warnings: Required. Warnings encountered while processing document.
    :type warnings: list[~azure.ai.textanalytics.v3_0.models.TextAnalyticsWarning]
    """

    _validation = {
        'id': {'required': True},
        'sentiment': {'required': True},
        'confidence_scores': {'required': True},
        'sentences': {'required': True},
        'warnings': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'sentiment': {'key': 'sentiment', 'type': 'str'},
        'statistics': {'key': 'statistics', 'type': 'DocumentStatistics'},
        'confidence_scores': {'key': 'confidenceScores', 'type': 'SentimentConfidenceScorePerLabel'},
        'sentences': {'key': 'sentences', 'type': '[SentenceSentiment]'},
        'warnings': {'key': 'warnings', 'type': '[TextAnalyticsWarning]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DocumentSentiment, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.sentiment = kwargs['sentiment']
        self.statistics = kwargs.get('statistics', None)
        self.confidence_scores = kwargs['confidence_scores']
        self.sentences = kwargs['sentences']
        self.warnings = kwargs['warnings']


class DocumentStatistics(msrest.serialization.Model):
    """if showStats=true was specified in the request this field will contain information about the document payload.

    All required parameters must be populated in order to send to Azure.

    :param characters_count: Required. Number of text elements recognized in the document.
    :type characters_count: int
    :param transactions_count: Required. Number of transactions for the document.
    :type transactions_count: int
    """

    _validation = {
        'characters_count': {'required': True},
        'transactions_count': {'required': True},
    }

    _attribute_map = {
        'characters_count': {'key': 'charactersCount', 'type': 'int'},
        'transactions_count': {'key': 'transactionsCount', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DocumentStatistics, self).__init__(**kwargs)
        self.characters_count = kwargs['characters_count']
        self.transactions_count = kwargs['transactions_count']


class EntitiesResult(msrest.serialization.Model):
    """EntitiesResult.

    All required parameters must be populated in order to send to Azure.

    :param documents: Required. Response by document.
    :type documents: list[~azure.ai.textanalytics.v3_0.models.DocumentEntities]
    :param errors: Required. Errors by document id.
    :type errors: list[~azure.ai.textanalytics.v3_0.models.DocumentError]
    :param statistics: if showStats=true was specified in the request this field will contain
     information about the request payload.
    :type statistics: ~azure.ai.textanalytics.v3_0.models.RequestStatistics
    :param model_version: Required. This field indicates which model is used for scoring.
    :type model_version: str
    """

    _validation = {
        'documents': {'required': True},
        'errors': {'required': True},
        'model_version': {'required': True},
    }

    _attribute_map = {
        'documents': {'key': 'documents', 'type': '[DocumentEntities]'},
        'errors': {'key': 'errors', 'type': '[DocumentError]'},
        'statistics': {'key': 'statistics', 'type': 'RequestStatistics'},
        'model_version': {'key': 'modelVersion', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EntitiesResult, self).__init__(**kwargs)
        self.documents = kwargs['documents']
        self.errors = kwargs['errors']
        self.statistics = kwargs.get('statistics', None)
        self.model_version = kwargs['model_version']


class Entity(msrest.serialization.Model):
    """Entity.

    All required parameters must be populated in order to send to Azure.

    :param text: Required. Entity text as appears in the request.
    :type text: str
    :param category: Required. Entity type, such as Person/Location/Org/SSN etc.
    :type category: str
    :param subcategory: Entity sub type, such as Age/Year/TimeRange etc.
    :type subcategory: str
    :param offset: Required. Start position (in Unicode characters) for the entity text.
    :type offset: int
    :param length: Required. Length (in Unicode characters) for the entity text.
    :type length: int
    :param confidence_score: Required. Confidence score between 0 and 1 of the extracted entity.
    :type confidence_score: float
    """

    _validation = {
        'text': {'required': True},
        'category': {'required': True},
        'offset': {'required': True},
        'length': {'required': True},
        'confidence_score': {'required': True},
    }

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
        'subcategory': {'key': 'subcategory', 'type': 'str'},
        'offset': {'key': 'offset', 'type': 'int'},
        'length': {'key': 'length', 'type': 'int'},
        'confidence_score': {'key': 'confidenceScore', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Entity, self).__init__(**kwargs)
        self.text = kwargs['text']
        self.category = kwargs['category']
        self.subcategory = kwargs.get('subcategory', None)
        self.offset = kwargs['offset']
        self.length = kwargs['length']
        self.confidence_score = kwargs['confidence_score']


class EntityLinkingResult(msrest.serialization.Model):
    """EntityLinkingResult.

    All required parameters must be populated in order to send to Azure.

    :param documents: Required. Response by document.
    :type documents: list[~azure.ai.textanalytics.v3_0.models.DocumentLinkedEntities]
    :param errors: Required. Errors by document id.
    :type errors: list[~azure.ai.textanalytics.v3_0.models.DocumentError]
    :param statistics: if showStats=true was specified in the request this field will contain
     information about the request payload.
    :type statistics: ~azure.ai.textanalytics.v3_0.models.RequestStatistics
    :param model_version: Required. This field indicates which model is used for scoring.
    :type model_version: str
    """

    _validation = {
        'documents': {'required': True},
        'errors': {'required': True},
        'model_version': {'required': True},
    }

    _attribute_map = {
        'documents': {'key': 'documents', 'type': '[DocumentLinkedEntities]'},
        'errors': {'key': 'errors', 'type': '[DocumentError]'},
        'statistics': {'key': 'statistics', 'type': 'RequestStatistics'},
        'model_version': {'key': 'modelVersion', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EntityLinkingResult, self).__init__(**kwargs)
        self.documents = kwargs['documents']
        self.errors = kwargs['errors']
        self.statistics = kwargs.get('statistics', None)
        self.model_version = kwargs['model_version']


class ErrorResponse(msrest.serialization.Model):
    """ErrorResponse.

    All required parameters must be populated in order to send to Azure.

    :param error: Required. Document Error.
    :type error: ~azure.ai.textanalytics.v3_0.models.TextAnalyticsError
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'TextAnalyticsError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs['error']


class InnerError(msrest.serialization.Model):
    """InnerError.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. Error code. Possible values include: "invalidParameterValue",
     "invalidRequestBodyFormat", "emptyRequest", "missingInputRecords", "invalidDocument",
     "modelVersionIncorrect", "invalidDocumentBatch", "unsupportedLanguageCode",
     "invalidCountryHint".
    :type code: str or ~azure.ai.textanalytics.v3_0.models.InnerErrorCodeValue
    :param message: Required. Error message.
    :type message: str
    :param details: Error details.
    :type details: dict[str, str]
    :param target: Error target.
    :type target: str
    :param innererror: Inner error contains more specific information.
    :type innererror: ~azure.ai.textanalytics.v3_0.models.InnerError
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '{str}'},
        'target': {'key': 'target', 'type': 'str'},
        'innererror': {'key': 'innererror', 'type': 'InnerError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(InnerError, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.details = kwargs.get('details', None)
        self.target = kwargs.get('target', None)
        self.innererror = kwargs.get('innererror', None)


class KeyPhraseResult(msrest.serialization.Model):
    """KeyPhraseResult.

    All required parameters must be populated in order to send to Azure.

    :param documents: Required. Response by document.
    :type documents: list[~azure.ai.textanalytics.v3_0.models.DocumentKeyPhrases]
    :param errors: Required. Errors by document id.
    :type errors: list[~azure.ai.textanalytics.v3_0.models.DocumentError]
    :param statistics: if showStats=true was specified in the request this field will contain
     information about the request payload.
    :type statistics: ~azure.ai.textanalytics.v3_0.models.RequestStatistics
    :param model_version: Required. This field indicates which model is used for scoring.
    :type model_version: str
    """

    _validation = {
        'documents': {'required': True},
        'errors': {'required': True},
        'model_version': {'required': True},
    }

    _attribute_map = {
        'documents': {'key': 'documents', 'type': '[DocumentKeyPhrases]'},
        'errors': {'key': 'errors', 'type': '[DocumentError]'},
        'statistics': {'key': 'statistics', 'type': 'RequestStatistics'},
        'model_version': {'key': 'modelVersion', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(KeyPhraseResult, self).__init__(**kwargs)
        self.documents = kwargs['documents']
        self.errors = kwargs['errors']
        self.statistics = kwargs.get('statistics', None)
        self.model_version = kwargs['model_version']


class LanguageBatchInput(msrest.serialization.Model):
    """LanguageBatchInput.

    All required parameters must be populated in order to send to Azure.

    :param documents: Required.
    :type documents: list[~azure.ai.textanalytics.v3_0.models.LanguageInput]
    """

    _validation = {
        'documents': {'required': True},
    }

    _attribute_map = {
        'documents': {'key': 'documents', 'type': '[LanguageInput]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(LanguageBatchInput, self).__init__(**kwargs)
        self.documents = kwargs['documents']


class LanguageInput(msrest.serialization.Model):
    """LanguageInput.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Unique, non-empty document identifier.
    :type id: str
    :param text: Required.
    :type text: str
    :param country_hint:
    :type country_hint: str
    """

    _validation = {
        'id': {'required': True},
        'text': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'country_hint': {'key': 'countryHint', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(LanguageInput, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.text = kwargs['text']
        self.country_hint = kwargs.get('country_hint', None)


class LanguageResult(msrest.serialization.Model):
    """LanguageResult.

    All required parameters must be populated in order to send to Azure.

    :param documents: Required. Response by document.
    :type documents: list[~azure.ai.textanalytics.v3_0.models.DocumentLanguage]
    :param errors: Required. Errors by document id.
    :type errors: list[~azure.ai.textanalytics.v3_0.models.DocumentError]
    :param statistics: if showStats=true was specified in the request this field will contain
     information about the request payload.
    :type statistics: ~azure.ai.textanalytics.v3_0.models.RequestStatistics
    :param model_version: Required. This field indicates which model is used for scoring.
    :type model_version: str
    """

    _validation = {
        'documents': {'required': True},
        'errors': {'required': True},
        'model_version': {'required': True},
    }

    _attribute_map = {
        'documents': {'key': 'documents', 'type': '[DocumentLanguage]'},
        'errors': {'key': 'errors', 'type': '[DocumentError]'},
        'statistics': {'key': 'statistics', 'type': 'RequestStatistics'},
        'model_version': {'key': 'modelVersion', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(LanguageResult, self).__init__(**kwargs)
        self.documents = kwargs['documents']
        self.errors = kwargs['errors']
        self.statistics = kwargs.get('statistics', None)
        self.model_version = kwargs['model_version']


class LinkedEntity(msrest.serialization.Model):
    """LinkedEntity.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Entity Linking formal name.
    :type name: str
    :param matches: Required. List of instances this entity appears in the text.
    :type matches: list[~azure.ai.textanalytics.v3_0.models.Match]
    :param language: Required. Language used in the data source.
    :type language: str
    :param id: Unique identifier of the recognized entity from the data source.
    :type id: str
    :param url: Required. URL for the entity's page from the data source.
    :type url: str
    :param data_source: Required. Data source used to extract entity linking, such as Wiki/Bing
     etc.
    :type data_source: str
    """

    _validation = {
        'name': {'required': True},
        'matches': {'required': True},
        'language': {'required': True},
        'url': {'required': True},
        'data_source': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'matches': {'key': 'matches', 'type': '[Match]'},
        'language': {'key': 'language', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'data_source': {'key': 'dataSource', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(LinkedEntity, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.matches = kwargs['matches']
        self.language = kwargs['language']
        self.id = kwargs.get('id', None)
        self.url = kwargs['url']
        self.data_source = kwargs['data_source']


class Match(msrest.serialization.Model):
    """Match.

    All required parameters must be populated in order to send to Azure.

    :param confidence_score: Required. If a well-known item is recognized, a decimal number
     denoting the confidence level between 0 and 1 will be returned.
    :type confidence_score: float
    :param text: Required. Entity text as appears in the request.
    :type text: str
    :param offset: Required. Start position (in Unicode characters) for the entity match text.
    :type offset: int
    :param length: Required. Length (in Unicode characters) for the entity match text.
    :type length: int
    """

    _validation = {
        'confidence_score': {'required': True},
        'text': {'required': True},
        'offset': {'required': True},
        'length': {'required': True},
    }

    _attribute_map = {
        'confidence_score': {'key': 'confidenceScore', 'type': 'float'},
        'text': {'key': 'text', 'type': 'str'},
        'offset': {'key': 'offset', 'type': 'int'},
        'length': {'key': 'length', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Match, self).__init__(**kwargs)
        self.confidence_score = kwargs['confidence_score']
        self.text = kwargs['text']
        self.offset = kwargs['offset']
        self.length = kwargs['length']


class MultiLanguageBatchInput(msrest.serialization.Model):
    """Contains a set of input documents to be analyzed by the service.

    All required parameters must be populated in order to send to Azure.

    :param documents: Required. The set of documents to process as part of this batch.
    :type documents: list[~azure.ai.textanalytics.v3_0.models.MultiLanguageInput]
    """

    _validation = {
        'documents': {'required': True},
    }

    _attribute_map = {
        'documents': {'key': 'documents', 'type': '[MultiLanguageInput]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MultiLanguageBatchInput, self).__init__(**kwargs)
        self.documents = kwargs['documents']


class MultiLanguageInput(msrest.serialization.Model):
    """Contains an input document to be analyzed by the service.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. A unique, non-empty document identifier.
    :type id: str
    :param text: Required. The input text to process.
    :type text: str
    :param language: (Optional) This is the 2 letter ISO 639-1 representation of a language. For
     example, use "en" for English; "es" for Spanish etc. If not set, use "en" for English as
     default.
    :type language: str
    """

    _validation = {
        'id': {'required': True},
        'text': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MultiLanguageInput, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.text = kwargs['text']
        self.language = kwargs.get('language', None)


class RequestStatistics(msrest.serialization.Model):
    """if showStats=true was specified in the request this field will contain information about the request payload.

    All required parameters must be populated in order to send to Azure.

    :param documents_count: Required. Number of documents submitted in the request.
    :type documents_count: int
    :param valid_documents_count: Required. Number of valid documents. This excludes empty, over-
     size limit or non-supported languages documents.
    :type valid_documents_count: int
    :param erroneous_documents_count: Required. Number of invalid documents. This includes empty,
     over-size limit or non-supported languages documents.
    :type erroneous_documents_count: int
    :param transactions_count: Required. Number of transactions for the request.
    :type transactions_count: long
    """

    _validation = {
        'documents_count': {'required': True},
        'valid_documents_count': {'required': True},
        'erroneous_documents_count': {'required': True},
        'transactions_count': {'required': True},
    }

    _attribute_map = {
        'documents_count': {'key': 'documentsCount', 'type': 'int'},
        'valid_documents_count': {'key': 'validDocumentsCount', 'type': 'int'},
        'erroneous_documents_count': {'key': 'erroneousDocumentsCount', 'type': 'int'},
        'transactions_count': {'key': 'transactionsCount', 'type': 'long'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RequestStatistics, self).__init__(**kwargs)
        self.documents_count = kwargs['documents_count']
        self.valid_documents_count = kwargs['valid_documents_count']
        self.erroneous_documents_count = kwargs['erroneous_documents_count']
        self.transactions_count = kwargs['transactions_count']


class SentenceSentiment(msrest.serialization.Model):
    """SentenceSentiment.

    All required parameters must be populated in order to send to Azure.

    :param text: Required. The sentence text.
    :type text: str
    :param sentiment: Required. The predicted Sentiment for the sentence. Possible values include:
     "positive", "neutral", "negative".
    :type sentiment: str or ~azure.ai.textanalytics.v3_0.models.SentenceSentimentValue
    :param confidence_scores: Required. The sentiment confidence score between 0 and 1 for the
     sentence for all classes.
    :type confidence_scores: ~azure.ai.textanalytics.v3_0.models.SentimentConfidenceScorePerLabel
    :param offset: Required. The sentence offset from the start of the document.
    :type offset: int
    :param length: Required. The length of the sentence by Unicode standard.
    :type length: int
    """

    _validation = {
        'text': {'required': True},
        'sentiment': {'required': True},
        'confidence_scores': {'required': True},
        'offset': {'required': True},
        'length': {'required': True},
    }

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'sentiment': {'key': 'sentiment', 'type': 'str'},
        'confidence_scores': {'key': 'confidenceScores', 'type': 'SentimentConfidenceScorePerLabel'},
        'offset': {'key': 'offset', 'type': 'int'},
        'length': {'key': 'length', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SentenceSentiment, self).__init__(**kwargs)
        self.text = kwargs['text']
        self.sentiment = kwargs['sentiment']
        self.confidence_scores = kwargs['confidence_scores']
        self.offset = kwargs['offset']
        self.length = kwargs['length']


class SentimentConfidenceScorePerLabel(msrest.serialization.Model):
    """Represents the confidence scores between 0 and 1 across all sentiment classes: positive, neutral, negative.

    All required parameters must be populated in order to send to Azure.

    :param positive: Required.
    :type positive: float
    :param neutral: Required.
    :type neutral: float
    :param negative: Required.
    :type negative: float
    """

    _validation = {
        'positive': {'required': True},
        'neutral': {'required': True},
        'negative': {'required': True},
    }

    _attribute_map = {
        'positive': {'key': 'positive', 'type': 'float'},
        'neutral': {'key': 'neutral', 'type': 'float'},
        'negative': {'key': 'negative', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SentimentConfidenceScorePerLabel, self).__init__(**kwargs)
        self.positive = kwargs['positive']
        self.neutral = kwargs['neutral']
        self.negative = kwargs['negative']


class SentimentResponse(msrest.serialization.Model):
    """SentimentResponse.

    All required parameters must be populated in order to send to Azure.

    :param documents: Required. Sentiment analysis per document.
    :type documents: list[~azure.ai.textanalytics.v3_0.models.DocumentSentiment]
    :param errors: Required. Errors by document id.
    :type errors: list[~azure.ai.textanalytics.v3_0.models.DocumentError]
    :param statistics: if showStats=true was specified in the request this field will contain
     information about the request payload.
    :type statistics: ~azure.ai.textanalytics.v3_0.models.RequestStatistics
    :param model_version: Required. This field indicates which model is used for scoring.
    :type model_version: str
    """

    _validation = {
        'documents': {'required': True},
        'errors': {'required': True},
        'model_version': {'required': True},
    }

    _attribute_map = {
        'documents': {'key': 'documents', 'type': '[DocumentSentiment]'},
        'errors': {'key': 'errors', 'type': '[DocumentError]'},
        'statistics': {'key': 'statistics', 'type': 'RequestStatistics'},
        'model_version': {'key': 'modelVersion', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SentimentResponse, self).__init__(**kwargs)
        self.documents = kwargs['documents']
        self.errors = kwargs['errors']
        self.statistics = kwargs.get('statistics', None)
        self.model_version = kwargs['model_version']


class TextAnalyticsError(msrest.serialization.Model):
    """TextAnalyticsError.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. Error code. Possible values include: "invalidRequest",
     "invalidArgument", "internalServerError", "serviceUnavailable".
    :type code: str or ~azure.ai.textanalytics.v3_0.models.ErrorCodeValue
    :param message: Required. Error message.
    :type message: str
    :param target: Error target.
    :type target: str
    :param innererror: Inner error contains more specific information.
    :type innererror: ~azure.ai.textanalytics.v3_0.models.InnerError
    :param details: Details about specific errors that led to this reported error.
    :type details: list[~azure.ai.textanalytics.v3_0.models.TextAnalyticsError]
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'innererror': {'key': 'innererror', 'type': 'InnerError'},
        'details': {'key': 'details', 'type': '[TextAnalyticsError]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TextAnalyticsError, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)
        self.innererror = kwargs.get('innererror', None)
        self.details = kwargs.get('details', None)


class TextAnalyticsWarning(msrest.serialization.Model):
    """TextAnalyticsWarning.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. Error code. Possible values include: "LongWordsInDocument",
     "DocumentTruncated".
    :type code: str or ~azure.ai.textanalytics.v3_0.models.WarningCodeValue
    :param message: Required. Warning message.
    :type message: str
    :param target_ref: A JSON pointer reference indicating the target object.
    :type target_ref: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target_ref': {'key': 'targetRef', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TextAnalyticsWarning, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target_ref = kwargs.get('target_ref', None)
