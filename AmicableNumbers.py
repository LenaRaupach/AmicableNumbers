import yaml
from multiprocessing import Pool

def load_config(path="config.yml"):
    # loads config file
    try:
        with open(path, "r") as file:
            return yaml.safe_load(file)
    except OSError:
        print(f"Failed to load the config file")
        return {}

def get_amicable_numbers(max_value):
    # calculated the proper divisors for every number until the maximum value
    amicable_numbers = set()
    # use parallel processing to increase performance, use all accessible cores per default
    with Pool() as pool:
        result = pool.map(calc_proper_divisor_sum, range(1, max_value))
    proper_divisors_sum_dict = dict(result)
    # compares the dictionary keys and values for amicable number matches
    for number1, proper_divisors_sum1 in proper_divisors_sum_dict.items():
        for number2, proper_divisors_sum2 in proper_divisors_sum_dict.items():
            if (number1 != number2
                    and number1 == proper_divisors_sum2
                    and proper_divisors_sum1 == number2)\
                    and number1 < number2:
                amicable_numbers.add((number1, number2))
    return sorted(amicable_numbers)

def calc_proper_divisor_sum(number):
    return (number, sum(get_proper_divisors(number)))

def get_proper_divisors(number):
    # 1 is always a proper divisor
    proper_divisors = {1}
    # check only until the root of the number to avoid double check
    for divisor in range(2, int(number ** 0.5) +1):
        if number != divisor and number % divisor == 0:
            proper_divisors.add(divisor)
            proper_divisors.add(number // divisor)
    return proper_divisors


if __name__ == '__main__':
    config = load_config("config.yml")
    limit = config['limit']
    print(get_amicable_numbers(limit))
