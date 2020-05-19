import json
import unittest
from unittest.mock import patch, Mock
from blueprints import gears_blueprint as gb


MOCK_GEARS = [
    {
        'type': 'malee',
        'gears': [
            {
                'image': 'path_to_image',
                'name': 'Rusty Sword',
                'description': 'Kills things. Sometimes...',
                'location': 'Starter melee weapon until ...',
                'base_dps': '119 DPS',
                'special_dps': 'N/A',
                'scaling': 'path_to_image'
            }
        ]
    }
]


class test_blueprint_get_gears(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_gears',
        return_value=MOCK_GEARS
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_GEARS)
    )
    def test_get_gears_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = gb.get_gears()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_GEARS))
        mock_json.assert_called()
        mock_scrapper.assert_called()

    @patch(
        'blueprints.gears_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_gears',
        side_effect=Exception('Exception')
    )
    def test_get_gears_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = gb.get_gears()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()


class test_blueprint_get_gears_by_type(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_gears',
        return_value=MOCK_GEARS
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_GEARS)
    )
    def test_get_gears_by_type_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = gb.get_gears_by_type('malee')
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_GEARS[0]))
        mock_json.assert_called()
        mock_scrapper.assert_called()

    def test_get_gears_by_type_invalid_gear_type(self):
        ret = gb.get_gears_by_type(None)
        self.assertEqual(ret.status_code, 400)
        self.assertEqual(ret.data.decode(), 'Invalid gear type.')

    @patch(
        'blueprints.gears_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_gears',
        side_effect=Exception('Exception')
    )
    def test_get_gears_by_type_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = gb.get_gears_by_type('malee')
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()


class test_blueprint_get_gear_by_name(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_gears',
        return_value=MOCK_GEARS
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_GEARS)
    )
    def test_get_gear_by_name_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = gb.get_gear_by_name(MOCK_GEARS[0]['gears'][0]['name'])
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_GEARS[0]['gears'][0])
        )
        mock_json.assert_called()
        mock_scrapper.assert_called()

    @patch(
        'scrapper.Scrapper.get_gears',
        return_value=MOCK_GEARS
    )
    def test_get_gear_by_name_not_found(self, mock_scrapper):
        ret = gb.get_gear_by_name(None)
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Gear not found.')

    @patch(
        'blueprints.gears_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_gears',
        side_effect=Exception('Exception')
    )
    def test_get_gear_by_name_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = gb.get_gear_by_name(MOCK_GEARS[0]['gears'][0]['name'])
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()
