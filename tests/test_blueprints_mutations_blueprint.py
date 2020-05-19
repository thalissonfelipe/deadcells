import json
import unittest
from unittest.mock import patch, Mock
from blueprints import mutations_blueprint as mb


MOCK_MUTATIONS = [
    {
        'type': 'brutality',
        'mutations': [
            {
                'name': 'Killer Instinct',
                'image': 'path_to_image',
                'description': 'Reduces the cooldown of your skills by ...',
                'acquisition_method': 'N/A (Always available)',
                'unlock_cost': 'N/A',
                'notes': [
                    'Reduces your skill cooldowns when you kill an enemy ..'
                ]
            }
        ]
    }
]


class test_blueprint_get_mutations(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_mutations',
        return_value=MOCK_MUTATIONS
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_MUTATIONS)
    )
    def test_get_mutations_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = mb.get_mutations()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_MUTATIONS))
        mock_json.assert_called()
        mock_scrapper.assert_called()

    @patch(
        'blueprints.mutations_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_mutations',
        side_effect=Exception('Exception')
    )
    def test_get_mutations_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = mb.get_mutations()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()


class test_blueprint_get_mutations_by_type(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_mutations',
        return_value=MOCK_MUTATIONS
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_MUTATIONS)
    )
    def test_get_mutations_by_type_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = mb.get_mutations_by_type('brutality')
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_MUTATIONS[0]))
        mock_json.assert_called()
        mock_scrapper.assert_called()

    def test_get_mutations_by_type_invalid_mutation_type(self):
        ret = mb.get_mutations_by_type(None)
        self.assertEqual(ret.status_code, 400)
        self.assertEqual(ret.data.decode(), 'Invalid mutation type.')

    @patch(
        'blueprints.mutations_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_mutations',
        side_effect=Exception('Exception')
    )
    def test_get_mutations_by_type_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = mb.get_mutations_by_type('brutality')
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()


class test_blueprint_get_mutation_by_name(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_mutations',
        return_value=MOCK_MUTATIONS
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_MUTATIONS)
    )
    def test_get_mutation_by_name_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = mb.get_mutation_by_name(
            MOCK_MUTATIONS[0]['mutations'][0]['name'])
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_MUTATIONS[0]['mutations'][0])
        )
        mock_json.assert_called()
        mock_scrapper.assert_called()

    @patch(
        'scrapper.Scrapper.get_mutations',
        return_value=MOCK_MUTATIONS
    )
    def test_get_mutation_by_name_not_found(self, mock_scrapper):
        ret = mb.get_mutation_by_name(None)
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Mutation not found.')

    @patch(
        'blueprints.mutations_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_mutations',
        side_effect=Exception('Exception')
    )
    def test_get_mutation_by_name_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = mb.get_mutation_by_name(
            MOCK_MUTATIONS[0]['mutations'][0]['name'])
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()
