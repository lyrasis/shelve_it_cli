# Shelve It CLI

Assigning containers to locations in ArchivesSpace.

## Requirements

This module requires the [shelve_it](https://github.com/lyrasis/shelve_it.git) plugin to be enabled
for ArchivesSpace.

Shelve It CLI is a Python module and can be installed using pip:

```bash
pip3 install shelve_it_cli
```

## Usage

Create a basic configuration file with these settings:

```yml
base_url: http://localhost:4567 # update to your api url
username: admin
password: admin
```

Do not use `admin` with a production system. The user must be able to:

- view repository
- update containers
- update locations

Test the connection to ArchivesSpace:

```bash
shelve_it_cli ping --config=/path/to/config.yml
# test config for devs running the backend locally
shelve_it_cli ping --config=config.test.yml
```

Create a CSV containing two columns with data to import. For example:

```txt
repo_code,container_barcode,location_barcode
test,123456,987654
```

Run the command to import it:

```bash
shelve_it_cli process --config=/path/to/config.yml --data=/path/to/import.csv --output=/path/to/result.csv
```

## Developer setup

```txt
# install system wide for editors (optional)
pip3 install ArchivesSnake fire
# install within virtualenv
virtualenv venv --python=python3
source venv/bin/activate
pip3 install -r requirements.txt

# commands
python shelve_it_cli.py ping --config config.test.yml
python shelve_it_cli.py process --config config.test.yml --data barcodes.csv --output result.csv

# test install
python -m unittest
pip3 install .
pip3 uninstall shelve_it_cli
```
