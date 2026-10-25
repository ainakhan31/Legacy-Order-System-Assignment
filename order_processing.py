"""Order processing system.
All prices and delivery charges are in PKR.
"""

# Named constants
STUDENT_DISCOUNT = 0.10
STAFF_DISCOUNT = 0.05
EXPRESS_DELIVERY_FEE = 250
STANDARD_DELIVERY_FEE = 100

def calculate_subtotal(items):
    """Calculate subtotal and validate prices and quantities."""
    subtotal = 0

    for item in items:
        if item['price'] < 0:
            raise ValueError("Item price cannot be negative")

        if item['qty'] < 0:
            raise ValueError("Item quantity cannot be negative")

        subtotal += item['price'] * item['qty']

    return subtotal

def calculate_discount(subtotal, customer_type):
    """Calculate the discount amount for the given customer type."""
    if customer_type == 'student':
        return subtotal * STUDENT_DISCOUNT
    elif customer_type == 'staff':
        return subtotal * STAFF_DISCOUNT

    return 0



def calculate_delivery_fee(delivery):
    """Return the delivery charge for the selected delivery method."""
    if delivery == 'express':
        return EXPRESS_DELIVERY_FEE
    elif delivery == 'standard':
        return STANDARD_DELIVERY_FEE

    return 0


def order_total(items, customer_type, delivery):
    """Calculate and return the final order total."""
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal, customer_type)
    delivery_fee = calculate_delivery_fee(delivery)

    total = subtotal - discount + delivery_fee

    return round(total, 2)

def print_receipt(items, customer_type, delivery):
    """Create and return a formatted receipt for the order."""
    amount = order_total(items, customer_type, delivery)

    result = 'ORDER RECEIPT\n'

    for item in items:
        line_total = item['price'] * item['qty']
        result += (
            f"{item['qty']} x {item['name']} = "
            f"{line_total}\n"
        )

    result += f'Customer: {customer_type}\n'
    result += f'Delivery: {delivery}\n'
    result += f'Total: {amount:.2f}'

    return result



if __name__ == '__main__':
    sample = [
        {'name': 'Notebook', 'category': 'book',
         'price': 300, 'qty': 2},
        {'name': 'USB Drive', 'category': 'electronics',
         'price': 800, 'qty': 1},
    ]

    print(print_receipt(sample, 'student', 'standard'))
