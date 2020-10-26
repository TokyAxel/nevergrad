# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# Based on https://github.com/Foloso/MixSimulator/tree/nevergrad_experiment

import numpy as np
from ..base import ExperimentFunction
from mixsimulator.MixSimulator import MixSimulator  #type: ignore


class OptimizeMix(ExperimentFunction):
    """
        MixSimulator is an application with an optimization model for calculating 
        and simulating the least cost of an energy mix under certain constraints.
        
        For now, it uses a default dataset (more will be added soon).
        
        For more information, visit : https://github.com/Foloso/MixSimulator     
        
        Parameters
        ----------
        time: int
            total time over which it evaluates the mix (must be in hour)
                
    """
    def __init__(self,time: int = 168) -> None:
        self.__mix = MixSimulator()
        self.__mix.set_data_to("Toamasina")
        self.__mix.set_penalisation_cost(100)
        self.__mix.set_carbon_cost(10)
        parameters = self.__mix.get_opt_params(time)
        parameters.set_name("dims")
        super().__init__(self._simulate_mix , parameters)
        self.register_initialization(time=time)
        self.add_descriptors(time=time)

    def _simulate_mix(self, x: np.ndarray) -> float:
        return self.__mix.loss_function(x)
    
