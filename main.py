from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(input("Which currency will you use? (Type All CAPS)"))
        bot.select_place_to_go(input("Where do you want to go? (City & Country)"))
        bot.select_dates(check_in_date=input("What is the check in date? (Year-Month-Day)"),
                         check_out_date=input("What is the check out date? (Year-Month-Day)"))
        bot.select_adults(int(input("How many people?")))
        bot.click_search()
        bot.apply_filter()
        bot.refresh()
        bot.report_results()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
