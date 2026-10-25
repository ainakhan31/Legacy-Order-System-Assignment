import pytest

from order_processing import order_total, print_receipt


def test_student_discount_standard_delivery():
    """Subtotal: 1400. Student discount: 140. Delivery: 100. Total: 1360."""
    sample = [
        {'name': 'Notebook', 'category': 'book', 'price': 300, 'qty': 2},
        {'name': 'USB Drive', 'category': 'electronics', 'price': 800, 'qty': 1},
    ]

    assert order_total(sample, 'student', 'standard') == 1360.00


def test_regular_customer_no_delivery():
    """Subtotal: 600. No discount or delivery fee. Total: 600."""
    sample = [
        {'name': 'Notebook', 'category': 'book', 'price': 300, 'qty': 2}
    ]

    assert order_total(sample, 'regular', 'none') == 600.00


def test_staff_discount_express_delivery():
    """Subtotal: 800. Staff discount: 40. Express delivery: 250. Total: 1010."""
    sample = [
        {'name': 'USB Drive', 'category': 'electronics', 'price': 800, 'qty': 1}
    ]

    assert order_total(sample, 'staff', 'express') == 1010.00


def test_invalid_negative_price_raises_value_error():
    """Negative price must raise ValueError."""
    sample = [
        {'name': 'Corrupted Item', 'category': 'book', 'price': -100, 'qty': 1}
    ]

    with pytest.raises(ValueError, match="Item price cannot be negative"):
        order_total(sample, 'regular', 'standard')


def test_invalid_negative_quantity_raises_value_error():
    """Negative quantity must raise ValueError."""
    sample = [
        {'name': 'Notebook', 'category': 'book', 'price': 300, 'qty': -2}
    ]

    with pytest.raises(ValueError, match="Item quantity cannot be negative"):
        order_total(sample, 'regular', 'standard')


def test_receipt_formatting():
    """Validate the receipt structure and content."""
    sample = [
        {'name': 'Notebook', 'category': 'book', 'price': 300, 'qty': 2}
    ]

    receipt = print_receipt(sample, 'student', 'standard')

    assert 'ORDER RECEIPT' in receipt
    assert '2 x Notebook = 600' in receipt
    assert 'Total: 640.0' in receipt