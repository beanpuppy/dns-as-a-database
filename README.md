# dns-as-a-database

DNS as a Database (DAAB) is a key-value database using DNS TXT records for it's data structure.

## Features

* Redis-like
* No storage or memory requirements
* Works

## Requirements

* Python 3.6+
* A DigitalOcean account and API key
* A domain name

## Installation and Setup

To install DAAB use pip:

```bash
pip install daab
```

But you're also going to need to:

* [Buy a domain name](https://www.wikihow.com/Buy-a-Domain-Name)
* [Point it to DigitalOcean Namservers](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
* [Add it to your DigitalOcean account](https://www.digitalocean.com/docs/networking/dns/how-to/add-domains/)
* [Create an access token](https://www.digitalocean.com/docs/apis-clis/api/create-personal-access-token/)

## Examples

```python
from daab import DAAB

daab = DAAB('<DIGITALOCEAN_API_KEY>', '<DOMAIN_NAME>')

# Create/update a record
daab.set('mykey', 'myvalue')

# Use glob search to find keys
daab.scan('*key')

# Get record
daab.get('mykey')

# Delete record
daab.delete('mykey')
```

## License

MIT.
