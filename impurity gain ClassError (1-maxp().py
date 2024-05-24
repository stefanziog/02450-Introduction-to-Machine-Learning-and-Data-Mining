#Check purity Gain!
def classification_error(class_counts):
    """Calculate the classification error impurity."""
    total = sum(class_counts)
    if total == 0:
        return 1  # Maximum impurity if no samples are present
    max_prob = max(count / total for count in class_counts)
    return 1 - max_prob

def purity_gain(before_split, splits):
    """Calculate the purity gain from a split."""
    total_samples_before = sum(before_split)
    impurity_before = classification_error(before_split)
    
    # Calculate weighted impurity after the split
    total_samples_after = sum(sum(split) for split in splits)
    weighted_impurity_after = 0
    for split in splits:
        split_impurity = classification_error(split)
        weighted_impurity_after += (sum(split) / total_samples_before) * split_impurity

    # Calculate purity gain
    return impurity_before - weighted_impurity_after

# Example usage:
before_split = [146, 119, 68]  # 70 Kama, 70 Rosa, 70 Canadian
splits = [
    [149, 119, 0],  # 24 Kama, 70 Rosa, 0 Canadian
    [0, 0, 68]   # 46 Kama, 0 Rosa, 70 Canadian
]

# gain = purity_gain(before_split, splits)
# print(f"Purity Gain: {gain:.4f}")

#WITHOUT BEFORE SPLIT 

def classification_error(class_counts):
    """Calculate the classification error impurity."""
    total = sum(class_counts)
    if total == 0:
        return 1  # Maximum impurity if no samples are present
    max_prob = max(count / total for count in class_counts)
    return 1 - max_prob

def purity_gain(splits):
    """Calculate the purity gain from a split."""
    # Calculate before_split by summing up the corresponding counts in each category
    before_split = [sum(category) for category in zip(*splits)]
    total_samples_before = sum(before_split)
    impurity_before = classification_error(before_split)
    
    # Calculate weighted impurity after the split
    weighted_impurity_after = 0
    for split in splits:
        split_impurity = classification_error(split)
        weighted_impurity_after += (sum(split) / total_samples_before) * split_impurity

    # Calculate purity gain
    return impurity_before - weighted_impurity_after
# IT CAN BE DONE IN EXERCISE 18 FALL 20
# Example usage:
splits = [
    [149, 119, 0],  # 24 Kama, 70 Rosa, 0 Canadian
    [0, 0, 68]   # 46 Kama, 0 Rosa, 70 Canadian
]

gain = purity_gain(splits)
print(f"Purity Gain: {gain:.4f}")