import pandas as pd
import math

# Example dataset
# data = {
#     'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy'],
#     'Play Tennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
# }

# data = {
#     'income': ['high', 'high', 'high', 'medium', 'low', 'low', 'low', 'medium', 'low', 'medium', 'medium', 'medium', 'high', 'medium'],
#     'buys_computer': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
# }
data = {
    'Shirt_color': ['black', 'maroon', 'maroon', 'black', 'gray'],
    'Shirt_size': ['small', 'small', 'medium', 'large', 'large'],
    'sold': ['yes', 'no', 'yes', 'yes', 'no']
}

df = pd.DataFrame(data)

def entropy(prob_yes, prob_no):
    if prob_yes == 0 or prob_no == 0:
        return 0
    print(f"Entropy of yes: {round(-prob_yes * math.log2(prob_yes), 3)}")
    print(f"Entropy of no: {round(-prob_no * math.log2(prob_no), 3)}")
    return -prob_yes * math.log2(prob_yes) - prob_no * math.log2(prob_no)

def information_gain(data, feature, target):
    print('\nCalculation Entropy of target')
    entropy_before = round(entropy(data[target].value_counts(normalize=True).get('yes', 0), data[target].value_counts(normalize=True).get('no', 0)), 3)
    print(f"Entropy before: {entropy_before}\n")
    
    values = data[feature].unique()
    weighted_entropy_after = 0
    
    for value in values:
        print(f"Calculating entropy for {value}")
        subset = data[data[feature] == value]
        prob_value = round(len(subset) / len(data), 3)
        entropy_after = entropy(subset[target].value_counts(normalize=True).get('yes', 0), subset[target].value_counts(normalize=True).get('no', 0))
        print(f"Entropy after {value}: {entropy_after}")
        print(f"Prob {value}: {prob_value}")
        print(f"Weighted entropy after {value}: {round(prob_value * entropy_after, 3)}\n")
        weighted_entropy_after += round(prob_value * entropy_after, 3)
    
    weighted_entropy_after = round(weighted_entropy_after, 3)
    information_gain = round(entropy_before - weighted_entropy_after, 3)
    print(f"Information Gain = {entropy_before} -  {weighted_entropy_after}")
    return information_gain

# Calculate Information Gain for the Shirt_color feature
ig_shirt_color = information_gain(df, 'Shirt_color', 'sold')
print(f"Information Gain for Shirt_color: {ig_shirt_color}")

# Calculate Information Gain for the Shirt_size feature
ig_shirt_size = information_gain(df, 'Shirt_size', 'sold')
print(f"Information Gain for Shirt_size: {ig_shirt_size}")