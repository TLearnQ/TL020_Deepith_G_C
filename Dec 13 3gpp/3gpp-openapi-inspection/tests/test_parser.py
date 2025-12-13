import json
from pathlib import Path
from src.parser import extract_metadata
def test_extract_metadata_minimal():
    spec = {
        'openapi': '3.0.0',
        'info': {'title': 'test'},
        'paths': {
            '/hello': {'get': {'responses': {'200': {'description': 'OK'}}}}
        }
    }
    meta = extract_metadata(spec)
    assert meta['openapi'] == '3.0.0'
    assert '/hello' in meta['paths']
    assert 'get' in meta['paths']['/hello']
