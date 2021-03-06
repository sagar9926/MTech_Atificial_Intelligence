# -*- coding: utf-8 -*-

from sys import argv
import math
import itertools
import copy 
import numpy as np
import random
import time


def goodness_function(schedule,dis,sim):
      
    """
      Returns the goodness of the schedule
    
      Parameters:
          schedule : Nested list of size t (time slot)x p (prallel session)x k (papers).
          dis :  Matrix containing the dissimilarity scores for all papers
          sim : dis :  Matrix containing the similarity scores for all papers
    
      Returns:
          goodness : Numerical Goodness value corresponding to a particular schedule.
    """
    goodness = {}
    
    global c
    for time_slot_index in range(len(schedule)):
      goodness[time_slot_index] = 0 
    
      # fetch the schedule for one time slot
      single_time_slot_sessions = schedule[time_slot_index]
    
      # Calculate similarity score and update goodness
      for index in range(len(single_time_slot_sessions)):
        session = single_time_slot_sessions[index]
        for session_i in session:
          for session_j in session:
            if(session_i != session_j):
              goodness[time_slot_index] += sim[session_i][session_j] / 2
    
      # Calculate dissimilarity score and update goodness
      for session_a in single_time_slot_sessions:
        for session_b in single_time_slot_sessions:
          if session_a != session_b:
            for session_i in session_a:
              for session_j in session_b:
                goodness[time_slot_index] += c*dis[session_i][session_j] / 2
    
    return goodness

def generate_neighbour (current_schedule_state):
    
    """
      Returns a randomly generated next state. This function helps algorithm to traverse the entire seach space randomly. 
      The next state generated is completely random when compared to the current state. This function can be interpreted
      as "Random Jumping Mechanism" which helps us to explore the search space by randomly jumping from one state to another
      
      Parameters:
          current_schedule_state : This is the current state of our search problem.
        
      Returns:
          next_schedule_state : A randomly generated next state. The function takes into consideration all the papers and generates 
          neighbouring state by randomly rearranging all papers among parallel sessions across all time slots
          
    """
    papers = sum(list(itertools.chain(*current_schedule_state)),[])
    global t
    global p
    global k
    next_schedule_state = [[[None for _ in range(k)] for _ in range(p)] for _ in range(t)]
    
    for slot in range(t):
      for session in range(p):
        for paper in range(k):
          temp = random.sample(papers,k = 1)[0]
          next_schedule_state[slot][session][paper] = temp
          papers.remove(temp)
    return next_schedule_state


def generate_neighbour2 (current_schedule_state):
    
    """
      Returns next state. The next state is obtained by randomly swapping any two papers (irrespective of their session or time slot)
      This function can be interpreted as baby steps taken to move towards the goal state. In this current and the next state are
      very much similar and just differ for any two random paper locations
      
      Parameters:
          current_schedule_state : This is the current state of our search problem.
        
      Returns:
           next_schedule_state :  A randomly generated next state. The function takes into consideration all the papers and generates 
          neighbouring state by randomly swapping any two papers.
    
          
    """
    
    global t
    global p
    global k
    next_schedule_state = copy.deepcopy(current_schedule_state)
    slot1,session1,paper1  = np.random.randint(t),np.random.randint(p),np.random.randint(k)
    slot2,session2,paper2  = np.random.randint(t),np.random.randint(p),np.random.randint(k)
    
    temp = next_schedule_state[slot2][session2][paper2]
    next_schedule_state[slot2][session2][paper2] = next_schedule_state[slot1][session1][paper1]
    next_schedule_state[slot1][session1][paper1] = temp
    
    return next_schedule_state

def exploration(initial_schedule_state):
 
    """
     This function uses the "generate_neighbour()" function to perform exploration, which is a "Random Jumping Mechanism" i.e we can jump from one 
     state to some enitrely different state. Exploration allows a search algorithm to come close to the global minimum or good local minimum also
     the exploration ensures the algorithm to reach different promising regions of the search space. This functions Scans the search space by randomly
     jumping from one state to another and for every state it compares the goodness value of it's current state with new state and store the best state
     visited (i.e. with highest goodness score). Every time it checks if neighbor is best so far and  if the new solution is better, accept it and continue exploration.
    
    Parameters:
        initial_schedule_state : This is the Initial state of our search problem.
      
    Returns:
         best_initial_state :  The state visited with highest goodness value in exploration process .

        
    """

    # Exploration to find best initial state
    print("Exploration Start")
    
    # Exploration parameter
    exploration = 100 
    
    #Exploration decay amount
    update_exploration = 0.001

    while exploration > 0.1:
      exploration = exploration - update_exploration
      neighbor = generate_neighbour(initial_schedule_state)

      # Check if neighbor is best so far
      cost_diff_1 = sum([next_cost - current_cost for current_cost , next_cost  in  zip(goodness_function(initial_schedule_state,dis,sim).values() , goodness_function(neighbor,dis,sim).values())])

      # if the new solution is better, accept it
      if cost_diff_1 > 0:
        best_initial_state = neighbor
      initial_schedule_state = neighbor
        
    return(best_initial_state)

