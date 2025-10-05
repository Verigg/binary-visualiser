import math
import argparse
from pathlib import Path
from PIL import Image, ImageDraw

def get_binary(file_path):
    with open(file_path, 'rb') as file:
        raw_bytes = file.read()
    bytes_list = list(raw_bytes)
    return bytes_list

def get_byte_pairs(bytes_list):
    pairs = []
    for i in range(len(bytes_list) - 1):
        pairs.append((bytes_list[i], bytes_list[i + 1]))
    return pairs

def create_byte_distribution_plot(byte_pairs, input_file):
    width, height = 256, 256
    image = Image.new('RGB', (width, height), 'Black')
    draw = ImageDraw.Draw(image)
    
    pair_counter = {}
    for pair in byte_pairs:
        pair_counter[pair] = pair_counter.get(pair, 0) + 1
    
    if not pair_counter:
        print("Not enough data for graph.")
        return
    
    max_frequency = max(pair_counter.values())
    
    for (x, y), frequency in pair_counter.items():
        log_frequency = math.log(frequency + 1)
        log_max = math.log(max_frequency + 1)
        normalized = log_frequency / log_max 
        intensity = int(255 * normalized)
        color = (intensity, intensity, intensity)        
        draw.point((x, y), fill=color)

    image.save(input_file + ".binvis.png")

def main():
    parser = argparse.ArgumentParser(description='Binary visualiser')
    parser.add_argument('input', nargs='+', help='Input files') 
    args = parser.parse_args()

    for input_file in args.input:
        if not Path(input_file).exists():
            print(f"Error: file {input_file} not found")
            continue
        
        bytes = get_binary(input_file)
        byte_pairs = get_byte_pairs(bytes)
        create_byte_distribution_plot(byte_pairs, input_file)

        print(f"Processed: {input_file}")

if __name__ == "__main__":
    main()