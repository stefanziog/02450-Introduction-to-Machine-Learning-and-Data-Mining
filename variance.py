#VARIANCE IF YOU HAVE THE σ1, σ2, σ3, σ4 values from SVD, specifically S table


def calculate_specific_proportion_of_variance(singular_values, component_index):
    # Calculate variances by squaring the singular values
    variances = [sigma ** 2 for sigma in singular_values]
    # Calculate the total variance
    total_variance = sum(variances)
    # Extract the variance of the specific component (component_index should be 1-based)
    specific_variance = variances[component_index - 1] if 0 < component_index <= len(variances) else 0
    # Calculate the proportion of variance explained by the specified component
    proportion = specific_variance / total_variance
    return proportion

# Example usage:
singular_values = [14.4, 8.19, 7.83, 6.91, 6.01]  # Replace with your actual singular values

# Calculate and print the proportion of variance explained by the second component
component_index = 1  # Set to the index of the component you are interested in
proportion_s1= calculate_specific_proportion_of_variance(singular_values, component_index)
print(f"Proportion of variance explained by σ{component_index}^2: {proportion_s1:.4f}")

component_index = 2  # Set to the index of the component you are interested in
proportion_s2= calculate_specific_proportion_of_variance(singular_values, component_index)
print(f"Proportion of variance explained by σ{component_index}^2: {proportion_s2:.4f}")

component_index = 3  # Set to the index of the component you are interested in
proportion_s3= calculate_specific_proportion_of_variance(singular_values, component_index)
print(f"Proportion of variance explained by σ{component_index}^2: {proportion_s3:.4f}")

component_index = 4  # Set to the index of the component you are interested in
proportion_s4= calculate_specific_proportion_of_variance(singular_values, component_index)
print(f"Proportion of variance explained by σ{component_index}^2: {proportion_s4:.4f}")

component_index = 5  # Set to the index of the component you are interested in
proportion_s5= calculate_specific_proportion_of_variance(singular_values, component_index)
print(f"Proportion of variance explained by σ{component_index}^2: {proportion_s4:.4f}")

last_four =  proportion_s2 + proportion_s3 + proportion_s4 + proportion_s5
print (f"Proportion of variance explained by first two components: {last_four:.4f}")