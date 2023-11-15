import json
from fieldInterface import FieldInterface
import re

class Measure(FieldInterface):
    def __init__(self, fieldItem, table):
        super().__init__(fieldItem, table)
        self.itemType = "calculated"
        self.expression = fieldItem["expression"]
        matches = re.findall('(([\w_]+)\[([\w ]+)\])', self.expression)
        if matches and len(matches) > 1:
            raise Exception("{} uses two fields".format(self))
        elif matches:
            self.fromTable = matches[0][1]
            self.fromField = matches[0][2]
            if table.name.lower() != self.fromTable.lower():
                raise Exception("Table {} for {} is different ".format(self.fromTable, self))
            for field in table.fields:
                if field.name.lower() == self.fromField.lower():
                    self.field = field