// Import libraries into script 

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to get random double between 0.0 and 1.0
double rand_double() {
    return (double) rand() / (double) RAND_MAX;
}

int main() {
    int num_simulations = 10000;
    int order_wuantity = 200;

    double selling_price = 120.0; 
    double order_cost = 30.0; 

    double total_profit = 0.0; 

    // Seed random number generator
    srand(time(NULL));

    for (int i = 0; i < num_simulations; i++)
    {
        // Demand is uniformly distributed between 0 and 300 units
        int demand = (int)(rand_double() * 300.0);

        int units_sold = (demand < order_quantity) ? demand : order_quantity;
        int units_leftover = order_quantity - units_sold;

        // Calculate financial outcome for this trial
        double revenue = units_sold * selling_price;
        double cost = order_quantity * order_cost;
        double profit = revenue - cost;

        // Excess boxes are discarded, losing the cost of the unit
        // (No salvage value)
        total_profit += profit;
    }

    double expected_profit = total_profit / num_simulations;

    printf("Simulation Results (Order Quantity: %d):\n", order_quantity);
    printf("Expected Profit: %.2f\n", expected_profit);

    return 0;
}