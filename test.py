"""Test metprint
"""
from metprint import (
	LogType,
	Logger,
	MeterpreterFormatter,
	FHFormatter,
	PythonFormatter,
	ColorLogFormatter,
	PrintTagsFormatter,
	CustomFormatter,
)


print("#########################")
print("#      Meterpreter      #")
print("#########################")
metLogger = Logger(MeterpreterFormatter())
metLogger.logPrint("none", LogType.NONE)
metLogger.logPrint("bold", LogType.BOLD)
metLogger.logPrint("debug", LogType.DEBUG)
metLogger.logPrint("info", LogType.INFO)
metLogger.logPrint("success", LogType.SUCCESS)
metLogger.logPrint("warning", LogType.WARNING)
metLogger.logPrint("error", LogType.ERROR)
metLogger.logPrint("critical", LogType.CRITICAL)


print("#########################")
print("#          FH           #")
print("#########################")
fhLogger = Logger(FHFormatter())
fhLogger.logPrint("none", LogType.NONE)
fhLogger.logPrint("bold", LogType.BOLD)
fhLogger.logPrint("debug", LogType.DEBUG)
fhLogger.logPrint("info", LogType.INFO)
fhLogger.logPrint("success", LogType.SUCCESS)
fhLogger.logPrint("warning", LogType.WARNING)
fhLogger.logPrint("error", LogType.ERROR)
fhLogger.logPrint("critical", LogType.CRITICAL)

print("#########################")
print("#        Python         #")
print("#########################")
pythonLogger = Logger(PythonFormatter())
pythonLogger.logPrint("none", LogType.NONE)
pythonLogger.logPrint("bold", LogType.BOLD)
pythonLogger.logPrint("debug", LogType.DEBUG)
pythonLogger.logPrint("info", LogType.INFO)
pythonLogger.logPrint("success", LogType.SUCCESS)
pythonLogger.logPrint("warning", LogType.WARNING)
pythonLogger.logPrint("error", LogType.ERROR)
pythonLogger.logPrint("critical", LogType.CRITICAL)

print("#########################")
print("#       ColorLog        #")
print("#########################")
colorLogLogger = Logger(ColorLogFormatter())
colorLogLogger.logPrint("none", LogType.NONE)
colorLogLogger.logPrint("bold", LogType.BOLD)
colorLogLogger.logPrint("debug", LogType.DEBUG)
colorLogLogger.logPrint("info", LogType.INFO)
colorLogLogger.logPrint("success", LogType.SUCCESS)
colorLogLogger.logPrint("warning", LogType.WARNING)
colorLogLogger.logPrint("error", LogType.ERROR)
colorLogLogger.logPrint("critical", LogType.CRITICAL)

print("#########################")
print("#       PrintTags       #")
print("#########################")
printTagsLogger = Logger(PrintTagsFormatter())
printTagsLogger.logPrint("none", LogType.NONE)
printTagsLogger.logPrint("bold", LogType.BOLD)
printTagsLogger.logPrint("debug", LogType.DEBUG)
printTagsLogger.logPrint("info", LogType.INFO)
printTagsLogger.logPrint("success", LogType.SUCCESS)
printTagsLogger.logPrint("warning", LogType.WARNING)
printTagsLogger.logPrint("error", LogType.ERROR)
printTagsLogger.logPrint("critical", LogType.CRITICAL)

print("#########################")
print("#        Custom         #")
print("#########################")
customLogger = Logger(CustomFormatter())
customLogger.logPrint("none", LogType.NONE)
customLogger.logPrint("bold", LogType.BOLD)
customLogger.logPrint("debug", LogType.DEBUG)
customLogger.logPrint("info", LogType.INFO)
customLogger.logPrint("success", LogType.SUCCESS)
customLogger.logPrint("warning", LogType.WARNING)
customLogger.logPrint("error", LogType.ERROR)
customLogger.logPrint("critical", LogType.CRITICAL)
