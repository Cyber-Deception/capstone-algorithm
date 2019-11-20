# capstone-algorithm

MiniMax implementation:

How to run: python3 miniMax.py [INPUT_TEXT_NAME_HERE].txt

(1) fileManager.py // deals with the output of whole program when miniMax.py is run
        Input: Takes in output of miniMax.py
        Output: Outputs data structure into the masked configuration

(2) networkManager.py
        Input: Takes in [INPUT_TEXT_NAME_HERE].txt
        Output: Creates the data structure of the observable configuration
        
(3) miniMax.py
        Input: Takes in output from networkManager.py which is the observable configuration, 
                runs the minimax algorithm and configuration
        Output: the best configuration of the network, along with the scores in a .txt file (changing to datastructure once I add the ports, etc.)
