
from ctypes import *
import os

UCI_LIB_LOCATION = '../uci/libuci.so'
STRUCT_LIST = ['uci_context',
					'uci_package',
					'uci_list',
					'uci_element',
					'uci_backend',
					'uci_section',
					'uci_opton',
					'uci_hook',
					'uci_plugin']

class value_indll(Structure):
	_fields_ = [("name", c_char_p),
		("code", POINTER(c_ubyte)),
		("size", c_int)]

def value(name):
	val_ptr = POINTER(value_indll)
	return val_ptr

def get_structs():
	struct_dict = {}
	for name in STRUCT_LIST:
		struct_dict[name] = value(name)
	return struct_dict

def init_lib(lib_path=UCI_LIB_LOCATION):
	global lib
	lib = ctypes.CDLL(lib_path)

def _safe_path(path):
	if os.path.exists(path) and os.isdir(path):
		return True
	return False

def _is_context(context):
	if type(context) == int: return True
	return False

def alloc_context():
	'''struct uci_context *uci_alloc_context(void)'''
	return_value = lib.uci_alloc_context()
	return return_value

def free_context(context):
	'''void uci_free_context(struct uci_context *ctx)'''
	if _is_context(context):
		lib.uci_free_context(context)
	return

def set_confdir(context, directory):
	'''int uci_set_confdir(struct uci_context *ctx, const char *dir)'''
	if _is_context(context) and _safe_dir(directory):
		lib.set_confdir(context, directory)
	return

def parse_error(context, message):
	'''void uci_perror(struct uci_context *ctx, const char *str)'''
	if _is_context(context):
		lib.uci_perror(context, message)
	return

def get_error_string(context, dest, prefix):
	'''void uci_get_errorstr(struct uci_context *ctx, char **dest, const char *prefix)'''
	if _is_context(context):
		lib.uci_get_errorstr(context, dest, prefix)
	return

def list_configs(context, configs=[]):
	'''int uci_list_configs(struct uci_context *ctx, char ***list)'''
	if _is_context(context):
		return_value = lib.uci_list_configs(context, configs)
	return return_value

def commit(context, package, overwrite):
	'''int uci_commit(struct uci_context *ctx, struct uci_package **package, bool overwrite)'''
	if _is_context(context):
		return_value = lib.uci_commit(context, package, overwrite)
	return return_value

def load(context, name, package):
	'''int uci_load(struct uci_context *ctx, const char *name, struct uci_package **package)'''
	if _is_context(context):
		return_value = lib.uci_load(context, name, package)
		return return_value
	return None

# PLUGIN STUFF '#ifdef UCI_PLUGIN_SUPPORT'
def add_backend(context, backend):
	'''__plugin int uci_add_backend(struct uci_context *ctx, struct uci_backend *b)'''
	if _is_context(context):
		return_value = lib.uci_add_backend(context, backend)
		return return_value
	return None

def del_backend(context, backend):
	'''__plugin int uci_del_backend(struct uci_context *ctx, struct uci_backend *b)'''
	if _is_context(context):
		return_value = lib.uci_del_backend(context, backend)
		return return_value
	return None

def set_backend(context, name):
	'''int uci_set_backend(struct uci_context *ctx, const char *name)'''
	if _is_context(context):
		return_value = lib.uci_set_backend(context, name)
		return return_value
	return None

def add_hook(context, hook_ops):
	'''int uci_add_hook(struct uci_context *ctx, const struct uci_hook_ops *ops)'''
	if _is_context(context):
		return_value = lib.uci_add_hook(context, hook_ops)
		return return_value
	return None

def remove_hook(context, hook_ops):
	'''int uci_remove_hook(struct uci_context *ctx, const struct uci_hook_ops *ops)'''
	if _is_context(context):
		return_value = lib.uci_remove_hook(context, hook_ops)
		return return_value
	return None

def load_plugin(context, file_name):
	'''int uci_load_plugin(struct uci_context *ctx, const char *filename)'''
	if _is_context(context):
		return_value = lib.uci_load_plugin(context, file_name)
		return return_value
	return None

def unload_plugin(context, plugin):
	'''static void uci_unload_plugin(struct uci_context *ctx, struct uci_plugin *p)'''
	if _is_context(context):
		lib.uci_unload_plugin(context, plugin)
	return None

def load_plugins(context, pattern):
	'''int uci_load_plugins(struct uci_context *ctx, const char *pattern)'''
	if _is_context(context):
		return_value = lib.uci_load_plugins(context, pattern)
		return return_value
	return None

