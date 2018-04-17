
import random
r=[[0,0,-1,0,-1,-1,-1,-1,-1],
   [0,0,0,-1,0,-1,-1,-1,-1],
   [-1,0,-1,-1,-1,0,-1,-1,-1],
   [0,-1,-1,-1,0,-1,0,-1,-1],
   [-1,0,-1,0,-1,0,-1,0,-1],
   [-1,-1,0,-1,0,-1,-1,-1,100],
   [-1,-1,-1,0,-1,-1,-1,0,-1],
   [-1,-1,-1,-1,0,-1,0,-1,100],
   [-1,-1,-1,-1,-1,0,-1,0,-1]
   ]
q=[[0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0]
   ]

max_Va=0
def train():
    state=random.randint(0,8)
    finish=False
    while(not finish):
        finish_state=False
        while(not finish_state):
            state_next=random.randint(0,8)
            max_va=max_val()
            if r[state][state_next]>=max_va:
                finish_state=True
        update(state,state_next)
        state=state_next
        if state==8:
            finish=True


def update(state,state_next):
    gamma=0.5
    alpha=0.8
    q[state][state_next]+=(alpha*(r[state][state_next]+(gamma*(maximum(q[state_next])))-q[state][state_next]))


def maximum(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max
def max_val(state):
    max_v=0
    for i in range(0,12):
        if R[state][i]>max_v:
            max_v=R[state][i]
    return max_v


for i in range(10000):
    train()
for i in q:
    print i
