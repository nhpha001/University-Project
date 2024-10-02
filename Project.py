# Import necessary libraries
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import glob
import os

# Function to load data from multiple CSV files, concatenate them into one DataFrame, and save the result
def load_data():
    directory_path = "/Users/mia/Desktop/Minh/Electives/Basic in Python/Dataset - Topic 14 (EPEX)"  # Path to the directory containing the dataset
    all_csv_files = glob.glob(os.path.join(directory_path, "*.csv"))  # Get all CSV files in the directory
    data_frames = [pd.read_csv(file, skiprows=1) for file in all_csv_files]  # Read each CSV, skipping the first row
    data_frame = pd.concat(data_frames, ignore_index=True)  # Concatenate all data into one DataFrame
    data_frame.to_csv("concatenated_data.csv", index=False)  # Save the concatenated data to a CSV file
    return data_frame  # Return the final DataFrame

# Function to filter data by a specific date and hour
def filter_data_by_date_hour(df):
    while True:
        # Prompt user to input a valid day in July
        day = input("Please specify the day in July you want to filter, with two digits (e.g. 07, 17):\n")
        date = f"{day}/07/2023"  # Format the date
        if date in [d for d in df["Date"]]:  # Check if the date exists in the dataset
            break
        print("Invalid date!")  # Prompt error if date is invalid
    while True:
        # Prompt user to input a valid hour
        hour = int(input("Please specify the hour you want to filter (1 - 24):\n"))
        if hour in [h for h in df["Hour"]]:  # Check if the hour exists in the dataset
            break
        print("Invalid hour!")  # Prompt error if hour is invalid
    # Return the filtered data based on the chosen date and hour
    return df[(df["Date"] == date) & (df["Hour"] == hour)]

# Function to adjust the supply volumes based on a user-specified percentage increase
def adjust_supply(df):
    while True:
        # Ask the user for the percentage increase in energy supply
        increase_percent = float(input("Please specify the percent of energy to add to the supply, e.g. 10:\n"))
        if increase_percent > 0:
            break
        print("The input value should be a positive number.")  # Ensure the input is positive
    
    # Filter the data to only include the rows where the Sale/Purchase column equals "Sell" (representing supply)
    adjust_supply_df = df[df["Sale/Purchase"] == "Sell"]

    # Filter the supply data based on price ranges
    in_range_prices = (adjust_supply_df["Price"] >= 0) & (adjust_supply_df["Price"] <= 10)  # Prices between 0 and 10
    following_prices = adjust_supply_df["Price"] > 10  # Prices greater than 10

    # Get the initial volumes for the selected price range
    initial_in_range_volumes = adjust_supply_df.loc[in_range_prices, "Volume"]
    altered_in_range_volumes = initial_in_range_volumes.copy()  # Create a copy of the volumes to modify

    # Adjust the supply volumes based on the percentage increase
    for a in range(1, len(altered_in_range_volumes)):
        initial_delta = (initial_in_range_volumes.iloc[a] - initial_in_range_volumes.iloc[a-1])
        altered_in_range_volumes.iloc[a] = altered_in_range_volumes.iloc[a-1] + (initial_delta * (1 + increase_percent / 100))
    
    # Update the adjusted supply DataFrame with the new volumes
    adjust_supply_df.loc[in_range_prices, "Volume"] = altered_in_range_volumes
    print(adjust_supply_df.loc[in_range_prices, "Volume"])  # Output the adjusted volumes for the user

    # Adjust the volumes for the prices greater than 10
    following_volumes = adjust_supply_df.loc[following_prices, "Volume"]
    delta_diff = altered_in_range_volumes.iloc[-1] - initial_in_range_volumes.iloc[-1]  # Calculate the difference in volume
    following_volumes = [volume + delta_diff for volume in following_volumes]
    
    # Update the adjusted supply DataFrame with the altered volumes for higher prices
    adjust_supply_df.loc[following_prices, "Volume"] = following_volumes
    print(adjust_supply_df.loc[following_prices, "Volume"])  # Output the adjusted volumes for higher prices
    return adjust_supply_df  # Return the DataFrame with adjusted supply volumes

# Function to plot the demand and supply curves, comparing initial and altered supply
def plot_demand_and_supply(i_df, a_df):
    # Separate initial supply, altered supply, and demand data
    initial_supply = i_df[(i_df["Sale/Purchase"] == "Sell")]
    altered_supply = a_df[(a_df["Sale/Purchase"] == "Sell")]
    demand = i_df[(i_df["Sale/Purchase"] == "Purchase")]

    # Plot the curves
    plt.figure(figsize=(15, 7.5))
    plt.plot(initial_supply["Volume"], initial_supply["Price"], label="Initial Supply", color="red")
    plt.plot(altered_supply["Volume"], altered_supply["Price"], label="Altered Supply", color="green")
    plt.plot(demand["Volume"], demand["Price"], label="Demand", color="blue")

    # Label the axes and add titles
    plt.xlabel("Volume (MWh)", loc="center")
    plt.ylabel("Price ($/MWh)", loc="center")
    
    # Retrieve and display the date and hour for the plot title
    date = i_df["Date"].iloc[0]
    hour = i_df["Hour"].iloc[0]
    plt.title(f"Date: {date}, Hour {hour}")
    
    # Add a grid, title, and legend to the plot
    plt.grid(True)
    plt.suptitle(f"Demand and Supply (Initial vs. Altered) Curves", fontweight="bold")
    plt.legend()

    # Show the plot
    plt.show()

# Main function to run the data loading, filtering, adjusting, and plotting
def main():
    dataframe = load_data()  # Load the dataset
    date_hour_filtered_df = filter_data_by_date_hour(dataframe)  # Filter data by the specified date and hour
    altered_supply_df = adjust_supply(date_hour_filtered_df)  # Adjust the supply based on user input
    plot_demand_and_supply(date_hour_filtered_df, altered_supply_df)  # Plot the initial and altered demand and supply curves

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
    