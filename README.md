# WP Media Export Sizer

Use this script to retrieve the file sizes for all media in a WordPress site.

It works by taking a WordPress export file (WXR format, from Tools > Export), then checking the file size of each media attachment in the export by executing a HEAD request on the server. Once it has each file's size, it creates a row in the output CSV with that data. The final result will be a simple spreadsheet which can be manipulated, and calculated against in any spreadsheet software.

## Requirements

* Python 3

## Usage

The script takes the import file from STDIN, and dumps the output CSV to STDOUT. Typically command line usage would be something like this:

```
python sizer.py < import_file.xml > summary.csv
```

If you're on a Mac, make sure to use the correct version of python (might be `python3` instead of `python`).

## Issues

The script is not fast--it issues HTTP requests synchronously, blocking until the response is received. This may take a few hours on larger sites. This does have the unintended side effect ofeffectively rate-limiting requests to reduce server load, though.