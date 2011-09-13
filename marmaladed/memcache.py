import re, telnetlib

class MemcacheOutput:
    CONSOLE, VALUE = range(2)

class Memcache:

	_client = None
	_output_mode = MemcacheOutput.CONSOLE
	
	def __init__(self, host='localhost', port='11211'):
		self._host = host
		self._port = port

	@property
	def client(self):
		if self._client is None:
			self._client = telnetlib.Telnet(self._host, self._port)
		return self._client
		
	@property
	def outputmode(self):
		return self._output_mode
	
	@outputmode.setter
	def outputmode(self, value):
		self._output_mode = value

	def stats(self, stat_args = None):
		if not stat_args:
			self.client.write("stats\n")
		else:
			self.client.write('stats %s\n' % stat_args)
		response = self.client.expect(["ERROR", "CLIENT_ERROR", "END", "SERVER_ERROR"])[2]
		if self.outputmode == MemcacheOutput.CONSOLE:
			return response
		else:
			data = {}
			lines = response.splitlines()
			for line in lines:
				if not line or line.strip() == 'END': break
				stats = line.split(' ', 2)
				data[stats[1]] = stats[2]
			return data
		
	def delete(self, del_args = None):
		if del_args:
			self.client.write('delete %s\n' % del_args)
			if not "noreply" in del_args:
				return self.client.expect(["ERROR", "CLIENT_ERROR", "DELETED", "NOT_FOUND", "SERVER_ERROR"])[2]
			else:
				return ""
		else:
			return "ERROR"
			
	def get(self, get_args = None):
		if get_args:
			self.client.write('get %s\n' % get_args)
			return self.client.expect(["ERROR", "CLIENT_ERROR", "END", "SERVER_ERROR"])[2]
		else:
			return "ERROR"
			
	def storage(self, command, args = None, value = None):
		if args and value:
			self.client.write('%s %s\r\n%s\r\n' % (command, args, value))
			if not "noreply" in args:
				return self.client.expect(["ERROR", "CLIENT_ERROR", "STORED", "NOT_STORED", "EXISTS", "NOT_FOUND", "SERVER_ERROR"])[2]
			else:
				return ""
		else:
			return "ERROR"
			
	def close(self):
		self.client.close()