# Create your own DataFrame called sales with columns: month. revenue, expenses
# Then print it out.

import pandas as pd


data = {
	"month": ["January", "February", "March"],
	"revenue": [5000, 7000, 6500],
	"expenses": [3000, 4000, 3500],
}

sales = pd.DataFrame(data)

# Print the DataFrame
print(sales)

