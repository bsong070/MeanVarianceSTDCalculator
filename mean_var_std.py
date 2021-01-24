import numpy as np

def calculate(list):

    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")

    input = np.array(list).reshape(3,3)

    calculations = {
        'mean': [input.mean(axis=0).tolist(), input.mean(axis=1).tolist(), input.mean()],
        'variance': [input.var(axis=0).tolist(), input.var(axis=1).tolist(), input.var()],
        'standard deviation': [input.std(axis=0).tolist(), input.std(axis=1).tolist(), input.std()],
        'max': [input.max(axis=0).tolist(), input.max(axis=1).tolist(), input.max()],
        'min': [input.min(axis=0).tolist(), input.min(axis=1).tolist(), input.min()],
        'sum': [input.sum(axis=0).tolist(), input.sum(axis=1).tolist(), input.sum()]
    }


    return calculations