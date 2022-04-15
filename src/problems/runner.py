import time
from os import path


import joblib

from AckleyProblem import Ackley

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

def objective(trial):
    problem = Ackley()
    x = trial.suggest_float("x",-32.768, 32.768)
    y = trial.suggest_float("y",-32.768, 32.768)
    return problem.eval(x, y)

def optuna_search():
    """A function to start the search."""
    filename = "RandomForestClassifier_study.pkl"

    study = None

    if path.exists(filename):
        study = joblib.load(filename)
        print("Study loaded.")
    else:
        study = optuna.create_study(direction="minimize", sampler=optuna.samplers.CmaEsSampler())
        print("Study created.")

    for x in range(1):
        study.optimize(objective, n_trials=100)
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


# printTimer("Starting")
# p1 = Ackley()
# printTimer("AckleyCreated")
# p1.draw()
# printTimer("Done")

# print(p1.objective(1,1))
print("test")

optuna_search()