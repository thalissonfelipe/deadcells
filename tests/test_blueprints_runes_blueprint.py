import json
import unittest
from unittest.mock import patch, Mock
from blueprints import runes_blueprint as rb


MOCK_RUNES = {
    'name': 'runes',
    'data': [
        {
            'name': 'Vine Rune',
            'image': 'path_to_image',
            'biome': 'Promenade of the Condemned',
            'location': 'In a room accessed by entering a door' +
            'found at the base of a large overhang',
            'enemy': 'Undead Archer',
            'ability': 'Ability to sprout vines from special green blobs.',
            'access': [
                'Toxic Sewers',
                'Ramparts',
                'Dilapidated Arboretum (when paired with Teleportation Rune)'
            ]
        }
    ]
}


class test_blueprint_get_runes(unittest.TestCase):

    @patch(
        'blueprints.runes_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_runes_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_runes = Mock(
            return_value=MOCK_RUNES
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = rb.get_runes()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_runes.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_RUNES['data']))

    @patch(
        'blueprints.runes_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_runes_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=MOCK_RUNES)

        ret = rb.get_runes()
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_RUNES['data']))

    @patch(
        'blueprints.runes_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_runes_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_runes = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = rb.get_runes()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_runes.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')


class test_blueprint_get_rune_by_name(unittest.TestCase):

    @patch(
        'blueprints.runes_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_rune_by_name_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_runes = Mock(
            return_value=MOCK_RUNES
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = rb.get_rune_by_name(MOCK_RUNES['data'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_runes.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_RUNES['data'][0]))

    @patch(
        'blueprints.runes_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_rune_by_name_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=MOCK_RUNES)

        ret = rb.get_rune_by_name(MOCK_RUNES['data'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_RUNES['data'][0]))

    @patch(
        'blueprints.runes_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_rune_by_name_not_found(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_runes = Mock(
            return_value=MOCK_RUNES
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = rb.get_rune_by_name(None)
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_runes.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Rune not found.')

    @patch(
        'blueprints.runes_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_rune_by_name_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_runes = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = rb.get_rune_by_name(MOCK_RUNES['data'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_runes.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
