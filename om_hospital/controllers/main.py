from odoo import http
from odoo.http import request
import json


class YourController(http.Controller):

    @http.route('/api/test', auth='public', methods=['POST'], csrf=False)
    def api_test(self, **kwargs):
        try:
            # Get the raw data from the request
            data = request.httprequest.data.decode('utf-8')

            # Check if the data is JSON
            if data:
                try:
                    json_payload = json.loads(data)
                except ValueError:
                    return "Invalid JSON format"

                # Process your JSON data here
                doctor_name = json_payload.get('doctor_name')
                age = json_payload.get('age')
                gender = json_payload.get('gender')

                # Create a new record in hospital.doctor
                Doctor = request.env['hospital.doctor']
                new_doctor = Doctor.create({
                    'doctor_name': doctor_name,
                    'age': age,
                    'gender': gender
                })

                # Optionally, return a response confirming the creation
                return f"Doctor '{doctor_name}' created successfully with ID: {new_doctor.id}"
            else:
                return "Empty request body"

        except Exception as e:
            return f"Error: {e}"
