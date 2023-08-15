#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------
%   File: Circuits_generator.py
%   Description: This script generates rendered circuit assemblies
%                for the ElectroLab based on a YAML file with the
%                connections defined.
%   Author: J.G.Aguado
%   Email: jon-garcia@hotmail.com
%   Date of creation: 27/04/2023
------------------------------------------------------------
"""
import os
import numpy as np
import pandas as pd
import yaml
import cv2
import cairo
import math
import shutil

import matplotlib.colors as colors

left_clicks = list()


class ElectroLab():
    def __init__(self, board, circuits_path):
        super().__init__()
        with open(board, 'r', encoding='utf8') as config:
            try:
                self.config = yaml.safe_load(config)
            except yaml.YAMLError as exc:
                print(exc)
        # self.board_mapping(board)
        self.main(circuits_path)

    def main(self, circuits_path):
        for file in os.listdir(circuits_path):
            if file.endswith('.xlsx'):
                self.circuit = pd.read_excel(circuits_path + '\\' + file)
                name = file.split('.')[0]
                self.render_circuit(name)
                self.generate_html(name)
            else:
                continue

    def render_circuit(self, name):
        """ Load config of the circuit in excel file """

        output_path = self.config['output_path'] + name
        isExist = os.path.exists(output_path)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(output_path)

        # Create a surface and a context

        board = cairo.ImageSurface.create_from_png(self.config['image'])
        imagesize = (board.get_width(), board.get_height())


        k = 0.2
        if 'd' in self.circuit.columns:
            k = self.circuit['d'][0]

        jj = 0
        for ii, row in self.circuit.iterrows():

            surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, *imagesize)
            context = cairo.Context(surface)

            # Color selection
            color = self.config['colors'][jj]
            jj += 1

            if jj > len(self.config['colors'])-1:
                jj = 0
            # Import the points
            p1 = self.config['mapping'][row[0]]
            p2 = self.config['mapping'][row[1]]


            # Calculate the control points
            # Calculate the distance between p1 and p2
            dist = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
            angle_1 = 45
            angle_2 = 135
            d = k * dist

            l1_angle = math.degrees(math.atan2(p2[1] - p1[1], p2[0] - p1[0]))

            p3_x = p1[0] + d * math.cos(math.radians(l1_angle + angle_1))
            p3_y = p1[1] + d * math.sin(math.radians(l1_angle + angle_1))
            cp2 = (p3_x, p3_y)

            p3_x = p2[0] + d * math.cos(math.radians(l1_angle + angle_2))
            p3_y = p2[1] + d * math.sin(math.radians(l1_angle + angle_2))
            cp3 = (p3_x, p3_y)

            # Draw the Bezier curve
            context.set_source_rgb(*color)  # Green color
            context.move_to(*p1)
            context.curve_to(*cp2, *cp3, *p2)
            context.set_line_width(10)
            context.stroke()

            # Draw the circles
            context.set_source_rgb(1, 0, 0)  # Red color
            context.arc(p1[0], p1[1], 10, 0, 2 * math.pi)
            context.fill()
            context.set_source_rgb(1, 0, 0)  # Blue color
            context.arc(p2[0], p2[1], 10, 0, 2 * math.pi)
            context.fill()

            surface.write_to_png(output_path + '\\' + str(ii+1) + '.png')
            # Save the image
        # output = circuit.replace('.xlsx', '.png')
        # surface.write_to_png(output)

    def generate_html(self, name):
        output_path = self.config['output_path'] + name

        shutil.copyfile("Template.html", output_path + '\\' + "Circuit.html")
        shutil.copyfile(self.config['image'], output_path + '\\' + "0.png")

        self.generate_js_file(self.circuit, output_path + '\\data.js')

    def generate_js_file(self, dataframe, js_filename):
        with open(js_filename, "w") as js_file:
            js_file.write("const curvesData = [\n")

            for index, row in dataframe.iterrows():
                from_value = row["From"]
                to_value = row["To"]
                js_item = f'  {{"from": "{from_value}", "to": "{to_value}"}},\n'
                js_file.write(js_item)

            js_file.write("];")

    def board_mapping(self, board):
        self.image = cv2.imread(self.config['image'])
        self.pinout = {}
        for item, value in self.config['mapping'].items():
            self.pinout[item] = {}
            for i in range(1, value + 1):
                self.pinout[item]["{}{}".format(item, i)] = None

        self.selected_item = None
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.assign_coordinate)
        self.run_mapping()

        self.config['pinout'] = {}
        for key, value in self.pinout.items():
            for pin, coords_list in value.items():
                if coords_list:
                    self.config['pinout'].update({pin: list(coords_list)})
        with open(board, 'w') as yaml_file:
            yaml.safe_dump(self.config, yaml_file, default_flow_style=False, sort_keys=False)

    def assign_coordinate(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            for item, subsets in self.pinout.items():
                for subset, coordinate in subsets.items():
                    if coordinate is None:
                        subsets[subset] = (x, y)
                        self.selected_item = subset
                        return
        elif event == cv2.EVENT_RBUTTONDOWN:
            print(self.pinout)

    def run_mapping(self):
        while True:
            img_with_text = self.image.copy()
            if self.selected_item is not None:
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 1
                thickness = 2
                text = self.selected_item
                text_size = cv2.getTextSize(text, font, font_scale, thickness)
                text_x = int((self.image.shape[1] - text_size[0][0]) / 2)
                text_y = int((self.image.shape[0] + text_size[0][1]) / 2)
                cv2.putText(img_with_text, text, (text_x, text_y), font, font_scale, (0, 0, 255), thickness)
            cv2.imshow("image", img_with_text)
            if cv2.waitKey(1) == ord('q'):
                break

        cv2.destroyAllWindows()






if __name__ == "__main__":

    circuits_path = '0_Circuits'
    board= 'ElectroLab_R2.yaml'

    ElectroLab(board, circuits_path)

