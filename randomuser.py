import requests
import logging
from datetime import date

logger = logging.getLogger(__name__)


BASE_URL = 'http://api.randomuser.me/'
API_VERSION = '1.0'

GENDERS = {
    'male',
    'female',
}

NATIONALITIES = {
    'au',
    'br',
    'ca',
    'ch',
    'de',
    'dk',
    'es',
    'fi',
    'fr',
    'gb',
    'ie',
    'ir',
    'nl',
    'nz',
    'tr',
    'us',
}

FIELDS = {
    'gender',
    'name',
    'location',
    'email',
    'login',
    'registered',
    'dob',
    'phone',
    'cell',
    'id',
    'picture',
    'nat',
}

def make_sequence(param):
    return [param] if isinstance(param, str) else param

def make_csv(seq):
    return ','.join(seq)


class RandomUser(object):

    def __init__(self):
        self.api_url = BASE_URL + API_VERSION
        self.session = requests.Session()

    def generate(self, results=None, gender=None, nationalities=[], include_fields=[], exclude_fields=[], seed=None, ):

        nat_set = set(make_sequence(nationalities))
        inc_set = set(make_sequence(include_fields))
        exc_set = set(make_sequence(exclude_fields))

        params = {}

        if gender:
            if gender in GENDERS:
                params['gender'] = gender
            else:
                raise ValueError('invalid gender: %s' % gender)

        if nat_set:
            invalid_nationalities = nat_set - NATIONALITIES
            if invalid_nationalities:
                raise ValueError('invalid nationalities: %s' % make_csv(invalid_nationalities))
            else:
                params['nat'] = make_csv(nat_set)

        dupe_fields = inc_set & exc_set
        if dupe_fields:
                raise ValueError('cannot both include and exclude same field: %s' % make_csv(dupe_fields))

        invalid_fields = (inc_set | exc_set) - FIELDS
        if invalid_fields:
            raise ValueError('invalid fields: %s' % make_csv(invalid_fields))

        if inc_set:
            params['inc'] = make_csv(inc_set)
        if exc_set:
            params['exc'] = make_csv(exc_set)

        if seed:
            params['seed'] = seed
        if results:
            params['results'] = results

        return self.session.get(self.api_url, params=params).json()['results']