def simulated_annealing(initial_schedule_state):
    """
    This function leverages the best initial state obtained in exploration state and starts simulated annealing.
    
    Algorithm : 
        1. Perform exploration to get a starting state with some high goodness value.
        2. From this best start state take a random move and generate a neighbouring state 
        3. Calculate the goodness cost difference between the new neighbour and current state
        4. If the cost difference is positive then make update current state with new state with probability = 1
        5. If the cost difference is negative then update current state with new state with probability which is a function 
           of cost difference and temperature paremeter.
           
    Parameters:
        initial_schedule_state : This is the Initial state of our search problem.
      
    Returns:
         solution : schedule with the high goodness value

        
    """    
    
    best_initial_state = exploration(initial_schedule_state)
    print("Exploration End")
    print("Simulated Annealing Starts ")
    initial_temp = 180
    final_temp = .1
    alpha = 0.001
    
    current_temp = initial_temp

    # Start by initializing the current state with the initial state
    current_schedule_state = best_initial_state
    solution = best_initial_state

    while current_temp > final_temp:
        neighbor = generate_neighbour2(current_schedule_state)

        # Check if neighbor is best so far
        cost_diff = sum([next_cost - current_cost for current_cost , next_cost  in  zip(goodness_function(current_schedule_state,dis,sim).values() , goodness_function(neighbor,dis,sim).values())])
        # if the new solution is better, accept it
        if cost_diff > 0:
            solution = neighbor
            current_schedule_state = neighbor
            last_best_state = neighbor
        # if the new solution is not better, accept it with a probability of e^(-cost/temp)
        else:
            if random.uniform(0, 1) < math.exp(cost_diff / current_temp):
                solution = neighbor
                current_schedule_state = neighbor
        # decrement the temperature
        current_temp -= alpha

    return last_best_state , solution


if __name__ == '__main__' :

    _,input_file , output_file = argv
    
    # Reading the input file
    f = open(input_file)

    # Each session has k papers
    k=int(f.readline()) 
    
    # Schedule have p parallel sessions
    p=int(f.readline()) 
    
    # Total of t timeslots
    t=int(f.readline())
    
    # tradeoff parameter
    c=float(f.readline())
    
    # total number of paper
    tnp=p*k*t 
    
    dim=k*p*t
    dis=[]  #Distance array
    
    sim=[]  #Similarity array
    
    
    ## The following loop computes the similarity and disimmilarity matrices
    for i in range(dim):
      m=[]
      l=f.readline().strip().split(' ')
      for i in range(len(l)):
        l[i]=float(l[i])
        m+=[round(1.0-float(l[i]),2)]
      dis+=[l]
      sim+=[m]
    
    ## Randomly finding the initial state
    # create a one dimensional list of all papers
    papers_1d = list(np.arange(dim))
    
    # Randomly shuffle the paper list
    random.shuffle(papers_1d)
    
    start = time.time()
    
    # Let's initialise the initial state of my search problem
    initial_state = [[[papers_1d.pop() for _ in range(k)] for _ in range(p)] for _ in range(t)] 
    last_best_state,result  = simulated_annealing(initial_state)
    goodness_cost = goodness_function(result,dis,sim)
    
    # Printing goodness value
    total_goodness = 0
    for i,val in goodness_cost.items():
      print("Goodness value for time slot : ",i + 1, " is ",round(val,2))
      total_goodness += val
    print("Total Goodness value of Schedule is ",round(total_goodness,2))
    time_slot = []
    for i in result:
      parallel_session = []
      for j in i :
        parallel_session.append((" ".join([str(paper + 1) for paper in j])))
    
      time_slot.append(" | ".join(parallel_session))
    
    
    print("Writing result to output file")
    with open(output_file, 'w') as myfile:  
        for line in time_slot:
            myfile.write(line+'\n')
    end = time.time()
    print("Time Elapsed ", (end - start)/60," minutes")
