#Program for Monthly Sales Analysis
#Set initial values for tracking the sales data
total_sales = 0
highest_sales = 0
lowest_sales = 0
high_sales_months = 0

#Accept sales figures for all 12 months
for month in range(1, 13):

    #Read the monthly sales amount from the user.
    print("Enter sales for month", month, ": ")
    sales = float(input())

    #Add the current month's sales to the annual total.
    total_sales += sales

    #Store the first sales value as the initial lowest value.
    if month == 1:
        highest_sales = sales
        lowest_sales = sales

    #Update the highest and lowest sales values.
    if sales > highest_sales:
        highest_sales = sales

    elif sales < lowest_sales:
        lowest_sales = sales

    #Count months where sales exceed ₹1,00,000.
    if sales > 100000:
        high_sales_months = high_sales_months + 1

#Calculate the average monthly sales.
average_sales = total_sales / 12

#Calculate the percentage of months with high sales.
high_sales_percentage = (high_sales_months / 12) * 100

#Display the complete sales analysis
print("Total annual sales: ₹", total_sales)
print("Average monthly sales: ₹", average_sales)
print("Highest monthly sales: ₹", highest_sales)
print("Lowest monthly sales: ₹", lowest_sales)
print("High-sales months:", high_sales_months)
print("Percentage of high-sales months:", high_sales_percentage, "%")