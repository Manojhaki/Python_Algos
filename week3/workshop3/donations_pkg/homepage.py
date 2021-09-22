def show_homepage():
    print("")
    print("          === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register         |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donation    |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("|            5.    Exit                    |")
    print("------------------------------------------")


def donate(username):
    donation_amtFloat = float(input("Enter amount to donate: "))
    donation_amt = str(donation_amtFloat)
    donation = username + " donated " + "$"+donation_amt
    print("Thank you for your generosity")
    return donation


def show_donations(donations):
    print("\n--- All Donations ---")
    if not donations:
        print("Currently, there are no donations.")
    else:
        for x in donations:
            print(x)
