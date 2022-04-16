import time
import os
from os import path
import joblib
from AckleyProblem import Ackley
from BoothProblem import Booth
from BukinN6Problem import BukinN6
from BealeProblem import Beale
from GoldsteinPriceProblem import GoldsteinPrice

start = None
end = None

def printTimer(message):
    global start
    global end
    if start == None:
        start = time.time()
        print(message)
        return
    else:
        end = time.time()
        print(message+' {}'.format(end-start))
        start = end   

printTimer("Starting optuna import")
import optuna
printTimer("optuna import done")

def objective(trial, problem):
    x = trial.suggest_float("x", problem.xmin(), problem.xmax())
    y = trial.suggest_float("y", problem.ymin(), problem.ymax())
    return problem.eval(x, y)

def optuna_search(problem):
    save_results_to = os.path.dirname(os.path.abspath(__file__)) + '/pickels/'
    if not os.path.exists(save_results_to):
        os.makedirs(save_results_to)

    filename = save_results_to + problem.name()+"_study.pkl"

    study = None

    if path.exists(filename):
        study = joblib.load(filename)
        print("Study loaded.")
    else:
        study = optuna.create_study(direction=problem.direction(), sampler=optuna.samplers.CmaEsSampler(restart_strategy="ipop",))
        print("Study created.")

    for x in range(1):
        study.optimize(lambda trial: objective(trial, problem), n_trials=1000)
        joblib.dump(study, filename)
        print("Study saved.")

    # joblib.dump(study, filename)
    print("Optuna search done...")
    print("Best trial:")
    print(study.best_trial)
    print("Best params:")
    print(study.best_params)
    print("Best value:")
    print(study.best_value)

list = [] 

# list.append( Ackley() )
# list.append( Booth() )
# list.append( BukinN6() )
# list.append( Beale() )
list.append( GoldsteinPrice() )
  
for problem in list:
    problem.draw()

for problem in list:
    optuna_search(problem)