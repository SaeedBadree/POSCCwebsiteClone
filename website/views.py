from flask import Blueprint, render_template, url_for, request, jsonify
from flask_login import login_required, current_user
from .forms import ChangeOwnershipForm, RemoveOwnershipForm, IncludeOwnershipForm, TransferAllotmentForm, FoodHandlersForm, PublicComplaintForm,CopySearchForm, BlockingFootwayForm, BuildingApplicationForm
from .models import db, ChangeOwnershipFormModel,PublicComplaint,FoodHandler,CopySearchRequest,BlockingFootwayRequest,BuildingApplication
  
from flask import flash, redirect, url_for, render_template, request

views = Blueprint('views', __name__)

@views.route('/')
#@login_required
def home():
    return render_template('index.html', user=current_user)

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/services')
def services():
    return render_template('services.html')

@views.route('/departments')
def departments():
    return render_template('departments.html')

@views.route('/council')
def meet_the_council():
    councillors = [
        {
            "name": "Alderman Chinua Alleyne",
            "ward": "Ward 1",
            "image": "Alderman_Chinua_Alleyne.jpg",
            "description": "Alderman Chinua Alleyne is the Mayor of the City of Port of Spain and can be contacted via chinua.alleyne@gmail.com."
        },
        {
            "name": "Mr. Wade Coker",
            "ward": "Ward 2",
            "image": "Mr._Wade_Coker.jpg",
            "description": "Mr. Wade Coker can be contacted via wadecoker69@gmail.com."
        },
        {
            "name": "Mr. Brian Lewis",
            "ward": "Ward 3",
            "image": "Mr._Brian_Lewis.jpg",
            "description": "Mr. Brian Lewis can be contacted via briaclewis@gmail.com."
        },
        {
            "name": "Mr. Kareem Marcelle",
            "ward": "Ward 4",
            "image": "Mr._Kareem_Marcelle.jpg",
            "description": "Mr. Kareem Marcelle can be contacted via kareemmarcelle17@gmail.com."
        },
        {
            "name": "Ms. Maloula Bourne",
            "ward": "Ward 5",
            "image": "Ms._Maloula_Bourne.jpg",
            "description": "Ms. Maloula Bourne can be contacted via belmontnorthandwest@gmail.com."
        },
        {
            "name": "Mr. Raphael Bournes",
            "ward": "Ward 6",
            "image": "Mr._Raphael_Bournes.jpg",
            "description": "Mr. Raphael Bournes can be contacted via raphael.bournes77@gmail.com."
        },
        {
            "name": "Ms. Nicole Young",
            "ward": "Ward 7",
            "image": "Ms._Nicole_Young.jpg",
            "description": "Ms. Nicole Young can be contacted via belmonteast1@gmail.com."
        },
        {
            "name": "Ms. Alicia Gift",
            "ward": "Ward 8",
            "image": "Ms._Alicia_Gift.jpg",
            "description": "Ms. Alicia Gift can be contacted via aliciagift@hotmail.com."
        },
        {
            "name": "Ms. Abena Hartley",
            "ward": "Ward 9",
            "image": "Ms._Abena_Hartley.jpg",
            "description": "Ms. Abena Hartley is the Deputy Mayor and can be contacted via abenahartley@gmail.com."
        },
        {
            "name": "Mr. Dennis Russel Bristol",
            "ward": "Ward 10",
            "image": "Mr._Dennis_Russel_Bristol.jpg",
            "description": "Mr. Dennis Russel Bristol can be contacted via southernposcouncillor@gmail.com."
        },
        {
            "name": "Mr. Owen St. Rose",
            "ward": "Ward 11",
            "image": "Mr._Owen_St._Rose.jpg",
            "description": "Mr. Owen St. Rose can be contacted via ostrose21@gmail.com."
        },
        {
            "name": "Mr. Imran Khan",
            "ward": "Ward 12",
            "image": "Mr._Imran_Khan.jpg",
            "description": "Mr. Imran Khan can be contacted via 1868imrankhan@gmail.com."
        },
        {
            "name": "Mr. Jameel Bisnath",
            "ward": "Ward 13",
            "image": "Mr._Jameel_Bisnath.jpg",
            "description": "Mr. Jameel Bisnath can be contacted via jameelbisnath5@gmail.com."
        },
        {
            "name": "Mr. Clint Baptiste",
            "ward": "Ward 14",
            "image": "Mr._Clint_Baptiste.jpg",
            "description": "Mr. Clint Baptiste can be contacted via clintb1604@gmail.com."
        },
        {
            "name": "Ms. Esther Sylvester",
            "ward": "Ward 15",
            "image": "Ms._Esther_Sylvester.jpg",
            "description": "Ms. Esther Sylvester can be contacted via estar8322@gmail.com."
        },
        {
            "name": "Ms. Jenneil Frederick",
            "ward": "Ward 16",
            "image": "Ms._Jenneil_Frederick.jpg",
            "description": "Ms. Jenneil Frederick can be contacted via stanns.river.south@gmail.com."
        },
    ]
    return render_template('council.html', councillors=councillors)



