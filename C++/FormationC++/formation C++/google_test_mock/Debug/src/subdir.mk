################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../src/Hello.cpp 

OBJS += \
./src/Hello.o 

CPP_DEPS += \
./src/Hello.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: Cygwin C++ Compiler'
	g++ -std=gnu++1y -I"C:\Users\ftourlon\Documents\5G_corner\Environnement\workspace\google_test_mock\gtest_src" -I"C:\Users\ftourlon\Documents\5G_corner\Environnement\workspace\google_test_mock\src" -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


