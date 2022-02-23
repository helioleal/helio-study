#!/bin/bash

# Author: Helio Leal
# This program goal is to learn how to use regex in shell script.

# Pattern variable defines that needs to start with prefix helio_ + 8 numbers
#
# ^ means that pattern needs to start with helio_
# [0-9] means that accepts only numbers
# {8} means that after underscore needs to have 8 numbers
pattern="^helio_[0-9]{8}"

# Define variables to test.
test_one="helio_19901127"
test_two="helio_leal"

# Test pattern with variable test_one
if [[ $test_one =~ $pattern ]]; then 
    echo "Content '${test_one}' matches pattern '${pattern}'"
else
    echo "Content '${test_one}' does not match pattern '${pattern}'"
fi

# Test pattern with variable test_two
if [[ $test_two =~ $pattern ]]; then 
    echo "Content '${test_two}' matches pattern '${pattern}'"
else
    echo "Content '${test_two}' does not match pattern '${pattern}'"
fi
