# Binary Visualiser
A Python tool that creates visual representation of binary files by count byte pair frequencies. It generates 256x256 grayscale image where each pixel's intensity corresponds to how often specific byte pairs occur in the file.

Based on: 
 - https://www.youtube.com/watch?v=AUWxl0WdiNI
 - https://github.com/tsoding/binviz
 - https://www.youtube.com/watch?v=4bM3Gut1hIk

## Examples
### Executables
![exec1](examples\exec\exec1.exe.binvis.png)
![exec2](examples\exec\exec2.exe.binvis.png)
![exec3](examples\exec\exec3.exe.binvis.png)

### Images
![img1](examples\imgs\img1.jpg.binvis.png)
![img2](examples\imgs\img2.jpg.binvis.png)
![img3](examples\imgs\img3.png.binvis.png)
![img4](examples\imgs\img4.png.binvis.png)

### Wavs
![wav1](examples\wavs\wav1.wav.binvis.png)
![wav2](examples\wavs\wav2.wav.binvis.png)
![wav3](examples\wavs\wav3.wav.binvis.png)

## Installation

Clone or download the script
```console
$ git clone https://github.com/Verigg/binary-visualiser.git
$ cd binary-visualiser
```
Create virtual enviroment
```console
$ python -m venv venv
$ venv/scripts/activate
```
Install dependencies with
```console
$ pip install pillow
```
or
```console
$ pip install -r requirements.txt
```

## Usage

### Basic usage: 
```
python binary-visualiser.py <file1> [file2 ...]
```

### Output

For each input file, tool generates a PNG image with the same name plus `.binvis.png`.
 - document.pdf &rarr; document.pdf.binvis.png
 - image.png &rarr; image.png.binvis.png