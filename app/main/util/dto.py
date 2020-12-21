from flask_restx import Namespace, fields, Model


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'phone': fields.String(required=True, description='user phone number')
    })
    _user = api.model('_user', {
        'username': fields.String(),
        'public_id': fields.String(),
        'email': fields.String(),
        'phone': fields.String(),
        'registered_robot_id': fields.String(),
    })
    _farm = api.model('_farm',{
        'name':fields.String(),
        'city':fields.String(),
        'owner':fields.String(),
        'public_id':fields.String(),
        'user_id':fields.String()
        })

    _robot = api.model('_robot', {
        'name' : fields.String(),
        'model': fields.String(),
        'public_id': fields.String(),
        'user_id': fields.String(),
        'pi_type': fields.String(),
        'aurdino_type': fields.String(),
        'motor_type': fields.String(),
        'motor_driver_type': fields.String(),
        'battey_info': fields.String(),
        'public_url': fields.String(),
        'public_pnumber':fields.String(),
        'is_solar': fields.Boolean(),
        'is_led': fields.Boolean(),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

