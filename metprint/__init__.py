"""Print in fancy ways
"""
# pylint: disable=too-few-public-methods

from enum import Enum
class LogType(Enum):
	'''Contains logtypes for this module

	DEBUG
	Detailed information, typically of interest only when diagnosing problems.

	INFO
	Confirmation that things are working as expected.

	WARNING
	An indication that something unexpected happened, or indicative of some
	problem in the near future (e.g. ‘disk space low’). The software is still
	working as expected.

	ERROR
	Due to a more serious problem, the software has not been able to perform
	some function.

	CRITICAL
	A serious error, indicating that the program itself may be unable to
	continue running.

	'''
	NONE = 0
	BOLD = 1
	ITALIC = 2
	HEADER = 3
	DEBUG = 4
	INFO = 5
	SUCCESS = 6
	WARNING = 7
	ERROR = 8
	CRITICAL = 9


class MeterpreterFormatter():
	'''Format text in meterpreter style '''
	def __init__(self):
		self.format = {
			LogType.NONE    : "{}",
			LogType.BOLD    : "\033[01m{}\033[00m",
			LogType.ITALIC  : "\033[03m{}\033[00m",
			LogType.HEADER  : "\033[01m\033[04m{}\033[00m",
			LogType.DEBUG   : "\033[96m[$]\033[00m {}",
			LogType.INFO    : "\033[96m[*]\033[00m {}",
			LogType.SUCCESS : "\033[92m[+]\033[00m {}",
			LogType.WARNING : "\033[93m[/]\033[00m {}",
			LogType.ERROR   : "\033[91m[-]\033[00m {}",
			LogType.CRITICAL: "\033[91m[!]\033[00m {}",
		}

class FHFormatter():
	'''Format text in my own style '''
	def __init__(self):
		self.format = {
			LogType.NONE    : "{}",
			LogType.BOLD    : "\033[01m{}\033[00m",
			LogType.ITALIC  : "\033[03m{}\033[00m",
			LogType.HEADER  : "\033[01m\033[04m{}\033[00m",
			LogType.DEBUG   : "[\033[01m\033[96m$  Deb\033[00m] {}",
			LogType.INFO    : "[\033[96m* Info\033[00m] {}",
			LogType.SUCCESS : "[\033[92m+   Ok\033[00m] {}",
			LogType.WARNING : "[\033[93m/ Warn\033[00m] {}",
			LogType.ERROR   : "[\033[91m-  Err\033[00m] {}",
			LogType.CRITICAL: "[\033[01m\033[91m! Crit\033[00m] {}",
		}

class FHNFFormatter():
	'''Format text in my own style with nerd fonts'''
	def __init__(self):
		self.format = {
			LogType.NONE    : "{}",
			LogType.BOLD    : "\033[01m{}\033[00m",
			LogType.ITALIC  : "\033[03m{}\033[00m",
			LogType.HEADER  : "\033[01m\033[04m{}\033[00m",
			LogType.DEBUG   : "[\033[01m\033[96m\uf46f  Deb\033[00m] {}",
			LogType.INFO    : "[\033[96m\uf449 Info\033[00m] {}",
			LogType.SUCCESS : "[\033[92m\uf42e   Ok\033[00m] {}",
			LogType.WARNING : "[\033[93m\uf467 Warn\033[00m] {}",
			LogType.ERROR   : "[\033[91m\uf46e  Err\033[00m] {}",
			LogType.CRITICAL: "[\033[01m\033[91m\uf421 Crit\033[00m] {}",
		}

class PythonFormatter():
	'''Format text in my python logger style '''
	def __init__(self):
		self.format = {
			LogType.NONE    : "{}",
			LogType.BOLD    : "{}",
			LogType.ITALIC  : "{}",
			LogType.HEADER  : "HEADER:{}",
			LogType.DEBUG   : "DEBUG:{}",
			LogType.INFO    : "INFO:{}",
			LogType.SUCCESS : "SUCCESS:{}",
			LogType.WARNING : "WARNING:{}",
			LogType.ERROR   : "ERROR:{}",
			LogType.CRITICAL: "CRITICAL:{}",
		}

class ColorLogFormatter():
	'''Format text in colorlog style
	https://github.com/borntyping/python-colorlog
	'''
	def __init__(self):
		self.format = {
			LogType.NONE    : "{}",
			LogType.BOLD    : "\033[01m{}\033[00m",
			LogType.ITALIC  : "\033[03m{}\033[00m",
			LogType.HEADER  : "\033[01m\033[04m{}\033[00m",
			LogType.DEBUG   : "\033[36mDEBUG    \033[00m\033[34m{}\033[00m",
			LogType.INFO    : "\033[32mINFO     \033[00m\033[34m{}\033[00m",
			LogType.SUCCESS : "\033[32mSUCCESS  \033[00m\033[34m{}\033[00m",
			LogType.WARNING : "\033[33mWARNING  \033[00m\033[34m{}\033[00m",
			LogType.ERROR   : "\033[31mERROR    \033[00m\033[34m{}\033[00m",
			LogType.CRITICAL: "\033[31mCRITICAL \033[00m\033[34m{}\033[00m",
		}

