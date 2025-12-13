import requests
import json
from logger_setup import get_logger
from errors import APIResponseError

logger = get_logger('api-client')

class APIClient:
    def __init__(self, base_url, timeout=10, auth=None, headers=None):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.auth = auth
        self.headers = headers or {'Accept': 'application/json'}

    def _full_url(self, path):
        if path.startswith('http'):
            return path
        return f"{self.base_url}{path if path.startswith('/') else '/' + path}"

    def get(self, path, params=None, headers=None):
        url = self._full_url(path)
        h = self.headers.copy()
        if headers:
            h.update(headers)
        logger.info("HTTP GET", extra={'url': url, 'params': params})
        resp = requests.get(url, params=params, timeout=self.timeout, auth=self.auth, headers=h)
        return self._handle_response(resp)

    def post(self, path, json_body=None, headers=None):
        url = self._full_url(path)
        h = self.headers.copy()
        if headers:
            h.update(headers)
        logger.info("HTTP POST", extra={'url': url})
        resp = requests.post(url, json=json_body, timeout=self.timeout, auth=self.auth, headers=h)
        return self._handle_response(resp)

    def _handle_response(self, resp: requests.Response):
        log_extra = {
            'status_code': resp.status_code,
            'url': resp.url,
            'headers': dict(resp.headers.get('content-type',''))
        }
        try:
            body = resp.json()
            log_extra['body_preview'] = body if isinstance(body, (dict,list)) else str(body)[:200]
        except Exception:
            log_extra['body_preview'] = resp.text[:200]
        logger.info("HTTP Response", extra=log_extra)
        if resp.status_code >= 400:
            raise APIResponseError(status_code=resp.status_code, url=resp.url, message=resp.text, payload=resp.text)
        return resp