@views.route('/contact')
def contact():
    return render_template('contact.html')



@views.route('/geospatial')
def geospatial():
    return render_template('geospatial.html')

@views.route('/procurement')
def procurement():
    pdf_url = url_for('static', filename='files/AnnualProcurement.pdf')
    return render_template('procurement.html', pdf_url=pdf_url)


@views.route('/projects')
def projects():
    current_projects = [
        {
            'id': '1',
            'title': 'Road Improvement Project',
            'image': 'images/road_improvement.jpg',
            'description': 'This project involves the improvement of major roads...'
        },
        {
            'id': '2',
            'title': 'New Community Center',
            'image': 'images/community_center.jpg',
            'description': 'A new community center is being built...'
        }
    ]

    completed_projects = [
        {
            'id': '3',
            'title': 'City Park Renovation',
            'image': 'images/city_park.jpg',
            'description': 'The city park renovation was completed...'
        },
        {
            'id': '4',
            'title': 'Downtown Cleanup',
            'image': 'images/downtown_cleanup.jpg',
            'description': 'A major cleanup initiative was successfully...'
        }
    ]

    return render_template('projects.html', current_projects=current_projects, completed_projects=completed_projects)


@views.route('/help')
def help():
    return render_template('help.html')


@views.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    
    # Simple logic to respond to specific questions
    if "hours" in user_message.lower():
        response = "The Port of Spain City Corporation is open from 8am to 4pm, Monday to Friday."
    elif "building permit" in user_message.lower():
        response = "You can apply for a building permit through our online portal or by visiting the Building Inspectorate office."
    elif "property taxes" in user_message.lower():
        response = "Property taxes can be paid at the Finance Department or through our online payment system."
    else:
        response = "Thank you for your message. We will get back to you shortly."
    
    return jsonify({"response": response})


@views.route('/cityAdmin', methods=['GET', 'POST'])
def cityAdmin():
    change_ownership_form = ChangeOwnershipForm()
    remove_ownership_form = RemoveOwnershipForm()
    include_ownership_form = IncludeOwnershipForm()
    transfer_allotment_form = TransferAllotmentForm()

    return render_template(
        'cityAdmin.html',
        change_ownership_form=change_ownership_form,
        remove_ownership_form=remove_ownership_form,
        include_ownership_form=include_ownership_form,
        transfer_allotment_form=transfer_allotment_form,
    )
    
@views.route('/city_engineers', methods=['GET'])
def city_engineers():
    """Render the City Engineers page with forms."""
    copy_search_form = CopySearchForm()
    blocking_footway_form = BlockingFootwayForm()
    building_application_form = BuildingApplicationForm()
    return render_template(
        'cityEngineering.html',
        copy_search_form=copy_search_form,
        blocking_footway_form=blocking_footway_form,
        building_application_form=building_application_form
    )


@views.route('/cityPolice')
def cityPolice():
    return render_template('cityPolice.html')

@views.route('/publicHealth', methods=['GET'])
def publicHealth():
    # Instantiate both forms
    food_handlers_form = FoodHandlersForm()
    public_complaint_form = PublicComplaintForm()

    # Render the public health page with both forms
    return render_template(
        'publicHealth.html',
        food_handlers_form=food_handlers_form,
        public_complaint_form=public_complaint_form
    )





