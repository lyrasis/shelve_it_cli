import unittest
import responses
from shelve_it_cli import ArchivesSpace


class TestArchivesSpace(unittest.TestCase):

    @responses.activate
    def test_con_uri_from_barcode_success(self):
        service = ArchivesSpace()
        barcode = '123456'
        request_path = f'/repositories/2/top_containers/by_barcode/{barcode}'
        uri = '/repositories/2/top_containers/1'
        responses.add(
            responses.GET,
            service.client.config['baseurl'] + request_path,
            json={'uri': uri},
            status=200
        )
        service.con_uri_from_barcode('/repositories/2', barcode)
        self.assertEqual(service.containers[barcode], uri)

    @responses.activate
    def test_loc_uri_from_barcode_success(self):
        service = ArchivesSpace()
        barcode = '987654'
        request_path = f'/locations/by_barcode/{barcode}'
        uri = '/locations/1'
        responses.add(
            responses.GET,
            service.client.config['baseurl'] + request_path,
            json={'uri': uri},
            status=200
        )
        service.loc_uri_from_barcode(barcode)
        self.assertEqual(service.locations[barcode], uri)

    @responses.activate
    def test_repo_uri_from_code_success(self):
        service = ArchivesSpace()
        repo_code = 'test'
        request_path = f'/repositories/by_repo_code/{repo_code}'
        uri = '/repositories/2'
        responses.add(
            responses.GET,
            service.client.config['baseurl'] + request_path,
            json={'uri': uri},
            status=200
        )
        service.repo_uri_from_code(repo_code)
        self.assertEqual(service.repositories[repo_code], uri)
