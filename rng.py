"""
the class middle square grabs the middle digits from a given number after multiplying squaring it by itself
"""


class MiddleSquare:

    # this init method takes in seed as an int
    def __init__(self, seed: int):

        # checks and makes sure that  seed is an int
        if isinstance(seed, int):
            digit_check = len(str(seed))

            # checks and makes sure the seed is 2 digits
            if (digit_check % 2) == 0:
                self.seed = seed

            # if its not 2 digits and raises type error
            elif (digit_check % 2) != 0:
                raise ValueError("There are not an even amount of digits")
        else:
            raise TypeError("Only integers are allowed")

        # the list of seeds to check if its repeating
        self.seed_list = []

        # its seed squared and I originally thought it was just used for zfill but its also used in
        # a couple of other places
        self.num_zfill = len(str(self.seed)) * 2

        # created this so get and set state would work and less repeating code
        self.state_squared_divided = int(self.num_zfill / 2)

    """""
     iter just returns self so that it can go over itself
    """""

    def __iter__(self):
        return self

    """
    required for iter to work and does most of the heavy lifting such as the math and makes the new seed. It grabs 
    the middle digits of whatever length seed after it was squared. It will update the seed with the new numbers 
    grabbed from the previous seed being squared
    """

    def __next__(self):

        # checks if seed is in list and if it is raises a stop iteration to stop the class
        if self.seed in self.seed_list:
            raise StopIteration(print("Repeat number, so terminate!"))

        # if its not in the list already it updates it with the seed
        else:
            self.seed_list.append(self.seed)

        seed_square = self.seed * self.seed

        # checks to see if the seed needs 0's in fornt of the see to make it equal to the seed digits doubled
        if len(str(seed_square)) < self.num_zfill:
            new_numb = str(seed_square).zfill(self.num_zfill)

        # if it doesn't it just skips that part and makes the seed^2 into a string
        else:
            new_numb = str(seed_square)

        # floor decided to get the middle 2 numbers regardless of length
        middle = len(new_numb) // 2
        middle_1 = middle // 2
        middle_2 = -middle_1
        middle_digits_str = new_numb[middle_1:middle_2]

        # sets seed the int of the middle digits
        self.seed = int(middle_digits_str)
        return self.seed

    """
    get state returns the values necessary to pickup where the class previously ended if the program where to stop after
    x amount of time and 
    """

    def get_state(self):
        state = {'val': self.seed, 'ndigits': self.state_squared_divided}
        return state

    """
    set state is what is in the constructor and sets the items necessary such as seed, num_zfill and 
    state_squared_divided. The reason we need these is to stop repeating code
    """

    def set_state(self, state):
        self.seed = state['val']
        self.state_squared_divided = state['ndigits']
        self.num_zfill = state['ndigits'] * 2


"""
Linear Congruential is a random number generator that multiples the seed by a (a number) and ads by c (another number)
then takes the remainder of m (another number) after that it continues until the seed starts repeating 
"""


class LinearCongruential:
    def __init__(self, seed: int, a: int, c: int, m: int):

        # constructors to global parameters
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

        # list of seeds that already been seen
        self.seed_list = []

    """
    iter returns self
    """

    def __iter__(self):
        return self

    """
    next produces the next sequence for the seed does the math and edits over itself
    """

    def __next__(self):

        # should stop the rng if the seed repeats
        if self.seed in self.seed_list:
            raise StopIteration("Repeat number, so terminate!")

        # adds new seed to list of seeds
        else:
            self.seed_list.append(self.seed)

        # math part, a * current seed + c  % m and then updates seed and returns it
        lc_rng_math = (self.a * self.seed + self.c) % self.m
        self.seed = lc_rng_math

        return self.seed

    """
    get states returns the current values if the rng is to stop and can be used at a later date 
    """

    def get_state(self):
        state = {'a': self.a, 'c': self.c, 'm': self.m, 'val': self.seed}
        return state

    """
    set state is used with get state to restart an rng after it was stop and picks ip where it was left off
    """

    def set_state(self, state):
        self.a = state['a']
        self.c = state['c']
        self.m = state['m']
        self.seed = state['val']


"""
gets rid of the fist digit after grabbing the k digit and j digit and adding the new number created to the 
end of the list and goes for x amount of time or until numbers start repeating
"""


