import json
import unittest
from unittest.mock import patch, Mock
from blueprints import biomes_blueprint as bb


MOCK_BIOMES = [
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


class test_blueprint_get_biomes(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_biomes',
        return_value=MOCK_BIOMES
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_BIOMES)
    )
    def test_get_biomes_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = bb.get_biomes()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_BIOMES))
        mock_json.assert_called()
        mock_scrapper.assert_called()

    @patch(
        'blueprints.biomes_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_biomes',
        side_effect=Exception('Exception')
    )
    def test_get_biomes_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = bb.get_biomes()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()


class test_blueprint_get_biome_by_name(unittest.TestCase):

    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_BIOMES[0])
    )
    @patch(
        'scrapper.Scrapper.get_biome',
        return_value=MOCK_BIOMES[0]
    )
    def test_get_biome_by_name_success(
        self,
        mock_scrapper,
        mock_json,
    ):
        ret = bb.get_biome_by_name(MOCK_BIOMES[0]['name'])
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_BIOMES[0]))
        mock_scrapper.assert_called()
        mock_json.assert_called()

    @patch(
        'scrapper.Scrapper.get_biome',
        return_value=None
    )
    def test_get_biome_by_name_not_found(
        self,
        mock_scrapper
    ):
        ret = bb.get_biome_by_name(None)
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Biome not found.')
        mock_scrapper.assert_called()

    @patch(
        'blueprints.biomes_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_biome',
        side_effect=Exception('Exception')
    )
    def test_get_biome_by_name_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = bb.get_biome_by_name(None)
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()
