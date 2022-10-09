import numpy as np
import pandas as pd
import time

from fasterrisk.fasterrisk import RiskScoreOptimizer, RiskScoreClassifier

def get_expected_answers():
    expected_logisticLosses = np.asarray([9798.652346518875, 9914.75974232043, 9859.615757931417, 9883.324461826953, 9895.728067750335, 9923.881690282931, 10004.826348100678, 9988.041001585896, 9980.639483585337, 10023.144780691362, 10000.803138904073, 10000.838406643863, 10030.439083768599, 10023.507653592056, 10027.26240920617, 10027.26240920617, 10024.816378572234, 10028.557714258925, 10035.510372611705, 10054.179137320903, 10045.516949571933, 10054.903429536253, 10064.52587881103, 10072.250543371647, 10082.486290745104, 10071.493061045443, 10057.369163995263, 10067.44943799388, 10067.922597085122, 10064.658255792961, 10066.98198453515, 10067.428679067445, 10064.912776396004, 10058.183697460874, 10073.921111400768, 10136.949587680912, 10156.006003703993, 10159.611021158398, 10184.96322485103, 10196.138801812713, 10261.125789923517, 10232.625475088009, 10229.435056996523, 10206.19527767557, 10232.08711343806, 10232.08711343806, 10258.249327857036, 10252.622156121819, 10226.013558258059, 10232.07439049685])
    expected_test_accs = np.asarray([0.8178746928746928, 0.8005221130221131, 0.8184889434889435, 0.8151105651105651, 0.8134213759213759, 0.8134213759213759, 0.8135749385749386, 0.8134213759213759, 0.8123464373464373, 0.8141891891891891, 0.8134213759213759, 0.8146498771498771, 0.8134213759213759, 0.8157248157248157, 0.8126535626535627, 0.8126535626535627, 0.8135749385749386, 0.8148034398034398, 0.812960687960688, 0.8128071253071253, 0.8131142506142506, 0.8134213759213759, 0.8134213759213759, 0.8134213759213759, 0.8134213759213759, 0.8134213759213759, 0.8134213759213759, 0.8134213759213759, 0.8134213759213759, 0.8134213759213759, 0.8134213759213759, 0.8134213759213759, 0.8140356265356266, 0.8144963144963145, 0.8144963144963145, 0.8144963144963145, 0.8144963144963145, 0.817414004914005, 0.8144963144963145, 0.8144963144963145, 0.8144963144963145, 0.8166461916461917, 0.8144963144963145, 0.8144963144963145, 0.8144963144963145, 0.8144963144963145, 0.8141891891891891, 0.8144963144963145, 0.8144963144963145, 0.8144963144963145])
    expected_test_aucs = np.asarray([0.8563665226703818, 0.8563965677626262, 0.8537520168739454, 0.854236947252862, 0.856064711948506, 0.8520139341885565, 0.8465119914236803, 0.849000035872804, 0.8494034430380665, 0.8505721582749558, 0.8481150006986778, 0.8516687393895173, 0.8499638099093635, 0.8477661797678163, 0.8505703452090445, 0.8505703452090445, 0.8461956761745139, 0.8463334044314179, 0.8496980662486513, 0.8465220927909003, 0.8454862493843668, 0.8486957645614769, 0.8449127377852131, 0.8449127377852131, 0.8480982298389984, 0.8449127377852131, 0.8457977729593392, 0.8449127377852131, 0.8449127377852131, 0.8449127377852131, 0.8449127377852131, 0.8449127377852131, 0.848706189690467, 0.8488617895970682, 0.8484641453913093, 0.8478423285360905, 0.8438468492864355, 0.8439950026723297, 0.8437872771207787, 0.8444376497641007, 0.8412959950539562, 0.8438715199332998, 0.8418599233047219, 0.8430658711451465, 0.8446141646810357, 0.8446141646810357, 0.8416119865413526, 0.8428930471123882, 0.8423596172203444, 0.8418487858998382])
    expected_multipliers = np.asarray([1.6009212957184902, 1.8083813115298006, 1.6302321077470971, 1.9506044001331857, 1.9070488740746325, 1.864929400026542, 1.4386742980497977, 1.3526381437087225, 1.2292289100530223, 1.8552853193785677, 1.3729023791599888, 1.6111475665340051, 1.9167899605602254, 1.5438481488974296, 1.699410438057984, 1.699410438057984, 1.4615021241505528, 1.4623624146457352, 1.5361305626364792, 1.5695203334630954, 1.4412022373512403, 1.5425789526415132, 1.4468977560887175, 1.4025213773343999, 1.4970902273817992, 1.4055697492135484, 1.4856219002834257, 1.531493235706423, 1.5344356525991238, 1.4455635806026785, 1.5284329020159226, 1.5313607497289834, 1.8263366152992284, 1.6462703201811821, 1.3855574211071695, 1.664789811454832, 1.480936829294527, 1.740490540475248, 1.697360438570229, 1.4339408776818425, 1.407510507523874, 1.4359335099545212, 1.8414886032504594, 1.690965299930628, 1.799631223751181, 1.799631223751181, 1.4882036355027979, 1.7728180338888297, 1.5996059147879733, 1.6009816442773879])
    return expected_logisticLosses, expected_test_accs, expected_test_aucs, expected_multipliers

