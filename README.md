Excel-to-Localizable.strings
=============

A Python Script for Generating Localizable.strings for iOS from Excel file

## Overview

![Sample Excel File](http://assets.vaibhavnath.com/XLS-Sampler1.png) ![Output Localizable.strings file](http://assets.vaibhavnath.com/XLS-Sampler2.png)

## Features

- Works natively on macOS as Python is pre-installed.
- Uses xlrd package which is well supported and widely used.
- Works with both New Excel file format[.xlsx], and old one[.xls].

## Usage

1. Install xlrd package on your system. **Note: Python must be installed on your system for executing this script**
	1. Navigate to the folder in which **xlrd** tarball is located. Also you can download the Updated **xlrd** tarball from <a href="https://pypi.org/project/xlrd/#files" target="_blank">this link</a>
	2. Extract the tarball using following command in terminal
	```bash
	tar -xvzf xlrd-1.1.0.tar.gz
	```
	3. Navigate to **xlrd** extracted folder
	4. Install **xlrd** package using following command in terminal
	```bash
	sudo python setup.py install
	```
2. Navigate to the directory containing your Excel file and copy xls2strings-script.py file to that directory.
	1. Delete any additional Columns and Sheets in the Excel file (Look Sample Format in excelSampler.xlsx).
3. Edit the xls2strings-script.py file according your File's Name [default is **Input-Excel-File.xlsx**] and Column titles [default are **BaseLanguage** and **LocalisedLanguage**].
4. Execute script using following command in terminal
```bash
python xls2strings-script.py
```
