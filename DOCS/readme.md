Module metprint
===============
Print in fancy ways

Functions
---------

    
`LAZY_PRINT(text: str, logType: LogType = LogType.NONE, indentPlain: bool = False)`
:   Print in the formatter style
    
    Args:
            text (str): Text to print
            logType (LogType, optional): How to print. Defaults to "LogType.NONE".
            indentPlain (bool, optional): Indent for 'plain' formats (None,
            Bold, Italic, and Header). Defaults to False

Classes
-------

`ColorLogFormatter()`
:   Format text in colorlog style
    https://github.com/borntyping/python-colorlog

    ### Ancestors (in MRO)

    * metprint.Formatter

`CustomFormatter(none: str = '{}', bold: str = '\x1b[01m{}\x1b[00m', italic: str = '\x1b[03m{}\x1b[00m', header: str = '\x1b[01m\x1b[04m{}\x1b[00m', debug: str = '[\x1b[01m\x1b[96m$  Deb\x1b[00m] {}', info: str = '[\x1b[36m* Info\x1b[00m] {}', success: str = '[\x1b[32m+   Ok\x1b[00m] {}', warning: str = '[\x1b[33m/ Warn\x1b[00m] {}', error: str = '[\x1b[31m-  Err\x1b[00m] {}', critical: str = '[\x1b[01m\x1b[91m! Crit\x1b[00m] {}', indentPlain: int = 9)`
:   Create a custom formatter
    
    Args:
            none (str, optional): Set format for LogType.NONE.
            Defaults to "{}".
            bold (str, optional): Set format for LogType.BOLD.
            Defaults to "[01m{}[00m".
            italic (str, optional): Set format for LogType.ITALIC.
            Defaults to "[03m{}[00m".
            header (str, optional): Set format for LogType.HEADER.
            Defaults to "[01m[04m{}[00m".
            debug (str, optional): Set format for LogType.DEBUG.
            Defaults to "[[01m[96m$  Deb[00m] {}".
            info (str, optional): Set format for LogType.INFO.
            Defaults to "[[96m* Info[00m] {}".
            success (str, optional): Set format for LogType.SUCCESS.
            Defaults to "[[92m+   Ok[00m] {}".
            warning (str, optional): Set format for LogType.WARNING.
            Defaults to "[[93m/ Warn[00m] {}".
            error (str, optional): Set format for LogType.ERROR.
            Defaults to "[[91m-  Err[00m] {}".
            critical (str, optional): Set format for LogType.CRITICAL.
            Defaults to "[[01m[91m! Crit[00m] {}".
            indentPlain (int, optional): Set indent for 'plain' formats (None,
            Bold, Italic, and Header). Defaults to 9

    ### Ancestors (in MRO)

    * metprint.Formatter

`FHFormatter()`
:   Format text in my own style

    ### Ancestors (in MRO)

    * metprint.Formatter

`FHNFFormatter()`
:   Format text in my own style with nerd fonts

    ### Ancestors (in MRO)

    * metprint.Formatter

`Formatter()`
:   Format text in meterpreter style

    ### Descendants

    * metprint.ColorLogFormatter
    * metprint.CustomFormatter
    * metprint.FHFormatter
    * metprint.FHNFFormatter
    * metprint.LamuFormatter
    * metprint.MeterpreterFormatter
    * metprint.PrintTagsFormatter
    * metprint.PythonFormatter
    * metprint.XaFormatter

`LamuFormatter()`
:   Format text in Lamu style
    https://github.com/egoist/lamu

    ### Ancestors (in MRO)

    * metprint.Formatter

`LogType(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   Contains logtypes for this module
    
    NONE
    No special formatting
    
    BOLD
    Bold text
    
    ITALIC
    Italic text
    
    HEADER
    Some form of heading
    
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
    
    INDENT
    Stores the indent for NONE, BOLD, ITALIC, HEADER

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `BOLD`
    :

    `CRITICAL`
    :

    `DEBUG`
    :

    `ERROR`
    :

    `HEADER`
    :

    `INDENT`
    :

    `INFO`
    :

    `ITALIC`
    :

    `NONE`
    :

    `SUCCESS`
    :

    `WARNING`
    :

`Logger(formatter: Formatter = <metprint.MeterpreterFormatter object>)`
:   Setup a logger and call logPrint to print text in certian formats

    ### Methods

    `logPrint(self, text: str, logType: LogType = LogType.NONE, indentPlain: bool = False)`
    :   Print in the formatter style
        
        Args:
                text (str): Text to print
                logType (LogType, optional): How to print. Defaults to "LogType.NONE".
                indentPlain (bool, optional): Indent for 'plain' formats (None,
                Bold, Italic, and Header). Defaults to False

    `logString(self, text: str, logType: LogType = LogType.NONE, indentPlain: bool = False) ‑> str`
    :   Get a string in the formatter style
        
        Args:
                text (str): Text to print
                logType (LogType, optional): How to print. Defaults to "LogType.NONE".
                indentPlain (bool, optional): Indent for 'plain' formats (None,
                Bold, Italic, and Header). Defaults to False

`MeterpreterFormatter()`
:   Format text in meterpreter style

    ### Ancestors (in MRO)

    * metprint.Formatter

`PrintTagsFormatter()`
:   Format text in PrintTag style
    https://github.com/mdlockyer/PrintTags
    Note that this project provides other functionality that this one lacks

    ### Ancestors (in MRO)

    * metprint.Formatter

`PythonFormatter()`
:   Format text in my python logger style

    ### Ancestors (in MRO)

    * metprint.Formatter

`XaFormatter()`
:   Format text in Xa style
    https://github.com/xxczaki/xa

    ### Ancestors (in MRO)

    * metprint.Formatter