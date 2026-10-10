from rental import rental_fee

def test_fee_is_days_times_rate():
    assert rental_fee(days=3, daily_rate=50) == 150