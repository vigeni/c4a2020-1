def handleError(message):
    print(message)
    prompt()


def extractNumber(phone):
    countryCode = phone[0:3]
    gsmCode = phone[3:5]
    phoneNumber = phone[5:12]
    print("You entered: " + phone + "\n")
    print("The country code: " + countryCode + "\n")
    print("The GSM code: " + gsmCode + "\n")
    print("The number: " + phoneNumber + "\n")
    print('Phone number is: \n ( {countryCode} ) {gsmCode} - {phoneNumber}'.format(countryCode=countryCode,
                                                                                   gsmCode=gsmCode,
                                                                                   phoneNumber=phoneNumber))


def prompt():
    phone = input("Please input your number, including the country code, without leading zeros. Enter 0 to exit. \n")
    if phone == "0":
        print("Bye!")
        exit()
    if not phone.isnumeric():
        return handleError("Phone number is invalid")
    if not len(phone) == 12:
        return handleError("Phone number is invalid")
    return extractNumber(phone)


prompt()
