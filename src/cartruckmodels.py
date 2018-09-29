import os
import numpy as np
from collections import OrderedDict
import sys
import MNMAPI
# change this folder to include the MNM_mcnb.py
sys.path.append("/home/alanpi/Desktop/MAC-POSTS/side_project/network_builder")
from MNM_mcnb import *
import pickle


''' Implementation of car-truck simulator '''
class Cartruck_Simulator():
    def __init__(self, nb):
        print "Init simulation"
        self.num_assign_interval = nb.config.config_dict['DTA']['max_interval']
        self.nb = nb
        self.dta = MNMAPI.mcdta_api()

    def run_simulation(self, data_folder, link_ID_list):
        self.dta.initialize(data_folder)
        self.dta.register_links(link_ID_list)
        self.dta.run_whole()

    def print_out_overall_stats(self):
        self.dta.print_emission_stats()

    def get_enroute_and_queue_veh_stats_agg(self):
        return self.dta.get_enroute_and_queue_veh_stats_agg()

    def get_queue_veh_each_link(self, useful_links, intervals):
        return self.dta.get_queue_veh_each_link(useful_links, intervals)

    def get_link_car_count(self, start_intervals, end_intervals):
        return self.dta.get_link_car_inflow(start_intervals, end_intervals)

    def get_link_truck_count(self, start_intervals, end_intervals):
        return self.dta.get_link_truck_inflow(start_intervals, end_intervals)

    def get_link_car_speed(self, start_intervals):
        return self.dta.get_car_link_speed(start_intervals)

    def get_link_truck_speed(self, start_intervals):
        return self.dta.get_truck_link_speed(start_intervals)

    def get_link_car_tt(self, start_intervals):
        return self.dta.get_car_link_tt(start_intervals) * 5  # seconds

    def get_link_truck_tt(self, start_intervals):
        return self.dta.get_truck_link_tt(start_intervals) * 5 # seconds

    def get_waiting_time_at_intersections(self):
        return self.dta.get_waiting_time_at_intersections()

    def get_link_spillback(self):
        return self.dta.get_link_spillback()

    def get_path_tt_car(self, path_links, start_intervals):
        return self.dta.get_path_tt_car(path_links, start_intervals)
    
    def get_path_tt_truck(self, path_links, start_intervals):
        return self.dta.get_path_tt_truck(path_links, start_intervals)