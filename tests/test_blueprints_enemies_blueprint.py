import json
import unittest
from unittest.mock import patch, Mock
from blueprints import enemies_blueprint as eb


MOCK_ENEMIES = {
    'name': 'enemies',
    'data': [
        {
            'image': 'path_to_image',
            'name': 'Zombie',
            'zones': ['Prisoners\' Quarters'],
            'offensive_abilities': ['Clawing attack'],
            'deffensive_abilities': 'Hops backwards',
            'elite': 'Yes',
            'cell_drops': '1 (33%)',
            'blueprint_drops': [
                'Blood Sword (100%)',
                'Double Crossb-o-matic (0.4%) ',
                'Boeby Outfit (1+ BSC; 0.4%)'
            ]
        }
    ]
}


class test_blueprint_get_enemies(unittest.TestCase):

    @patch(
        'blueprints.enemies_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_enemies_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_enemies = Mock(
            return_value=MOCK_ENEMIES
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = eb.get_enemies()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_enemies.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_ENEMIES['data']))

    @patch(
        'blueprints.enemies_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_enemies_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(
            return_value=MOCK_ENEMIES
        )

        ret = eb.get_enemies()
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_ENEMIES['data']))

    @patch(
        'blueprints.enemies_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_enemies_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_enemies = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = eb.get_enemies()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_enemies.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')


class test_blueprint_get_enemy_by_name(unittest.TestCase):

    @patch(
        'blueprints.enemies_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_enemy_by_name_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_enemies = Mock(
            return_value=MOCK_ENEMIES
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = eb.get_enemy_by_name(MOCK_ENEMIES['data'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_enemies.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_ENEMIES['data'][0])
        )

    @patch(
        'blueprints.enemies_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_enemy_by_name_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(
            return_value=MOCK_ENEMIES
        )

        ret = eb.get_enemy_by_name(MOCK_ENEMIES['data'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_ENEMIES['data'][0])
        )

    @patch(
        'blueprints.enemies_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_enemy_by_name_not_found(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_enemies = Mock(
            return_value=MOCK_ENEMIES
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = eb.get_enemy_by_name(None)
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_enemies.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Enemy not found.')

    @patch(
        'blueprints.enemies_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_enemy_by_name_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_enemies = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = eb.get_enemy_by_name(None)
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_enemies.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
