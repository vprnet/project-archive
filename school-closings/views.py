from index import app
from flask import render_template, request
from config import BASE_URL
from closings import closings
from query import get_callout


@app.route('/')
def index():
    page_url = BASE_URL + request.path
    page_title = 'School Closings'
    school_closings, timestamp = closings()

    social = {
        'title': "Is Your School Closed Today?",
        'subtitle': "VPR's School Closing Listings",
        'img': "static/img/vpr_school_closings_2.jpg",
        'description': "Find the list of school cancellations and delays, by county, in Vermont and areas of New York and New Hampshire. This list is provided by the VAB and is smartphone and tablet friendly.",
        'twitter_text': "Is your school closed today? Find out using VPR's smartphone friendly listings",
        'twitter_hashtag': "vtwx"
    }

    SHEET_ID = 'tzE2PsqJoWRpENlMr-ZlS8A'
    callout = get_callout(SHEET_ID)

    return render_template('content.html',
        page_title=page_title,
        school_closings=school_closings,
        social=social,
        timestamp=timestamp,
        callout=callout,
        page_url=page_url)
