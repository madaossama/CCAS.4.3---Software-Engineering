import unittest

# ====== GIVEN CODE (System Under Test) ======
class Order:
    def __init__(self, table_number):
        self.table_number = table_number
        self.order_items = []

    def add_item(self, item_name, quantity):
        if quantity <= 0:
            return "Quantity must be greater than zero."
        self.order_items.append({'item': item_name, 'quantity': quantity})
        return f"{quantity} x {item_name} added to order for Table {self.table_number}."

    def view_order(self):
        if not self.order_items:
            return f"No items ordered for Table {self.table_number}."
        return "\n".join([f"{item['quantity']} x {item['item']}" for item in self.order_items])

    def calculate_total(self, menu_prices):
        total = 0
        for item in self.order_items:
            total += menu_prices.get(item['item'], 0) * item['quantity']
        return f"Total bill for Table {self.table_number}: ${total}"

# ====== TEST CASES ======
class TestOrder(unittest.TestCase):

    def setUp(self):
        self.order = Order(1)
        self.menu_prices = {"Pizza": 12, "Pasta": 10}

    def test_add_item_valid_quantity(self):
        result = self.order.add_item("Pizza", 2)
        self.assertEqual(result, "2 x Pizza added to order for Table 1.")

    def test_add_item_invalid_quantity(self):
        result = self.order.add_item("Pizza", 0)
        self.assertEqual(result, "Quantity must be greater than zero.")

    def test_view_order_no_items(self):
        result = self.order.view_order()
        self.assertEqual(result, "No items ordered for Table 1.")

    def test_calculate_total_item_not_in_menu(self):
        self.order.add_item("Burger", 2)
        result = self.order.calculate_total(self.menu_prices)
        self.assertEqual(result, "Total bill for Table 1: $0")

if __name__ == "__main__":
    unittest.main()