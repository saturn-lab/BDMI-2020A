#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import tensorflow as tf
data = open('input.txt', 'r').read()  # should be simple plain text file
chars = list(set(data))
data_size, vocab_size = len(data), len(chars)

char2idx = { ch:i for i, ch in enumerate(chars)}
idx2char = np.array(chars)


# In[3]:



def get_raw_data():
    data_as_int = np.array(list(map(char2idx.get,data)))
    return data_as_int[0:-1],data_as_int[1:]

get_raw_data()


# In[6]:


state_size = 100
batch_size = 5
seq_length = 25
learning_rate = 1e-1

def get_batch_seq(data):
    raw_x, raw_y = data
    batch_partition_length = len(raw_x) // batch_size
    print(batch_partition_length)
    print(raw_x[:-(len(raw_x)%batch_partition_length)])
    data_x=raw_x[:-(len(raw_x)%batch_partition_length)].reshape(-1,batch_partition_length)
    data_y=raw_y[:-(len(raw_x)%batch_partition_length)].reshape(-1,batch_partition_length)
    
    epoch_steps = batch_partition_length // seq_length
    for step in range(epoch_steps):        
        x = data_x[:, step*seq_length:(step+1)*seq_length]
        y = data_y[:, step*seq_length:(step+1)*seq_length]
        yield x,y           

def get_epoch(n):
    for i in range(n):
        yield get_batch_seq(get_raw_data())


# In[7]:


class CharRnnModel():
    
    def __init__(self):
        self.sess = tf.Session()
        
    def create_compute_graph(self):

        with tf.variable_scope(str(id(self)) + 'rnn_cell'):
            w = tf.get_variable('w',[vocab_size + state_size, state_size])
            b = tf.get_variable('b',[state_size],initializer=tf.constant_initializer(0.0))

        def rnn_cell(rnn_input,pre_state):

            with tf.variable_scope(str(id(self)) + 'rnn_cell',reuse=True):
                w = tf.get_variable('w',[vocab_size + state_size, state_size])
                b = tf.get_variable('b',[state_size],initializer=tf.constant_initializer(0.0))
            return tf.tanh(tf.matmul(tf.concat([rnn_input,pre_state],axis=1), w) + b)
        
        # def create_compute_graph():
        x = tf.placeholder(tf.int32, [None, seq_length])
        y = tf.placeholder(tf.int32, [None, seq_length])
        init_state = tf.placeholder(tf.float32,[None, state_size])

        x_one_hot = tf.one_hot(x,vocab_size)
        y_one_hot = tf.one_hot(y,vocab_size)

        rnn_inputs = tf.unstack(x_one_hot,axis=1)
        rnn_labels = tf.unstack(y_one_hot,axis=1)

        state = init_state
        rnn_outputs = []
        for rnn_input in rnn_inputs:
            state = rnn_cell(rnn_input, state)
            rnn_outputs.append(state)
        final_state = state

        with tf.variable_scope(str(id(self)) + 'softmax'):
            w = tf.get_variable('w',[state_size, vocab_size])
            b = tf.get_variable('b',[vocab_size],initializer=tf.constant_initializer(0.0))

        logits = [tf.matmul(rnn_output, w) + b for rnn_output in rnn_outputs]
        #predictions = [tf.nn.softmax(logit) for logit in logits]

        losses = [tf.nn.softmax_cross_entropy_with_logits(labels=label, logits=logit)                   for logit, label in zip(logits, rnn_labels)]
        total_loss = tf.reduce_mean(losses)
        update = tf.train.AdagradOptimizer(learning_rate).minimize(total_loss)
        
        return x,y,init_state,final_state,total_loss,update
    
    def train(self,num_epochs):
        x,y,init_state,final_state,total_loss,update = self.create_compute_graph()
        
        self.sess.run(tf.global_variables_initializer())
        training_losses=[]
        for epoch in get_epoch(num_epochs):
            training_loss = 0
            training_state = np.zeros((batch_size, state_size))
            for step, (X, Y) in enumerate(epoch):
                training_loss_, training_state, _ = self.sess.run([total_loss,final_state,update],
                                                             feed_dict={x:X, y:Y, init_state:training_state})
                training_loss += training_loss_
                if step % 1000 == 0 and step > 0:
                    print("Average loss at step", step,
                          "for last 250 steps:", training_loss/100)
                    training_losses.append(training_loss/100)
                    training_loss = 0
        print('train finished')
        return training_losses
    
    def create_test_graph(self):
        x = tf.placeholder(tf.int32,[1])
        x_one_hot = tf.one_hot(x,vocab_size)
        init_state = tf.placeholder(tf.float32,[1,state_size])
        
        with tf.variable_scope(str(id(self)) + 'rnn_cell',reuse=True):
            w = tf.get_variable('w',[vocab_size + state_size, state_size])
            b = tf.get_variable('b',[state_size],initializer=tf.constant_initializer(0.0))
            
        state = tf.tanh(tf.matmul(tf.concat([x_one_hot,init_state],axis=1),w) + b)
        
        with tf.variable_scope(str(id(self)) + 'softmax', reuse=True):
            w2 = tf.get_variable('w',[state_size, vocab_size])
            b2 = tf.get_variable('b',[vocab_size],initializer=tf.constant_initializer(0.0))
        y = tf.matmul(state,w2) + b2
        p = tf.nn.softmax(y)
        out = tf.argmax(p,axis=1) 
        return x, init_state,state, out
    
    def sample(self,n):
        x, init_state, state,out = self.create_test_graph()
        test_x = np.array([char2idx.get(data[0])])
        training_state = np.zeros([1,state_size])
        result = []
        for i in range(n):
            result.append(test_x[0])
            training_state,test_x = self.sess.run([state,out],feed_dict = {x:test_x, 
                                                                           init_state:training_state})
        return "".join(list(map(lambda x:idx2char[x],result)))
        
    
model = CharRnnModel()    
model.train(1)

model.sample(100)

