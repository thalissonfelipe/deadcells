import json
import unittest
from unittest.mock import patch, Mock
from blueprints import gears_blueprint as gb


MOCK_GEARS = {
    'name': 'gears',
    'data': [
        {
            'type': 'malee_weapons',
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
}


class test_blueprint_get_gears(unittest.TestCase):

    @patch(
        'blueprints.gears_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_gears_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_gears = Mock(
            return_value=MOCK_GEARS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = gb.get_gears()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_gears.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_GEARS['data']))

    @patch(
        'blueprints.gears_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_gears_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=MOCK_GEARS)

        ret = gb.get_gears()
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_GEARS['data']))

    @patch(
        'blueprints.gears_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_gears_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_gears = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = gb.get_gears()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_gears.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')


class test_blueprint_get_gears_by_type(unittest.TestCase):

    @patch(
        'blueprints.gears_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_gears_by_type_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_gears = Mock(
            return_value=MOCK_GEARS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = gb.get_gears_by_type('malee_weapons')
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_gears.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_GEARS['data'][0]))

    @patch(
        'blueprints.gears_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_gears_by_type_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=MOCK_GEARS)

        ret = gb.get_gears_by_type('malee_weapons')
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_GEARS['data'][0]))

    def test_get_gears_by_type_invalid_gear_type(self):
        ret = gb.get_gears_by_type(None)
        self.assertEqual(ret.status_code, 400)
        self.assertEqual(ret.data.decode(), 'Invalid gear type.')

    @patch(
        'blueprints.gears_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_gears_by_type_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_gears = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = gb.get_gears_by_type('malee_weapons')
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_gears.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')


class test_blueprint_get_gear_by_name(unittest.TestCase):

    @patch(
        'blueprints.gears_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_gear_by_name_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_gears = Mock(
            return_value=MOCK_GEARS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = gb.get_gear_by_name(MOCK_GEARS['data'][0]['gears'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_gears.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_GEARS['data'][0]['gears'][0])
        )

    @patch(
        'blueprints.gears_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_gear_by_name_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=MOCK_GEARS)

        ret = gb.get_gear_by_name(MOCK_GEARS['data'][0]['gears'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_GEARS['data'][0]['gears'][0])
        )

    @patch(
        'blueprints.gears_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_gear_by_name_not_found(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_gears = Mock(
            return_value=MOCK_GEARS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = gb.get_gear_by_name(None)
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_gears.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Gear not found.')

    @patch(
        'blueprints.gears_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_gear_by_name_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_gears = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = gb.get_gear_by_name(MOCK_GEARS['data'][0]['gears'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_gears.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
