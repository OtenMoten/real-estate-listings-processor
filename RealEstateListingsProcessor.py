# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime


class RealEstateListingsProcessor:
    """
    RealEstateListingsProcessor: Your Friendly Neighborhood Market Analyzer 🏘️📊

    This class is designed to process and analyze real estate listings data.
    It's like having a personal real estate expert in your pocket, minus the
    expensive suit and cheesy smile. 😉

    Key Features:
    - Data loading and cleaning (because let's face it, raw data is messy 🧹)
    - Statistical analysis (numbers that actually mean something! 🤓)
    - Visualization generation (pretty pictures for your reports 📈)
    - Report creation (impress your boss with markdown magic ✨)
    """

    def __init__(self):
        """
        Initialize the RealEstateListingsProcessor

        Sets up two main attributes:
        - self.data: Where all our lovely data will live 📦
        - self.report: A dictionary to store our insightful findings 🔍
        """
        self.data = None  # Our data playground
        self.report = {}  # Where the magic insights happen

    def load_data(self, folder_path):
        """
        Load and Clean the Real Estate Data

        Parameters:
        - folder_path: Path to the folder containing our Excel files 📁

        This method does the dirty work:
        1. Finds all Excel files in the specified folder
        2. Loads them into a single DataFrame
        3. Cleans up the mess (hello, NaN values 👋)

        Raises:
        - ValueError: If no Excel files are found (sad pandas 🐼)
        """
        all_files = list(Path(folder_path).glob("*.xlsx"))
        if not all_files:
            raise ValueError(f"No Excel files found in '{folder_path}'. Did you forget to save? 🤔")

        df_list = [pd.read_excel(file) for file in all_files]
        self.data = pd.concat(df_list, ignore_index=True)

        # Clean up our data - no room for NaNs in this house! 🧽
        self.data['Price'] = pd.to_numeric(self.data['Price'], errors='coerce')
        self.data['SquareMeters'] = pd.to_numeric(self.data['SquareMeters'], errors='coerce')
        self.data.dropna(subset=['Price', 'SquareMeters'], inplace=True)

    def process_data(self):
        """
        Process the Data and Extract Key Insights

        This is where we put on our data scientist hat 🎩
        and crunch those numbers:

        - Calculate price per square meter (for those fancy price/m² conversations)
        - Compute average prices (how much does a dream home cost these days?)
        - Find the most expensive and cheapest properties (for when you win the lottery 🎉 or need a fixer-upper 🔨)
        - Calculate median prices and price ranges (statistically sound and impressive in reports)
        """
        # Price per square meter - the real estate equivalent of 'price per pound' 😄
        self.data['PricePerSqm'] = self.data['Price'] / self.data['SquareMeters']

        self.report['average_price'] = self.data['Price'].mean()
        self.report['average_price_per_sqm'] = self.data['PricePerSqm'].mean()
        self.report['number_of_properties'] = len(self.data)
        self.report['most_expensive_property'] = self.data.loc[self.data['Price'].idxmax()]
        self.report['cheapest_property'] = self.data.loc[self.data['Price'].idxmin()]
        self.report['median_price'] = self.data['Price'].median()
        self.report['price_range'] = self.data['Price'].max() - self.data['Price'].min()

    def generate_visualizations(self):
        """
        Create Eye-Catching Visualizations

        Because sometimes, a picture is worth a thousand spreadsheet cells.
        We'll create two key plots:
        1. A scatter plot of price vs. square meters (aka the "dream home finder")
        2. A histogram of price per square meter (or "how much bang for your buck")

        Warning: May cause sudden urges to buy or sell property
        """
        # The "dream home finder" plot
        plt.figure(figsize=(10, 6))
        plt.scatter(self.data['SquareMeters'], self.data['Price'])
        plt.title('Price vs. Size: The Dream Home Finder')
        plt.xlabel('Size (m²) - From Cozy to Palatial')
        plt.ylabel('Price (€) - From Piggy Bank to Bank Vault')
        plt.savefig('price_vs_sqm.png')
        plt.close()

        # The "bang for your buck" plot
        plt.figure(figsize=(10, 6))
        self.data['PricePerSqm'].hist(bins=20)
        plt.title('Price per m²: How Much Bang for Your Buck?')
        plt.xlabel('Price per m² (€) - The True Cost of Your Dance Space')
        plt.ylabel('Frequency - Popular Price Points')
        plt.savefig('price_per_sqm_distribution.png')
        plt.close()

    def generate_report(self):
        """
        Generate the Final Report 📝✨

        Compile all our hard-earned insights into a markdown report.
        This method will:
        - Summarize key market statistics
        - Highlight the creme de la creme and the bargain bin of properties
        - Include our dazzling visualizations

        The result? A report so good, it might be mistaken for actual market expertise! 🕵️‍♂️📈
        """
        report_md = f"""
        # Real Estate Market Analysis Report 🏘️📊
        Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

        ## Market Overview 🌆
        - Total properties analyzed: {self.report['number_of_properties']} 🏠
        - Average property price: {self.report['average_price']:,.2f} € 💰
        - Average price per m²: {self.report['average_price_per_sqm']:,.2f} €/m² 📏
        - Median property price: {self.report['median_price']:,.2f} € (perfectly balanced, as all things should be)
        - Price range: {self.report['price_range']:,.2f} € (from "first home" to "lottery win")

        ## Property Extremes 🎢
        ### Most Expensive Property 🏰💎
        - Price: {self.report['most_expensive_property']['Price']:,.2f} €
        - Size: {self.report['most_expensive_property']['SquareMeters']:,.2f} m²
        - Location: {self.report['most_expensive_property']['Location']}

        ### Most Affordable Property 🏠💡
        - Price: {self.report['cheapest_property']['Price']:,.2f} €
        - Size: {self.report['cheapest_property']['SquareMeters']:,.2f} m²
        - Location: {self.report['cheapest_property']['Location']}

        ## Market Visualizations 📈🖼️
        ![Price vs. Size: The Dream Home Finder](price_vs_sqm.png)
        ![Price per m²: How Much Bang for Your Buck?](price_per_sqm_distribution.png)

        Remember, in real estate as in life, it's all about location, location, location! 🗺️🏠🗺️
        """
        with open('real-estate-report.md', 'w', encoding='utf-8') as f:
            f.write(report_md)
