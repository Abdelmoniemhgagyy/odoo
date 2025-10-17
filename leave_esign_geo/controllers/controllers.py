from odoo import http, fields
from odoo.http import request
import base64
import logging

_logger = logging.getLogger(__name__)


class LeaveSignController(http.Controller):

    @http.route(['/leave/sign/<string:token>'], type='http', auth='public', website=True)
    def leave_sign_page(self, token, **kwargs):
        rec = request.env['leave.esign'].sudo().search([('token', '=', token)], limit=1)
        if not rec:
            return request.render('leave_esign_geo.leave_sign_not_found', {})
        return request.render('leave_esign_geo.leave_sign_template', {'rec': rec})

    @http.route(['/leave/sign/submit'], type='json', auth='public', website=True, csrf=False)
    def leave_sign_submit(self, token=None, signature_data=None, lat=None, lon=None, **kwargs):
        _logger.info('=== Leave Sign Submit Called ===')
        _logger.info('Token: %s', token)
        _logger.info('Has signature: %s', bool(signature_data))
        _logger.info('Lat received: %s (type: %s)', lat, type(lat))
        _logger.info('Lon received: %s (type: %s)', lon, type(lon))

        try:
            if not token:
                _logger.warning('Missing token')
                return {'success': False, 'error': 'missing_token'}

            if not signature_data:
                _logger.warning('Missing signature')
                return {'success': False, 'error': 'missing_signature'}

            rec = request.env['leave.esign'].sudo().search([('token', '=', token)], limit=1)
            if not rec:
                _logger.warning('Record not found for token: %s', token)
                return {'success': False, 'error': 'not_found'}

            if signature_data.startswith('data:'):
                header, b64 = signature_data.split(',', 1)
                mime = header.split(';')[0].replace('data:', '')

                # Format location properly
                location_str = ''
                if lat and lon and lat != '' and lon != '':
                    try:
                        lat_float = float(lat)
                        lon_float = float(lon)
                        location_str = f"{lat_float},{lon_float}"
                        _logger.info('Location formatted: %s', location_str)
                    except (ValueError, TypeError) as e:
                        _logger.warning('Could not parse location: %s', e)
                        location_str = 'Location not available'
                else:
                    location_str = 'Location not available'
                    _logger.warning('Location not provided or empty')

                rec.sudo().write({
                    'signature': base64.b64decode(b64),
                    'signature_mime': mime,
                    'signature_time': fields.Datetime.now(),
                    'signed_location': location_str
                })

                _logger.info('Signature saved successfully for record: %s with location: %s', rec.name, location_str)

                # Call action if exists
                if hasattr(rec, 'action_mark_waiting_hr'):
                    rec.sudo().action_mark_waiting_hr()
                    _logger.info('Action mark_waiting_hr executed')

                return {'success': True}
            else:
                _logger.warning('Invalid signature format')
                return {'success': False, 'error': 'invalid_signature_format'}

        except Exception as e:
            _logger.exception('Error in leave_sign_submit')
            return {'success': False, 'error': str(e)}