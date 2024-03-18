import random

class Product:
    def __init__(self, code, name, sale_price, manufacture_cost, stock_level, monthly_units):
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.monthly_units = monthly_units

    def simulate_month(self):
        self.stock_level += self.monthly_units
        units_sold = random.randint(self.monthly_units - 10, self.monthly_units + 10)
        units_sold = min(units_sold, self.stock_level)
        self.stock_level -= units_sold
        
        revenue = units_sold * self.sale_price
        cost = units_sold * self.manufacture_cost
        profit = revenue - cost
        
        return units_sold, self.monthly_units, revenue, cost, profit

    def simulate_12_months(self):
        total_units_sold = 0
        total_units_manufactured = 0
        total_revenue = 0
        total_cost = 0
        month = 1
        
        print("\nPredicted Stock Statement for the next 12 months:")
        print(f"{'Month':<10}{'Stock Level':<15}{'Units Sold':<15}{'Units Produced':<15}{'Revenue':<15}{'Cost':<15}{'Profit':<15}")
        
        while month <= 12:
            units_sold, units_produced, revenue, cost, profit = self.simulate_month()
            total_units_sold += units_sold
            total_units_manufactured += units_produced
            total_revenue += revenue
            total_cost += cost
            
            print(f"{month:<10}{self.stock_level:<15}{units_sold:<15}{units_produced:<15}${revenue:<14.2f}${cost:<14.2f}${profit:<14.2f}")
            
            month += 1
        
        net_profit = (total_units_sold * self.sale_price) - (total_units_manufactured * self.manufacture_cost)
        
        print(f"\nTotal Units Sold: {total_units_sold}")
        print(f"Total Units Manufactured: {total_units_manufactured}")
        print(f"Net Profit/Loss: ${net_profit:.2f}")

def main():
    code = int(input("Enter Product Code (100 to 1000): "))
    name = input("Enter Product Name: ")
    sale_price = float(input("Enter Product Sale Price: "))
    manufacture_cost = float(input("Enter Product Manufacture Cost: "))
    stock_level = int(input("Enter Stock Level: "))
    monthly_units = int(input("Enter Estimated Monthly Units Manufactured: "))
    
    product = Product(code, name, sale_price, manufacture_cost, stock_level, monthly_units)
    
    product.simulate_12_months()

if __name__ == "__main__":
    main()