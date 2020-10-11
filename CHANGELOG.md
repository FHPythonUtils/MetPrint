# Changelog
All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2020.7.1 - 2020/10/11
- Actually drop the versions in pyproject.toml

## 2020.7 - 2020/10/11
- Added typing (so dropping python < 3.7)
- Added indent for 'plain' formats (None, Bold, Italic, and Header)
- Updated docs

## 2020.6.1 - 2020/05/06
- Updated classifiers
- Added docs

## 2020.6 - 2020/04/24
- New LAZY_PRINT function to make the lives of those who do not wish to
initialize a logger just to print that bit easier.
- Customize the LAZY_PRINT function with `builtins.METPRINT_LAZY_FORMATTER`
- Show dependencies or your own project some love by setting a dictionary of
projects and donation URLs to `builtins.METPRINT_DONATIONS`

## 2020.5 - 2020/04/19
- Build with poetry and dephell

## 2020.4 - 2020/03/28
- Use Logger without formatter defaults to MeterpreterFormatter

## 2020.3 - 2020/03/26
- Colour improvements to MeterpreterFormatter, FHFormatter, FHNFFormatter,
XaFormatter and LamuFormatter

## 2020.2 - 2020/03/26
- Added FHNFFormatter
- Updated readme

## 2020.1 - 2020/03/25
- Added XaFormatter and LamuFormatter
- Added LogType.ITALIC and LogType.HEADER
- Added logger.logString to return a string (write to file/ print)

## 2020 - 2020/03/25
- First release
