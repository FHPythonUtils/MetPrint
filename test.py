#!/usr/bin/env python3
"""Test metprint
"""
from metprint import (
	LogType,
	Logger,
	#MeterpreterFormatter,
	FHFormatter,
	FHNFFormatter,
	PythonFormatter,
	ColorLogFormatter,
	PrintTagsFormatter,
	XaFormatter,
	LamuFormatter,
	CustomFormatter,
)

from io import StringIO
import sys
from pathlib import Path
from ansitoimg.render import ansiToSVG
result = StringIO()
oldStdout = sys.stdout
sys.stdout = result
THISDIR = str(Path(__file__).resolve().parent)

print("#########################")
print("#      Meterpreter      #")
print("#########################")
metLogger = Logger()
metLogger.logPrint("none", LogType.NONE)
metLogger.logPrint("bold indent", LogType.BOLD, True)
metLogger.logPrint("italic indent", LogType.ITALIC, True)
metLogger.logPrint("header", LogType.HEADER)
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
fhLogger.logPrint("bold indent", LogType.BOLD, True)
fhLogger.logPrint("italic indent", LogType.ITALIC, True)
fhLogger.logPrint("header", LogType.HEADER)
fhLogger.logPrint("debug", LogType.DEBUG)
fhLogger.logPrint("info", LogType.INFO)
fhLogger.logPrint("success", LogType.SUCCESS)
fhLogger.logPrint("warning", LogType.WARNING)
fhLogger.logPrint("error", LogType.ERROR)
fhLogger.logPrint("critical", LogType.CRITICAL)

print("#########################")
print("#         FHNF          #")
print("#########################")
fhnfLogger = Logger(FHNFFormatter())
fhnfLogger.logPrint("none", LogType.NONE)
fhnfLogger.logPrint("bold indent", LogType.BOLD, True)
fhnfLogger.logPrint("italic indent", LogType.ITALIC, True)
fhnfLogger.logPrint("header", LogType.HEADER)
fhnfLogger.logPrint("debug", LogType.DEBUG)
fhnfLogger.logPrint("info", LogType.INFO)
fhnfLogger.logPrint("success", LogType.SUCCESS)
fhnfLogger.logPrint("warning", LogType.WARNING)
fhnfLogger.logPrint("error", LogType.ERROR)
fhnfLogger.logPrint("critical", LogType.CRITICAL)

print("#########################")
print("#        Python         #")
print("#########################")
pythonLogger = Logger(PythonFormatter())
pythonLogger.logPrint("none", LogType.NONE)
pythonLogger.logPrint("bold indent", LogType.BOLD, True)
pythonLogger.logPrint("italic indent", LogType.ITALIC, True)
pythonLogger.logPrint("header", LogType.HEADER)
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
colorLogLogger.logPrint("bold indent", LogType.BOLD, True)
colorLogLogger.logPrint("italic indent", LogType.ITALIC, True)
colorLogLogger.logPrint("header", LogType.HEADER)
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
printTagsLogger.logPrint("bold indent", LogType.BOLD, True)
printTagsLogger.logPrint("italic indent", LogType.ITALIC, True)
printTagsLogger.logPrint("header", LogType.HEADER)
printTagsLogger.logPrint("debug", LogType.DEBUG)
printTagsLogger.logPrint("info", LogType.INFO)
printTagsLogger.logPrint("success", LogType.SUCCESS)
printTagsLogger.logPrint("warning", LogType.WARNING)
printTagsLogger.logPrint("error", LogType.ERROR)
printTagsLogger.logPrint("critical", LogType.CRITICAL)

print("#########################")
print("#          Xa           #")
print("#########################")
xaLogger = Logger(XaFormatter())
xaLogger.logPrint("none", LogType.NONE)
xaLogger.logPrint("bold indent", LogType.BOLD, True)
xaLogger.logPrint("italic indent", LogType.ITALIC, True)
xaLogger.logPrint("header", LogType.HEADER)
xaLogger.logPrint("debug", LogType.DEBUG)
xaLogger.logPrint("info", LogType.INFO)
xaLogger.logPrint("success", LogType.SUCCESS)
xaLogger.logPrint("warning", LogType.WARNING)
xaLogger.logPrint("error", LogType.ERROR)
xaLogger.logPrint("critical", LogType.CRITICAL)

print("#########################")
print("#         Lamu          #")
print("#########################")
lamuLogger = Logger(LamuFormatter())
lamuLogger.logPrint("none", LogType.NONE)
lamuLogger.logPrint("bold indent", LogType.BOLD, True)
lamuLogger.logPrint("italic indent", LogType.ITALIC, True)
lamuLogger.logPrint("header", LogType.HEADER)
lamuLogger.logPrint("debug", LogType.DEBUG)
lamuLogger.logPrint("info", LogType.INFO)
lamuLogger.logPrint("success", LogType.SUCCESS)
lamuLogger.logPrint("warning", LogType.WARNING)
lamuLogger.logPrint("error", LogType.ERROR)
lamuLogger.logPrint("critical", LogType.CRITICAL)

print("#########################")
print("#        Custom         #")
print("#########################")
customLogger = Logger(CustomFormatter())
customLogger.logPrint("none", LogType.NONE)
customLogger.logPrint("bold indent", LogType.BOLD, True)
customLogger.logPrint("italic indent", LogType.ITALIC, True)
customLogger.logPrint("header", LogType.HEADER)
customLogger.logPrint("debug", LogType.DEBUG)
customLogger.logPrint("info", LogType.INFO)
customLogger.logPrint("success", LogType.SUCCESS)
customLogger.logPrint("warning", LogType.WARNING)
customLogger.logPrint("error", LogType.ERROR)
customLogger.logPrint("critical", LogType.CRITICAL)

textStream = result.getvalue()
ansiToSVG(textStream, THISDIR + "/readme-assets/screenshots/screenshot-0.svg")
print(textStream, file=oldStdout)
