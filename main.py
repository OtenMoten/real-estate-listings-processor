# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de

from RealEstateListingsProcessor import RealEstateListingsProcessor


def main():
    """
    The main function: Where the magic happens! 🎩✨

    This is like the command center for our real estate analysis mission.
    We're going to crunch numbers, generate charts, and create reports
    faster than you can say "location, location, location!" 📊
    """
    print("Welcome to the Real Estate Market Analyzer! 🏘️🔍")
    print("Fasten your seatbelts, we're about to dive into a sea of property data! 🏊‍♂️💼")

    # Create our trusty RealEstateListingsProcessor, it's like summoning a data wizard! 🧙‍♂️
    app = RealEstateListingsProcessor()

    try:
        # Step 1: Load the data (it's like filling our cauldron with real estate potion ingredients)
        print("Loading data from the 'input' folder... 📂")
        app.load_data('input')

        # Step 2: Process the data (time to wave our wand and cast some analysis spells!)
        print("Processing data... 🧮")
        app.process_data()

        # Step 3: Create visualizations (painting pretty pictures with cold, hard data)
        print("Generating visualizations... 🎨📊")
        app.generate_visualizations()

        # Step 4: Generate the report (the grand finale, our magnum opus!)
        print("Creating the final report... 📝✨")
        app.generate_report()

        print("\nAnalysis complete! Your report is ready. Time to impress your boss! 🎉👔")
        print("Check out 'real-estate-report.md' for the full scoop on the real estate market!")

    except Exception as e:
        # Uh-oh, looks like our crystal ball encountered an error
        print(f"Oops! We've hit a snag in our analysis: {str(e)} 😱")
        print("Don't worry, even real estate moguls have off days. Let's try again! 💪")


if __name__ == "__main__":
    main()
