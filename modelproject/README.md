# OLG Model under PAYG System

This code provides an implementation of the Overlapping Generations (OLG) model under a Pay-as-you-go (PAYG) system. The OLG model is an economic model that captures the interactions between different generations over time, while the PAYG system refers to a system where the younger generation pays for a portion of the consumption of the older generation.

## Model Description

The OLG model considers an economy with a population that grows at a fixed annual rate. The population is divided into two groups: workers and retirees. The economy features identical firms with Cobb-Douglas production functions, where output depends on capital and labor inputs. The wage and interest rates are determined by the marginal product of the respective factors.

Individuals in the economy maximize their intertemporal utility, taking into account their consumption and savings decisions. The utility function is assumed to be logarithmic, and individuals are subject to budget constraints. Under the PAYG system, the young generation contributes a portion of their wage income to support the consumption of the older generation.

## Analytical Solution

The code provides an analytical solution to the OLG model under the PAYG system. The following key equations are derived and displayed:

- Utility Function: The logarithmic utility function that represents individuals' preferences over consumption in different periods.
- Euler Equation: The equation that characterizes the optimal consumption path, relating consumption in the current period to consumption in the next period and the interest rate.
- Optimal Savings: The equation that determines the optimal savings decision of individuals, considering the budget constraints and interest rates.
- Capital Accumulation: The equation that describes the accumulation of capital over time based on the production function and savings decisions.
- Steady State: The equation that defines the steady-state level of capital in the economy.

## Graphical Analysis

The code includes graphical content to visualize the dynamics of the OLG model. Specifically:

- Capital Accumulation Plot: A plot showing the relationship between capital levels in different periods, illustrating how capital accumulates over time.
- Impact of Parameter Changes: Plots demonstrating the effect of changing parameters, such as the interest rate coefficient (`rho`), on capital accumulation.

## Interactive Plot

The code also provides an interactive plot using `ipywidgets`. Users can adjust parameter values and observe the corresponding changes in capital accumulation. This interactive plot allows for a more intuitive exploration of the model's dynamics.

## Conclusion

In conclusion, this code offers an implementation of the OLG model under a PAYG system, allowing for the analysis of intertemporal utility maximization, optimal savings, capital accumulation, and the steady state of the model. It provides an analytical solution, graphical visualizations, and an interactive plot to facilitate the understanding of the model's dynamics and the impact of different parameters on key variables.

Note: The code assumes a specific functional form for the utility function and production function. Further extensions and modifications can be made to explore different specifications and scenarios within the OLG framework.
