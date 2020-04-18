################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../src/ChatDomestique.cpp \
../src/ChatSauvage.cpp \
../src/Felin.cpp \
../src/factorial.cpp 

OBJS += \
./src/ChatDomestique.o \
./src/ChatSauvage.o \
./src/Felin.o \
./src/factorial.o 

CPP_DEPS += \
./src/ChatDomestique.d \
./src/ChatSauvage.d \
./src/Felin.d \
./src/factorial.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: Cygwin C++ Compiler'
	g++ -std=gnu++1y -I"C:\Users\ftourlon\Documents\5G_corner\Environnement\workspace\unit_test_FTS\gtest_src" -I"C:\Users\ftourlon\Documents\5G_corner\Environnement\workspace\unit_test_FTS\src" -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


