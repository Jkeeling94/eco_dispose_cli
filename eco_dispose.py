SUPPORTED_DEVICES = [
    "Mobile Phone",
    "Laptop",
    "Tablet",
    "Desktop Computer",
    "Monitor",
    "Television",
    "Printer",
    "Router",
    "Games Console",
    "Camera",
]


def welcome():
    print("\nWelcome to EcoDispose by GreenTech Solutions!\n")
    print("""This program helps you responsibly recycle and dispose of your electronic equipment.
You will be asked a series of simple questions about your device.
Based on your responses, we provide tailored disposal guidance.
All guidance is designed to support WEEE-compliant disposal decisions.\n
Let's get started!""")


def privacy_policy():
    print("\nPrivacy Policy - EcoDispose")
    print("""\nWe take your privacy seriously.\n
This program does not store personal data permanently.
Any information gathered is used only to provide recycling guidance.
In accordance with GDPR, we do not share your data with third parties.
This system is designed to minimise data collection and avoid storing personal information.\n
By continuing, you agree to use this service responsibly.""")

    accepted = get_yes_no_input("\nDo you accept the Privacy Policy? (yes/no)\nAnswer: ")

    if accepted:
        print("\nYou chose: Yes\nThank you. Continuing...\n")
        return

    print("""\nYou chose: No. To continue with this service you must accept the Privacy Policy.
This service will now close. Goodbye.""")
    raise SystemExit


def get_yes_no_input(prompt):
    while True:
        choice = input(prompt).strip().lower()

        if choice in ("yes", "y"):
            return True

        if choice in ("no", "n"):
            return False

        print("Invalid input. Please enter yes or no.")


def get_non_empty_input(prompt):
    while True:
        answer = input(prompt).strip()

        if answer:
            return answer

        print("This field cannot be blank. Please try again.")


def show_name_easter_egg(name):
    if name.lower() == "frank zappa":
        print("\nFrank Zappa detected. Proceeding with a Valley Girl.\n")
        return

    if name.lower() == "arnie":
        print("\nArnie detected. We're coming with you as we want to live.\n")


def show_weee_links():
    print("""\nUseful WEEE Links
WEEE Regulations (GOV.UK):
https://www.gov.uk/guidance/regulations-waste-electrical-and-electronic-equipment

What WEEE Means (GOV.UK):
https://www.gov.uk/guidance/when-electrical-and-electronic-equipment-eee-becomes-waste-weee
""")


def customer_type():
    print("""Customer Type Selection

To provide accurate recycling guidance, we first need to determine your user type.

Enter:
- Domestic
- Commercial
""")

    while True:
        customer = input("Enter user type (Domestic/Commercial): ").strip().lower()

        if customer == "domestic":
            print("\nDomestic user selected.\n")
            return "domestic"

        if customer == "commercial":
            print("\nCommercial user selected.\n")
            return "commercial"

        print("Invalid input. Please enter 'Domestic' or 'Commercial'.")


def collect_domestic_info():
    print("Domestic Information")
    name = get_non_empty_input("Enter your name: ")
    show_name_easter_egg(name)
    town_city = get_non_empty_input("Enter your town or city: ")

    print("\nThank you. Your domestic details have been noted for this session only.\n")
    return {
        "name": name,
        "town_city": town_city,
    }


def collect_commercial_info():
    print("Commercial Information")
    business_name = get_non_empty_input("Enter your business name: ")
    contact_name = get_non_empty_input("Enter a contact name: ")
    show_name_easter_egg(contact_name)
    town_city = get_non_empty_input("Enter the business town or city: ")

    print("\nThank you. Your commercial details have been noted for this session only.\n")
    return {
        "business_name": business_name,
        "contact_name": contact_name,
        "town_city": town_city,
    }


def get_valid_device_type():
    print("Device Type")
    print("Supported Device Types:")

    for device_name in SUPPORTED_DEVICES:
        print(f"- {device_name}")

    while True:
        device_input = input("\nEnter the device type: ").strip().lower()

        for device_name in SUPPORTED_DEVICES:
            if device_input == device_name.lower():
                print(f"\nDevice recognised: {device_name}\n")
                return device_name

        print("That device type is not recognised. Please choose a supported electronic device.")


def ensure_data_removed(device_name):
    print("Data Removal Check")
    data_removed = get_yes_no_input(
        f"Has all personal or company data been removed from the {device_name}? (yes/no)\nAnswer: "
    )

    while not data_removed:
        print(f"""\nBefore disposal, ensure the {device_name} has been fully cleared.
- Sign out of any accounts
- Remove memory cards or SIM cards
- Factory reset the device where possible
- Delete stored files and saved passwords\n""")

        data_removed = get_yes_no_input("Have you now removed all data? (yes/no)\nAnswer: ")

    print("\nData Removal Confirmed.\n")


def get_device_condition():
    print("Condition Check")

    while True:
        condition = input("Is the device working or broken? ").strip().lower()

        if condition in ("working", "broken"):
            print(f"\nCondition recorded: {condition}\n")
            return condition

        print("Invalid input. Please enter 'working' or 'broken'.")


