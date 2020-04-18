################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../test/gtest_main.cpp \
../test/test_Felin.cpp 

OBJS += \
./test/gtest_main.o \
./test/test_Felin.o 

CPP_DEPS += \
./test/gtest_main.d \
./test/test_Felin.d 


# Each subdirectory must supply rules for building sources it contributes
test/%.o: ../test/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: Cygwin C++ Compiler'
	g++ -std=gnu++1y -I"C:\Users\ftourlon\Documents\5G_corner\Environnement\workspace\unit_test_FTS\gtest_src" -I"C:\Users\ftourlon\Documents\5G_corner\Environnement\workspace\unit_test_FTS\src" -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


