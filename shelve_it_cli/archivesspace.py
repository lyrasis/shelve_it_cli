from asnake.client import ASnakeClient

class ArchivesSpace(object):

  def __init__(self, config = {}):
    self.client = None
    self.config = config
    self.containers = {}
    self.locations = {}
    self.repositories = {}

  def handle(self, line_count, repo_code, container_barcode, location_barcode):
    try:
      self.__repositories_uri_from_code(repo_code)
    except Exception:
      print(f'Could not get repository from code: {repo_code} [{line_count}]')
      return None
    repository_uri = self.repositories[repo_code]

    try:
      self.__container_uri_from_barcode(repository_uri, container_barcode)
    except Exception:
      print(f'Could not get container from barcode: {container_barcode} [{line_count}]')
      return None
    container_uri = self.containers[container_barcode]

    try:
      self.__location_uri_from_barcode(location_barcode)
    except Exception:
      print(f'Could not get location from barcode: {location_barcode} [{line_count}]')
      return None
    location_uri = self.locations[location_barcode]

    print(f'Assigning: {repository_uri}, {container_uri}, {location_uri} [{line_count}]')
    try:
      uri  = f'{repository_uri}/top_containers/bulk/locations'
      data = { container_uri: location_uri }
      self.client.post(uri, json=data)
    except Exception:
      print(f'Failed to update: {repo_code}, {container_barcode}, {location_barcode}')

  def ping(self):
    try:
      self.reset_client()
      self.client.authorize()
      print('Login OK!')
    except Exception as ex:
      print(ex)

  def reset_client(self):
    self.client = ASnakeClient(
      baseurl  = self.config['baseurl'],
      username = self.config['username'],
      password = self.config['password'],
    )

  def __container_uri_from_barcode(self, repo_uri, barcode):
    if barcode not in self.containers:
      uri = self.client.get(f'{repo_uri}/top_containers/by_barcode/{barcode}').json()['uri']
      self.containers[barcode] = uri

  def __location_uri_from_barcode(self, barcode):
    if barcode not in self.locations:
      uri = self.client.get(f'/locations/by_barcode//{barcode}').json()['uri']
      self.locations[barcode] = uri

  def __repositories_uri_from_code(self, repo_code):
    if repo_code not in self.repositories:
      uri = self.client.get(f'/repositories/by_repo_code/{repo_code}').json()['uri']
      self.repositories[repo_code] = uri
