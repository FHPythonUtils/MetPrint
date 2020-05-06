<a name=".lazytest"></a>
## lazytest

Test metprint LAZY_PRINT and donations

<a name=".make"></a>
## make

Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build

<a name=".metprint"></a>
## metprint

Print in fancy ways

<a name=".metprint.LogType"></a>
### LogType

```python
class LogType(Enum)
```

Contains logtypes for this module

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

<a name=".metprint.MeterpreterFormatter"></a>
### MeterpreterFormatter

```python
class MeterpreterFormatter():
 |  MeterpreterFormatter()
```

Format text in meterpreter style

<a name=".metprint.FHFormatter"></a>
### FHFormatter

```python
class FHFormatter():
 |  FHFormatter()
```

Format text in my own style

<a name=".metprint.FHNFFormatter"></a>
### FHNFFormatter

```python
class FHNFFormatter():
 |  FHNFFormatter()
```

Format text in my own style with nerd fonts

<a name=".metprint.PythonFormatter"></a>
### PythonFormatter

```python
class PythonFormatter():
 |  PythonFormatter()
```

Format text in my python logger style

<a name=".metprint.ColorLogFormatter"></a>
### ColorLogFormatter

```python
class ColorLogFormatter():
 |  ColorLogFormatter()
```

Format text in colorlog style
https://github.com/borntyping/python-colorlog

<a name=".metprint.PrintTagsFormatter"></a>
### PrintTagsFormatter

```python
class PrintTagsFormatter():
 |  PrintTagsFormatter()
```

Format text in PrintTag style
https://github.com/mdlockyer/PrintTags
Note that this project provides other functionality that this one lacks

<a name=".metprint.XaFormatter"></a>
### XaFormatter

```python
class XaFormatter():
 |  XaFormatter()
```

Format text in Xa style
https://github.com/xxczaki/xa

<a name=".metprint.LamuFormatter"></a>
### LamuFormatter

```python
class LamuFormatter():
 |  LamuFormatter()
```

Format text in Lamu style
https://github.com/egoist/lamu

<a name=".metprint.CustomFormatter"></a>
### CustomFormatter

```python
class CustomFormatter():
 |  CustomFormatter(none="{}", bold="\033[01m{}\033[00m", italic="\033[03m{}\033[00m", header="\033[01m\033[04m{}\033[00m", debug="[\033[01m\033[96m$  Deb\033[00m] {}", info="[\033[36m* Info\033[00m] {}", success="[\033[32m+   Ok\033[00m] {}", warning="[\033[33m/ Warn\033[00m] {}", error="[\033[31m-  Err\033[00m] {}", critical="[\033[01m\033[91m! Crit\033[00m] {}")
```

Create a custom formatter

**Arguments**:

- `none` _str, optional_ - Set format for LogType.NONE.
  Defaults to "{}".
- `bold` _str, optional_ - Set format for LogType.BOLD.
  Defaults to "\033[01m{}\033[00m".
- `italic` _str, optional_ - Set format for LogType.ITALIC.
  Defaults to "\033[03m{}\033[00m".
- `header` _str, optional_ - Set format for LogType.HEADER.
  Defaults to "\033[01m\033[04m{}\033[00m".
- `debug` _str, optional_ - Set format for LogType.DEBUG.
  Defaults to "[\033[01m\033[96m$  Deb\033[00m] {}".
- `info` _str, optional_ - Set format for LogType.INFO.
  Defaults to "[\033[96m* Info\033[00m] {}".
- `success` _str, optional_ - Set format for LogType.SUCCESS.
  Defaults to "[\033[92m+   Ok\033[00m] {}".
- `warning` _str, optional_ - Set format for LogType.WARNING.
  Defaults to "[\033[93m/ Warn\033[00m] {}".
- `error` _str, optional_ - Set format for LogType.ERROR.
  Defaults to "[\033[91m-  Err\033[00m] {}".
- `critical` _str, optional_ - Set format for LogType.CRITICAL.
  Defaults to "[\033[01m\033[91m! Crit\033[00m] {}".

<a name=".metprint.Logger"></a>
### Logger

```python
class Logger():
 |  Logger(formatter=MeterpreterFormatter())
```

Setup a logger and call logPrint to print text in certian formats

<a name=".metprint.Logger.logPrint"></a>
#### logPrint

```python
 | logPrint(text, logType=LogType.NONE)
```

Print in the formatter style

**Arguments**:

- `text` _str_ - Text to print
- `logType` _str, optional_ - How to print. Defaults to "LogType.NONE".

<a name=".metprint.Logger.logString"></a>
#### logString

```python
 | logString(text, logType=LogType.NONE)
```

Get a string in the formatter style

**Arguments**:

- `text` _str_ - Text to print
- `logType` _str, optional_ - How to print. Defaults to "LogType.NONE".

