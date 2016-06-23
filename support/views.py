from index import app
from flask import render_template, request
from directory import get_uw, get_pledge_content, get_prize_content
from config import BASE_URL, GOOGLE_MAPS_API_URL

list_of_letters = map(chr, range(97, 123))


@app.route('/underwriter')
def underwriter():
    page_url = BASE_URL + request.path
    page_title = 'Become An Underwriter'
    social = {
        'title': "Become A VPR Underwriter",
        'subtitle': "",
        'img': "http://www.vpr.net/apps/support/static/img/vpr-logo-share.jpg",
        'description': "Grow your business: underwriting on VPR will reach our statewide audience of 200,000 listeners and 100,000 unique monthly visitors to VPR.net",
        'twitter_text': "Grow your business and become an underwriter! Support VPR and engage listeners.",
        'twitter_hashtag': ""
    }
    return render_template('underwriter.html',
        social=social,
        page_url=page_url,
        page_title=page_title)


@app.route('/directory')
def directory():
    """Takes a letter of the alphabet as an optional input and returns
    a rendered html document. If no argument is provided it returns the
    entire list of underwriters. All responses encoded as gzip"""

    page_url = BASE_URL + request.path
    page_title = 'Underwriter Directory'

    social = {
        'title': "VPR Underwriter Directory",
        'subtitle': "",
        'img': "http://www.vpr.net/apps/support/static/img/vpr-logo-share.jpg",
        'description': "Looking for an underwriter? Find businesses that support VPR here by using the map or searching by name.",
        'twitter_text': "Looking for an underwriter? Here's our full list!",
        'twitter_hashtag': ""
    }

    underwriters, locations = get_uw()
    google_maps_url = GOOGLE_MAPS_API_URL
    return render_template('directory.html',
        page_url=page_url,
        page_title=page_title,
        underwriters=underwriters,
        list_of_letters=list_of_letters,
        google_maps_url=google_maps_url,
        social=social,
        locations=locations)


@app.route('/index/<letter>')
def letter(letter):
    """Takes a letter of the alphabet as an optional input and returns
    a rendered html document. If no argument is provided it returns the
    entire list of underwriters. All responses encoded as gzip"""

    page_url = BASE_URL + request.path
    page_title = 'Underwriter Directory'

    social = {
        'title': "VPR Underwriter Directory",
        'subtitle': "",
        'img': "http://www.vpr.net/apps/support/static/img/vpr-logo-share.jpg",
        'description': "Looking for an underwriter? Find businesses that support VPR here by using the map or searching by name.",
        'twitter_text': "Looking for an underwriter? Here's our full list!",
        'twitter_hashtag': ""
    }

    underwriters, locations = get_uw(letter=letter)
    google_maps_url = GOOGLE_MAPS_API_URL
    return render_template('directory.html',
        page_url=page_url,
        page_title=page_title,
        underwriters=underwriters,
        list_of_letters=list_of_letters,
        google_maps_url=google_maps_url,
        social=social,
        locations=locations)


@app.route('/pledge')
def pledge():
    page_url = BASE_URL + request.path
    page_title = 'Make A Pledge'
    header, header_content, image = get_pledge_content()

    social = {
        'title': "Make A Contribution To VPR",
        'subtitle': "",
        'img': image,
        'description': "VPR counts on the local community for more than 90% of our funding. Make a gift or become a sustaining member of VPR today.",
        'twitter_text': "Make a contribution to VPR, pledge today",
        'twitter_hashtag': "pubRadio"
    }

    page = {'header': header,
            'header_content': header_content,
            'image': image}

    return render_template('pledge.html',
        page_url=page_url,
        page_title=page_title,
        page=page,
        social=social)


@app.route('/prizes')
def prizes():
    page_url = BASE_URL + request.path
    page_title = 'Pledge Drive Prizes'
    header, header_content, image, prizes = get_prize_content()

    social = {
        'title': "Pledge To VPR And Win",
        'subtitle': "",
        'img': image,
        'description': "VPR is giving away several fantastic prizes during this membership drive. Enter to win by making a gift at VPR.net or calling 1-800-639-6391.",
        'twitter_text': "VPR is giving away several fantastic prizes during this membership drive.",
        'twitter_hashtag': "pubRadio"
    }
    page = {'header': header,
            'header_content': header_content,
            'image': image}

    return render_template('prizes.html',
        page=page,
        social=social,
        page_url=page_url,
        page_title=page_title,
        prizes=prizes)
