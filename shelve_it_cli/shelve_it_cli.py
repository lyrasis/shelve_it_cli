from archivesspace import ArchivesSpace
import csv
import fire
import yaml

class ShelveItCLI(object):
  """Assigning containers to locations in ArchivesSpace."""

  def __init__(self):
    self.service = ArchivesSpace()

  def ping(self, config):
    print('Attempting to login to ArchivesSpace')
    self.service.config = self.__read_config(config)
    self.service.reset_client()
    self.service.ping()
    print('Login ok!')

  def process(self, data, config):
    self.service.config = self.__read_config(config)
    self.service.reset_client()
    with open(data, mode='r') as dt:
      csv_reader = csv.DictReader(dt)
      line_count = 0
      for row in csv_reader:
        if line_count == 0:
          pass
        rc = row["repo_code"]
        cb = row["container_barcode"]
        lb = row["location_barcode"]
        print(f'Processing: respository [{rc}], container [{cb}], location [{lb}]')
        self.service.handle(rc, cb, lb)
        line_count += 1
    return 'Done!'

  def __read_config(self, config):
    with open(config, 'r') as cfg:
      parsed_cfg = yaml.load(cfg)
    return {
      'baseurl':  parsed_cfg['base_url'],
      'username': parsed_cfg['username'],
      'password': parsed_cfg['password']
    }

if __name__ == '__main__':
  fire.Fire(ShelveItCLI)
