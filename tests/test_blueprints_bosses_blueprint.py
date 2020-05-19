import json
import unittest
from unittest.mock import patch, Mock
from blueprints import bosses_blueprint as bb


MOCK_BOSSES = {
    'name': 'bosses',
    'data': [
        {
            'name': 'The Concierge',
            'location(s)': 'Black Bridge',
            'reward': ['Challenger Rune (1st kill)'],
        }
    ]
}


class test_blueprint_get_bosses(unittest.TestCase):

    @patch(
        'blueprints.bosses_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_bosses_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_bosses = Mock(
            return_value=MOCK_BOSSES
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = bb.get_bosses()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_bosses.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_BOSSES['data']))
    
    @patch(
        'blueprints.bosses_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_bosses_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(
            return_value=MOCK_BOSSES
        )

        ret = bb.get_bosses()
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_BOSSES['data']))

    @patch(
        'blueprints.bosses_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_bosses_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_bosses = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = bb.get_bosses()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_bosses.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')


class test_blueprint_get_boss_by_name(unittest.TestCase):

    @patch(
        'blueprints.bosses_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_boss_by_name_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get_boss = Mock(
            return_value=MOCK_BOSSES['data'][0]
        )

        ret = bb.get_boss_by_name(MOCK_BOSSES['data'][0]['name'])
        mock_current_app.scrapper_manager.get_boss.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_BOSSES['data'][0])
        )

    @patch(
        'blueprints.bosses_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_boss_by_name_not_found(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get_boss = Mock(return_value=None)

        ret = bb.get_boss_by_name(None)
        mock_current_app.scrapper_manager.get_boss.assert_called()
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Boss not found.')

    @patch(
        'blueprints.bosses_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_boss_by_name_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get_boss = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = bb.get_boss_by_name(None)
        mock_current_app.scrapper_manager.get_boss.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
