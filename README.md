MiniMax implementation:

How to run: python3 miniMax.py [INPUT_TEXT_NAME_HERE].txt


(1) networkManager.py
        Input: Takes in [INPUT_TEXT_NAME_HERE].txt
        Output: Creates the data structure of the observable configuration, list of port #s, etc.
        
(2) miniMax.py
        Input: Takes in output from networkManager.py which is the observable configuration, 
                runs the minimax algorithm and configuration
        Output: the best configuration of the network
                (as of right now it is printing the ports in the terminal)
                    I will change it to output the data structure 

(3) fileManager.py // not being used right now - can be used if we want to print out the output into a file
        Input: Takes in output of miniMax.py
        Output: Outputs data structure into the masked configuration into a text file