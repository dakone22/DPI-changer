# DPI-changer

Just a small console script on *Python 3* to change the images DPI (without resizing).

## Install

You need *Python **3.6+***.

### Windows

1. Clone/Download project.
2. Create *venv*:
   ```
   python -m venv venv
   ```
3. Run `install.bat`.
4. *(optional)* Customize `config.ini`.

### Linux/Mac OS

> Sorry, but **install**/**run** scripts not supported for those OS. 
> You can install the project manually if you know how to do it.
> And you can open pull request to add scripts for those OS.

## Usage

0. *(optional)* Customize `config.ini`:
   1. `WidthDPI` and `HeightDPI` (*default: `(300, 300)`*) is DPI for new images.
   2. `InputDir` (*default: `IMAGES`*) is folder for input images.
   3. `SeparateOutput` (*default: `True`*): output new files to a separate folder.
      **If is `False` then new images will be override input images!**
   4. `SeparateOutputDir` (*default: `OUTPUT`*) is folder for output images, if `SeparateOutput` is `True`.
1. Drop your files into input folder (*default: `IMAGES`*)
2. Run *run-script*:
   - For *Windows* `run.bat`
3. Take out your new images from
   - output folder, if `SeparateOutput` is `True`;
   - input folder, if `SeparateOutput` is `False`;

## Bugs, issues, contribution and etc.

You can open issues or pull requests if you found a bug or want to fix/modify something.