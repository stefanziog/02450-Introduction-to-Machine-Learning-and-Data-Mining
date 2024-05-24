#confusion matrix
# FOR ACC, ERROR RATE, RECALL, PRECISION, FPR, TPR
import numpy as np

### Confusion Matrix2x2
def confusion_matrix(matrix=None, tp=None, fn=None, tn=None, fp=None):
    if matrix:
        [tp, fn], [fp, tn] = matrix

    print("TP:", tp, "FN:", fn, "TN:", tn, "FP:", fp)

    n = tp + fn + tn + fp
    accuracy = (tp + tn) / n
    error = 1 - accuracy
    recall = tp / (tp + fn)
    prec = tp / (tp + fp)
    fpr = fp / (fp + tn)
    tpr = tp / (tp + fn)

    print('Accuracy:', accuracy)
    print('Error rate:', error)
    print('Recall:', recall)
    print('Precision:', prec)
    print('FPR:', fpr)
    print('TPR:', tpr)
    
#for 2x2
conf_matrix = [
    [18, 12],  # TP = 40, FN = 5
    [9, 15]  # FP = 10, TN = 45
]

confusion_matrix(conf_matrix)



#for 3x3 
### Confusion Matrix3x3

def calculate_metrics(conf_matrix):
    # Convert list of lists to a numpy array for easier manipulation
    conf_matrix = np.array(conf_matrix)
    accuracy = np.trace(conf_matrix) / np.sum(conf_matrix)
    recall = np.diag(conf_matrix) / np.sum(conf_matrix, axis=1)
    precision = np.diag(conf_matrix) / np.sum(conf_matrix, axis=0)

    print("Accuracy:", accuracy)
    for i, (r, p) in enumerate(zip(recall, precision), 1):
        print(f"Class {i} - Recall: {r:.2f}, Precision: {p:.2f}")

# conf_matrix = [
#     [18,12],
#     [9,15]

# ]
# calculate_metrics(conf_matrix)



