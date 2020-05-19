import json
import unittest
from unittest.mock import patch, Mock
from blueprints import enemies_blueprint as eb


MOCK_ENEMIES = [
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


class test_blueprint_get_enemies(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_enemies',
        return_value=MOCK_ENEMIES
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_ENEMIES)
    )
    def test_get_enemies_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = eb.get_enemies()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_ENEMIES))
        mock_json.assert_called()
        mock_scrapper.assert_called()

    @patch(
        'blueprints.enemies_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_enemies',
        side_effect=Exception('Exception')
    )
    def test_get_enemies_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = eb.get_enemies()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()


class test_blueprint_get_enemy_by_name(unittest.TestCase):

    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_ENEMIES[0])
    )
    @patch(
        'scrapper.Scrapper.get_enemies',
        return_value=MOCK_ENEMIES
    )
    def test_get_enemy_by_name_success(
        self,
        mock_scrapper,
        mock_json,
    ):
        ret = eb.get_enemy_by_name(MOCK_ENEMIES[0]['name'])
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_ENEMIES[0]))
        mock_scrapper.assert_called()
        mock_json.assert_called()

    @patch(
        'scrapper.Scrapper.get_enemies',
        return_value=MOCK_ENEMIES
    )
    def test_get_enemy_by_name_not_found(
        self,
        mock_scrapper
    ):
        ret = eb.get_enemy_by_name(None)
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Enemy not found.')
        mock_scrapper.assert_called()

    @patch(
        'blueprints.enemies_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_enemies',
        side_effect=Exception('Exception')
    )
    def test_get_enemy_by_name_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = eb.get_enemy_by_name(None)
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()
