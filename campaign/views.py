from index import app
from query import api_feed, reporter_list
from flask import render_template, request
from config import BASE_URL


@app.route('/')
def index():
    tags = [237184207]
    page_url = BASE_URL + request.path
    page_title = 'Campaign 2014'
    page_explainer = ["VPR's guide to the 2014 campaign season. Get our latest coverage, special features and election news apps all in one place."]
    stories = api_feed(tags, numResults=10, thumbnail=True)
    reporters = reporter_list(tags)

    #To add featured stories to right panel of topic page, add story API IDs
    featured_ids = [347984643, 354095938,
        353539996, 349262333, 338098842, 341672291]

    featured = []
    for f_id in featured_ids:
        featured.append(api_feed([f_id], numResults=1, thumbnail=True, sidebar=True)[0])

    social = {
        'title': "Campaign 2014",
        'subtitle': '',
        'img': '',
        'description': "VPR's guide to the 2014 campaign season. Get our latest coverage, special features and election news apps all in one place.",
        'twitter_text': "VPR's guide to the 2014 campaign season.",
        'twitter_hashtag': ''
    }

    return render_template('content.html',
        page_title=page_title,
        page_explainer=page_explainer,
        stories=stories,
        social=social,
        featured=featured,
        reporters=reporters,
        page_url=page_url)
