# Shelve It CLI

Python module for assigning containers to locations in ArchivesSpace.

## Usage

Create a basic configuration file with these settings:

```yml
base_url: http://localhost:4567
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
```

Create a CSV containing two columns with data to import. For example:

```txt
container_barcode,location_barcode
123456,987654
```

Run the command to import it:

```bash
shelve_it_cli process --config=/path/to/config.yml --data=/path/to/import.csv
```

## Developer setup

```txt
virtualenv venv --python=python3
source venv/bin/activate
pip3 install -r requirements.txt
python shelve_it_cli/shelve_it_cli.py ping --config config.test.yml
python shelve_it_cli/shelve_it_cli.py process --config config.test.yml --data barcodes.csv
```
