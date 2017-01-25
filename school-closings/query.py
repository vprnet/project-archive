#!/usr/bin/python
import json
import requests
import gspread
from PIL import Image
from PIL import ImageOps
import urllib
import os
import markdown
from bs4 import BeautifulSoup as Soup
from datetime import datetime
from cStringIO import StringIO
from config import NPR_API_KEY, ABSOLUTE_PATH
from oauth2client.client import SignedJwtAssertionCredentials

def convert_date(timestamp):
    """Converts API timestamp to publication-ready dateline"""

    day = timestamp[5:7]
    month = datetime.strptime(timestamp[8:11], '%b').strftime('%B')
    year = timestamp[12:16]
    date = month + ' ' + day + ", " + year
    return date

def get_google_sheet():
    json_key = json.load(open('homepage.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(json_key["client_email"], json_key['private_key'], scope)
    authorization = gspread.authorize(credentials)
    spreadsheet = authorization.open("VPR Homepage App")
    worksheet = spreadsheet.get_worksheet(1)

    return worksheet.get_all_records()


def get_callout(sheet_key):
    callout = get_google_sheet()
    md = callout[0]['Text']
    if md:
        html = markdown.markdown(md)
    else:
        html = False
    return html
