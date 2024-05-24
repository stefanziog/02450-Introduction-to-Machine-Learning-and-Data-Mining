import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

# True binary labels
ya = [0,1,1,1,0,1,0,1,0]
yb = [1, 0, 1, 0, 0, 1, 1, 1]
yc = [0, 1, 1, 0, 1, 1, 1, 0]
yd = [0, 1, 1, 0, 1, 0, 1, 1]
yd = [1, 0, 0, 1, 0, 1, 0, 0]

# Scores for class 1
scores = [0,0.08,0.12,0.15,0.36,0.57,0.58, 0.75,0.81]

# Calculate the ROC curve
fpr, tpr, thresholds = metrics.roc_curve(ya, scores)

# Print the TPR and FPR values
for i in range(len(fpr)):
    print(f"FPR: {fpr[i]}, TPR: {tpr[i]}, Threshold: {thresholds[i]}")

# Calculate the AUC
auc = metrics.roc_auc_score(ya, scores)
print(f"AUC: {auc}")

# Plot the ROC curve
plt.figure()
plt.plot(fpr, tpr, label=f'ROC curve (AUC = {auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()
