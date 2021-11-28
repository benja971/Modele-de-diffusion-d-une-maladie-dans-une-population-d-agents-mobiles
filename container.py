from agent import Agent
from random import choice


class Container():
    """docstring for Container."""

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.agents = []
        self.healthys = []
        self.infecteds = []
        self.vaccinateds = []
        self.immunes = []

    def vaccine_people(self, agents, time):
        for agent in agents:
            agent.get_vaccinated(self.vaccinateds, time)
