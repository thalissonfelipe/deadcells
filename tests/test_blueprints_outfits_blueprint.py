import json
import unittest
from unittest.mock import patch, Mock
from blueprints import outfits_blueprint as ob


MOCK_OUTFITS = {
    'name': 'outfits',
    'data': [
        {
            'image': 'path_to_image',
            'name': 'Classic Outfit',
            'description': 'You went through a lot with this one, ...',
            'location': 'N/A',
            'difficulty_required': 'N/A',
            'cell_cost': 'N/A',
            'reference': ''
        }
    ]
}


class test_blueprint_get_outfits(unittest.TestCase):

    @patch(
        'blueprints.outfits_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_outfits_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_outfits = Mock(
            return_value=MOCK_OUTFITS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = ob.get_outfits()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_outfits.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_OUTFITS['data']))

    @patch(
        'blueprints.outfits_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_outfits_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(
            return_value=MOCK_OUTFITS
        )

        ret = ob.get_outfits()
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_OUTFITS['data']))

    @patch(
        'blueprints.outfits_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_outfits_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_outfits = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = ob.get_outfits()
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_outfits.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')


class test_blueprint_get_outfit_by_name(unittest.TestCase):

    @patch(
        'blueprints.outfits_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_outfit_by_name_success(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_outfits = Mock(
            return_value=MOCK_OUTFITS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = ob.get_outfit_by_name(MOCK_OUTFITS['data'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_outfits.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_OUTFITS['data'][0])
        )

    @patch(
        'blueprints.outfits_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_outfit_by_name_success_from_memory(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(
            return_value=MOCK_OUTFITS
        )

        ret = ob.get_outfit_by_name(MOCK_OUTFITS['data'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.data.decode(),
            json.dumps(MOCK_OUTFITS['data'][0])
        )

    @patch(
        'blueprints.outfits_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_outfit_by_name_not_found(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_outfits = Mock(
            return_value=MOCK_OUTFITS
        )
        mock_current_app.scrapper_manager.insert = Mock()

        ret = ob.get_outfit_by_name(None)
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_outfits.assert_called()
        mock_current_app.scrapper_manager.insert.assert_called()
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Outfit not found.')

    @patch(
        'blueprints.outfits_blueprint.current_app',
        return_value=Mock()
    )
    def test_get_outfit_by_name_internal_error(
        self,
        mock_current_app
    ):
        mock_current_app.scrapper_manager = Mock()
        mock_current_app.scrapper_manager.get = Mock(return_value=None)
        mock_current_app.scrapper_manager.get_outfits = Mock(
            side_effect=Exception()
        )
        mock_current_app.logger.exception = Mock()

        ret = ob.get_outfit_by_name(MOCK_OUTFITS['data'][0]['name'])
        mock_current_app.scrapper_manager.get.assert_called()
        mock_current_app.scrapper_manager.get_outfits.assert_called()
        mock_current_app.logger.exception.assert_called()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
