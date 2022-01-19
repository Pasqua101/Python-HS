rates = raw_input("Where are you sending your letter to? ex. Canada, U.S.A or Internationally")
place = raw_input("Where in that place do you want your letter to be sent to?")


if rates == "Canada":
    print "The price of your letter will be $0.52"
elif rates == "U.S.A":
    print "The price of your letter will be $0.93"
elif rates == "Internationally":
    print "The price of your letter will be $1.55"