@views.route('/led')
def led():
    return render_template('led.html')

@views.route('/disasterManagement')
def disasterManagement():
    return render_template('disasterManagement.html')

@views.route('/cityAssessors')
def cityAssessors():
    return render_template('cityAssessors.html')

@views.route('/market')
def market():
    return render_template('market.html')

@views.route('/maintenance')
def maintenance():
    return render_template('maintenance.html')

@views.route('/news')
def news():
    return render_template('news.html')

@views.route('/treasurers')
def treasurers():
    return render_template('treasurers.html')

@views.route('/propertyManagement')
def propertyManagement():
    return render_template('propertyManagement.html')


@views.route('/submit_change_ownership', methods=['GET', 'POST'])
def submit_change_ownership():
    form = ChangeOwnershipForm()
    if form.validate_on_submit():  # This ensures the form is valid
        # Save data to the database
        new_entry = ChangeOwnershipFormModel(
            date=form.date.data,
            cemetery=form.cemetery.data,
            block_number=form.block_number.data,
            grave_space=form.grave_space.data,
            owner_details=form.owner_details.data,
            contact_number=form.contact_number.data,
            name_1=form.name_1.data,
            address_1=form.address_1.data,
            signature_1=form.signature_1.data,
            id_number_1=form.id_number_1.data,
        )
        db.session.add(new_entry)
        db.session.commit()

        flash('Form submitted successfully!', 'success')
        return redirect(url_for('views.cityAdmin'))

    return render_template('cityAdmin.html', form=form)



@views.route('/submit_remove_ownership', methods=['GET', 'POST'])
def submit_remove_ownership():
    form = RemoveOwnershipForm()
    if form.validate_on_submit():
        # Process form data here, e.g., save to the database
        flash('Remove Ownership form submitted successfully!', 'success')
        return redirect(url_for('views.cityAdmin'))
    return render_template('cityAdmin.html', remove_ownership_form=form)

@views.route('/submit_include_ownership', methods=['GET', 'POST'])
def submit_include_ownership():
    form = IncludeOwnershipForm()
    if form.validate_on_submit():
        # Process form data here, e.g., save to the database
        flash('Include Ownership form submitted successfully!', 'success')
        return redirect(url_for('views.cityAdmin'))
    return render_template('cityAdmin.html', include_ownership_form=form)

@views.route('/submit_transfer_allotment', methods=['GET', 'POST'])
def submit_transfer_allotment():
    form = TransferAllotmentForm()
    if form.validate_on_submit():
        # Process form data here, e.g., save to the database
        flash('Transfer Allotment form submitted successfully!', 'success')
        return redirect(url_for('views.cityAdmin'))
    return render_template('cityAdmin.html', transfer_allotment_form=form)

@views.route('/submit_food_handlers', methods=['POST'])
def submit_food_handlers():
    form = FoodHandlersForm()
    if form.validate_on_submit():
        # Save the form data to the database
        new_food_handler_entry = FoodHandler(
            date=form.date.data,
            name=form.name.data,
            sex=form.sex.data,
            home_address=form.home_address.data,
            date_of_birth=form.date_of_birth.data,
            identification_no=form.identification_no.data,
            telephone=form.telephone.data,
            business_name=form.business_name.data,
            business_type=form.business_type.data,
            business_address=form.business_address.data,
            family_history={
                'typhoid': form.family_typhoid.data,
                'tuberculosis': form.family_tuberculosis.data,
                'jaundice': form.family_jaundice.data,
                'chronic_cough': form.family_chronic_cough.data,
                'hospitalization': form.family_hospitalization.data,
                'other': form.family_other.data
            },
            personal_history={
                'typhoid': form.personal_typhoid.data,
                'tuberculosis': form.personal_tuberculosis.data,
                'jaundice': form.personal_jaundice.data,
                'chronic_cough': form.personal_chronic_cough.data,
                'hospitalization': form.personal_hospitalization.data,
                'asthmatic_attacks': form.personal_asthmatic_attacks.data,
                'allergies': form.personal_allergies.data,
                'other': form.personal_other.data
            },
            declaration=form.declaration.data,
            applicant_signature=form.applicant_signature.data,
            applicant_signature_date=form.applicant_signature_date.data
        )
        db.session.add(new_food_handler_entry)
        db.session.commit()
        flash('Food Handlers form submitted successfully!', 'success')
    else:
        flash('There was an error submitting the Food Handlers form.', 'danger')
    
    return redirect(url_for('views.publicHealth'))



