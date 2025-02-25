from service_catalog.models import RequestState
from tests.test_service_catalog.base_test_request import BaseTestRequestAPI
from tests.permission_endpoint import TestingGetContextView, TestingPostContextView, TestPermissionEndpoint


class TestServiceCatalogRequestProcessPermissionsEndpoint(BaseTestRequestAPI, TestPermissionEndpoint):
    def setUp(self):
        super().setUp()
        self.test_request.state = RequestState.ACCEPTED
        self.test_request.save()

    def test_process_view(self):
        testing_view_list = [
            TestingGetContextView(
                url='api_request_process',
                perm_str_list=['service_catalog.process_request'],
                url_kwargs={'pk': self.test_request.id},
                expected_status_code=405,
                expected_not_allowed_status_code=405
            ),
            TestingPostContextView(
                url='api_request_process',
                perm_str_list=['service_catalog.process_request'],
                url_kwargs={'pk': self.test_request.id},
                expected_status_code=200
            )
        ]
        self.run_permissions_tests(testing_view_list)