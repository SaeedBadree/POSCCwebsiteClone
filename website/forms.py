from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, TelField, BooleanField, RadioField,IntegerField  # Ensure SubmitField is imported here
from wtforms.fields import DateField
from wtforms.validators import DataRequired,Length,Optional

class ChangeOwnershipForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    cemetery = StringField('Cemetery', validators=[DataRequired()])
    block_number = StringField('Block Number', validators=[DataRequired()])
    grave_space = StringField('Grave Space Number', validators=[DataRequired()])
    owner_details = TextAreaField('Owner Details (Name & Address)', validators=[DataRequired()])
    contact_number = TelField('Contact Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RemoveOwnershipForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    cemetery = StringField('Cemetery', validators=[DataRequired()])
    block_number = StringField('Block Number', validators=[DataRequired()])
    grave_space = StringField('Grave Space Number', validators=[DataRequired()])
    owner_details = TextAreaField('Owner Details (Name & Address)', validators=[DataRequired()])
    contact_number = TelField('Contact Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

class IncludeOwnershipForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    cemetery = StringField('Cemetery', validators=[DataRequired()])
    block_number = StringField('Block Number', validators=[DataRequired()])
    grave_space = StringField('Grave Space Number', validators=[DataRequired()])
    additional_owner_details = TextAreaField('Additional Owner Details (Name & Address)', validators=[DataRequired()])
    contact_number = TelField('Contact Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TransferAllotmentForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    cemetery = StringField('Cemetery', validators=[DataRequired()])
    block_number = StringField('Block Number', validators=[DataRequired()])
    grave_space = StringField('Grave Space Number', validators=[DataRequired()])
    transfer_to = TextAreaField('Transfer To (Name & Address)', validators=[DataRequired()])
    transfer_reason = TextAreaField('Reason for Transfer', validators=[DataRequired()])
    contact_number = TelField('Contact Number', validators=[DataRequired()])
    submit = SubmitField('Submit')


class FoodHandlersForm(FlaskForm):
    date = DateField('Date', format='%d/%m/%Y', validators=[DataRequired()], render_kw={"placeholder": "dd/mm/yyyy"})
    name = StringField('Name', validators=[DataRequired()])
    sex = RadioField('Sex', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    home_address = TextAreaField('Home Address', validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth', format='%d/%m/%Y', validators=[DataRequired()], render_kw={"placeholder": "dd/mm/yyyy"})
    identification_no = StringField('Identification No.', validators=[DataRequired()])
    telephone = StringField('Telephone', validators=[DataRequired()])
    business_name = StringField('Name of Business', validators=[DataRequired()])
    business_type = StringField('Type of Business', validators=[DataRequired()])
    business_address = TextAreaField('Address of Business', validators=[DataRequired()])

    # Family History
    family_typhoid = BooleanField('Typhoid (Family)')
    family_tuberculosis = BooleanField('Tuberculosis (Family)')
    family_jaundice = BooleanField('Jaundice (Family)')
    family_chronic_cough = BooleanField('Chronic Cough (Family)')
    family_hospitalization = BooleanField('Hospitalization (Family)')
    family_other = StringField('Other (Family)')

    # Personal History
    personal_typhoid = BooleanField('Typhoid (Personal)')
    personal_tuberculosis = BooleanField('Tuberculosis (Personal)')
    personal_jaundice = BooleanField('Jaundice (Personal)')
    personal_chronic_cough = BooleanField('Chronic Cough (Personal)')
    personal_hospitalization = BooleanField('Hospitalization (Personal)')
    personal_asthmatic_attacks = BooleanField('Asthmatic Attacks (Personal)')
    personal_allergies = BooleanField('Allergies, Skin disease, Ulcers')
    personal_other = StringField('Other (Personal)')

    # Declaration and Authorization
    declaration = BooleanField('I declare that the information I provided is correct.', validators=[DataRequired()])
    applicant_signature = StringField('Applicant Signature', validators=[DataRequired()])
    applicant_signature_date = DateField('Date', format='%d/%m/%Y', validators=[DataRequired()], render_kw={"placeholder": "dd/mm/yyyy"})

    submit = SubmitField('Submit')
    
    
class PublicComplaintForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()], format='%Y-%m-%d')
    premises = StringField('Premises', validators=[DataRequired(), Length(max=255)])
    nature_of_complaint = TextAreaField('Nature of Complaint', validators=[DataRequired()])
    complainant_name = StringField('Complainant Name', validators=[DataRequired(), Length(max=255)])
    contact_details = StringField('Contact Details', validators=[DataRequired(), Length(max=255)])
    action_taken = TextAreaField('Action Taken (optional)')
    submit = SubmitField('Submit') 
    
    
class CopySearchForm(FlaskForm):
    address_of_development = StringField(
        'Address of Development',
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter the address of development"}
    )
    date_of_approval = DateField(
        'Date of Approval',
        validators=[Optional()],
        render_kw={"type": "date"}  # Ensure it matches the HTML input type
    )
    registration_number = StringField(
        'Registration Number (if available)',
        validators=[Optional()],
        render_kw={"placeholder": "Enter the registration number"}
    )
    name_of_owner = StringField(
        'Name of Owner',
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter the owner's name"}
    )
    address_of_owner = StringField(
        'Address of Owner',
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter the owner's address"}
    )
    date = DateField(
        'Date',
        validators=[DataRequired()],
        render_kw={"type": "date"}  # Matches HTML input type
    )
    submit = SubmitField('Submit')
    
    
class BlockingFootwayForm(FlaskForm):
     location = TextAreaField(
        'Location',
        validators=[DataRequired(), Length(max=500)],
        render_kw={"placeholder": "Enter the location details"}
    )
     period_days = IntegerField(
        'Days',
        validators=[Optional()],
        render_kw={"placeholder": "Number of days"}
    )
     period_weeks = IntegerField(
        'Weeks',
        validators=[Optional()],
        render_kw={"placeholder": "Number of weeks"}
    )
     period_months = IntegerField(
        'Months',
        validators=[Optional()],
        render_kw={"placeholder": "Number of months"}
    )
     from_date = DateField(
        'From',
        format='%d/%m/%Y',
        validators=[DataRequired()],
        render_kw={"placeholder": "dd/mm/yyyy"}
    )
     to_date = DateField(
        'To',
        format='%d/%m/%Y',
        validators=[DataRequired()],
        render_kw={"placeholder": "dd/mm/yyyy"}
    )
     length_of_footway = IntegerField(
        'Length of Footway to be Obstructed (metres)',
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter the length in metres"}
    )
     existing_width = IntegerField(
        'Existing Width of Footway (metres)',
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter the existing width in metres"}
    )
     width_to_obstruct = IntegerField(
        'Width of Footway to be Obstructed (metres)',
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter the width to be obstructed"}
    )
     reason_for_application = TextAreaField(
        'Reason for Application',
        validators=[DataRequired(), Length(max=1000)],
        render_kw={"placeholder": "State the reason for application"}
    )
     applicant_name = StringField(
        'Name of Applicant',
        validators=[DataRequired(), Length(max=255)],
        render_kw={"placeholder": "Enter your full name"}
    )
     applicant_address = TextAreaField(
        'Address of Applicant',
        validators=[DataRequired(), Length(max=500)],
        render_kw={"placeholder": "Enter your address"}
    )
     owner_name = StringField(
        'Owner’s Name (Block Letters)',
        validators=[DataRequired(), Length(max=255)],
        render_kw={"placeholder": "Enter the owner's name"}
    )
     owner_signature = StringField(
        'Signature of Owner',
        validators=[DataRequired(), Length(max=255)],
        render_kw={"placeholder": "Owner's signature"}
    )
     submit = SubmitField('Submit')
    
class BuildingApplicationForm(FlaskForm):
    work_type = RadioField(
        'Type of Work',
        choices=[
            ('new_building', 'Erect a new building'),
            ('repairs', 'Carry out repairs/alterations'),
            ('additions', 'Construct additions'),
            ('change_of_use', 'Change of use')
        ],
        validators=[DataRequired()]
    )
    premises_no = StringField(
        'Premises No.',
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter premises number"}
    )
    north_dimension = StringField(
        'North Dimension',
        validators=[Optional()],
        render_kw={"placeholder": "Enter dimension"}
    )
    south_dimension = StringField(
        'South Dimension',
        validators=[Optional()],
        render_kw={"placeholder": "Enter dimension"}
    )
    east_dimension = StringField(
        'East Dimension',
        validators=[Optional()],
        render_kw={"placeholder": "Enter dimension"}
    )
    west_dimension = StringField(
        'West Dimension',
        validators=[Optional()],
        render_kw={"placeholder": "Enter dimension"}
    )
    nature_of_building = RadioField(
        'Nature of Building',
        choices=[
            ('residential', 'Residential'),
            ('mixed_use', 'Mixed Use'),
            ('commercial', 'Commercial'),
            ('institutional', 'Institutional')
        ],
        validators=[DataRequired()]
    )
    building_length = IntegerField(
        'Building Length (meters)',
        validators=[Optional()],
        render_kw={"placeholder": "Enter length"}
    )
    building_width = IntegerField(
        'Building Width (meters)',
        validators=[Optional()],
        render_kw={"placeholder": "Enter width"}
    )
    building_height = IntegerField(
        'Building Height (meters)',
        validators=[Optional()],
        render_kw={"placeholder": "Enter height"}
    )
    owner_name = StringField(
        'Name of Owner',
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter owner name"}
    )
    owner_signature = StringField(
        'Owner Signature',
        validators=[DataRequired()],
        render_kw={"placeholder": "Owner signature"}
    )
    contractor_name = StringField(
        'Name of Contractor',
        validators=[Optional()],
        render_kw={"placeholder": "Enter contractor name"}
    )
    submit = SubmitField('Submit')
    