from odoo import http
from odoo.http import request
import base64


class HotbaAPI(http.Controller):

    @http.route('/api/hotba/video/<int:hotba_id>', type='http', auth='public')
    def get_video(self, hotba_id):
        hotba = request.env['hotba'].sudo().browse(hotba_id)
        if hotba and hotba.video:
            video_data = base64.b64decode(hotba.video)
            headers = [
                ('Content-Type', 'video/mp4'),
                ('Content-Length', str(len(video_data)))
            ]
            return request.make_response(video_data, headers=headers)
        return request.not_found()
