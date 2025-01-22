from . import db
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer  # Updated import
from flask import current_app
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime, timezone


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, max_age=1800)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"<User {self.email}>"

class CopySearchRequest(db.Model):
    __tablename__ = 'copy_search_requests'

    id = db.Column(db.Integer, primary_key=True)
    address_of_development = db.Column(db.String(255), nullable=False)
    date_of_approval = db.Column(db.Date, nullable=True)  # Optional field
    registration_number = db.Column(db.String(50), nullable=True)  # Optional field
    name_of_owner = db.Column(db.String(255), nullable=False)
    address_of_owner = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)  # Date of request submission

    def __repr__(self):
        return f'<CopySearchRequest {self.id} - {self.name_of_owner}>'


class ChangeOwnershipFormModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    cemetery = db.Column(db.String(100), nullable=False)
    block_number = db.Column(db.String(50), nullable=False)
    grave_space = db.Column(db.String(50), nullable=False)
    owner_details = db.Column(db.Text, nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    name_1 = db.Column(db.String(100), nullable=True)
    address_1 = db.Column(db.String(200), nullable=True)
    signature_1 = db.Column(db.String(50), nullable=True)
    id_number_1 = db.Column(db.String(20), nullable=True)


class PublicComplaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    premises = db.Column(db.String(255), nullable=False)
    nature_of_complaint = db.Column(db.Text, nullable=False)
    complainant_name = db.Column(db.String(255), nullable=False)
    contact_details = db.Column(db.String(255), nullable=False)
    action_taken = db.Column(db.Text, nullable=True)
    
    
class FoodHandler(db.Model):
    __tablename__ = 'food_handlers'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    home_address = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    identification_no = db.Column(db.String(50), nullable=False)
    telephone = db.Column(db.String(20), nullable=True)
    business_name = db.Column(db.String(255), nullable=False)
    business_type = db.Column(db.String(255), nullable=False)
    business_address = db.Column(db.String(255), nullable=False)

    # Family History
    family_typhoid = db.Column(db.Boolean, nullable=True, default=False)
    family_tuberculosis = db.Column(db.Boolean, nullable=True, default=False)
    family_jaundice = db.Column(db.Boolean, nullable=True, default=False)
    family_chronic_cough = db.Column(db.Boolean, nullable=True, default=False)
    family_hospitalization = db.Column(db.Boolean, nullable=True, default=False)
    family_other = db.Column(db.String(255), nullable=True)

    # Personal History
    personal_typhoid = db.Column(db.Boolean, nullable=True, default=False)
    personal_tuberculosis = db.Column(db.Boolean, nullable=True, default=False)
    personal_jaundice = db.Column(db.Boolean, nullable=True, default=False)
    personal_chronic_cough = db.Column(db.Boolean, nullable=True, default=False)
    personal_hospitalization = db.Column(db.Boolean, nullable=True, default=False)
    personal_asthmatic_attacks = db.Column(db.Boolean, nullable=True, default=False)
    personal_allergies = db.Column(db.Boolean, nullable=True, default=False)
    personal_other = db.Column(db.String(255), nullable=True)


    # Declaration
    declaration = db.Column(db.Boolean, nullable=False)
    applicant_signature = db.Column(db.String(255), nullable=False)
    applicant_signature_date = db.Column(db.Date, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f'<FoodHandler {self.name}>'    
    
class RemoveOwnership(db.Model):
    __tablename__ = 'remove_ownership'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    cemetery = db.Column(db.String(255), nullable=False)
    block_number = db.Column(db.String(255), nullable=False)
    grave_space = db.Column(db.String(255), nullable=False)
    owner_details = db.Column(db.Text, nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<RemoveOwnership {self.id}>"


class IncludeOwnership(db.Model):
    __tablename__ = 'include_ownership'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    cemetery = db.Column(db.String(255), nullable=False)
    block_number = db.Column(db.String(255), nullable=False)
    grave_space = db.Column(db.String(255), nullable=False)
    additional_owner_details = db.Column(db.Text, nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<IncludeOwnership {self.id}>"


class TransferAllotment(db.Model):
    __tablename__ = 'transfer_allotment'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    cemetery = db.Column(db.String(255), nullable=False)
    block_number = db.Column(db.String(255), nullable=False)
    grave_space = db.Column(db.String(255), nullable=False)
    transfer_to = db.Column(db.Text, nullable=False)
    transfer_reason = db.Column(db.Text, nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<TransferAllotment {self.id}>" 
    
    
class BlockingFootwayRequest(db.Model):
    __tablename__ = 'blocking_footway_requests'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(500), nullable=False)
    period_days = db.Column(db.Integer, nullable=True)
    period_weeks = db.Column(db.Integer, nullable=True)
    period_months = db.Column(db.Integer, nullable=True)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=False)
    length_of_footway = db.Column(db.Integer, nullable=False)
    existing_width = db.Column(db.Integer, nullable=False)
    width_to_obstruct = db.Column(db.Integer, nullable=False)
    reason_for_application = db.Column(db.String(1000), nullable=False)
    applicant_name = db.Column(db.String(255), nullable=False)
    applicant_address = db.Column(db.String(500), nullable=False)
    owner_name = db.Column(db.String(255), nullable=False)
    owner_signature = db.Column(db.String(255), nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<BlockingFootwayRequest {self.id} - {self.applicant_name}>'
    
    
class BuildingApplication(db.Model):
    __tablename__ = 'building_applications'

    id = db.Column(db.Integer, primary_key=True)
    work_type = db.Column(db.String(50), nullable=False)
    premises_no = db.Column(db.String(255), nullable=False)
    north_dimension = db.Column(db.String(50), nullable=True)
    south_dimension = db.Column(db.String(50), nullable=True)
    east_dimension = db.Column(db.String(50), nullable=True)
    west_dimension = db.Column(db.String(50), nullable=True)
    nature_of_building = db.Column(db.String(50), nullable=False)
    building_length = db.Column(db.Integer, nullable=True)
    building_width = db.Column(db.Integer, nullable=True)
    building_height = db.Column(db.Integer, nullable=True)
    owner_name = db.Column(db.String(255), nullable=False)
    owner_signature = db.Column(db.String(255), nullable=False)
    contractor_name = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<BuildingApplication {self.id} - {self.owner_name}>'
    