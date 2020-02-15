# Monoply

#### Author: Derek Daniels

## Purpose:
Retrieve student loan balances from different loan providers

## Settings
Security questions are configured in the `settings.py` in a dictionary for easy lookup.  
In order to save to a Google sheet you must setup the Google Sheets API. You can follow this [article](https://towardsdatascience.com/accessing-google-spreadsheet-data-using-python-90a5bc214fd2) for more information

## Usage
```bash
read -s DISCOVER_PASS
export DISCOVER_PASS
python monoply.py --discover-user jane_done -s
# 1234.56
```
