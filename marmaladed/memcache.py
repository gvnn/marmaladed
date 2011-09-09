import re, telnetlib

class Memcache:

	_client = None
	
	def __init__(self, host='localhost', port='11211'):
		self._host = host
		self._port = port

	@property
	def client(self):
		if self._client is None:
			self._client = telnetlib.Telnet(self._host, self._port)
		return self._client

	def command(self, cmd):
		self.client.write("%s\n" % cmd)
		return self.client.read_until('STORED')

	def close(self):
		self.client.close()