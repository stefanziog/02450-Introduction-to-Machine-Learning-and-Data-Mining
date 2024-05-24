import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import auc

# Data
low_mpg = [2, 2, 13]
high_mpg = [3, 10, 2]

# Calculate True Positive Rate (TPR) and False Positive Rate (FPR) manually
tpr_manual = np.cumsum(high_mpg) / np.sum(high_mpg)
fpr_manual = np.cumsum(low_mpg) / np.sum(low_mpg)

# Insert the initial point (0,0)
tpr_manual = np.insert(tpr_manual, 0, 0)
fpr_manual = np.insert(fpr_manual, 0, 0)

# Calculate AUC
roc_auc_manual = auc(fpr_manual, tpr_manual)

# Plot ROC curve
plt.figure()
plt.plot(fpr_manual, tpr_manual, color='darkorange', lw=2, label=f'AUC = {roc_auc_manual:.2f}')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('ROC Curve (Manual)')
plt.legend(loc="lower right")
plt.show()
