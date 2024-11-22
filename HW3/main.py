#!/bin/python3
import re
import sys
import toml
from argparse import ArgumentParser


class ConfigParserError(Exception):
    """Ошибка синтаксического анализа."""


class ConfigParser:
    def __init__(self, source_file, output_file):
        self.source_file = source_file
        self.output_file = output_file
        self.constants = {}

    def parse(self):
        with open(self.source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        content = self.remove_multiline_comments(content)
        lines = content.splitlines()
        len_skip = 0
        config = {}
        for line in lines:
            if len_skip > 0:
                len_skip -= 1
                continue
            line = line.strip()
            if not line:
                continue
            if line.startswith("{") or re.match(r'^([a-zA-Z][a-zA-Z0-9_]*)\s*\=\s*{', line):
                dictionary = self.parse_dictionary(lines, lines.index(line))
                len_skip = len(dictionary)
                config.update(dictionary)
            elif "=" in line and not line.startswith("."):
                self.handle_constant_declaration(line)
            elif line.startswith("."):
                config.update(self.handle_constant_evaluation(line))
            #elif line.startswith("{") or re.match(r'^([a-zA-Z][a-zA-Z0-9_]*)\s*\=\s*{', line):
             #   dictionary = self.parse_dictionary(lines, lines.index(line))
              #  config.update(dictionary)
        return config

    def remove_multiline_comments(self, content):
        """Удаляет многострочные комментарии."""
        return re.sub(r'\|\#.*?\#\|', '', content, flags=re.DOTALL)

    def handle_constant_declaration(self, line):
        """Обрабатывает объявление константы."""
        match = re.match(r'^([a-z][a-zA-Z_]*)\s*=\s*(.+);?$', line)
        if not match:
            raise ConfigParserError(f"Ошибка в объявлении константы: {line}")
        name, value = match.groups()
        self.constants[name] = self.parse_value(value.strip(" ;"))

    def handle_constant_evaluation(self, line):
        """Обрабатывает вычисление констант."""
        match = re.match(r'^\.\[([a-zA-Z][a-zA-Z_]*)\]\.$', line)
        if not match:
            raise ConfigParserError(f"Ошибка в вычислении константы: {line}")
        name = match.group(1)
        if name not in self.constants:
            raise ConfigParserError(f"Неизвестная константа: {name}")
        return {name: self.constants[name]}

    def parse_dictionary(self, lines, start_index):
        """Парсит словарь."""
        dictionary = {}
        i = start_index + 1
        while i < len(lines):
            line = lines[i].strip()
            if line == "}" or line == "};":
                return dictionary
            match = re.match(r'^([a-z]+)\s*=\s*(.+);?$', line)
            if not match:
                raise ConfigParserError(f"Ошибка в словаре: {line}")
            name, value = match.groups()
            dictionary[name] = self.parse_value(value.strip(" ;"))
            i += 1
        raise ConfigParserError("Не закрыт словарь")

    def parse_value(self, value):
        """Парсит значение."""
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            return value[1:-1]  # Строка
        if value.isdigit():
            return int(value)  # Число
        if value[:-1].isdigit():
            return int(value[:-1])
        if re.match(r'\"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\"', value):
            return value.strip(" ;")[1:-1]
        if value == "true" or value == "false":
            return value
        if value.startswith("{") and value.endswith("}"):
            return self.parse_dictionary(value.splitlines(), 0)  # Вложенный словарь
        raise ConfigParserError(f"Неверное значение: {value}")

    def write_to_toml(self, config):
        """Записывает конфигурацию в TOML файл."""
        with open(self.output_file, 'w', encoding='utf-8') as f:
            toml.dump(self.constants, f)
            toml.dump(config, f)


def main():
    parser = ArgumentParser(description="Преобразует учебный конфигурационный язык в TOML.")
    parser.add_argument('--input', required=True, help="Путь к входному файлу.")
    parser.add_argument('--output', required=True, help="Путь к выходному TOML файлу.")
    args = parser.parse_args()

    try:
        parser = ConfigParser(args.input, args.output)
        config = parser.parse()
        parser.write_to_toml(config)
        print("Успешное преобразование.")
    except ConfigParserError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()

