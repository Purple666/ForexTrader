from gym.envs.registration import register
from copy import deepcopy

from . import datasets

register(
    id='forex-v1',
    entry_point='gym_forextrading.envs:MyForexEnv',
    kwargs={
        'df': deepcopy(datasets.FOREX_EURUSD_1H_2019Jan_Dec),
        'window_size': 24,
        'frame_bound': (24, len(datasets.FOREX_EURUSD_1H_2019Jan_Dec))
    }
)
