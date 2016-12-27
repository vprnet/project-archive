import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

def get_underwriter_sheet():
    json_key = json.load(open('underwriter_access.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
    authorization = gspread.authorize(credentials)
    spreadsheet = authorization.open('Underwriter Directory')
    worksheet = spreadsheet.get_worksheet(0)

    return worksheet.get_all_records()

def get_pledge_sheet():
    json_key = json.load(open('pledge_and_prize_access.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
    authorization = gspread.authorize(credentials)
    spreadsheet = authorization.open('Support Pages')
    worksheet = spreadsheet.get_worksheet(0)

    return worksheet.get_all_records()

def get_prize_sheet():
    json_key = json.load(open('pledge_and_prize_access.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
    authorization = gspread.authorize(credentials)
    spreadsheet = authorization.open('Support Pages')
    worksheet = spreadsheet.get_worksheet(1)

    return worksheet.get_all_records()
