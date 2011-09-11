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

	def stats(self, stat_args = None):
		if not stat_args:
			self.client.write("stats\n")
		else:
			self.client.write('stats %s\n' % stat_args)
		return self.client.expect(["ERROR", "END"])[2]
		
	def delete(self, del_args):
		if del_args:
			self.client.write('delete %s\n' % del_args)
			if not "noreply" in del_args:
				return self.client.expect(["ERROR", "DELETED", "NOT_FOUND"])[2]
			else:
				return ""
		else:
			return "ERROR"

	def close(self):
		self.client.close()