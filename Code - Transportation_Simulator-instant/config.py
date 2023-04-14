env_params = {
't_initial' :10800,   # 3-9
't_end' : 32400,
'delta_t' : 60,  # s
'vehicle_speed' : 22.788,   # km / h
'repo_speed' :22.788, #目前的设定需要与vehicl speed保持一致
'order_sample_ratio' : 1,
'order_generation_mode' : 'sample_from_base',
'driver_sample_ratio' : 1,
'maximum_wait_time_mean' : 300,
'maximum_wait_time_std' : 0,
"maximum_pickup_time_passenger_can_tolerate_mean":float('inf'),  # s
"maximum_pickup_time_passenger_can_tolerate_std":0, # s
"maximum_price_passenger_can_tolerate_mean":float('inf'), # ￥
"maximum_price_passenger_can_tolerate_std":0,  # ￥
'maximal_pickup_distance' : 1,  # km
'request_interval': 60,  #
'cruise_flag' :True,
'delivery_mode':'rg',
'pickup_mode':'rg',
'max_idle_time' : 300,  # 1s and 300s
'cruise_mode': 'nearby',   # modify
'reposition_flag': False,
'eligible_time_for_reposition' : 300, # s
'reposition_mode': '',
'track_recording_flag' : False,
'driver_far_matching_cancel_prob_file' : 'driver_far_matching_cancel_prob',
'request_file_name' : 'input1/order-11-13-frac=0.1', #'toy_requests',
'driver_file_name' : 'input1/driver_distribution_3am-4am',
'road_network_file_name' : 'road_network_information.pickle',
'dispatch_method': 'LD', #LD: lagarange decomposition method designed by Peibo Duan
# 'method': 'instant_reward_no_subway',
'simulator_mode' : 'toy_mode',
'experiment_mode' : 'test',
'driver_num':100,
'side':10,
'price_per_km':5,  # ￥ / km
'road_information_mode':'load',
'north_lat': 40.8845,
'south_lat': 40.6968,
'east_lng': -74.0831,
'west_lng': -73.8414,
'rl_mode': 'matching',  # reposition and matching
'method': 'sarsa_no_subway',  #  'sarsa_no_subway' / 'pickup_distance' / 'instant_reward_no_subway'   #  rl for matching
'reposition_method': 'A2C_global_aware',  # A2C, A2C_global_aware, random_cruise, stay  # rl for repositioning
}

#  rl for matching
# global variable and parameters for sarsa
START_TIMESTAMP = 10800  # the start timestamp
LEN_TIME_SLICE = 300  # the length of a time slice, 5 minute (300 seconds) in this experiment
LEN_TIME = 6 * 60 * 60 # 3 hours
NUM_EPOCH = 4001  # 4001 / 3001
FLAG_LOAD = False
sarsa_params = dict(learning_rate=0.005, discount_rate=0.95)  # parameters in sarsa algorithm
#  rl for matching

# rl for repositioning
# hyperparameters for rl
# NUM_EPOCH = 1301
STOP_EPOCH = 1300
DISCOUNT_FACTOR = 0.95
ACTOR_LR = 0.001
CRITIC_LR = 0.005
ACTOR_STRUCTURE = [64,128] #[16, 32] for A2C, and [64, 128] for A2C global aware
CRITIC_STRUCTURE = [64,128]
# rl for repositioning


#  rl for matching
# parameters for exploration
INIT_EPSILON = 0.9
FINAL_EPSILON = 0
DECAY = 0.997
PRE_STEP = 0
#  rl for matching

#  rl for matching
# TRAIN_DATE_LIST = ['2015-07-06', '2015-07-07', '2015-07-08', '2015-07-09', '2015-07-10',
#                    '2015-07-13', '2015-07-14', '2015-07-15', '2015-07-16', '2015-07-17'
#                    ]
TRAIN_DATE_LIST = ['2015-05-04','2015-05-05','2015-05-06','2015-05-07','2015-05-08',]

TEST_DATE_LIST = ['2015-05-11', '2015-05-12', '2015-05-13', '2015-05-14', '2015-05-15']
#  rl for matching