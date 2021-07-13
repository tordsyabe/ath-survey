from flask import Blueprint, render_template, request, redirect
from flask.helpers import url_for
from athsurveyapp.models.models import Branch, db
from athsurveyapp.blueprints.branch.forms import BranchForm

branch_page = Blueprint('branch_page', __name__, template_folder='templates')


@branch_page.route('/', methods=['GET'])
def branch_index():

    branches = Branch.query.all()
    print(branches)

    return render_template('branches.html', branches=branches)


@branch_page.route('/create', methods=['GET', 'POST'])
def create_branch():

    form = BranchForm()
    if request.method == 'POST' and form.validate_on_submit():
        branch_name = form.name.data
        branch_address = form.address.data

        new_branch = Branch(branch_name, branch_address)
        db.session.add(new_branch)
        db.session.commit()

        return redirect(url_for('branch_page.branch_index'))

    return render_template('create_branch.html', form=form)
