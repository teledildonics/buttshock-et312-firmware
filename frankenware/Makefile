# Makefile for Buttshock / et312 frankenware
###############################################################################

## General Flags
ifndef MCU
	MCU = atmega16
endif

REVISION = 16
PROJECT = buttshock_et312_r$(REVISION)_$(MCU)
BRAIN = ../firmware/312-$(REVISION)-decrypted-combined
FRANKENWARE = frankenbutt
TARGET = $(PROJECT).elf
CC = avr-gcc
SRCDIR = src
OBJDIR = obj

## Options common to compile, link and assembly rules
COMMON = -mmcu=$(MCU) -Os
COMMON += -fshort-enums -mcall-prologues

## Compile options common for all C compilation units.
CFLAGS += $(COMMON)
#CFLAGS += -Wall -Wfatal-errors -std=gnu99 -g -Wshadow
CFLAGS += -Wall -Wfatal-errors -std=c99 -g -Wshadow
CFLAGS += -pedantic
CFLAGS += -Wundef -Werror
CFLAGS += -MD -MP -MT $(*F).o
CFLAGS += -fdata-sections -ffunction-sections
CFLAGS += -ffreestanding
CFLAGS += -mrelax
CFLAGS += -ggdb
CFLAGS += -flto -fwhole-program

APPLICATION_ADDRESS = 0x2000

## Linker flags
LDFLAGS = $(COMMON)
LDFLAGS += -Wl,-Map=$(PROJECT).map
# Relocate code section
LDFLAGS += -Wl,--section-start -Wl,.text=$(APPLICATION_ADDRESS)
LDFLAGS += -Wl,--warn-section-align
LDFLAGS += -Wl,--relax
LDFLAGS += -nostartfiles

C_FILES = $(shell find $(SRCDIR) -name "*.c")
C_FILES := $(filter-out $(TEST_SOURCES), $(C_FILES))

OBJECTS = $(patsubst $(SRCDIR)/%.c, $(OBJDIR)/%_$(MCU).o, $(C_FILES))
OBJECTS += $(patsubst $(SRCDIR)/%.S, $(OBJDIR)/%_$(MCU).o, $(S_FILES))

## Objects explicitly added by the user
LINKONLYOBJECTS = 

## Build
all: $(TARGET) $(PROJECT).hex $(PROJECT).bin $(PROJECT).lss $(PROJECT).lst
	dd if=$(BRAIN).bin of=$(FRANKENWARE).bin bs=8192 count=1
	dd if=$(PROJECT).bin of=$(FRANKENWARE).bin seek=8192 bs=1
	dd if=/dev/zero of=$(FRANKENWARE).bin bs=1 count=0 seek=15872
	dd if=$(BRAIN).bin of=$(FRANKENWARE).bin bs=1 skip=15872 seek=15872
	xxd -ps $(FRANKENWARE).bin | sed 's/0c942a00/0c940010/g' | xxd -ps -r > $(FRANKENWARE)2.bin
	mv $(FRANKENWARE)2.bin $(FRANKENWARE).bin
	avr-objcopy -I binary -O ihex $(FRANKENWARE).bin $(FRANKENWARE).hex

$(OBJDIR)/%_$(MCU).o: $(SRCDIR)/%.c
	@mkdir -p $(shell dirname $@)
	$(CC) $(CFLAGS) -c -o $@ $<

## Linking / hex
$(TARGET): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) $(LINKONLYOBJECTS) $(LIBDIRS) $(LIBS) -o $(TARGET)
	avr-size $(TARGET)

## Intel Hex file production flags
# filter out these sections from the elf file with -R
HEX_FLASH_FLAGS = -R .eeprom -R .fuse -R .lock -R .signature

%.hex: $(TARGET)
	avr-objcopy -O ihex $(HEX_FLASH_FLAGS)  $< $@

%.lst : %.elf
	avr-objdump -S -D -z --show-raw-insn $< > $@

%.bin: $(TARGET)
	-avr-objcopy -I ihex -O binary $(PROJECT).hex $(PROJECT).bin

%.lss: $(TARGET)
	avr-objdump -h -S $< > $@

## Clean target
.PHONY: clean
clean: distclean
	-rm -rf $(TARGET) $(PROJECT).hex $(PROJECT).bin $(PROJECT).lst $(FRANKENWARE).bin $(FRANKENWARE).hex

distclean:
	-rm -rf $(OBJECTS) $(PROJECT).lss $(PROJECT).map $(OBJDIR)

# Other dependencies
-include $(-shell find $(OBJDIR) -name "*.d")