class PrintTagsFormatter():
	'''Format text in PrintTag style
	https://github.com/mdlockyer/PrintTags
	Note that this project provides other functionality that this one lacks
	'''
	def __init__(self):
		self.format = {
			LogType.NONE    : "{}",
			LogType.BOLD    : "\033[01m{}\033[00m",
			LogType.ITALIC  : "\033[03m{}\033[00m",
			LogType.HEADER  : "\033[01m\033[04m{}\033[00m",
			LogType.DEBUG   : "\033[36m[debug] {}\033[00m",
			LogType.INFO    : "\033[36m[info] {}\033[00m",
			LogType.SUCCESS : "\033[32m[success] {}\033[00m",
			LogType.WARNING : "\033[35m[warn] {}\033[00m",
			LogType.ERROR   : "\033[31m[error] {}\033[00m",
			LogType.CRITICAL: "\033[31m[critical] {}\033[00m",
		}

class XaFormatter():
	'''Format text in Xa style
	https://github.com/xxczaki/xa
	'''
	def __init__(self):
		self.format = {
			LogType.NONE    : "{}",
			LogType.BOLD    : "\033[01m{}\033[00m",
			LogType.ITALIC  : "\033[03m{}\033[00m",
			LogType.HEADER  : "\033[40m\033[93m TITLE \033[00m {}",
			LogType.DEBUG   : "\033[106m DEBUG \033[00m {}",
			LogType.INFO    : "\033[106m INFO \033[00m {}",
			LogType.SUCCESS : "\033[102m\033[30m SUCCESS \033[00m {}",
			LogType.WARNING : "\033[103m\033[30m WARNING \033[00m {}",
			LogType.ERROR   : "\033[101m ERROR \033[00m {}",
			LogType.CRITICAL: "\033[101m CRITICAL \033[00m {}",
		}

class LamuFormatter():
	'''Format text in Lamu style
	https://github.com/egoist/lamu
	'''
	def __init__(self):
		self.format = {
			LogType.NONE    : "{}",
			LogType.BOLD    : "\033[01m{}\033[00m",
			LogType.ITALIC  : "\033[03m{}\033[00m",
			LogType.HEADER  : "\033[01m\033[04m{}\033[00m",
			LogType.DEBUG   : "\033[96m   debug\033[00m  : :  {}",
			LogType.INFO    : "\033[96m    info\033[00m  : :  {}",
			LogType.SUCCESS : "\033[92m success\033[00m  : :  {}",
			LogType.WARNING : "\033[93m warning\033[00m  : :  {}",
			LogType.ERROR   : "\033[91m   error\033[00m  : :  {}",
			LogType.CRITICAL: "\033[91mcritical\033[00m  : :  {}",
		}

class CustomFormatter():
	"""Create a custom formatter

	Args:
		none (str, optional): Set format for LogType.NONE.
		Defaults to "{}".
		bold (str, optional): Set format for LogType.BOLD.
		Defaults to "\033[01m{}\033[00m".
		italic (str, optional): Set format for LogType.ITALIC.
		Defaults to "\033[03m{}\033[00m".
		header (str, optional): Set format for LogType.HEADER.
		Defaults to "\033[01m\033[04m{}\033[00m".
		debug (str, optional): Set format for LogType.DEBUG.
		Defaults to "[\033[01m\033[96m$  Deb\033[00m] {}".
		info (str, optional): Set format for LogType.INFO.
		Defaults to "[\033[96m* Info\033[00m] {}".
		success (str, optional): Set format for LogType.SUCCESS.
		Defaults to "[\033[92m+   Ok\033[00m] {}".
		warning (str, optional): Set format for LogType.WARNING.
		Defaults to "[\033[93m/ Warn\033[00m] {}".
		error (str, optional): Set format for LogType.ERROR.
		Defaults to "[\033[91m-  Err\033[00m] {}".
		critical (str, optional): Set format for LogType.CRITICAL.
		Defaults to "[\033[01m\033[91m! Crit\033[00m] {}".
	"""
	def __init__(self, none="{}", bold="\033[01m{}\033[00m",
	italic="\033[03m{}\033[00m", header="\033[01m\033[04m{}\033[00m",
	debug="[\033[01m\033[96m$  Deb\033[00m] {}",
	info="[\033[96m* Info\033[00m] {}", success="[\033[92m+   Ok\033[00m] {}",
	warning="[\033[93m/ Warn\033[00m] {}", error="[\033[91m-  Err\033[00m] {}",
	critical="[\033[01m\033[91m! Crit\033[00m] {}"):
		self.format = {
			LogType.NONE: none,
			LogType.BOLD: bold,
			LogType.ITALIC: italic,
			LogType.HEADER: header,
			LogType.DEBUG: debug,
			LogType.INFO: info,
			LogType.SUCCESS: success,
			LogType.WARNING: warning,
			LogType.ERROR: error,
			LogType.CRITICAL: critical,
		}


class Logger():
	'''Setup a logger and call logPrint to print text in certian formats '''
	def __init__(self, formatter):
		self.formatter = formatter if formatter is not None else MeterpreterFormatter()

	def logPrint(self, text, logType=LogType.NONE):
		'''Print in the formatter style

		Args:
			text (str): Text to print
			logType (str, optional): How to print. Defaults to "LogType.NONE".
		'''
		print(self.formatter.format[logType] .format(text))

	def logString(self, text, logType=LogType.NONE):
		'''Get a string in the formatter style

		Args:
			text (str): Text to print
			logType (str, optional): How to print. Defaults to "LogType.NONE".
		'''
		return self.formatter.format[logType] .format(text)
