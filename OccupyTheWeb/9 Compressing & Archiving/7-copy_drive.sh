#!/bin/bash

# Make a physical, bit-by-bit copy of one
# of your flash drives using the dd command.

dd if=/path/to/drive of=/new/drive/path bs=4096 conv:noerror
