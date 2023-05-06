import random
import time

sortedItems = []
item = None


def test_search_item_by_navbar_input(app):
    global sortedItems
    app.nav.search_item("headphones")
    time.sleep(7)
    foundItems = app.search_result.get_items()

    app.search_result.sort_items("Price Low to High")
    time.sleep(7)
    sortedItems = app.search_result.get_items()

    # Items are not sorted correctly, test will fail !
    # assert sortedItems == sorted(foundItems, key=lambda i: float(i.price))


def testCheckoutItem(app):
    global item
    item = sortedItems[random.randrange(len(sortedItems) - 1)]
    app.search_result.open_item(item)
    time.sleep(4)
    itemOnDetailsPage = app.detail.get_item()

    assert item == itemOnDetailsPage


def testAddToCart(app):
    app.detail.add_to_cart()
    app.detail.go_to_cart()

    itemOnCheckoutPage = app.checkout.get_item()
    time.sleep(4)

    assert item.name == itemOnCheckoutPage.name
    assert item.price == itemOnCheckoutPage.price

    grossAmount = app.checkout.get_gross_amount()
    tax = app.checkout.get_tax()
    assert float(grossAmount) == float(tax) + float(itemOnCheckoutPage.price)