def save_to_dict(int_sols_dict, multiplier, int_sol, train_acc, test_acc, train_auc, test_auc, logisticLoss):
    int_sols_dict["multipliers"].append(multiplier)
    int_sols_dict["int_sols"].append(int_sol)
    int_sols_dict["train_accs"].append(train_acc)
    int_sols_dict["test_accs"].append(test_acc)
    int_sols_dict["train_aucs"].append(train_auc)
    int_sols_dict["test_aucs"].append(test_auc)
    int_sols_dict["logisticLosses"].append(logisticLoss)

def test_check_solutions_interface():
    # import data
    train_data = np.asarray(pd.read_csv("tests/adult_train_data.csv"))
    X_train, y_train = train_data[:, 1:], train_data[:, 0]
    test_data = np.asarray(pd.read_csv("tests/adult_test_data.csv"))
    X_test, y_test = test_data[:, 1:], test_data[:, 0]
    
    
    lambda2 = 1e-8
    sparsity = 5
    sparseDiversePool_gap_tolerance = 0.05
    sparseDiversePool_select_top_m = 50
    parent_size = 10
    child_size = 10
    maxAttempts = 50
    num_ray_search = 20
    lineSearch_early_stop_tolerance = 0.001 
    
    # obtain sparse scoring systems
    int_sols_dict = {"int_sols": [], "train_accs": [], "test_accs": [], "train_aucs": [], "test_aucs": [], "logisticLosses": [], "multipliers": []}
    
    RiskScoreOptimizer_m = RiskScoreOptimizer(X = X_train, y = y_train, k = sparsity, select_top_m = sparseDiversePool_select_top_m, gap_tolerance = sparseDiversePool_gap_tolerance, parent_size = parent_size, maxAttempts = maxAttempts, num_ray_search = num_ray_search, lineSearch_early_stop_tolerance = lineSearch_early_stop_tolerance)

    start_time = time.time()
    
    RiskScoreOptimizer_m.optimize()
    
    int_sols_dict['run_time'] = time.time() - start_time

    multipliers, sparseDiversePool_beta0_integer, sparseDiversePool_betas_integer = RiskScoreOptimizer_m.get_models()

    for i in range(len(multipliers)):
        multiplier = multipliers[i]
        beta0_integer = sparseDiversePool_beta0_integer[i]
        betas_integer = sparseDiversePool_betas_integer[i]

        RiskScoreClassifier_m = RiskScoreClassifier(multiplier, beta0_integer, betas_integer)
        logisticLoss = RiskScoreClassifier_m.compute_logisticLoss(X_train, y_train)
        
        train_acc, train_auc = RiskScoreClassifier_m.get_acc_and_auc(X_train, y_train)
        test_acc, test_auc = RiskScoreClassifier_m.get_acc_and_auc(X_test, y_test)

        integer_sol = np.insert(betas_integer, 0, beta0_integer)
        save_to_dict(int_sols_dict, multiplier, integer_sol, train_acc, test_acc, train_auc, test_auc, logisticLoss)

    int_sols_dict["logisticLosses"] = np.asarray(int_sols_dict["logisticLosses"])
    int_sols_dict["test_accs"] = np.asarray(int_sols_dict["test_accs"])
    int_sols_dict["test_aucs"] = np.asarray(int_sols_dict["test_aucs"])
    int_sols_dict["multipliers"] = np.asarray(int_sols_dict["multipliers"])

    # check the answers
    expected_logisticLosses, expected_test_accs, expected_test_aucs, expected_multipliers = get_expected_answers()
  
    assert len(int_sols_dict["logisticLosses"]) == len(expected_logisticLosses), "logistcLosses do not have the expected length"
    assert np.max(np.abs(int_sols_dict["logisticLosses"] - expected_logisticLosses)) < 1e-8, "logisticLosses values are not correct"
    assert np.max(np.abs(int_sols_dict["multipliers"] - expected_multipliers)) < 1e-8, "multipliers values are not correct"
    assert np.max(np.abs(int_sols_dict["test_accs"] - expected_test_accs)) < 1e-8, "test_accs values are not correct"
    assert np.max(np.abs(int_sols_dict["test_aucs"] - expected_test_aucs)) < 1e-8, "test_aucs values are not correct"

if __name__ == "__main__":
    test_check_solutions_interface()