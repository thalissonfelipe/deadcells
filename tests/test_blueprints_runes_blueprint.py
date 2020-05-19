import json
import unittest
from unittest.mock import patch, Mock
from blueprints import runes_blueprint as rb


MOCK_RUNES = [
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


class test_blueprint_get_runes(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_runes',
        return_value=MOCK_RUNES
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_RUNES)
    )
    def test_get_runes_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = rb.get_runes()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_RUNES))
        mock_json.assert_called()
        mock_scrapper.assert_called()

    @patch(
        'blueprints.runes_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_runes',
        side_effect=Exception('Exception')
    )
    def test_get_runes_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = rb.get_runes()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()


class test_blueprint_get_rune_by_name(unittest.TestCase):

    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_RUNES[0])
    )
    @patch(
        'scrapper.Scrapper.get_runes',
        return_value=MOCK_RUNES
    )
    def test_get_rune_by_name_success(
        self,
        mock_scrapper,
        mock_json,
    ):
        ret = rb.get_rune_by_name(MOCK_RUNES[0]['name'])
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_RUNES[0]))
        mock_scrapper.assert_called()
        mock_json.assert_called()

    @patch(
        'scrapper.Scrapper.get_runes',
        return_value=MOCK_RUNES
    )
    def test_get_rune_by_name_not_found(
        self,
        mock_scrapper
    ):
        ret = rb.get_rune_by_name(None)
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Rune not found.')
        mock_scrapper.assert_called()

    @patch(
        'blueprints.runes_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_runes',
        side_effect=Exception('Exception')
    )
    def test_get_rune_by_name_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = rb.get_rune_by_name(None)
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()
