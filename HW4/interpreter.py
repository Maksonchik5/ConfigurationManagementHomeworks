#!/bin/python3
import struct
import json
import argparse

class VirtualMachine:
    def __init__(self, binary_file, result_file, memory_range):
        self.binary_file = binary_file
        self.result_file = result_file
        self.memory = [0] * 1024  # Память УВМ (условная память на 1024 ячейки)
        self.accumulator = 0
        self.memory_range = memory_range

    def execute(self):
        with open(self.binary_file, 'rb') as file:
            while True:
                opcode = file.read(1)
                if not opcode:
                    break

                opcode = struct.unpack("B", opcode)[0]
                if opcode == 0x45:  # LOAD_CONST
                    value = struct.unpack("<I", file.read(4))[0]
                    self.accumulator = value
                elif opcode == 0x4F:  # LOAD_MEM
                    offset = struct.unpack("<I", file.read(4))[0]
                    address = self.accumulator + offset
                    if address < len(self.memory):
                        self.accumulator = self.memory[address]
                    else:
                        raise IndexError("Memory access out of range")
                elif opcode == 0x3C:  # WRITE_MEM
                    address = struct.unpack("<I", file.read(4))[0]
                    if address < len(self.memory):
                        self.memory[address] = self.accumulator
                    else:
                        raise IndexError("Memory access out of range")
                elif opcode == 0xAB:  # MUL
                    address = struct.unpack("<I", file.read(4))[0]
                    if address < len(self.memory):
                        self.accumulator *= self.memory[address]
                    else:
                        raise IndexError("Memory access out of range")
                else:
                    raise ValueError(f"Unknown opcode: {opcode}")

        # Запись диапазона памяти в результат
        memory_snapshot = {i: self.memory[i] for i in range(self.memory_range[0], self.memory_range[1] + 1)}
        with open(self.result_file, 'w') as result:
            json.dump(memory_snapshot, result, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Interpreter for UVM")
    parser.add_argument("--binary", required=True, help="Path to binary file")
    parser.add_argument("--result", required=True, help="Path to result JSON file")
    parser.add_argument("--range", required=True, help="Memory range to dump (e.g., 0-100)")
    args = parser.parse_args()

    memory_range = list(map(int, args.range.split("-")))
    vm = VirtualMachine(args.binary, args.result, memory_range)
    vm.execute()

if __name__ == "__main__":
    main()

