import json
import unittest
from unittest.mock import patch, Mock
from blueprints import outfits_blueprint as ob


MOCK_OUTFITS = [
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


class test_blueprint_get_outfits(unittest.TestCase):

    @patch(
        'scrapper.Scrapper.get_outfits',
        return_value=MOCK_OUTFITS
    )
    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_OUTFITS)
    )
    def test_get_outfits_success(
        self,
        mock_json,
        mock_scrapper
    ):
        ret = ob.get_outfits()
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_OUTFITS))
        mock_json.assert_called()
        mock_scrapper.assert_called()

    @patch(
        'blueprints.outfits_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_outfits',
        side_effect=Exception('Exception')
    )
    def test_get_outfits_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = ob.get_outfits()
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()


class test_blueprint_get_outfit_by_name(unittest.TestCase):

    @patch(
        'json.dumps',
        return_value=json.dumps(MOCK_OUTFITS[0])
    )
    @patch(
        'scrapper.Scrapper.get_outfits',
        return_value=MOCK_OUTFITS
    )
    def test_get_outfit_by_name_success(
        self,
        mock_scrapper,
        mock_json,
    ):
        ret = ob.get_outfit_by_name(MOCK_OUTFITS[0]['name'])
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.data.decode(), json.dumps(MOCK_OUTFITS[0]))
        mock_scrapper.assert_called()
        mock_json.assert_called()

    @patch(
        'scrapper.Scrapper.get_outfits',
        return_value=MOCK_OUTFITS
    )
    def test_get_outfit_by_name_not_found(
        self,
        mock_scrapper
    ):
        ret = ob.get_outfit_by_name(None)
        self.assertEqual(ret.status_code, 404)
        self.assertEqual(ret.data.decode(), 'Outfit not found.')
        mock_scrapper.assert_called()

    @patch(
        'blueprints.outfits_blueprint.current_app',
        return_value=Mock()
    )
    @patch(
        'scrapper.Scrapper.get_outfits',
        side_effect=Exception('Exception')
    )
    def test_get_outfit_by_name_internal_error(
        self,
        mock_scrapper,
        mock_current_app
    ):
        mock_current_app.logger.exception = Mock()
        ret = ob.get_outfit_by_name(None)
        self.assertEqual(ret.status_code, 500)
        self.assertEqual(ret.data.decode(), 'Internal Server Error.')
        mock_scrapper.assert_called()
        mock_current_app.logger.exception.assert_called()
