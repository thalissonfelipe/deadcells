import json
import unittest
from unittest.mock import patch, Mock
from blueprints import mutations_blueprint as mb


MOCK_MUTATIONS = {
    'name': 'mutations',
    'data': [
        {
            'type': 'brutality',
            'mutations': [
                {
                    'name': 'Killer Instinct',
                    'image': 'path_to_image',
                    'description': 'Reduces the cooldown of your skills by',
                    'acquisition_method': 'N/A (Always available)',
                    'unlock_cost': 'N/A',
                    'notes': [
                        'Reduces your skill cooldowns when you kill an enemy'
                    ]
                }
            ]
        }
    ]
}


class test_blueprint_get_mutations(unittest.TestCase):

    @patch(
        'blueprints.mutations_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_mutations_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_mutations = Mock(
            return_value=MOCK_MUTATIONS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = mb.get_mutations()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_mutations.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_MUTATIONS['data']))

    @patch(
        'blueprints.mutations_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_mutations_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(
            return_value=MOCK_MUTATIONS
        )

        ret = mb.get_mutations()
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_MUTATIONS['data']))

    @patch(
        'blueprints.mutations_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_mutations_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_mutations = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = mb.get_mutations()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_mutations.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')


class test_blueprint_get_mutations_by_type(unittest.TestCase):

    @patch(
        'blueprints.mutations_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_mutations_by_type_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_mutations = Mock(
            return_value=MOCK_MUTATIONS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = mb.get_mutations_by_type('brutality')
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_mutations.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_MUTATIONS['data'][0])
        )

    @patch(
        'blueprints.mutations_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_mutations_by_type_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(
            return_value=MOCK_MUTATIONS
        )

        ret = mb.get_mutations_by_type('brutality')
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_MUTATIONS['data'][0])
        )

    def test_get_mutations_by_type_invalid_mutation_type(self):
        ret = mb.get_mutations_by_type(None)
        self.assertEqual(ret.status_code, 400)
        self.assertEqual(ret.data.decode(), 'Invalid mutation type.')

    @patch(
        'blueprints.mutations_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_mutations_by_type_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_mutations = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = mb.get_mutations_by_type('brutality')
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_mutations.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')


class test_blueprint_get_mutation_by_name(unittest.TestCase):

    @patch(
        'blueprints.mutations_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_mutation_by_name_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_mutations = Mock(
            return_value=MOCK_MUTATIONS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = mb.get_mutation_by_name(
            MOCK_MUTATIONS['data'][0]['mutations'][0]['name']
        )
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_mutations.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_MUTATIONS['data'][0]['mutations'][0])
        )

    @patch(
        'blueprints.mutations_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_mutation_by_name_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(
            return_value=MOCK_MUTATIONS
        )

        ret = mb.get_mutation_by_name(
            MOCK_MUTATIONS['data'][0]['mutations'][0]['name']
        )
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_MUTATIONS['data'][0]['mutations'][0])
        )

    @patch(
        'blueprints.mutations_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_mutation_by_name_not_found(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_mutations = Mock(
            return_value=MOCK_MUTATIONS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = mb.get_mutation_by_name(None)
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_mutations.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Mutation not found.')

    @patch(
        'blueprints.mutations_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_mutation_by_name_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_mutations = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = mb.get_mutation_by_name(
            MOCK_MUTATIONS['data'][0]['mutations'][0]['name']
        )
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_mutations.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
