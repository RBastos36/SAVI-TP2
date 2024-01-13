#!/usr/bin/env python3

import tkinter as tk
from PointCloud_Learning.dataset_splitter_off import splitDataset


def buttonSplitDataset():
    splitDataset()

def buttonContinueTrain():
    print('start train from checkpoint')

def buttonNewTrain():
    print('start train from 0')

def buttonTestModel():
    print('test model')


def main():

    window = tk.Tk()
    window.title("SAVI - Trabalho 2")
    window.resizable(width=False, height=False)

    button_frame = tk.Frame(window)
    button_frame.pack(side=tk.LEFT, padx=10)

    label = tk.Label(button_frame, text="Train Model", anchor="w", justify="left")
    label.pack()

    button = tk.Button(button_frame, text="Split Dataset", command=buttonSplitDataset, width=15)
    button.pack(pady=5)

    button = tk.Button(button_frame, text="Continue Train", command=buttonContinueTrain, width=15)
    button.pack(pady=5)

    button = tk.Button(button_frame, text="New Train", command=buttonNewTrain, width=15)
    button.pack(pady=5)

    button = tk.Button(button_frame, text="Test Model", command=buttonTestModel, width=15)
    button.pack(pady=5)

    text_area = tk.Text(window, height=10, width=30)
    text_area.insert(tk.END, 'Text\ngoes\nhere')
    text_area.pack(side=tk.RIGHT, padx=10, pady=10)
    # text_area.config(state=tk.DISABLED)     # read-only


    # Start the main loop
    window.mainloop()



if __name__ == '__main__':
    main()