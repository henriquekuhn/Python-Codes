import os
import pandas

DIRECTORY = os.getcwd() + "/Panda Introduction"
os.chdir(DIRECTORY)

data = pandas.read_csv("weather_data.csv")
print(data)

# Calculating temperature average
temp_list = data["temp"].to_list()
temp_avg = sum(temp_list)/len(temp_list)
print(f"Average temperature: {temp_avg}")

# OR
print(f"Mean temperature: {data['temp'].mean()}")

# Getting highest temperature
print(f"Maximum temperature: {data['temp'].max()}")

# Print the hole line
print(f"Line of the highest temperature:\n {data[data.temp == data['temp'].max()]}")

# Get condition through week day
monday = data[data.day == 'Monday']
monday_temp = monday.temp[0]  
print(f"Monday: {monday}")
print(f"Temperature from C to F: {monday_temp} -> {monday_temp* 9/5 + 32}")

# Create a dataframe from a dict
data_dict = {
    "students": ["Rosbif", "Chuck Norris", "Billy the Kid"],
    "scores": [10, 0, 5]
}

new_dataframe = pandas.DataFrame(data_dict)
new_dataframe.to_csv("new_data.csv")

