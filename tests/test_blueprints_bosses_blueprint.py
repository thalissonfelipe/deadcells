import json
import unittest
from unittest.mock import patch, Mock
from blueprints import bosses_blueprint as bb


MOCK_BOSSES = [
    {
        'name': 'The Concierge',
        'location(s)': 'Black Bridge',
        'reward': ['Challenger Rune (1st kill)'],
    }
]


class test_blueprint_get_bosss(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_bosses',
        return_value=MOCK_BOSSES
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_BOSSES)
    )
    def test_get_bosss_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = bb.get_bosses()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_BOSSES))
        mock_json.assert_called()
        mock_scrapper.assert_called()

    @patch(
        'blueprints.bosses_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_bosses',
        side_effect=Exception('Exception')
    )
    def test_get_bosses_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = bb.get_bosses()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()


class test_blueprint_get_boss_by_name(unittest.TestCase):

    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_BOSSES[0])
    )
    @patch(
        'scrapper.Scrapper.get_boss',
        return_value=MOCK_BOSSES[0]
    )
    def test_get_boss_by_name_success(
        self,
        mock_scrapper,
        mock_json,
    ):
        ret = bb.get_boss_by_name(MOCK_BOSSES[0]['name'])
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_BOSSES[0]))
        mock_scrapper.assert_called()
        mock_json.assert_called()

    @patch(
        'scrapper.Scrapper.get_boss',
        return_value=None
    )
    def test_get_boss_by_name_not_found(
        self,
        mock_scrapper
    ):
        ret = bb.get_boss_by_name(None)
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Boss not found.')
        mock_scrapper.assert_called()

    @patch(
        'blueprints.bosses_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_boss',
        side_effect=Exception('Exception')
    )
    def test_get_boss_by_name_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = bb.get_boss_by_name(None)
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()
