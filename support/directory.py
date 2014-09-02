from config import GOOGLE_SPREADSHEET_USER, GOOGLE_SPREADSHEET_PASSWORD, GOOGLE_SPREADSHEET_SOURCE, ABSOLUTE_PATH
from google_spreadsheet.api import SpreadsheetAPI
from operator import itemgetter
from datetime import datetime
from slugify import slugify
from time import sleep
import requests
import json

api = SpreadsheetAPI(GOOGLE_SPREADSHEET_USER, GOOGLE_SPREADSHEET_PASSWORD, GOOGLE_SPREADSHEET_SOURCE)

uw_json_f = ABSOLUTE_PATH + 'uw.json'


def get_underwriters():
    """Grab the Underwiter spreadsheet on Google Drive, look it see if it's been
    recently modified, if it has, remove entries that have been deleted, add new
    entries, and check for any changes to existing entries. Saves the results
    locally."""

    # get list of underwriters (as dictionaries) from GDrive (no coords)
    sheet = api.get_worksheet('tJ1HhJM7AFoUFP8t8EwgTLg', 'od6')
    new_underwriters = sheet.get_rows()

    # get cached version of UW listings, which include coords
    with open(uw_json_f, 'r') as f:
        old_underwriters = json.load(f)

    # create a dict of new UW listings to compare against old, no coords
    new_uw_dict = {}
    for new_uw in new_underwriters:
        new_uw_dict[new_uw['name']] = new_uw

    # create a dict of old values to compare to new data
    uw_dict = {}
    for old_uw in old_underwriters:
        # only add UWs currently on SS
        if old_uw['name'] in new_uw_dict:
            uw_dict[old_uw['name']] = old_uw

    # check to see what has changed. If something changed, copy and get coords
    for name, underwriter in new_uw_dict.iteritems():
        if name in uw_dict:
            if underwriter['lastupdated'] == uw_dict[name]['lastupdated']:
                continue
            else:
                print "Modified: ", underwriter['name']
                uw_dict[name] = underwriter
                lat, lng = get_coords(underwriter['address'], underwriter['zip'])
                uw_dict[name]['lat'], uw_dict[name]['lng'] = lat, lng
                uw_dict[name]['url'] = add_http(uw_dict[name]['url'])
        else:
            print "Added: ", underwriter['name']
            lat, lng = get_coords(underwriter['address'], underwriter['zip'])
            uw_dict[name] = underwriter
            uw_dict[name]['lat'] = lat
            uw_dict[name]['lng'] = lng
            uw_dict[name]['url'] = add_http(uw_dict[name]['url'])

    uw_list = json.dumps(sorted([v for k, v in uw_dict.iteritems()], key=itemgetter('name')))

    with open(uw_json_f, 'w') as uw_file:
        uw_file.write(uw_list)

    return uw_list


def add_http(url):
    """All URLs need http:// since they'll turn into hrefs on the page"""
    if url and "http://" not in url:
        url = "http://" + url
    return url


def get_uw(letter=None):
    """If this function is being called to generate the main directory, check
    cached directory against Google Sheet. Otherwise, use the cached version"""

    if not letter:
        get_underwriters()

    with(open(uw_json_f, 'r')) as f:
        underwriters = json.load(f)

    if letter:
        uw_by_letter = [uw for uw in underwriters if uw['letter'] == letter]
        underwriters = uw_by_letter

    locations = [[str(uw['name']), uw['lat'], uw['lng']] for uw in underwriters]

    return underwriters, locations


def get_pledge_content():
    sheet = api.get_worksheet('tR3nxBDe7HBQMaFtU2gg44w', 'od6')
    pledge_sheet = sheet.get_rows()
    header = pledge_sheet[0]['header']
    header_content = pledge_sheet[0]['headercontent']
    image = pledge_sheet[0]['image']
    return header, header_content, image


def get_prize_content():
    sheet = api.get_worksheet('tR3nxBDe7HBQMaFtU2gg44w', 'od7')
    prize_sheet = sheet.get_rows()
    header = prize_sheet[0]['header']
    header_content = prize_sheet[0]['headercontent']
    image = prize_sheet[0]['socialimage']

    del prize_sheet[0]

    prize_list = []
    for prize in prize_sheet:
        prize_object = {}
        title = prize['prizetitle']
        description = prize['description']
        prize_img = prize['imageurl']
        try:
            date_object = datetime.strptime(prize['date'], '%m/%d/%Y %H:%M:%S')
            date = datetime.strftime(date_object, '%A, %B %d').lstrip('0')
            time = datetime.strftime(date_object, '%I%p').lstrip('0')
        except TypeError:
            date, time = False, False
        try:
            date2_object = datetime.strptime(prize['additionaldate'], '%m/%d/%Y %H:%M:%S')
            now = datetime.now()
            if date2_object < now:
                date2, time2 = False, False
            else:
                date2 = datetime.strftime(date2_object, '%A, %B %d').lstrip('0')
                time2 = datetime.strftime(date2_object, '%I%p').lstrip('0')
        except TypeError:
            date2, time2 = False, False
        winners = prize['winners']
        prize_object = {'title': title,
                'description': description,
                'img': prize_img,
                'date': date,
                'time': time,
                'date2': date2,
                'time2': time2,
                'winners': winners}
        prize_list.append(prize_object)

    return header, header_content, image, prize_list


def get_coords(address, zipcode):
    sleep(0.2)
    location = slugify(unicode(address)) + "+" + str(zipcode)
    s = 'http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address='
    r = requests.get("%s%s" % (s, location))
    result = r.json()
    lat = result['results'][0]['geometry']['location']['lat']
    lng = result['results'][0]['geometry']['location']['lng']
    return lat, lng