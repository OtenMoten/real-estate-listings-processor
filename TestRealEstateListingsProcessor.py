# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de

import unittest
import pandas as pd
from pathlib import Path

from RealEstateListingsProcessor import RealEstateListingsProcessor


class TestRealEstateListingsProcessor(unittest.TestCase):
    """
    Test suite for RealEstateListingsProcessor 🏠🧪

    We're putting our property analysis tool through its paces!
    No stone left unturned, no property left unanalyzed. 🕵️‍♂️📊
    """

    def setUp(self):
        """
        Set up our testing playground 🎢

        We're creating a fresh RealEstateListingsProcessor and a cozy
        little folder for our test data. It's like setting up a miniature
        real estate office, but with more code and less coffee. ☕️💻
        """
        self.app = RealEstateListingsProcessor()
        self.test_data_folder = Path('test_real_estate_data')
        self.test_data_folder.mkdir(exist_ok=True)

    def tearDown(self):
        """
        Clean up after our tests 🧹

        We're responsible property managers here. After the test party,
        we clean up our fake files and tidy away our test folder.
        Leave no trace! 🌿
        """
        for file in self.test_data_folder.glob("*.xlsx"):
            file.unlink()
        self.test_data_folder.rmdir()

    def create_test_excel(self, filename, data):
        """
        Create a test Excel file 📑

        This is our little Excel factory. Feed it data, and it spits out
        a shiny new Excel file. It's like SimCity, but for spreadsheets! 🏙️
        """
        df = pd.DataFrame(data)
        df.to_excel(self.test_data_folder / filename, index=False)

    def test_load_data(self):
        """
        Test the data loading process 📥📊

        We're making sure our app can handle multiple Excel files and
        combine them correctly. It's like watching a master chef prepare
        ingredients for a data soup! 🍲
        """
        self.create_test_excel('test1.xlsx', {'Price': [100000, 200000], 'SquareMeters': [50, 100], 'Location': ['A', 'B']})
        self.create_test_excel('test2.xlsx', {'Price': [150000, 250000], 'SquareMeters': [75, 125], 'Location': ['C', 'D']})

        self.app.load_data(str(self.test_data_folder))
        self.assertEqual(len(self.app.data), 4, "Oops! We're missing some properties. Did they get lost in the move? 🏠🚚")
        self.assertTrue(all(col in self.app.data.columns for col in ['Price', 'SquareMeters', 'Location']),
                        "Houston, we have a problem. Some columns are MIA! 🕵️‍♂️")

    def test_process_data(self):
        """
        Test the data processing functionality 🧮

        Time to crunch those numbers! We're making sure our app can calculate
        averages, count properties, and do all sorts of mathematical wizardry.
        It's like Hogwarts, but for real estate! 🧙‍♂️🏠
        """
        self.app.data = pd.DataFrame({
            'Price': [100000, 200000, 150000],
            'SquareMeters': [50, 100, 75],
            'Location': ['A', 'B', 'C']
        })
        self.app.process_data()
        self.assertEqual(self.app.report['number_of_properties'], 3, "Lost count of our properties? Time to recalibrate our abacus! 🧮")
        self.assertEqual(self.app.report['average_price'], 150000, "Average price seems off. Did we accidentally include that castle in our calculations? 🏰")
        self.assertAlmostEqual(self.app.report['average_price_per_sqm'], 2000, places=2,
                               msg="Price per square meter calculation went rogue. Time to dust off the old calculator! 🖩")

    def test_generate_visualizations(self):
        """
        Test the visualization generation 📊🎨

        We're making sure our app can paint pretty pictures with data.
        It's like a Bob Ross painting, but with more bar charts and less
        happy little trees. 🌳📈
        """
        self.app.data = pd.DataFrame({
            'Price': [100000, 200000, 150000],
            'SquareMeters': [50, 100, 75],
            'Location': ['A', 'B', 'C']
        })
        self.app.data['PricePerSqm'] = self.app.data['Price'] / self.app.data['SquareMeters']
        self.app.generate_visualizations()
        self.assertTrue(Path('price_vs_sqm.png').exists(), "Looks like our price vs size chart took an unscheduled vacation. Time to call it back! 🏖️📊")
        self.assertTrue(Path('price_per_sqm_distribution.png').exists(), "Our price distribution chart seems to be playing hide and seek. Olly olly oxen free! 🙈📉")

    def test_generate_report(self):
        """
        Test the report generation 📝✨

        The grand finale! We're making sure our app can write a bestseller
        about real estate trends. Move over, Tolstoy! 📚🏠
        """
        self.app.data = pd.DataFrame({
            'Price': [100000, 200000, 150000],
            'SquareMeters': [50, 100, 75],
            'Location': ['A', 'B', 'C']
        })
        self.app.process_data()
        self.app.generate_report()
        self.assertTrue(Path('real-estate-report.md').exists(), "Our report seems to have writer's block. Time for some creative inspiration! ✍️💡")

    def test_most_expensive_property(self):
        """
        Test identification of the most expensive property 💎

        We're making sure our app can spot the crown jewel in our property collection.
        It's like finding the shiniest diamond in a very expensive rough! 💍
        """
        self.app.data = pd.DataFrame({
            'Price': [100000, 500000, 200000],
            'SquareMeters': [50, 200, 100],
            'Location': ['A', 'B', 'C']
        })
        self.app.process_data()
        self.assertEqual(self.app.report['most_expensive_property']['Price'], 500000, "Our luxury detector seems to be malfunctioning. Did we forget to calibrate it with gold? 🥇")

    def test_cheapest_property(self):
        """
        Test identification of the cheapest property 🏚️

        We're ensuring our app can find the best deal in town.
        It's like being a bargain-hunting ninja in the real estate world! 🥷
        """
        self.app.data = pd.DataFrame({
            'Price': [100000, 500000, 50000],
            'SquareMeters': [50, 200, 25],
            'Location': ['A', 'B', 'C']
        })
        self.app.process_data()
        self.assertEqual(self.app.report['cheapest_property']['Price'], 50000, "Our bargain basement finder seems to be stuck in the penthouse. Time to take the elevator down! 🛗")

    def test_price_range(self):
        """
        Test calculation of the price range 📏💰

        We're checking if our app can measure the grand canyon of property prices.
        It's like calculating the distance between a cardboard box and Buckingham Palace! 🏰📦
        """
        self.app.data = pd.DataFrame({
            'Price': [100000, 500000, 50000],
            'SquareMeters': [50, 200, 25],
            'Location': ['A', 'B', 'C']
        })
        self.app.process_data()
        expected_range = 500000 - 50000
        self.assertEqual(self.app.report['price_range'], expected_range, "Our price range calculator seems to be using a rubber ruler. Time to switch to a metal one! 📏")


if __name__ == '__main__':
    unittest.main()
