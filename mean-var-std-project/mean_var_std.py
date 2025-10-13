import numpy as np

def calculate():

    lst = input("Enter 9 digits, they must be separated by spaces: ").split()

    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    my_list = np.array(lst, dtype=float).reshape(3, 3)

    return {
        'mean': [np.mean(my_list,axis=0).tolist(), np.mean(my_list,axis=1).tolist(), float(my_list.mean())],
        'variance': [np.var(my_list,axis=0).tolist(), np.var(my_list,axis=1).tolist(), float(my_list.var())],
        'standard deviation': [np.std(my_list,axis=0).tolist(), np.std(my_list,axis=1).tolist(), float(my_list.std())],
        'max': [np.max(my_list,axis=0).tolist(), np.max(my_list,axis=1).tolist(), float(my_list.max())],
        'min': [np.min(my_list,axis=0).tolist(), np.min(my_list,axis=1).tolist(), float(my_list.min())],
        'sum': [np.sum(my_list,axis=0).tolist(), np.sum(my_list,axis=1).tolist(), float(my_list.sum())]
    }

if __name__ == "__main__":
    print(calculate())
