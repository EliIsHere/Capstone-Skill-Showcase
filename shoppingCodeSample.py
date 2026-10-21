#sample code for the purpose of showcasing github skills
TAX_RATE = 0.1
GREETING = "Thanks for shopping at Insert Shop Name!"
 
 
def calculate_total(prices):
    subtotal = sum(prices)
    return subtotal * (1 + TAX_RATE)
 
 
def main():
    print(GREETING)
    items = [10.00, 5.50, 240.10, 9.2]

    for price in items:
        print(f"Item: ${price:.2f}")

    print(f"Tax Rate: {TAX_RATE * 100:.1f}%")
    print(f"Total: ${calculate_total(items):.2f}")
 
 
if __name__ == "__main__":
    main()
