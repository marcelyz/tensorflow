import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt

# tensor: represent an array of 0 to n order
c = np.arange(24).reshape(2, 4, 3)
print(c)

# tf tensor
a = tf.constant([1, 5], dtype=tf.int64)
print(a)
print(a.dtype)
print(a.shape)

# numpy format to tf tensor
a = np.arange(0, 5)
b = tf.convert_to_tensor(a, dtype=tf.int64)
print(a)
print(b)

# tensor of different values
a = tf.zeros([2, 3])
b = tf.ones(4)
c = tf.fill([2, 2], 9)
print(a)
print(b)
print(c)

# tensor of different distribution random
d = tf.random.normal([2, 2], mean=0.5, stddev=1)
print(d)
e = tf.random.truncated_normal([2, 2], mean=0.5, stddev=1)
print(e)
f = tf.random.uniform([2, 2], minval=0, maxval=1)
print(f)

# common functions
x1 = tf.constant([1., 2., 3.], dtype=tf.float64)
print(x1)
x2 = tf.cast(x1, tf.int32)
print(x2)

x = tf.constant([[1, 2, 3], [2, 2, 3]])
print(x)
print(tf.reduce_mean(x))
print(tf.reduce_sum(x, axis=1))

w = tf.Variable(tf.random.normal([2, 2], mean=0, stddev=1))

a = tf.ones([1, 3])
b = tf.fill([1, 3], 3.)
print(a)
print(b)
print(tf.add(a, b))
print(tf.subtract(a, b))
print(tf.multiply(a, b))
print(tf.divide(b, a))

a = tf.fill([1, 2], 3.)
print(a)
print(tf.pow(a, 3))
print(tf.square(a))
print(tf.sqrt(a))

a = tf.ones([3, 2])
b = tf.fill([2, 3], 3.)
print(tf.matmul(a, b))

features = tf.constant([12, 23, 10, 17])
labels = tf.constant([0, 1, 1, 0])
dataset = tf.data.Dataset.from_tensor_slices((features, labels))
print(dataset)
for element in dataset:
    print(element)

with tf.GradientTape() as tape:
    w = tf.Variable(tf.constant(3.0))
    loss = tf.pow(w, 2)
grad = tape.gradient(loss, w)
print(grad)

classes = 3
labels = tf.constant([1, 0, 2])
output = tf.one_hot(labels, depth=classes)
print(output)

y = tf.constant([1.01, 2.01, -0.66])
y_pro = tf.nn.softmax(y)
print("After softmax, y_pro is: ", y_pro)

w = tf.Variable(4)
w.assign_sub(1)
print(w)

test = np.array([[1, 2, 3], [2, 3, 4], [5, 4, 3], [8, 7, 2]])
print(test)
print(tf.argmax(test, axis=0))
print(tf.argmax(test, axis=1))

print(tf.where([True, False, True, False], [1, 2, 3, 4], [5, 6, 7, 8]))

x = tf.constant([2, 4])
y = tf.constant(2)
print(tf.math.equal(x, y))

# forward
x1 = tf.constant([[5.8, 4.0, 1.2, 0.2]])
w1 = tf.constant([[-0.8, -0.34, -1.4],
                  [0.6, 1.3, 0.25],
                  [0.5, 1.45, 0.9],
                  [0.65, 0.7, -1.2]])
b1 = tf.constant([2.52, -3.1, 5.62])
y = tf.matmul(x1, w1) + b1
print("x1.shape: ", x1.shape)
print("w1.shape: ", w1.shape)
print("b1.shape: ", b1.shape)
print("y.shape: ", y.shape)
print("y: ", y)

y_dim = tf.squeeze(y)
y_pro = tf.nn.softmax(y_dim)
print("y_dim: ", y_dim)
print("y_pro: ", y_pro)

# back propagation
w = tf.Variable(tf.constant(5, dtype=tf.float32))
lr = 0.2
epoch = 40
for epoch in range(epoch):
    with tf.GradientTape() as tape:
        loss = tf.square(w + 1)
    grads = tape.gradient(loss, w)
    w.assign_sub(lr * grads)
    print("After %s epoch, w is %f, loss is %s " % (epoch, w.numpy(), loss))

# optimizers
# sgd
w = tf.Variable(tf.constant(5, dtype=tf.float32))
lr = 0.2
with tf.GradientTape() as tape:
    loss = tf.square(w + 1)
grads = tape.gradient(loss, w)
w.assign_sub(lr * grads)
print("sgd w: ", w)

# sgdm: sgd with momentum
w = tf.Variable(tf.constant(5, dtype=tf.float32))
lr = 0.2
beta = 0.9
m_w = 0
with tf.GradientTape() as tape:
    loss = tf.square(w + 1)
grads = tape.gradient(loss, w)
m_w = beta * m_w + (1 - beta) * grads
w.assign_sub(lr * m_w)
print("sgdm w: ", w)

