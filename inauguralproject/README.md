# Household Specialization Model

This repository implements a household specialization model to analyze the joint utility maximization of labor within households. The model considers various parameters and preferences to determine optimal choices for male and female household members regarding market work and home production.

## Classes

### HouseholdSpecializationModelClass

This class represents the household specialization model. It contains methods to solve the model, estimate parameters, and analyze the results.

#### Methods

- `__init__()`: Initializes the class and sets default parameter values.

- `calc_utility(LM, HM, LF, HF)`: Calculates the utility given the parameters LM, HM, LF, and HF.

- `solve_discrete()`: Solves the model discretely by finding the combination of choices for market work and home production that maximizes utility.

- `solve_con()`: Solves the model continuously using numerical optimization techniques.

- `solve_wF_vec(discrete=False)`: Solves the model for different female wages. It can be solved discretely or continuously based on the `discrete` argument.

- `run_regression()`: Performs a regression analysis to estimate the parameters beta0 and beta1.

- `estimate(alpha=0.5, sigma=0.5)`: Estimates the optimal values for alpha and sigma by minimizing the error between the estimated beta0 and beta1 values and target values.

- `estimation_extended(sigma=0.5, epsilon=1, extended=True)`: Extends the estimation process by considering additional parameters sigma and epsilon. It estimates the optimal values for sigma and epsilon when extended is set to True. Otherwise, it estimates only the optimal value for sigma.

## Functions

### plot_HFHM_alpha()

This function plots the relationship between HF/HM and alpha for different values of sigma. It demonstrates how HF/HM changes when varying alpha.

### plot_HFHM_wFwM()

This function plots the relationship between HF/HM and wF/wM for different values of wF. It illustrates how HF/HM changes with varying wF/wM.

### plot_HFHM_wFwM_continuous()

This function plots the relationship between HF/HM and wF/wM for different values of wF using the continuous model.

### estimate_parameters()

This function estimates the optimal values for alpha and sigma by minimizing the error between the estimated beta0 and beta1 values and target values. It plots the regression model to visualize the fit to the data.

### extend_model()

This function suggests and implements an extension of the model by considering the parameter epsilon. It analyzes whether the extended model can better match the data when alpha = 0.5.

## Usage

To use the model and functions simply clone the repository to your local machine: git clone https://github.com/your-username/household-specialization-model.git 