def get_council_area():
    print("""Council Recycling Website

Choose a Council Area to View Official Recycling Centre Information:
- Nottinghamshire
- Chesterfield
- Leicestershire
- Sheffield
""")

    while True:
        area = input("Enter Council Area: ").strip().lower()

        if area in (
            "nottinghamshire",
            "chesterfield",
            "leicestershire",
            "sheffield",
        ):
            return area

        print("Invalid input. Please choose one of the listed council areas.")


def show_council_website(area):
    if area == "nottinghamshire":
        print("""\nOfficial Nottinghamshire Recycling Centres Page:
https://www.nottinghamshire.gov.uk/waste-and-recycling/recycling-centres/details

Use the Council website to choose a Recycling Centre yourself.""")
        return

    if area == "chesterfield":
        print("""\nOfficial Derbyshire Recycling Centres Page for the Chesterfield Area:
https://www.derbyshire.gov.uk/environment/rubbish-waste/recyling-centres/centre-locations/recycling-centre-locations.aspx

Use the Council website to choose a Recycling Centre yourself.""")
        return

    if area == "leicestershire":
        print("""\nOfficial Leicestershire Recycling and Household Waste Sites Page:
https://www.leicestershire.gov.uk/environment-and-planning/waste-and-recycling/find-a-recycling-and-household-waste-site

Use the Council website to choose a Recycling Centre yourself.""")
        return

    if area == "sheffield":
        print("""\nOfficial Sheffield Household Waste Recycling Centres Page:
https://www.sheffield.gov.uk/bins-recycling-services/local-recycling-sites

Use the Council website to choose a Recycling Centre yourself.""")
        return


def show_disposal_options(town_city):
    print(f"""Choose one of these four disposal options in {town_city}:
1. Local Council Household Waste Recycling Centre
2. Large Electrical Retailer Take-Back Service
3. Manufacturer Return or Take-Back Scheme
4. Licensed WEEE Collection Provider""")

    while True:
        choice = input("Select disposal option (1-4): ").strip()

        if choice == "1":
            area = get_council_area()
            show_council_website(area)
            return

        if choice == "2":
            print("\nCheck whether a large retailer near you offers in-store take-back for old electronics.")
            return

        if choice == "3":
            print("\nVisit the manufacturer's website to see whether a return or recycling scheme is available.")
            return

        if choice == "4":
            print("\nArrange collection only with a licensed WEEE recycling provider.")
            return

        print("Invalid input. Please choose a number from 1 to 4.")


def handle_working_device(device_name, town_city):
    print(
        f"It looks like your {device_name} still works. "
        f"We suggest that you consider reuse before disposal, "
        f"however we understand if you choose not to."
    )

    while True:
        next_step = input("Would you like guidance for Resale, Donation or Recycling? ").strip().lower()

        if next_step == "resale":
            print(f"""\nResale Guidance
- Clean the {device_name} and check that it powers on correctly
- Include chargers or accessories if available
- Record the serial number for your own records
- Use a trusted resale platform in {town_city}\n
Your device may be suitable for resale.""")
            return "resale"

        if next_step == "donation":
            print(f"""\nDonation Options in {town_city}
1. Local Charity Shops that accept Electrical Items
2. Community Reuse Centres
3. Schools or Training Groups accepting donated equipment
4. Registered Online Donation Platforms\n
Check with the organisation first to confirm they accept a working {device_name}.""")
            return "donation"

        if next_step == "recycling":
            print(f"\nYou can still recycle your {device_name} if you do not want to choose Resale or Donation.")
            show_disposal_options(town_city)
            return "recycling"

        print("Invalid input. Please enter 'resale', 'donation' or 'recycling'.")


def handle_broken_device(device_name, town_city):
    print(f"""\nThe {device_name} is broken, so it should be sent through a WEEE-compliant disposal route.

""")
    show_disposal_options(town_city)


def thank_you(display_name):
    if display_name.lower() == "frank zappa":
        print(f"\nThank you for using EcoDispose, {display_name}.")
        print("Please continue to Sheik Yerbouti.")
        print("We hope you'll be back.")
        return

    if display_name.lower() == "arnie":
        print(f"\nThank you for using EcoDispose, {display_name}. Goodbye.")
        print("We'll be back.")
        return

    print("\nThank you for using EcoDispose. Goodbye.")
    print("We hope you'll be back.")


def main():
    welcome()
    privacy_policy()
    user_type = customer_type()

    if user_type == "domestic":
        customer_details = collect_domestic_info()
        display_name = customer_details["name"]
    else:
        customer_details = collect_commercial_info()
        display_name = customer_details["business_name"]

    device_name = get_valid_device_type()
    ensure_data_removed(device_name)
    condition = get_device_condition()

    if condition == "working":
        handle_working_device(device_name, customer_details["town_city"])
    else:
        handle_broken_device(device_name, customer_details["town_city"])

    show_weee_links()
    thank_you(display_name)


if __name__ == "__main__":
    main()
