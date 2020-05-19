import json
import unittest
from unittest.mock import patch, Mock
from blueprints import pickups_blueprint as pb


MOCK_PICKUPS = [
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


class test_blueprint_get_pickups(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_pickups',
        return_value=MOCK_PICKUPS
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_PICKUPS)
    )
    def test_get_pickups_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = pb.get_pickups()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_PICKUPS))
        mock_json.assert_called()
        mock_scrapper.assert_called()

    @patch(
        'blueprints.pickups_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_pickups',
        side_effect=Exception('Exception')
    )
    def test_get_pickups_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = pb.get_pickups()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()


class test_blueprint_get_pickups_by_type(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_pickups',
        return_value=MOCK_PICKUPS
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_PICKUPS)
    )
    def test_get_pickups_by_type_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = pb.get_pickups_by_type('gems')
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_PICKUPS[0]))
        mock_json.assert_called()
        mock_scrapper.assert_called()

    def test_get_pickups_by_type_invalid_mutation_type(self):
        ret = pb.get_pickups_by_type(None)
        self.assertEqual(ret.status_code, 400)
        self.assertEqual(ret.data.decode(), 'Invalid pickup type.')

    @patch(
        'blueprints.pickups_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_pickups',
        side_effect=Exception('Exception')
    )
    def test_get_pickups_by_type_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = pb.get_pickups_by_type('gems')
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()


class test_blueprint_get_pickup_by_name(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_pickups',
        return_value=MOCK_PICKUPS
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_PICKUPS)
    )
    def test_get_pickup_by_name_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = pb.get_pickup_by_name(MOCK_PICKUPS[0]['pickups'][0]['name'])
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_PICKUPS[0]['pickups'][0])
        )
        mock_json.assert_called()
        mock_scrapper.assert_called()

    @patch(
        'scrapper.Scrapper.get_pickups',
        return_value=MOCK_PICKUPS
    )
    def test_get_pickup_by_name_not_found(self, mock_scrapper):
        ret = pb.get_pickup_by_name(None)
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Pickup not found.')

    @patch(
        'blueprints.pickups_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_pickups',
        side_effect=Exception('Exception')
    )
    def test_get_pickup_by_name_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = pb.get_pickup_by_name(MOCK_PICKUPS[0]['pickups'][0]['name'])
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()
