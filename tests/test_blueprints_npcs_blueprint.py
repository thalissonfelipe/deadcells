import json
import unittest
from unittest.mock import patch, Mock
from blueprints import npcs_blueprint as nb


MOCK_NPCS = [
    {
        'name': 'Tutorial Knight',
        'info': 'Guides the player throughout the start of the game, ...',
        'location': 'Prisoners\' Quarters',
        'image': 'path_to_image'
    }
]


class test_blueprint_get_npcs(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_npcs',
        return_value=MOCK_NPCS
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_NPCS)
    )
    def test_get_npcs_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = nb.get_npcs()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_NPCS))
        mock_json.assert_called()
        mock_scrapper.assert_called()

    @patch(
        'blueprints.npcs_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_npcs',
        side_effect=Exception('Exception')
    )
    def test_get_npcs_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = nb.get_npcs()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()


class test_blueprint_get_npc_by_name(unittest.TestCase):

    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_NPCS[0])
    )
    @patch(
        'scrapper.Scrapper.get_npcs',
        return_value=MOCK_NPCS
    )
    def test_get_npc_by_name_success(
        self,
        mock_scrapper,
        mock_json,
    ):
        ret = nb.get_npc_by_name(MOCK_NPCS[0]['name'])
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_NPCS[0]))
        mock_scrapper.assert_called()
        mock_json.assert_called()

    @patch(
        'scrapper.Scrapper.get_npcs',
        return_value=MOCK_NPCS
    )
    def test_get_npc_by_name_not_found(
        self,
        mock_scrapper
    ):
        ret = nb.get_npc_by_name(None)
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'NPC not found.')
        mock_scrapper.assert_called()

    @patch(
        'blueprints.npcs_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_npcs',
        side_effect=Exception('Exception')
    )
    def test_get_npc_by_name_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = nb.get_npc_by_name(None)
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()
