import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import auc

# Data
#low_mpg = [2, 2, 13]
#high_mpg = [3, 10, 2]

#I NEED TO ADD 2+2+13=17 for the one axis points and 3+2+10=15 for the other

# Convert to binary classes (0 for low, 1 for high)
#y_true = np.concatenate([np.zeros(sum(low_mpg)), np.ones(sum(high_mpg))])

# Points on the ROC curve based on your manual calculations
fpr_manual = [0,4/28, 10/17.5, 1]
tpr_manual = [0,10/16, 15/16, 1]

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