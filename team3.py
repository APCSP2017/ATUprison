####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Petcaugh' # Only 10 chars displayed.
strategy_name = 'Percentage Attack'
strategy_description = 'You wish you knew.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    opp_b = 0
    opp_c = 0
    if len(their_history)<10: #Collude for the first 10 rounds
        return 'c'
    elif len(their_history)<20:#Betray for rounds 10-20
        return 'b'
    else:
        #Record how many times the opponent has betrayed and colluded.
        #This will then be used to make decisions based on percentages
        for choice in their_history:
            if choice == 'b':
                opp_b += 1
            else:
                opp_c += 1
                
        #If the opponent has not colluded, then BETRAY.
        #Otherwise, calculate the percentage
        if opp_c != 0:
            percentage = float(opp_b / opp_c)
        else:
            return 'b'
            
        #If the opponent has betrayed more than they have colluded,
        #then BETRAY. Otherwise COLLUDE.
        if percentage >= 1:
            return 'b'
        else:
            return 'c'
    

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             