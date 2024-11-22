#!/bin/python3
import struct
import json
import argparse

class Assembler:
    def __init__(self, input_file, output_file, log_file):
        self.input_file = input_file
        self.output_file = output_file
        self.log_file = log_file
        self.commands = []

    def assemble(self):
        with open(self.input_file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line.startswith("LOAD_CONST"):
                _, a, b = line.split()
                opcode = 0x45
                a = int(a)
                b = int(b)
                command = struct.pack("B", opcode) + struct.pack("<I", b)
                self.commands.append({"opcode": "LOAD_CONST", "A": a, "B": b, "binary": command.hex()})
            elif line.startswith("LOAD_MEM"):
                _, a, b = line.split()
                opcode = 0x4F
                a = int(a)
                b = int(b)
                command = struct.pack("B", opcode) + struct.pack("<I", b)
                self.commands.append({"opcode": "LOAD_MEM", "A": a, "B": b, "binary": command.hex()})
            elif line.startswith("WRITE_MEM"):
                _, a, b = line.split()
                opcode = 0x3C
                a = int(a)
                b = int(b)
                command = struct.pack("B", opcode) + struct.pack("<I", b)
                self.commands.append({"opcode": "WRITE_MEM", "A": a, "B": b, "binary": command.hex()})
            elif line.startswith("MUL"):
                _, a, b = line.split()
                opcode = 0xAB
                a = int(a)
                b = int(b)
                command = struct.pack("B", opcode) + struct.pack("<I", b)
                self.commands.append({"opcode": "MUL", "A": a, "B": b, "binary": command.hex()})
            else:
                raise ValueError(f"Unknown command: {line}")

        # Запись в бинарный файл
        with open(self.output_file, 'wb') as file:
            for command in self.commands:
                file.write(bytes.fromhex(command["binary"]))

        # Запись лога в JSON файл
        with open(self.log_file, 'w') as log:
            json.dump(self.commands, log, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Assembler for UVM")
    parser.add_argument("--input", required=True, help="Path to input assembly file")
    parser.add_argument("--output", required=True, help="Path to output binary file")
    parser.add_argument("--log", required=True, help="Path to log file in JSON format")
    args = parser.parse_args()

    assembler = Assembler(args.input, args.output, args.log)
    assembler.assemble()

if __name__ == "__main__":
    main()

