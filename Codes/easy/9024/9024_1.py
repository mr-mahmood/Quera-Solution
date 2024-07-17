# https://quera.org/problemset/9024


def find_winner(numbers):

    player1_score, player2_score = 0, 0

    current_player = 1 # game start with player 1

    

    while numbers:

        # Player 1's strategy

        if current_player == 1:

            

            # Player 1 will choose the number that max his score and left some bad choose for player 2

            

            max_difference = -float('inf') # it is negative infinity, so all number in start are bigger than this

            choice = -float('inf')

            flag = True

            

            for i in range(len(numbers)):

                

                # leaving the smallest possible sum for Player 2

                sums = sum(numbers[i+1:])

                difference = numbers[i] - sums 

                

                if (difference >= max_difference) or (difference < max_difference and numbers[i] >= choice):

                    max_difference = difference

                    choice = numbers[i]

                    index = i

                    

                if difference < max_difference:

                    

                    # Simulate Player 2's best choice after Player 1's current choice

                    next_best_for_p2 = max(numbers[i+1:]) if numbers[i+1:] else 0

                    

                    # Simulate Player 2's best choice after Player 1's previous best choice

                    prev_best_for_p2 = max(numbers[index+1:]) if numbers[index+1:] else 0

                    

                    # Choose the current number if it leaves Player 2 with a worse option than the previous best choice

                    if next_best_for_p2 < prev_best_for_p2 and flag == True:

                        choice = numbers[i]

                        index = i

                        flag = False

                    

            player1_score += choice

        # Player 2's strategy

        else:

            # Player 2 will choose the largest available number

            choice = max(numbers)

            player2_score += choice

            index = numbers.index(choice)

        

        

        numbers = numbers[index+1:] # Remove the chosen number and all numbers before it

        

        # Switch players

        current_player = 2 if current_player == 1 else 1

    



    if player1_score > player2_score:

        return f"karakter e komaki_1: {player1_score-player2_score}"

    elif player2_score > player1_score:

        return f"karakter e komaki_2: {player2_score-player1_score}"

    else:

        return "mosavi"



n = int(input())

winner = find_winner(list(map(int, input().split())))

print(winner)