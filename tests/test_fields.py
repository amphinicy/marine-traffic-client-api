import unittest
import marinetrafficapi.fields as fields
from marinetrafficapi.models import Model

class TestResponse(unittest.TestCase):

    def test_NumberField(self):
        field = fields.NumberField('dummy_index')

        self.assertRaises(ValueError,field._convert_field_item,'')


    def test_RealNumberField(self):
        field = fields.RealNumberField('dummy_index')
        self.assertRaises(ValueError,field._convert_field_item,'')


    def test_BooleanField(self):
        field = fields.BooleanField('dummy_index')
        self.assertRaises(ValueError,field._convert_field_item,'')


    def test_DatetimeField(self):
        field = fields.DatetimeField('dummy_index')
        self.assertRaises(ValueError,field._convert_field_item,'',format='%Y-%m-%d %H:%M:%S')


    def test_LinestringField(self):
        field = fields.LinestringField('dummy_index')
        self.assertRaises(ValueError,field._convert_field_item,'')