# adagrad: adaptive learning rate sgd
w = tf.Variable(tf.constant(5, dtype=tf.float32))
lr = 0.2
v_w = 0
with tf.GradientTape() as tape:
    loss = tf.square(w + 1)
grads = tape.gradient(loss, w)
v_w += tf.square(grads)
w.assign_sub(lr * grads / tf.sqrt(v_w))
print("adagrad w: ", w)

# RMSProp: Root Mean Square Prop
w = tf.Variable(tf.constant(5, dtype=tf.float32))
lr = 0.2
beta = 0.9
v_w = 0
with tf.GradientTape() as tape:
    loss = tf.square(w + 1)
grads = tape.gradient(loss, w)
v_w = beta * v_w + (1 - beta) * tf.square(grads)
w.assign_sub(lr * grads / tf.sqrt(v_w))
print("RMSProp w: ", w)

# adam: adaptive moment estimation
w = tf.Variable(tf.constant(5, dtype=tf.float32))
lr = 0.2
v_w, v_b = 0, 0
beta1, beta2 = 0.9, 0.999
global_step = 1
with tf.GradientTape() as tape:
    loss = tf.square(w + 1)
grads = tape.gradient(loss, w)
m_w = beta1 * m_w + (1 - beta1) * grads
v_w = beta2 * v_w + (1 - beta2) * grads
m_w_correction = m_w / (1 - tf.pow(beta1, int(global_step)))
v_w_correction = v_w / (1 - tf.pow(beta2, int(global_step)))
w.assign_sub(lr * m_w_correction / tf.sqrt(v_w_correction))
print("adam w: ", w)

# learning rate strategy
# ExponentialDecay
N = 400
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    0.5,
    decay_steps=10,
    decay_rate=0.9,
    staircase=False)
y = []
for global_step in range(N):
    lr = lr_schedule(global_step)
    y.append(lr)
x = range(N)
plt.figure(figsize=(8, 6))
plt.plot(x, y, "r-")
plt.ylim([0, max(plt.ylim())])
plt.xlabel("step")
plt.ylabel("Learning Rate")
plt.title("ExponentialDecay")
plt.show()

# PiecewiseConstantDecay

N = 400
lr_schedule = tf.keras.optimizers.schedules.PiecewiseConstantDecay(
    boundaries=[100, 200, 300],
    values=[0.1, 0.05, 0.025, 0.001])
y = []
for global_step in range(N):
    lr = lr_schedule(global_step)
    y.append(lr)
x = range(N)
plt.figure(figsize=(8, 6))
plt.plot(x, y, "r-")
plt.ylim([0, max(plt.ylim())])
plt.xlabel("step")
plt.ylabel("Learning Rate")
plt.title("PieceConstantDecay")
plt.show()

# activate functions
# sigmoid
x = tf.constant([1., 2., 3.])
print(tf.math.sigmoid(x))
print(1/(1+tf.math.exp(-x)))

# tanh
x = tf.constant([-float("inf"), -5, -0.5, 1, 1.2, 2, 3, float("inf")])
print(tf.math.tanh(x))
print((tf.math.exp(x)-tf.math.exp(-x)) / (tf.math.exp(x)+tf.math.exp(-x)))

# relu
print(tf.nn.relu([-2., 0., -0., 3.]))
print([i if i >= 0 else 0 for i in [-2., 0., -0., 3.]])

# leaky_relu
print(tf.nn.leaky_relu([-2., 0., -0., 3.], alpha=0.2))
alpha = 0.2
print([i if i >= 0 else alpha*i for i in [-2., 0., -0., 3.]])

# softmax
logits = tf.constant([4., 5., 1.])
print(tf.nn.softmax(logits))
print(tf.exp(logits) / tf.reduce_sum(tf.exp(logits)))

# loss functions
# mse
y_true = tf.constant([0.5, 0.8])
y_pred = tf.constant([1.0, 1.0])
print(tf.keras.losses.mse(y_true, y_pred))
print(tf.reduce_mean(tf.square(y_true - y_pred)))

# categorical_crossentropy
y_true = [1, 0, 0]
y_pred = [0.5, 0.4, 0.1]
print(tf.keras.losses.categorical_crossentropy(y_true, y_pred))
print(-tf.reduce_sum(y_true * tf.math.log(y_pred)))

# softmax_cross_entropy_with_logits
labels = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]
logits = [[4.0, 2.0, 1.0], [0.0, 5.0, 1.0]]  # 机器学习中，把未经softmax归一化的向量值称为logits
print(tf.nn.softmax_cross_entropy_with_logits(labels=labels, logits=logits))
print(-tf.reduce_sum(labels * tf.math.log(tf.nn.softmax(logits)), axis=1))

# sparse_softmax_cross_entropy_with_logits
labels = [0, 1]
logits = [[4.0, 2.0, 1.0], [0.0, 5.0, 1.0]]
print(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=labels, logits=logits))
print(-tf.reduce_sum(tf.one_hot(labels, tf.shape(logits)[1]) * tf.math.log(tf.nn.softmax(logits)), axis=1))
