"""
as seen in
https://python.plainenglish.io/how-i-built-a-cvs-vaccine-appointment-availability-checker-in-python-6beb379549e4

This is a python script that requires you have python installed, or in a cloud environment.

This script scrapes the CVS website looking for vaccine appointments in the cities you list.
To update for your area, update the locations marked with ### below and the cities.py list.

If you receive an error that says something is not install, type

pip install beepy
and
pip install docopt

in your terminal.

todo: walgrens, safeway, rite aid, kaiser, blue shield
"""

# ignore too-long lines                 --  pylint: disable=C0301
import time
import requests
from beepy import beep
from docopt import docopt

import cities


def check_scc(opts):
    """see if the Santa Clara County site is making appointments
    """
    response = requests.get(
        'https://vax.sccgov.org/',
        headers={"Referer":r'https://www.sccgov.org/sites/covid19/Pages/COVID19-vaccine-information-for-public.aspx#appointment'})
    ct_str = time.ctime()
    try:
        landing = response.links['canonical']['url']
        if not 'no_appointments' in landing:
            print('\n', ct_str, landing)
            with open(opts['--file'], 'a') as f_out:
                f_out.write(f'{ct_str} {landing}\n')
            if not opts['--silent']:
                beep(sound='success')
    # if links missing, either canonical or url,
    except IndexError:
        print('\n', ct_str, 'missing canonical url links:', response.links)
        beep(sound='error')


def find_cvs_vaccine(opts, city_lst):
    """ get the CVS vaccine availability
        if found, display the CVS city and make a sound
        else, print a '.' (period)
    """
    city_str_len = max([len(x) for x in city_lst])

    state = 'CA' ###Update with your state abbreviation. Be sure to use all CAPS, e.g. RI

    try:
        response = requests.get(
            "https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.{}.json?vaccineinfo".format(state.lower()),
            headers={"Referer":"https://www.cvs.com/immunizations/covid-19-vaccine"})
        payload = response.json()

        mappings = {}
        for item in payload["responsePayloadData"]["data"][state]:
            mappings[item.get('city')] = item.get('status')

        got_lst = []
        ct_str = time.ctime()
        for key in mappings:
            if (key in city_lst) and (mappings[key] != 'Fully Booked'):
                got_lst += [f'{ct_str} - {key:{city_str_len}s} - {mappings[key]}']
        if got_lst:
            print('\n', '\n'.join(got_lst), end='', flush=True)
            with open(opts['--file'], 'a') as f_out:
                f_out.write('\n'.join(got_lst))
                f_out.write('\n')
            if not opts['--silent']:
                beep(sound='success')
        else:
            print('.', end='', flush=True)
    except TimeoutError:
        print('*', end='', flush=True)



USAGE_STR = """
Usage:
  vaccine  [--bay] [--debug=<D>] [--file=<F>] [--period=<P>] [--silent] [--time=<T>] [--help]
  vaccine -h | --help

Options:
  -b --bay          Greater SF Bay Area; else only Santa Clara County
  -d --debug=<D>    Bitfield: 1 test cities likely w/ stock  [default: 0]
  -f --file=<F>     File name to save available locations [default: available.txt]
  -h --help         Show this help screen.
  -p --period=<P>   Seconds between scrapes [default: 60]
  -s --silent       Don't mmake noise
  -t --time=<T>     Hours to loop [default: 3]
  """


if __name__ == '__main__':
    CLI_OPTS = docopt(USAGE_STR)
    if CLI_OPTS['--bay']:                   # command line argument
        CITIES = cities.cities_near         # cities within about a 2 hour drive of San Jose, CA
    else:
        CITIES = cities.cities_scc          # cities in Santa Cara County

    if int(CLI_OPTS['--debug']) & 1:           # command line argument
        CITIES += ['BAKERSFIELD', 'FRESNO',]   # add a couple of cities that probably have stock
    MY_CITY_STR = ', '.join('%s%14s'%('' if i%6 != 0 else '\n', x) for i, x in enumerate(CITIES))
    PERIOD_STR = time.strftime("%H:%M:%S", time.gmtime(int(CLI_OPTS["--period"])))
    print('\n',
          time.ctime(),
          f'checking every {PERIOD_STR} for {CLI_OPTS["--time"]} hours',
          MY_CITY_STR)

    # loop every --period seconds for --time hours
    HOURS_TO_RUN = int(CLI_OPTS['--time']) # command line argument
    MAX_TIME = time.time() + HOURS_TO_RUN*60*60
    while time.time() < MAX_TIME:
        find_cvs_vaccine(CLI_OPTS, CITIES)
        check_scc(CLI_OPTS)
        time.sleep(int(CLI_OPTS['--period'])) # command line argument
