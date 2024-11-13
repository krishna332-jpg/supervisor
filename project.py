import re

class SupermarketSupervisor:
    def __init__(self):
        # Define updated sections for recognized categories based on new data
        self.sections = {
            "stationery": "1st section",
            "fruits and vegetables": "2nd section",
            "tools": "3rd section",
            "home appliances": "4th section",
            "food items": "5th section",
            "grocery": "6th section"
        }

    def get_item_price(self, item):
        # Updated pricing data with prices in USD, converted to INR
        pricing_data = {
            "apple": 1.2, "banana": 0.5, "orange": 0.7, "paper": 3.0,
            "color pencil": 1.5, "sketch": 2.0, "screwdriver": 5.99,
            "microwave": 99.99, "pasta": 2.5
        }
        price_in_usd = pricing_data.get(item.lower(), None)
        if price_in_usd:
            return round(price_in_usd * 83, 2)  # Convert USD to INR
        return None

    def categorize_item(self, item):
        # Updated category keywords for matching items to sections
        category_keywords = {
            "fruits and vegetables": ["apple", "banana", "orange", "grape", "mango"],
            "stationery": ["paper", "color pencil", "sketch", "pen", "notebook"],
            "tools": ["screwdriver", "hammer", "drill", "tool"],
            "home appliances": ["microwave", "blender", "fridge", "oven", "appliance"],
            "food items": ["pasta", "rice", "flour", "sugar", "oil", "food"],
            "grocery": ["soap", "detergent", "shampoo", "toothpaste", "grocery"]
        }
        for category, keywords in category_keywords.items():
            if any(keyword in item.lower() for keyword in keywords):
                return category
        return None

    def extract_item(self, sentence):
        # Updated list of possible items from the PDF
        possible_items = [
            "apple", "banana", "orange", "grape", "mango", "paper", "color pencil", "sketch",
            "screwdriver", "hammer", "microwave", "pasta", "soap", "detergent", "pen", "notebook",
            "tool", "blender", "fridge", "rice", "flour", "sugar", "oil", "shampoo", "toothpaste"
        ]
        for item in possible_items:
            if re.search(rf"\b{item}\b", sentence.lower()):
                return item
        return None

    def start_conversation(self):
        print("Hello! What item are you looking for?")
        sentence = input("Enter the item with any sentence: ").strip().lower()

        item = self.extract_item(sentence)
        if item:
            section = self.categorize_item(item)
            if section:
                print(f"The item '{item}' is located in the {self.sections[section]}.")
                if input(f"Would you like the price for '{item}'? (yes/no): ").strip().lower() == "yes":
                    self.handle_pricing_request(item)
                else:
                    print("Alright, anything else I can help with?")
            else:
                print("Sorry, we don’t seem to have that item in any section.")
                self.start_conversation()
        else:
            print("Couldn't identify the item. Please try again with a different description.")
            self.start_conversation()

    def handle_pricing_request(self, item):
        price_inr = self.get_item_price(item)
        if price_inr:
            print(f"The price for '{item.capitalize()}' is ₹{price_inr}.")
        else:
            print(f"Sorry, no price is available for '{item.capitalize()}' right now.")

        if input("\nNeed help with anything else? (yes/no): ").strip().lower() == "yes":
            self.start_conversation()
        else:
            print("Thanks for visiting! Have a great day!")

# Example usage
supervisor = SupermarketSupervisor()
supervisor.start_conversation()
