# -*- coding: utf-8 -*-
from django.conf import settings
import requests

from indigo.analysis.publications.base import BasePublicationFinder
from indigo.plugins import plugins


@plugins.register('publications')
class GazetteMachinePublicationFinder(BasePublicationFinder):
    """ Publication finder that uses Gazette Machine.
    Tries to lookup publications for any locale.
    """

    headers = {'Authorization': 'Token %s' % settings.GM['API_AUTH_TOKEN']}
    api_url = settings.GM.get('API_URL', 'https://api.gazettes.laws.africa/v1')
    timeout = 5.0

    def find_publications(self, params):
        date = params.get('date')
        number = params.get('number')
        jurisdiction = params.get('country')
        publication = self.get_publication(jurisdiction, params.get('name'))

        if not date:
            raise ValueError("I need at least a date to find a gazette.")

        params = {
            'date': date,
            'jurisdiction': jurisdiction,
        }
        if number:
            params['number'] = number
        if publication:
            params['publication'] = publication
        headers = self.headers
        resp = requests.get(self.api_url + '/gazettes/archived/', params=params, timeout=self.timeout, headers=headers)
        resp.raise_for_status()

        data = resp.json().get('results', [])
        for d in data:
            d['trustworthy'] = True
            d['url'] = d['download_url']
        return data

    def get_publication(self, country, name):
        # TODO: handle publication names
        return 'Government Gazette'
