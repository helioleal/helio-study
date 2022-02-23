#!/bin/bash

# This program calls a function with two parameters.

function_with_two_parameters()
{
    parameter1=$1
    parameter2=$2

    echo "Parameter 1: ${parameter1}"
    echo "Parameter 2: ${parameter2}"
}

# Below we call the function and pass two parameters.
function_with_two_parameters "My name is Helio" "My wife is Julina"


