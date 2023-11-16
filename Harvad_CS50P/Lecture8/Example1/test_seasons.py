from seasons import check_date
from datetime import date


def test_is_date_valid():
    assert check_date('1999', '09', '18') == 'twelve million, seven hundred and eight thousand'
