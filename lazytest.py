#!/usr/bin/env python3
"""Test metprint LAZY_PRINT and donations
"""
import builtins

# Show some love to 'Test'
builtins.METPRINT_DONATIONS = {"Test": "Test URL"}
# Set this if you want to set the LAZY_PRINT formatter
builtins.METPRINT_LAZY_FORMATTER = "FHFormatter"

from metprint import LAZY_PRINT, LogType

print("#########################")
print("#      FHFormatter      #")
print("#########################")
# You will still need LogType for this
LAZY_PRINT("none", LogType.NONE)
LAZY_PRINT("bold", LogType.BOLD)
LAZY_PRINT("italic", LogType.ITALIC)
LAZY_PRINT("header", LogType.HEADER)
LAZY_PRINT("debug", LogType.DEBUG)
LAZY_PRINT("info", LogType.INFO)
LAZY_PRINT("success", LogType.SUCCESS)
LAZY_PRINT("warning", LogType.WARNING)
LAZY_PRINT("error", LogType.ERROR)
LAZY_PRINT("critical", LogType.CRITICAL)

# Test that the donations message is not triggered again
#pylint: disable=unused-import
import metprint
