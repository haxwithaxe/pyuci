
import libuci

_structs = libuci.get_structs()

def struct(name):
	if name in _structs:
		return _structs[name]
	return None

class UCI(object):
	def __init__(self, config_dir='/etc/conf', lib='/opt/byzantium/lib/libuci.so'):
		self.config_dir = config_dir
		self.context = libuci.alloc_context()

	def initialize(self):
		self.set_confdir(self.config_dir)
	
	def free_context(self):
		libuci.free_context(self.context)

	def set_confdir(self, directory):
		libuci.set_confdir(self.context, directory)

	def parse_error(self, message):
		libuci.parse_error(self.context, message)

	def get_error_string(self, dest, prefix):
		libuci.get_error_string(self.context, dest, prefix)

	def list_configs(self, configs=[]):
		return libuci.list_configs(self.context, configs)

	def commit(self, package, overwrite):
		return libuci.commit(self.context, package, overwrite)

	def load(self, name, package):
		return libuci.load(self.context, name, package)

	# PLUGIN STUFF '#ifdef UCI_PLUGIN_SUPPORT'
	def add_backend(self, backend):
		return libuci.add_backend(backend)

	def del_backend(self, backend):
		return libuci.del_backend(self.context, backend)

	def set_backend(self, name):
		return libuci.set_backend(self.context, name)

	def add_hook(self, hook_ops):
		return libuci.add_hook(self.context, hook_ops)

	def remove_hook(self, hook_ops):
		return libuci.remove_hook(self.context, hook_ops)

	def load_plugin(self, file_name):
		return libuci.load_plugin(self.context, file_name)

	def unload_plugin(self, plugin):
		libuci.unload_plugin(self.context, plugin)

	def load_plugins(self, pattern):
		return libuci.load_plugins(self.context, pattern)

def test():
	import unittest
	class OOUCITest(unittest.TestCase):
		def setUp(self):
			self.test_dir = 'test'
			self.uci = UCI(config_dir=self.test_dir, lib='../uci/libuci.so')
			self.package_name = 'testing'
			self.config_list = ['istest','isreally','iswin']
			self.make_fake_configs()

		def tearDown(self):
			self.uci.free_context()

		def make_fake_configs(self):
			pass

	class initialize(OOUCITest):
		def runTest(self):
			self.uci.initialize()
	
	class free_context(OOUCITest):
		def runTest(self):
			self.uci.free_context()

	class set_confdir(OOUCITest):
		def runTest(self):
			self.uci.set_confdir(self.test_dir)

	class parse_error(OOUCITest):
		def runTest(self):
			self.uci.parse_error(self.message)

	class load(OOUCITest):
		def runTest(self):
			self.package = struct('uci_package')
			self.uci.load(self.context, self.package_name, self.package)

	class get_error_string(OOUCITest):
		def runTest(self):
			self.uci.get_error_string(dest, prefix)

	class list_configs(OOUCITest):
		def runTest(self):
			self.uci.list_configs(self.config_list)

	class commit(OOUCITest):
		def runTest(self):
			self.uci.commit(self.package, True)


if __name__ == '__main__':
	test()

