#creating a class for the application
import random 
class product:
    def __init__(self,code = int,name = str,sale_price= float,manufacture_cost = float,stock_level = int,monthly_units= int):
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.monthly_units= monthly_units

     # stimulating monthly production and sale ends.
    def stimulate_month(self):
      #finding the estimated monthly production.
       self.stock_level = self.monthly_units + self.stock_level
       # getting the units_sold 
       unit_sold = random.randint (self.monthly_units -10,self.monthly_units +10)
       # this is to find the lowest value between the unit sold and stock level so it wont be higher than stock level.
       unit_sold = min (unit_sold, self.stock_level)
       self. stock_level = self.stock_level - unit_sold
       revenue = unit_sold * self.sale_price
       cost = self.manufacture_cost - unit_sold
       profit = revenue - cost

       return revenue, cost, profit, unit_sold, self. monthly_units
    # for 12 months with prdicted values
    def stimulate_12_months(self):
        total_units_sold = 0
        total_units_manufactured = 0
        total_revenue = 0
        total_cost = 0
        month = 1
        print (f"predicted stock statement for the next 12 months")
        print(f"{'Month':<10}{'Stock Level':<15}{'Units Sold':<15}{'Units Produced':<15}{'Revenue':<15}{'Cost':<15}{'Profit':<15}")
        while month <=12:
           units_sold, units_produced, revenue, cost, profit = self.stimulate_month()
           total_units_sold += units_sold
           total_units_manufactured += units_produced
           total_revenue += revenue
           total_cost += cost
           month += 1
           print(f"{month:<10}{self.stock_level:<15}{units_sold:<15}{units_produced:<15}${revenue:<14.2f}${cost:<14.2f}${profit:<14.2f}")

        net_profit = (total_units_sold * self.sale_price) - (total_units_manufactured * self.manufacture_cost)

        print (F"total units sold: {total_units_sold}")
        print(f"total units manufactured: {total_units_manufactured}")
        print(f"print profit/loss: ${net_profit:}")       
 
def main():
    code = input("Enter Product Code (100 to 1000): ")
    name = input("Enter Product Name: ")
    sale_price = float(input("Enter Product Sale Price: "))
    manufacture_cost = float(input("Enter Product Manufacture Cost: "))
    stock_level = int(input("Enter Stock Level: "))
    monthly_units = int(input("Enter Estimated Monthly Units Manufactured: "))
    prod = product(code, name, sale_price, manufacture_cost, stock_level, monthly_units)

    prod.stimulate_12_months()



if __name__ == "__main__":
    main()






 


