import json
import unittest
from unittest.mock import patch, Mock
from blueprints import npcs_blueprint as nb


MOCK_NPCS = {
    'name': 'npcs',
    'data': [
        {
            'name': 'Tutorial Knight',
            'info': 'Guides the player throughout the start of the game, ...',
            'location': 'Prisoners\' Quarters',
            'image': 'path_to_image'
        }
    ]
}


class test_blueprint_get_npcs(unittest.TestCase):

    @patch(
        'blueprints.npcs_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_npcs_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_npcs = Mock(
            return_value=MOCK_NPCS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = nb.get_npcs()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_npcs.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_NPCS['data']))

    @patch(
        'blueprints.npcs_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_npcs_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=MOCK_NPCS)

        ret = nb.get_npcs()
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_NPCS['data']))

    @patch(
        'blueprints.npcs_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_npcs_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_npcs = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = nb.get_npcs()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_npcs.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')


class test_blueprint_get_npc_by_name(unittest.TestCase):

    @patch(
        'blueprints.npcs_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_npc_by_name_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_npcs = Mock(
            return_value=MOCK_NPCS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = nb.get_npc_by_name(MOCK_NPCS['data'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_npcs.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_NPCS['data'][0]))

    @patch(
        'blueprints.npcs_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_npc_by_name_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=MOCK_NPCS)

        ret = nb.get_npc_by_name(MOCK_NPCS['data'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_NPCS['data'][0]))

    @patch(
        'blueprints.npcs_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_npc_by_name_not_found(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_npcs = Mock(
            return_value=MOCK_NPCS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = nb.get_npc_by_name(None)
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_npcs.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'NPC not found.')

    @patch(
        'blueprints.npcs_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_npc_by_name_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_npcs = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = nb.get_npc_by_name(MOCK_NPCS['data'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_npcs.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
