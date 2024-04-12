import numpy as np

from chainer import dataset

def hasone(node_index, dim_index):
    bin_i, bin_j = np.binary_repr(node_index), np.binary_repr(dim_index)
    length = len(bin_j)
    return (bin_i[:length] == bin_j) * 1

def hasone_print(node_index, dim_index):
    print('start hasone')
    print('node_index: ', node_index)
    print('dim_index: ', dim_index)
    bin_i, bin_j = np.binary_repr(node_index), np.binary_repr(dim_index)
    print('bin_i: ', bin_i)
    print('bin_j: ', bin_j)
    length = len(bin_j)
    print('length of bin_j: ', length)
    print('bin_i[:length]: ', bin_i[:length])
    print('hasone returns: ', (bin_i[:length] == bin_j) * 1)
    print('end hasone')
    return (bin_i[:length] == bin_j) * 1


def hamming_distance(x, y):
    return (x.astype(np.int32) ^ y.astype(np.int32)).sum()


def euclid_distance(x, y):
    return np.sqrt(((x - y)**2).sum(axis=-1))

def get_data(depth, dtype=np.float32):
    n = 2**depth - 1

    x = np.fromfunction(lambda i, j: np.vectorize(hasone)(i + 1, j + 1),
                        (n, n), dtype=np.int32).astype(dtype)
    return x

# def get_data(depth, dtype=np.float32):
#     n = 2**(depth+1) - 1
#     x = np.fromfunction(lambda i, j: np.vectorize(hasone)(i + 1, j + 1),
#                         (n, n), dtype=np.int32).astype(dtype)
#     return x

# def get_data_print(depth, dtype=np.float32):
#     print('start get_data')
#     n = 2**(depth+1) - 1
#     print('depth: ', depth)
#     print('n: ', n)

#     x = np.fromfunction(lambda i, j: np.vectorize(hasone_print)(i + 1, j + 1),
#                         (n, n), dtype=np.int32).astype(dtype)
#     print('get_data returns x: ', x)
#     print('end get_data')
#     return x


class ProbabilisticBinaryTreeDataset(dataset.DatasetMixin):

    def __init__(self, data, eps):
        self.data = data
        self.eps = eps
        self.shape = data.shape

    def __len__(self):
        return len(self.data)

    def get_example(self, i):
        filter_ = np.random.random(size=self.shape[-1]) < self.eps
        return (self.data[i].astype(bool) ^ filter_).astype(self.data.dtype)