@views.route('/submit_public_complaint', methods=['POST'])
def submit_public_complaint():
    form = PublicComplaintForm()
    if form.validate_on_submit():
        # Save the form data to the database
        new_complaint = PublicComplaint(
            date=form.date.data,
            premises=form.premises.data,
            nature_of_complaint=form.nature_of_complaint.data,
            complainant_name=form.complainant_name.data,
            contact_details=form.contact_details.data,
            action_taken=form.action_taken.data,
        )
        db.session.add(new_complaint)
        db.session.commit()
        flash('Public Complaint form submitted successfully!', 'success')
    else:
        flash('There was an error submitting the Public Complaint form.', 'danger')

    return redirect(url_for('views.publicHealth'))

@views.route('/submit_copy_search', methods=['POST'])
def submit_copy_search():
    """Handle the submission of the Copy/Search form."""
    form = CopySearchForm()
    if form.validate_on_submit():
        # Save the submitted form data to the database
        new_request = CopySearchRequest(
            address_of_development=form.address_of_development.data,
            date_of_approval=form.date_of_approval.data,
            registration_number=form.registration_number.data,
            name_of_owner=form.name_of_owner.data,
            address_of_owner=form.address_of_owner.data,
            date=form.date.data
        )
        db.session.add(new_request)
        db.session.commit()
        flash('Application for Copy/Search submitted successfully!', 'success')
        return redirect(url_for('views.city_engineers'))  # Redirect to the main City Engineers page

    # Log form errors to help debug
    print(form.errors)  # Add this to log errors to the console
    flash('There were errors in your form submission.', 'danger')
    return render_template('cityEngineering.html', form=form)


@views.route('/submit_blocking_footway', methods=['POST'])
def submit_blocking_footway():
    form = BlockingFootwayForm()
    if form.validate_on_submit():
        # Save the form data to the database
        new_request = BlockingFootwayRequest(
            location=form.location.data,
            period_days=form.period_days.data,
            period_weeks=form.period_weeks.data,
            period_months=form.period_months.data,
            from_date=form.from_date.data,
            to_date=form.to_date.data,
            length_of_footway=form.length_of_footway.data,
            existing_width=form.existing_width.data,
            width_to_obstruct=form.width_to_obstruct.data,
            reason_for_application=form.reason_for_application.data,
            applicant_name=form.applicant_name.data,
            applicant_address=form.applicant_address.data,
            owner_name=form.owner_name.data,
            owner_signature=form.owner_signature.data
        )
        db.session.add(new_request)
        db.session.commit()
        flash('Form submitted successfully!', 'success')
        return redirect(url_for('views.city_engineers'))  # Adjust as necessary

    flash('There were errors in your form submission.', 'danger')
    return render_template('cityEngineering.html', form=form)


@views.route('/submit_building_application', methods=['POST'])
def submit_building_application():
    form = BuildingApplicationForm()
    if form.validate_on_submit():
        new_application = BuildingApplication(
            work_type=form.work_type.data,
            premises_no=form.premises_no.data,
            north_dimension=form.north_dimension.data,
            south_dimension=form.south_dimension.data,
            east_dimension=form.east_dimension.data,
            west_dimension=form.west_dimension.data,
            nature_of_building=form.nature_of_building.data,
            building_length=form.building_length.data,
            building_width=form.building_width.data,
            building_height=form.building_height.data,
            owner_name=form.owner_name.data,
            owner_signature=form.owner_signature.data,
            contractor_name=form.contractor_name.data
        )
        db.session.add(new_application)
        db.session.commit()
        flash('Building Application submitted successfully!', 'success')
    else:
        print(form.errors)  # Add this to log errors to the console
        flash('There was an error in the Building Application form.', 'danger')
    return redirect(url_for('views.city_engineers'))