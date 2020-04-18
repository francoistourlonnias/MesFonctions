/*
 * factorial.cpp
 *
 *  Created on: 15 juin 2016
 *      Author: mmeinero
 */
#include <iostream>
#include <factorial.hpp>

int myFactor::factorial(int value)
{
    int result = 1;
    for (int i = 1; i <= value; i++) {
            result *= i;
     }
    return result;
}








