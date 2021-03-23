import importlib
import logging
import jsonpickle
import json
import os
import unittest
import sys
from unittest import mock
from aws_xray_sdk import global_sdk_config
global_sdk_config.set_sdk_enabled(False)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
function = __import__('lambda_function')
handler = function.lambda_handler

with open('bucket-name.txt','r') as f:
  bucket = f.read()

@mock.patch.dict(os.environ, {"bucket": bucket})
class TestFunction(unittest.TestCase):

  def test_function(self):
    stream_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stream_handler)
    with open('event.json','rb') as f:
      event = jsonpickle.decode(bytearray(f.read()))
      context = {'requestid' : '1234'}
      result = handler(event, context)
      print(str(result))
      self.assertRegex(str(result), 's3://lookoutmetrics-dataset', 'Should match')
    logger.removeHandler(stream_handler)

  def test_backfill(self):
    stream_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stream_handler)
    with open('event-backfill.json','rb') as f:
      event = jsonpickle.decode(bytearray(f.read()))
      context = {'requestid' : '1234'}
      result = handler(event, context)
      print(str(result))
      self.assertRegex(str(result), 's3://lookoutmetrics-dataset', 'Should match')
    logger.removeHandler(stream_handler)

if __name__ == '__main__':
    unittest.main()