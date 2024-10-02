# University-Project
Python Project - German Spot Energy Market: EPEX DA Energy Market Modelling and Visualization

- Goals:

1. Build a script capable of reconstructing the aggregated demand and supply curves in a plot, based on the data from the CSV
files.
• Make your script interactive so that a user could type in a date and the script would produce a plot of supply and
demand curves with hourly data for that day.

2. Add functionality to your script that would allow to adjust energy supply (quantity of energy “Sell”) in a specific price range. For example, we want to simulate 20% or 30% more energy being offered to the market at the prices between 0Eur/MWh and 10Eur/MWh.
• Make it possible for the user to give input on how much more percent of energy should be added to the supply (e.g., +10%, +20%, etc.).
• Your script should then plot a chart with both supply curves in it (an initial and an altered one).

- Given:
• Raw data from the energy exchange (aggregated curves of supply and demand containing information about volumes and prices of the EPEX Day Ahead Auction for July 2023).

- Background information:
• EPEX Spot is a subsidiary of the EEX which is the largest energy exchange and a clearing house in Europe. Day-Ahead markets, among the other, are operated through a Day-Ahead blind auction which takes place once a day, every day of the year. The electricity traded on this Day-Ahead auction is delivered on the next day. A blind auction simply means that bidders submit their buy and sell bids without any information about the bids of the others. Here we consider 24 hourly contracts corresponding to the 24 delivery hours of the following day.
• When the auction takes place, all sellers and buyers of the energy digitally submits their bids to EPEX, which then aggregates them, creates the supply and demand curves, and calculates the market clearing prices (equilibrium prices) for each hourly product of the next day. In this context, you are given the raw data for the aggregated curves which are prepared based on the submitted bids.
