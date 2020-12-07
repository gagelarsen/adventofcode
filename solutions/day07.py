"""
Day 07 of the Advent of Code Challenge Code

Author: Gage Larsen
Date: December 6, 2020
"""
from inputs.day07 import puzzle_data, example_data


def get_rules(data, include_numbers=False):
    rules = data.split('\n')
    rules_dict = {}
    for rule in rules:
        rule_split = rule.split(' contain ')
        things_contained = []
        for split in rule_split[1].split(', '):
            if not include_numbers:
                things_contained.append(split.replace(' bags', '').replace(' bag', '').replace('.', '')[2:])
            else:
                things_contained.append(split.replace(' bags', '').replace(' bag', '').replace('.', ''))
        rules_dict[rule_split[0]] = things_contained
    return rules_dict


def count_bags_that_contain(data, bag_type):
    rules_dict = get_rules(data)
    return len(bags_that_contain(rules_dict, bag_type, first_time=True))


def bags_that_contain(rules_dict, bag_type, first_time=False):
    bags_that_contain_bag_type = []
    for bag in rules_dict:
        if bag_type in rules_dict[bag] and bag.replace(' bags', '') != bag_type:
            bags_that_contain_bag_type.append(bag.replace(' bags', ''))
            bags_that_contain_bag_type += bags_that_contain(rules_dict, bag.replace(' bags', ''))
    if first_time:
        return set(bags_that_contain_bag_type)
    return bags_that_contain_bag_type


def count_required_bags(data, bag_type):
    rules_dict = get_rules(data, include_numbers=True)
    return bags_required(rules_dict, bag_type)


def bags_required(rules_dict, bag_type):
    bag_count = 0
    rules = rules_dict[bag_type + ' bags']
    for sub_bag in rules:
        if sub_bag == 'no other':
            return bag_count
        bag_count += int(sub_bag[:2])
        contained_bags = bags_required(rules_dict, sub_bag[2:])
        if contained_bags > 0:
            bag_count += int(sub_bag[:2]) * contained_bags
    return bag_count


def main():
    do_puzzle = True
    data = puzzle_data if do_puzzle else example_data
    answer = count_bags_that_contain(data, 'shiny gold')
    print(f'The answer to part 1 is: {answer}')
    answer = count_required_bags(data, 'shiny gold')
    print(f'The answer to part 2 is: {answer}')


if __name__ == "__main__":
    main()
