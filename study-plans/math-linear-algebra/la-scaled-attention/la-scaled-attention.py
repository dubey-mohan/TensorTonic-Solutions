import numpy as np

def scaled_dot_product_attention(Q, K, V):
    """
    Returns: ndarray, the attention output softmax(Q @ K.T / sqrt(d_k)) @ V.
    """
    Q = np.array(Q)
    K = np.array(K)
    V = np.array(V)

    qk = Q @ K.T
    scaled_qk = qk / np.sqrt(Q.shape[1])
    exp_scores = np.exp(scaled_qk - np.max(scaled_qk))
    softmax_sqk = exp_scores / np.sum(exp_scores, axis = 1,  keepdims=True)
    weighted_v = softmax_sqk @ V

    return weighted_v