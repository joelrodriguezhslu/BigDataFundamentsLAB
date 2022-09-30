#Importing libraries

from time import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading pattern from Keyboard
input = input ('Enter the Protein Pattern to search for: \n')

#convert to uppercase
pattern = input.upper()

print('Searching for pattern: '+pattern)
#start measurement
start = time()

#read CSV
df = pd.read_csv('proteins.csv', delimiter=',')

#counting Occurrences and sorting
df['count']=df.sequence.str.count(pattern)
df_sorted=df.sort_values('count',ascending=False).head(10)
print(df_sorted)

#stop measurement
end = time()
print("Processing time = ", end - start)

#plotting
df_sorted.plot(kind='bar',x='structureId',y='count')
plt.title("Top 10 proteins for search pattern: "+pattern)
plt.xlabel("Structure ID")
plt.ylabel("Occurrences")
plt.show()

#print max occurrence
print("Protein with max Occurrences for Search: " +pattern)
print(df_sorted.head(1))




#Reads the pattern to search from the keyboard.
#2. Changes the pattern to UPPERCASE
#3. Start metering exec time
#4. Reads the protein patterns from the file in pair (id, sequence)
#5. Look for occurrences of the pattern string inside each protein sequence
#6. If there are occurrence, register the id of the protein and the
#number of occurrences in the sequence
#7. Print a histogram using protein id as X and number of
#occurrences as Y (you can use matplotlib.pyplot). Show 10
#proteins with more matches
#8. Print the protein id with max occurrences.