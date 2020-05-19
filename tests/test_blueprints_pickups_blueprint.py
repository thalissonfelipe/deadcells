import json
import unittest
from unittest.mock import patch, Mock
from blueprints import pickups_blueprint as pb


MOCK_PICKUPS = {
    'name': 'pickups',
    'data': [
        {
            'type': 'gems',
            'pickups': [
                {
                    'name': 'Gold Tooth',
                    'image': 'path_to_image',
                    'description': 'A gold tooth worth (value) GOLD.',
                    'value_range': '35-65',
                    'sources': 'One per enemy parried with the Greed Shield.'
                }
            ]
        }
    ]
}


class test_blueprint_get_pickups(unittest.TestCase):

    @patch(
        'blueprints.pickups_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_pickups_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_pickups = Mock(
            return_value=MOCK_PICKUPS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = pb.get_pickups()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_pickups.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_PICKUPS['data']))

    @patch(
        'blueprints.pickups_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_pickups_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(
            return_value=MOCK_PICKUPS
        )

        ret = pb.get_pickups()
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_PICKUPS['data']))

    @patch(
        'blueprints.pickups_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_pickups_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_pickups = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = pb.get_pickups()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_pickups.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')


class test_blueprint_get_pickups_by_type(unittest.TestCase):

    @patch(
        'blueprints.pickups_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_pickups_by_type_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_pickups = Mock(
            return_value=MOCK_PICKUPS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = pb.get_pickups_by_type('gems')
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_pickups.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_PICKUPS['data'][0])
        )

    @patch(
        'blueprints.pickups_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_pickups_by_type_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(
            return_value=MOCK_PICKUPS
        )

        ret = pb.get_pickups_by_type('gems')
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_PICKUPS['data'][0])
        )

    def test_get_pickups_by_type_invalid_mutation_type(self):
        ret = pb.get_pickups_by_type(None)
        self.assertEqual(ret.status_code, 400)
        self.assertEqual(ret.data.decode(), 'Invalid pickup type.')

    @patch(
        'blueprints.pickups_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_pickups_by_type_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_pickups = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = pb.get_pickups_by_type('gems')
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_pickups.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')


class test_blueprint_get_pickup_by_name(unittest.TestCase):

    @patch(
        'blueprints.pickups_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_pickup_by_name_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_pickups = Mock(
            return_value=MOCK_PICKUPS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = pb.get_pickup_by_name(
            MOCK_PICKUPS['data'][0]['pickups'][0]['name']
        )
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_pickups.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_PICKUPS['data'][0]['pickups'][0])
        )

    @patch(
        'blueprints.pickups_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_pickup_by_name_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(
            return_value=MOCK_PICKUPS
        )

        ret = pb.get_pickup_by_name(
            MOCK_PICKUPS['data'][0]['pickups'][0]['name']
        )
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_PICKUPS['data'][0]['pickups'][0])
        )

    @patch(
        'blueprints.pickups_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_pickup_by_name_not_found(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_pickups = Mock(
            return_value=MOCK_PICKUPS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = pb.get_pickup_by_name(None)
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_pickups.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Pickup not found.')

    @patch(
        'blueprints.pickups_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_pickup_by_name_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_pickups = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = pb.get_pickup_by_name(
            MOCK_PICKUPS['data'][0]['pickups'][0]['name']
        )
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_pickups.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
