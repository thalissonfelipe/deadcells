import json
import unittest
from unittest.mock import patch, Mock
from blueprints import biomes_blueprint as bb


MOCK_BIOMES = {
    'name': 'biomes',
    'data': [
        {
            'name': 'Prisoners Quarters',
            'location': 'Above the Promenade of the Condemned',
            'next_biome(s)':
            'Promenade of the Condemned, Toxic Sewers, Dilapidated Arboretum',
            'enemy_tier': '1 (0 BSC) / 6 (5 BSC)',
            'gear_level': '1 (0 BSC) / 4 (5 BSC)',
            'scrolls': '2 Scrolls of Power',
            'blueprints_from_secret_areas':
                'Quick Bow, Broadsword, Disengagement,' +
                'Golden Outfit, Crowbar, HEV Outfit',
            'enemies': [
                'Zombies, Shield Bearers, Grenadiers, Undead Archers',
                'Rancid Rat, Knife Throwers (1+ BSC, replaces Undead Archers)',
                'Guardians (2+ BSC)',
                'Rampagers (3+ BSC)',
                'Failed Experiments, (replaces Zombies) Inquisitors (4+ BSC)'
            ],
            'hazards': 'Spikes, rotating spiked balls',
            'wandering_elite_chance': '0%',
            'elite_room_chance': '5%',
            'stage': '1'
        }
    ]
}


class test_blueprint_get_biomes(unittest.TestCase):

    @patch(
        'blueprints.biomes_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_biomes_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_biomes = Mock(
            return_value=MOCK_BIOMES
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = bb.get_biomes()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_biomes.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_BIOMES['data'])
        )

    @patch(
        'blueprints.biomes_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_biomes_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(
            return_value=MOCK_BIOMES
        )

        ret = bb.get_biomes()
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_BIOMES['data'])
        )

    @patch(
        'blueprints.biomes_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_biomes_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_biomes = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = bb.get_biomes()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_biomes.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')


class test_blueprint_get_biome_by_name(unittest.TestCase):

    @patch(
        'blueprints.biomes_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_biome_by_name_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get_biome = Mock(
            return_value=MOCK_BIOMES['data'][0]
        )

        ret = bb.get_biome_by_name(MOCK_BIOMES['data'][0]['name'])
        mock_current_app.scrapper_manager.get_biome.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_BIOMES['data'][0])
        )

    @patch(
        'blueprints.biomes_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_biome_by_name_not_found(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get_biome = Mock(
            return_value=None
        )

        ret = bb.get_biome_by_name(None)
        mock_current_app.scrapper_manager.get_biome.assert_called()
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Biome not found.')

    @patch(
        'blueprints.biomes_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_biome_by_name_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get_biome = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = bb.get_biome_by_name(MOCK_BIOMES['data'][0]['name'])
        mock_current_app.scrapper_manager.get_biome.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