class LaggedFibonacci:
    def __init__(self, seed: list[int], j: int, k: int, m: int):

        # checks to see if seed is a list
        if isinstance(seed, list):

            # checks all values in seed to make sure there ints
            for i in seed:

                # if its not an int then it raises an error
                if not isinstance(i, int):
                    raise TypeError("items in list need to be an int")

                # otherwise continue through the list
                else:
                    continue

            # if it makes it through the list the self.seed can be seed
            self.seed = seed

        # if seed  isn't a list raises a typeError
        elif not isinstance(seed, list):
            raise TypeError("seed needs to be a list")

        # makes sure then j is greater then or = to - and that k is bigger then the length of the seed
        if 0 <= j < k <= len(seed):
            self.j = j
            self.k = k

        # if j is smaller than 0 and k is bigger than seed it raises error
        else:
            raise ValueError("values for j and k are not right")

        self.m = m

        # makes a list of seeds
        self.list_of_seed = []

    """
    iter returns self
    """

    def __iter__(self):
        return self

    """
    next goes over its self and does the math and updates seed until it starts repeating, it grabs j digits 
    and k digits away to grab those digits and adds them togather and takes the remainder of them. Also will shift all 
    the digits to the left one because it gets ride of the first digit
    """

    def __next__(self):

        # sets mod to m made it easier to keep track of
        mod = self.m

        # goes from the back and updates j num by the amount the original j num was. Does the same for k num
        j_num = self.seed[-self.j]
        k_num = self.seed[-self.k]

        # adds the numbers from the
        new_num = (j_num + k_num) % mod

        # gets rid of the first digit or last digit depending on how you read/look at it
        self.seed.pop(0)

        # adds new num to seed list
        self.seed.append(new_num)

        # uses tuple so that it cant be changed
        tuple_of_seed = tuple(self.seed)

        # checks to see if there is already a tuple in the list
        if tuple_of_seed in self.list_of_seed:
            raise StopIteration("repeat number")

        # if tuple isn't in seed list then it adds the tuple
        else:
            self.list_of_seed.append(tuple_of_seed)

        return new_num

    """
    get states returns the current values if the rng is to stop and can be used at a later date 
    """

    def get_state(self):
        state = {'j': self.j, 'k': self.k, 'm': self.m, 'val': self.seed}
        return state

    """
    set state is used with get state to restart an rng after it was stop and picks up where it was left off
    """

    def set_state(self, state):
        self.j = state['j']
        self.k = state['k']
        self.m = state['m']
        self.seed = state['val']


"""
the acorn rng wont let numbers get bigger then m and creates a new list of numbers. if keeps the first number of the
seed while updating the rest of the seed with new numbers and it will continue to do this until the 
seeds start repeating
"""


class Acorn:
    def __init__(self, seed: list[int], M: int):

        # checks if seed is list
        if isinstance(seed, list):

            # for all the items in list checks if its is an int
            for i in seed:

                # if it isnt an int then it raises a typer error
                if not isinstance(i, int):
                    raise TypeError("items in list need to be an int")

                # if it is an int keep going
                else:
                    continue

            # if the items in seed makes in trough the loop then self.seed can be seed
            self.seed = seed

        # if seed isn't a list raises a type error
        elif not isinstance(seed, list):
            raise TypeError("seed needs to be a list")

        # if M is greater than the first num in the list
        if M > self.seed[0]:
            self.m = M

        # if M isn't then it raises a value error
        else:
            raise ValueError("M needs to be bigger then the first number in seed")

        self.list_of_seed = []

    """
    iter returns self
    """

    def __iter__(self):
        return self

    """
    if the acorn class is called it will go over itself and return the next sequence. which is found by keeping the same
    first number and adding a the next number not letting it get bigger then m and then making that the new seed.
    after the new seed is made it restarts untill numbers start repeating or if it was specified to run a ceartin 
    number of times
    """

    def __next__(self):
        tuple_of_seed = tuple(self.seed)

        # use tuple so that it cant change and then adds it to the list or stops if its already in the list
        if tuple_of_seed in self.list_of_seed:
            raise StopIteration("repeat number")
        else:
            self.list_of_seed.append(tuple_of_seed)

        # this makes sure that the first number is always the same
        new_list = [self.seed[0]]
        i = 0
        numb = new_list[0]

        # had to be a while loop because I was getting index errors
        while len(new_list) < len(self.seed):
            i += 1

            # i works the same as if it was a for loop and this checks to see if the 2 numbers added up
            # are bigger than m
            if numb + self.seed[i] < self.m:
                numb += self.seed[i]
                new_list.append(numb)

            # if it is bigger than m it takes the remainder and updates the new list
            else:
                numb = (self.seed[i] + numb) % self.m
                new_list.append(numb)

        self.seed = new_list
        return self.seed

    """
    get states returns the current values if the rng is to stop and can be used at a later date 
    """

    def get_state(self):
        state = {'vals': self.seed, 'M': self.m}
        return state

    """
    set state is used with get state to restart an rng after it was stop and picks up where it was left off
    """

    def set_state(self, state):
        self.seed = state['vals']
        self.m = state['M']


class Analyzer:
    def __init__(self, rand_num_gen):
        self.rand_num_gen = rand_num_gen
        self.max = int()
        self.min = int()
        self.average = float()
        self.period = int()
        self.bit_freqs = []

    def analyze(self, max_nums=1e10):
        big = 0
        small = 0
        div_num = 0
        total = 0
        for i in max_nums:
            self.rand_num_gen(i)

#
# ms_seed = 456423
# lcg_seed = 3456
# lcg_a = 3
# lcg_c = 36
# lcg_m = 12
# lf_seed = [90, 9, 432, 434, 21 ,32, 234,7865, 999,7,4,43,13,432,7651,963,2357,85,2,4,686,5, 6, 12, 12, 3, 6, 5, 8, 12, 33, 421, 21, 12312, 334876, 23]
# lf_j = 7
# lf_k = 22
# lf_m = 2
# ac_seed = [90, 9, 5, 6, 12, 12, 3, 6, 5, 8, 12, 33, 421, 21, 12312, 334876, 23]
# ac_M = 123

# class LinearCongruential:
#     def __init__(self, seed: int, a: int, c: int, m: int):
lc = LinearCongruential()