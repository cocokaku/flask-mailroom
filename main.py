import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session
from model import Donor, Donation 

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('all'))


@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)
    

@app.route('/create_donation/', methods=['GET', 'POST'])
def create_donation():
	if request.method == 'POST':
		donor = Donor.get_or_none(name=request.form['name'])
		if donor:
			Donation(donor=donor, value=request.form['value']).save()
			return redirect(url_for('all'))
		else:
			return render_template('create_donation.jinja2', error="Error: Donor does not exist")
	else:
		return render_template('create_donation.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

