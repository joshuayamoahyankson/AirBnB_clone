import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.model = BaseModel()
     def test_instance_creation(self):
        """Test if instance is created properly"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_unique_id(self):
        """Test if each instance has a unique id"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_str_method(self):
        """Test the string representation of the instance"""
        expected_str = f"{self.model.__class__.__name__}, {self.model.id}, {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_save_method(self):
        """Test if updated_at is updated on save"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertGreater(self.model.updated_at, old_updated_at)

     def test_to_dict_method(self):
        """Test conversion to dictionary"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
    def test_kwargs_initialization(self):
        """Test initialization with kwargs"""
        id = str(uuid.uuid4())
        created_at = datetime.now().isoformat()
        updated_at = datetime.now().isoformat()
        kwargs = {
                'id': id,
                'created_at': created_at,
                'updated_at': updated_at,
                '__class__': 'BaseModel'
            }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, id)
        self.assertEqual(model.created_at.isoformat(), created_at)
        self.assertEqual(model.updated_at.isoformat(), updated_at)

if __name__ == '__main__':
    unittest.main()
                                                            }
