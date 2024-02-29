from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_hai(median_family_income, median_home_price, mortgage_interest_rate, down_payment_percent, max_monthly_payment_percent):
    # Calculate the qualifying income
    down_payment = median_home_price * down_payment_percent
    loan_amount = median_home_price - down_payment
    monthly_interest_rate = mortgage_interest_rate / 12 / 100
    num_payments = 30 * 12  # 30-year mortgage
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

    # Calculate HAI
    qualifying_income = monthly_payment / (max_monthly_payment_percent / 100)
    hai = (median_family_income / qualifying_income) * 100

    return {'hai': hai, 'qualifying_income': qualifying_income}

@app.route('/', methods=['GET', 'POST'])
def index():
    hai_result = None
    income_comparison = None
    hai_comparison = None

    if request.method == 'POST':
        median_family_income = float(request.form['median_family_income'])
        median_home_price = float(request.form['median_home_price'])
        mortgage_interest_rate = float(request.form['mortgage_interest_rate'])
        down_payment_percent = float(request.form['down_payment_percent'])
        max_monthly_payment_percent = float(request.form['max_monthly_payment_percent'])

        hai_result = calculate_hai(median_family_income, median_home_price, mortgage_interest_rate, down_payment_percent, max_monthly_payment_percent)

        # Add logic for income comparison and HAI comparison
        income_comparison = {
            'median_family_income': median_family_income,
            'qualifying_income': hai_result['qualifying_income']
        }

        hai_comparison = {
            'hai': hai_result['hai'],
            'requirement_met': hai_result['hai'] >= 100
        }

    return render_template('calculator.html', hai_result=hai_result, income_comparison=income_comparison, hai_comparison=hai_comparison)

if __name__ == '__main__':
    app.run(debug=True)

