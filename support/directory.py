from config import ABSOLUTE_PATH, OPEN_CAGE_API_KEY
from geopy.geocoders import OpenCage
from operator import itemgetter
from datetime import datetime
from slugify import slugify
from time import sleep
from sheet import get_underwriter_sheet, get_pledge_sheet, get_prize_sheet
import requests
import json

uw_json_f = ABSOLUTE_PATH + 'uw.json'

def get_underwriters():
    """Grab the Underwiter spreadsheet on Google Drive, look it see if it's been
    recently modified, if it has, remove entries that have been deleted, add new
    entries, and check for any changes to existing entries. Saves the results
    locally."""

    # get list of underwriters (as dictionaries) from GDrive (no coords)
    new_underwriters = get_underwriter_sheet()

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
                uw_dict[name]['url'] = add_http(uw_dict[name]['url'])

                # Only set the lat & long if the zip code is not 000000
                if str(underwriter['zip']) != '00000':
                    lat, lng = get_coords(underwriter['address'], underwriter['city'], underwriter['state'], underwriter['zip'])
                    if lat is not None and lng is not None:
                        uw_dict[name]['lat'], uw_dict[name]['lng'] = lat, lng
        else:
            # only add it if the name is present
            if underwriter['name'] is not None:
              print "Added: ", underwriter['name']
              uw_dict[name] = underwriter
              uw_dict[name]['url'] = add_http(uw_dict[name]['url'])

              # Only set the lat & long if the zip code is not 000000
              if str(underwriter['zip']) != '00000':
                  lat, lng = get_coords(underwriter['address'], underwriter['city'], underwriter['state'], underwriter['zip'])
                  if lat is not None and lng is not None:
                      uw_dict[name]['lat'] = lat
                      uw_dict[name]['lng'] = lng

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

    locations = []

    for uw in underwriters:
        try:
            locations.append([str(uw['name']), uw['lat'], uw['lng']])
        except:
            continue

    return underwriters, locations


def get_pledge_content():
    pledge_sheet = get_pledge_sheet()
    header = pledge_sheet[0]['header']
    header_content = pledge_sheet[0]['headercontent']
    image = pledge_sheet[0]['image']
    return header, header_content, image


def get_prize_content():
    prize_sheet = get_prize_sheet()
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


def get_coords(address, city, state, zipcode):
    geolocator = OpenCage(OPEN_CAGE_API_KEY)

    if address is None:
        address = ''

    full_address =  unicode(str(address)) + " " + unicode(str(city)) + " " + unicode(str(state)) + " " + unicode(str(zipcode))

    print "Full Address: ", full_address.strip()

    location = geolocator.geocode(full_address, timeout=5)

    if location is not None:
        return location.latitude, location.longitude
    else:
        return None, None
