from asnake.client import ASnakeClient

class ArchivesSpace(object):

  def __init__(self, config = {}):
    self.client = None
    self.config = config
    self.containers = {}
    self.locations = {}
    self.repositories = {}

  def handle(self, repo_code, container_barcode, location_barcode):
    repo_id = self.__repo_id_from_code(repo_code)
    # get container uri from barcode
    # get location uri from barcode
    return repo_id

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

  def __container_uri_from_barcode(self, barcode):
    return 1

  def __location_uri_from_barcode(self, barcode):
    return 1

  def __repo_id_from_code(self, repo_code):
    if repo_code not in self.repositories:
      # self.repositories[repo_code] = request it
      repo_id = 1
    else:
      repo_id = self.repositories[repo_code]
    return repo_id