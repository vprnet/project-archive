# Underwriters Support App

This app contains a directory of all of the underwriters that support VPR, as
well as some additional pages for supporting and becoming an underwriter.

## How It Works

This app uses a Google Spreadsheet that contains a list of underwriters and
their data such as name, address, city, zip code, etc. This sheet is used to
populate a `uw.json` file that is located at the project root. This file is used
to map out the various under writers.

## Configuring

NOTE: A `uw.json` file _must_ exist in the project root for this app to work.
It should contain an empty JSON object: `{}`:

    `touch uw.json && echo "{}" > uw.json`

Copy the config template `cp _config.py config.py` and specify the various empty
secrets within the new `config.py`.

### Open Cage

The app uses [OpenCage Geocoder](http://geocoder.opencagedata.com/) for getting
the latitude and longitude of Underwriter addresses. Register for an account and
set the `OPEN_CAGE_API_KEY` in `config.py`.

## Developing

Once the app is configured and dependencies are installed, run the app with `python index.py`.

## Deploying

Set the AWS S3 bucket and directory. Run `python index.py build` to generate the
site and upload it to AWS S3.

## Logic For Locations

If the zip code is set to `00000` in the Google Spreadsheet, do not set a
location.
