import json
import unittest
from unittest.mock import patch, Mock
from blueprints import achievements_blueprint as ab


MOCK_ACHIEVEMENTS = {
    'name': 'achievements',
    'data': [
        {
            'image': 'path_to_image',
            'name': 'Platinium',
            'description': 'Unlock all trophies (PS4 only)',
            'score': 'N/A',
            'trophy': 'Platinium'
        }
    ]
}


class test_blueprint_get_achievements(unittest.TestCase):

    @patch(
        'blueprints.achievements_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_achievements_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_achievements = Mock(
            return_value=MOCK_ACHIEVEMENTS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = ab.get_achievements()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_achievements.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_ACHIEVEMENTS['data'])
        )

    @patch(
        'blueprints.achievements_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_achievements_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(
            return_value=MOCK_ACHIEVEMENTS
        )

        ret = ab.get_achievements()
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_ACHIEVEMENTS['data'])
        )

    @patch(
        'blueprints.achievements_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_achievements_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_achievements = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = ab.get_achievements()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_achievements.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')


class test_blueprint_get_achievements_by_name(unittest.TestCase):

    @patch(
        'blueprints.achievements_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_achievement_by_name_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_achievements = Mock(
            return_value=MOCK_ACHIEVEMENTS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = ab.get_achievement_by_name(MOCK_ACHIEVEMENTS['data'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_achievements.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_ACHIEVEMENTS['data'][0])
        )

    @patch(
        'blueprints.achievements_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_achievement_by_name_succes_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(
            return_value=MOCK_ACHIEVEMENTS
        )

        ret = ab.get_achievement_by_name(MOCK_ACHIEVEMENTS['data'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_ACHIEVEMENTS['data'][0])
        )

    @patch(
        'blueprints.achievements_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_achievement_by_name_not_found(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_achievements = Mock(
            return_value=MOCK_ACHIEVEMENTS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = ab.get_achievement_by_name(None)
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_achievements.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Achievement not found.')

    @patch(
        'blueprints.achievements_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_achievement_by_name_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_achievements = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = ab.get_achievement_by_name(MOCK_ACHIEVEMENTS['data'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_achievements.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
