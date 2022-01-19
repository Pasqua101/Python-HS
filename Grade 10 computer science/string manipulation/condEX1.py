price = input("What was the price of your meal? ")
pst = 1.08
gst = 1.05

if price > 4:
    print price * pst * gst, "is the total price"
elif price < 4:
    print price * gst, "is the total price"

