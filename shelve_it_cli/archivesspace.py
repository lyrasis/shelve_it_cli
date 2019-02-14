from asnake.client import ASnakeClient


class ArchivesSpace(object):
    UPDATE_STATUS_FAILED = 'failed'
    UPDATE_STATUS_SUCCESS = 'success'

    def __init__(self, config={}):
        self.client = ASnakeClient()
        self.config = config
        self.containers = {}
        self.locations = {}
        self.repositories = {}
        self.results = []

    def handle(self, line_count, repo_code, con_barcode, loc_barcode):
        status = self.UPDATE_STATUS_FAILED  # default
        repo_uri = None
        try:
            self.repo_uri_from_code(repo_code)
            repo_uri = self.repositories[repo_code]
        except Exception:
            print(f'Failed repository code: {repo_code} [{line_count}]')

        con_uri = None
        try:
            self.con_uri_from_barcode(repo_uri, con_barcode)
            con_uri = self.containers[con_barcode]
        except Exception:
            print(f'Failed container barcode: {con_barcode} [{line_count}]')

        loc_uri = None
        try:
            self.loc_uri_from_barcode(loc_barcode)
            loc_uri = self.locations[loc_barcode]
        except Exception:
            print(f'Failed location barcode: {loc_barcode} [{line_count}]')

        if repo_uri and con_uri and loc_uri:
            print(f'Shelving: {repo_uri}, {con_uri}, {loc_uri} [{line_count}]')
            try:
                uri = f'{repo_uri}/top_containers/bulk/locations'
                data = {con_uri: loc_uri}
                self.client.post(uri, json=data)
                status = self.UPDATE_STATUS_SUCCESS
            except Exception:
                print(f'Failed: {repo_code}, {con_barcode}, {loc_barcode}')

        self.results.append({
          'row': line_count,
          'con_barcode': con_barcode,
          'con_uri': con_uri,
          'loc_barcode': loc_barcode,
          'loc_uri': loc_uri,
          'repo_code': repo_code,
          'repo_uri': repo_uri,
          'status': status,
        })

    def ping(self):
        try:
            self.reset_client()
            self.client.authorize()
            print('Login OK!')
        except Exception as ex:
            print(ex)

    def reset_client(self):
        self.client = ASnakeClient(
            baseurl=self.config['baseurl'],
            username=self.config['username'],
            password=self.config['password'],
        )

    def con_uri_from_barcode(self, repo_uri, barcode):
        if barcode not in self.containers:
            path = 'top_containers/by_barcode'
            uri = self.client.get(f'{repo_uri}/{path}/{barcode}').json()['uri']
            self.containers[barcode] = uri

    def loc_uri_from_barcode(self, barcode):
        if barcode not in self.locations:
            path = 'locations/by_barcode'
            uri = self.client.get(f'/{path}/{barcode}').json()['uri']
            self.locations[barcode] = uri

    def repo_uri_from_code(self, repo_code):
        if repo_code not in self.repositories:
            path = 'repositories/by_repo_code'
            uri = self.client.get(f'/{path}/{repo_code}').json()['uri']
            self.repositories[repo_code] = uri
