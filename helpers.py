def get_input(string):
	''' Get input from console regardless of python 2 or 3 '''
	try:
		return raw_input(string)
	except:
		return input(string)

def get_config():
	''' Create a config parser for reading INI files '''
	try:
		import ConfigParser
		return ConfigParser.ConfigParser()
	except:
		import configparser
		return configparser.ConfigParser()