# Indigo Gazette Machine plugin

This provides a PublicationFinder plugin for Indigo that looks up gazettes in
Laws.Africa's Gazette Machine.

# Install

Install the package:

```
pip install -e git+https://github.com/laws-africa/indigo-gm.git#egg=indigo-gm
```

Import the publication finder (for all locales) in your App to register it in the plugin system.


```python
from django.apps import AppConfig


class MyAppConfig(AppConfig):
    def ready(self):
        import indigo_gm.publications
```

Set the Gazette Machine authorization token in your `settings.py`:

```python
GM = {
    'API_AUTH_TOKEN': 'abc-123',
    'API_URL': 'https://api.gazettes.laws.africa/v1',
}
```
