import json
from fieldInterface import FieldInterface

class Field(FieldInterface):
    def __init__(self, fieldItem, table):
        super().__init__(fieldItem, table)
        self.dataType = fieldItem["dataType"]
        self.summarizeBy = fieldItem["summarizeBy"]
        self.sourceColumnName = fieldItem["sourceColumn"]
        self.sourceProviderType = fieldItem["sourceProviderType"]