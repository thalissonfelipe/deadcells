import json
import unittest
from unittest.mock import patch, Mock
from blueprints import achievements_blueprint as ab


MOCK_ACHIEVEMENTS = [
    {
        'image': 'path_to_image',
        'name': 'Platinium',
        'description': 'Unlock all trophies (PS4 only)',
        'score': 'N/A',
        'trophy': 'Platinium'
    }
]


class test_blueprint_get_achievements(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_achievements',
        return_value=MOCK_ACHIEVEMENTS
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_ACHIEVEMENTS)
    )
    def test_get_achievements_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = ab.get_achievements()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_ACHIEVEMENTS))
        mock_json.assert_called()
        mock_scrapper.assert_called()

    @patch(
        'blueprints.achievements_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_achievements',
        side_effect=Exception('Exception')
    )
    def test_get_achievements_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = ab.get_achievements()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()


class test_blueprint_get_achievements_by_name(unittest.TestCase):

    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_ACHIEVEMENTS[0])
    )
    @patch(
        'scrapper.Scrapper.get_achievements',
        return_value=MOCK_ACHIEVEMENTS
    )
    def test_get_achievement_by_name_success(
        self,
        mock_scrapper,
        mock_json,
    ):
        ret = ab.get_achievement_by_name(MOCK_ACHIEVEMENTS[0]['name'])
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_ACHIEVEMENTS[0]))
        mock_scrapper.assert_called()
        mock_json.assert_called()

    @patch(
        'scrapper.Scrapper.get_achievements',
        return_value=MOCK_ACHIEVEMENTS
    )
    def test_get_achievement_by_name_not_found(
        self,
        mock_scrapper
    ):
        ret = ab.get_achievement_by_name(None)
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Achievement not found.')
        mock_scrapper.assert_called()

    @patch(
        'blueprints.achievements_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_achievements',
        side_effect=Exception('Exception')
    )
    def test_get_achievement_by_name_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = ab.get_achievement_by_name(None)
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()
