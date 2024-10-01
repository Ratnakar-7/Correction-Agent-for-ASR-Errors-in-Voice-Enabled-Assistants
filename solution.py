class Agent(object):
    def __init__(self, phoneme_table, vocabulary) -> None:
        self.phoneme_table = phoneme_table
        self.vocabulary = vocabulary
        self.best_state = None

    def get_next_best_state(self, curr_state, environment, phoneme):

        new_state = curr_state
        curr_statement = curr_state[0]
        curr_cost = curr_state[-1]
        curr_word = curr_state[1]
        i = curr_state[-2]
        index = curr_state[2]
        if(i==len(curr_word)):
            return new_state
  
        for key in phoneme.keys():
            if curr_word[i:i+len(key)] == key:
                for v in phoneme[key]:
                    new_word = curr_word[:i] + v + curr_word[i+len(key):]
                    l = curr_statement.split(' ')
                    l[index] = new_word
                    new_statement = ' '.join(l)
                    new_cost = environment.compute_cost(new_statement)
                    if new_cost < curr_cost:
                        new_state = [new_statement, new_word, index, i+len(v), new_cost]
                        return self.get_next_best_state(new_state, environment, phoneme)
                        
        new_state = curr_state
        new_state[-2] += 1
        return self.get_next_best_state(new_state, environment, phoneme)      
        
    def create_state(self, statement, word, index, i, environment):
        current_cost = environment.compute_cost()
        current_state = [statement, word, index, i, current_cost]        
        return current_state
        

    def asr_corrector(self, environment):
        self.best_state = environment.init_state
        cost = environment.compute_cost(environment.init_state)

        phoneme = self.phoneme_table
        iphoneme = dict()

        for k,v in phoneme.items():
            for x in v:
                if x not in iphoneme.keys():
                    iphoneme[x] = []
                    iphoneme[x].append(k)
                else:
                    iphoneme[x].append(k)


        for i,word in enumerate(self.best_state.split(' ')):
            curr_state = [self.best_state, word, i, 0, environment.compute_cost(self.best_state)]
            new_state = self.get_next_best_state(curr_state, environment, iphoneme)
            self.best_state = new_state[0]


        current_cost = environment.compute_cost(self.best_state)
        current_state = self.best_state
        best_state = current_state
        best_cost = current_cost

        for i in self.vocabulary:
            new_state1 = i + " " + current_state
            new_cost1 = environment.compute_cost(new_state1)
            
            if new_cost1 < best_cost:
                best_state = new_state1
                best_cost = new_cost1 
            new_state1 = ""

        current_state = best_state
        current_cost = environment.compute_cost(current_state)

        for i in self.vocabulary:
            new_state1 = current_state + " " + i
            new_cost1 = environment.compute_cost(new_state1)
            
            if new_cost1 < best_cost:
                best_state = new_state1
                best_cost = new_cost1 
            new_state1 = "" 
        
        print(best_state, environment.compute_cost(best_state))
        self.best_state = best_state

        