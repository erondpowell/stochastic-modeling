#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 12:48:27 2021

@author: EronDonevan
"""

import ps3b_working as simulations


# virus = simulations.SimpleVirus(1.0, 0.0)
# # virus = simulations.SimpleVirus(random.random(), random.random())
# patient = simulations.Patient([virus], 100)

# patient.getViruses()
# rnd = 0
# for i in range(10):
#     #rnd += 1
#     #print(rnd)
#     print(patient.getTotalPop())
#     patient.update()
    

#simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials)

# simulations.simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)


# virus = simulations.ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
#virus = simulations.ResistantVirus(1.0, 0.0, {"drug1":True, "drug2":False}, 0.0)
#virus = simulations.ResistantVirus(1.0, 0.0, {"drug2": True}, 1.0)

simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials)



def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    """
    if numTrials > 100:
        raise Exception('numTrials must be 100 or less')
    timesteps = 300 
        
    virus_pop_by_timestep = [] #This will be a list of lists. The nested lists are virus_count_of_patient_per_timestep
    resistant_virus_pop_by_timestep = []
    for trial in numTrials:
        viruses_in_patient = []
        for virus in range(numViruses):
            viruses_in_patient.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        
        patient = TreatedPatient(viruses_in_patient, maxPop)
        
        for i in range(timesteps):
            if i == 150:
                patient.addPrescription('guttagonol') 
            patient.update()
            virus_pop_by_timestep[i] += patient.getTotalPop()
            resistant_virus_pop_by_timestep[i] += patient.getResistPop('guttagonol')
    
    avg_pop_per_timestep = [i/len(numTrials) for i in virus_pop_by_timestep]
    avg_resistant_pop_per_timestep = [i/len(numTrials) for i in resistant_virus_pop_by_timestep]
    
    pylab.plot(range(timesteps), avg_pop_per_timestep, label = "Avg. Total Pop")
    pylab.plot(range(timesteps), avg_resistant_pop_per_timestep, label = "Avg. Resistant Pop")

    pylab.title("TreatedVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()