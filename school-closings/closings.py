#!/usr/bin/python
import requests
import xml.etree.ElementTree as ET


def closings():
    """Takes all school closings and returns a JSON-like dictionary:
    {'Vermont':
        [{'county': 'Bennington',
          'closings': [{
                'school': school_name,
                'condition': condition},
                ...]
        }...]
    }"""

    url = 'http://www.vabdayoff.com/cgi-bin/schoolclosings.cgi?returnbody=xml'
    r = requests.get(url)
    root = ET.fromstring(r.text)
    timestamp = root[0].text
    closings = {}
    county_list = []
    for children in root[1]:
        school_dict = {}
        for child in children:
            school_dict[child.tag] = child.text
        state = school_dict['state']
        county = school_dict['county']
        closed_school = {'school': school_dict['school'],
            'condition': school_dict['condition']}
        if (county + state) in county_list:
            for each_county in closings[state]:
                if county == each_county['county']:
                    each_county['closings'].append(closed_school)
        else:
            county_list.append(county + state)
            if state in closings:
                closings[state].append({'county': county,
                'closings': [closed_school]})
            else:
                closings[state] = [{'county': county, 'closings': [closed_school]}]

    for state, counties in closings.iteritems():
        counties = sorted(counties, key=lambda k: k['county'])
    return closings, timestamp
