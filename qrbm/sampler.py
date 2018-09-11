from dwave.system.samplers import DWaveSampler  # Library to interact with the QPU
from dwave.system.composites import FixedEmbeddingComposite  # Library to embed our problem onto the QPU physical graph
from dimod.binary_quadratic_model import BinaryQuadraticModel
import minorminer
import numpy as np


class Sampler(object):
    """
    This module defines a sampler.
    :param num_samps: number of samples
    :type num_samps: int
    """

    def __init__(self, num_copies=1):
        self.endpoint = 'YOUR URL'
        self.token = 'YOUR TOKEN'
        self.solver = 'YOUR SOLVER'
        self.gamma = 1400
        self.chainstrength = 4700
        self.num_copies = num_copies
        self.child = DWaveSampler(endpoint=self.endpoint, token=self.token, solver=self.solver)

    def sample_qubo(self, Q, num_samps=100):
        """
        Sample from the QUBO problem
        :param qubo: QUBO problem
        :type qubo: numpy dictionary
        :return: samples, energy, num_occurrences
        """
        self.num_samps = num_samps

        if not hasattr(self, 'sampler'):

            bqm = BinaryQuadraticModel.from_qubo(Q)

            # apply the embedding to the given problem to map it to the child sampler
            __, target_edgelist, target_adjacency = self.child.structure

            # add self-loops to edgelist to handle singleton variables
            source_edgelist = list(bqm.quadratic) + [(v, v) for v in bqm.linear]

            # get the embedding
            embedding = minorminer.find_embedding(source_edgelist, target_edgelist)

            if bqm and not embedding:
                raise ValueError("no embedding found")

            self.sampler = FixedEmbeddingComposite(self.child, embedding)

        response = self.sampler.sample_qubo(Q, chain_strength=self.chainstrength, num_reads=self.num_samps)

        return np.array(response.__dict__['_samples_matrix'].tolist()), response.__dict__['_data_vectors']["energy"], \
               response.__dict__['_data_vectors']["num_occurrences"]
